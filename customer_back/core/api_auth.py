import logging

from django.contrib.auth import get_user_model
from django.db.models import Q
from drf_keycloak_auth.authentication import KeycloakAuthentication
from django.conf import settings
from drf_keycloak_auth.settings import api_settings
from keycloak import KeycloakOpenID
from keycloak.urls_patterns import URL_TOKEN
from keycloak.exceptions import KeycloakGetError, raise_error_from_response
from core.models import TokenData

User = get_user_model()

log = logging.getLogger("drf_keycloak_auth")


class CookiesKeycloakAuthentication(KeycloakAuthentication):
    def authenticate(self, request):
        if self.keycloak_openid is None:
            self.keycloak_openid = get_keycloak_openid_without_verify()
        return super().authenticate(request)


class CookiesKeycloakOpenID(KeycloakOpenID):
    def api_token(self):
        params_path = {"realm-name": self.realm_name}
        url = f"{URL_TOKEN.format(**params_path)}"
        data = (
            f"grant_type=client_credentials"
            f"&client_id={self.client_id}"
            f"&client_secret={self.client_secret_key}"
            f"&scope=openid"
        )
        data_raw = self.connection.raw_post(url, data=data)
        return raise_error_from_response(data_raw, KeycloakGetError)


def get_keycloak_openid_without_verify(
    oidc: dict = None, custom_headers: dict = None
) -> CookiesKeycloakOpenID:
    custom_headers = {} if not custom_headers else custom_headers
    try:
        if oidc:
            log.info("get_keycloak_openid: " f'OIDC realm={oidc["realm"]}')

            return CookiesKeycloakOpenID(
                server_url=oidc["auth-server-url"],
                realm_name=oidc["realm"],
                client_id=oidc["resource"],
                client_secret_key=oidc["credentials"]["secret"],
                verify=getattr(settings, "KEYCLOAK_VERIFY", True),
                custom_headers=custom_headers,
            )

        return CookiesKeycloakOpenID(
            server_url=api_settings.KEYCLOAK_SERVER_URL,
            realm_name=api_settings.KEYCLOAK_REALM,
            client_id=api_settings.KEYCLOAK_CLIENT_ID,
            client_secret_key=api_settings.KEYCLOAK_CLIENT_SECRET_KEY,
            verify=getattr(settings, "KEYCLOAK_VERIFY", True),
            custom_headers=custom_headers,
        )
    except KeyError as e:
        raise KeyError(f"invalid settings: {e}") from e


def remove_api_token():
    try:
        api_user = User.objects.get(id=settings.KEYCLOAK_SERVISE_ACCOUNT_ID)
    except User.DoesNotExist:
        User.objects.filter(
            Q(username=settings.KEYCLOAK_SERVISE_ACCOUNT_NAME)
            | Q(phone_number="00000")
            | Q(email="api@api.ru")
        ).delete()
        User.objects.filter().delete()
        api_user = User.objects.create(
            username=settings.KEYCLOAK_SERVISE_ACCOUNT_NAME,
            id=settings.KEYCLOAK_SERVISE_ACCOUNT_ID,
            phone_number="00000",
            email="api@api.ru",
        )
    token_data, created = TokenData.objects.get_or_create(
        user=api_user, defaults=dict(token="")
    )
    token_data.token = ""
    token_data.save()


def get_access_token() -> str:
    try:
        api_user = User.objects.get(id=settings.KEYCLOAK_SERVISE_ACCOUNT_ID)
    except User.DoesNotExist:
        User.objects.filter(
            Q(username=settings.KEYCLOAK_SERVISE_ACCOUNT_NAME)
            | Q(phone_number="00000")
            | Q(email="api@api.ru")
        ).delete()
        api_user = User.objects.create(
            username=settings.KEYCLOAK_SERVISE_ACCOUNT_NAME,
            id=settings.KEYCLOAK_SERVISE_ACCOUNT_ID,
            phone_number="00000",
            email="api@api.ru",
        )

    access_token = None
    token_data, created = TokenData.objects.get_or_create(
        user=api_user, defaults=dict(token="")
    )
    if not created and token_data.token:
        return token_data.token

    custom_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    keycloak_openid = get_keycloak_openid_without_verify(custom_headers=custom_headers)
    response_data = keycloak_openid.api_token()
    access_token = response_data["access_token"]
    token_data.token = access_token
    token_data.save()
    return access_token


def headers_with_token(headers: dict) -> dict:
    access_token = get_access_token()
    headers_copy = headers.copy()
    headers_copy.update({"Authorization": f"Bearer {access_token}"})
    return headers_copy
