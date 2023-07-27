from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import pymorphy3
from core.word_mat_file import word_mat_source
import re


def func_anti_mat(dict_mat: str):
    # нормализуем пришедшее слово
    morph = pymorphy3.MorphAnalyzer()
    # проверка вхождения с переводом слова в нижний регистр
    return morph.parse(dict_mat)[0].normal_form in word_mat_source


def func_curse_word(value):
    my_result = re.split(" |-|\n", value)

    for str_one in my_result:
        if len(str_one) > 0:
            result_str = func_anti_mat(str_one)
            if result_str:
                raise ValidationError(_('Вы употребили нецензурное слово!'), )
