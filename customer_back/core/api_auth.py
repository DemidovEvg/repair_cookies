import logging

from core.models import TokenData
from django.conf import settings
from django.contrib.auth import get_user_model
from drf_keycloak_auth.authentication import KeycloakAuthentication
from drf_keycloak_auth.settings import api_settings
from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakGetError, raise_error_from_response
from keycloak.urls_patterns import URL_TOKEN

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
    user, created = User.objects.get_or_create(
        username=settings.KEYCLOAK_SERVISE_ACCOUNT_NAME,
        id=settings.KEYCLOAK_SERVISE_ACCOUNT_ID,
        phone_number="00000",
    )
    token_data, created = TokenData.objects.get_or_create(
        user=user, defaults=dict(token="")
    )
    token_data.token = ""
    token_data.save()


def get_access_token() -> str:
    user, created = User.objects.get_or_create(
        username=settings.KEYCLOAK_SERVISE_ACCOUNT_NAME,
        id=settings.KEYCLOAK_SERVISE_ACCOUNT_ID,
        # add phone-number
        phone_number="00000",
    )

    access_token = None
    token_data, created = TokenData.objects.get_or_create(
        user=user, defaults=dict(token="")
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
