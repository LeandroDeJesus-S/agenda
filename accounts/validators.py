from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from django.shortcuts import render

def validate_password(password, pw_confirm):
    """Valida se a senha do usuario tem pelomenos um caractere maiusculo
    um minusculo, um caractere especial e um numero, e se possui no minimo
    8 digitos.

    Args:
        password (str): senha do usuario
        pw_confirm (str): senha de confirmação do usuario

    Raises:
        ValidationError: django.core.exeptions.ValidationError
    """
    from string import ascii_uppercase, ascii_lowercase, digits, punctuation

    MIN_LEN_PASSWORD = 8
    if len(password) < MIN_LEN_PASSWORD:
        raise ValidationError('A senha precisa ter no minimo 8 caracteres.')

    checks = []
    for digit in password:
        if digit in ascii_uppercase:
            checks.append('u')
        elif digit in ascii_lowercase:
            checks.append('l')
        elif digit in digits:
            checks.append('d')
        elif digit in punctuation:
            checks.append('p')
    
    if 'u' not in checks or 'l' not in checks or 'd' not in checks or 'p' not in checks:
        raise ValidationError(
            'A senha precisa ter pelo menos uma letra maiuscula, uma minuscula'
            ', um numero e um caracetere especial, por exemplo: "Exemplo@123".'
        )

    if password != pw_confirm:
        raise ValidationError('As senhas não são iguais.')


def validate_username(username: str):
    """Valida se o nome de usuario tem pelomenos 4 caracteres compostos por
    letras e numeros.

    Args:
        username (str): nome de usuario

    Raises:
        ValidationError: django.core.exeptions.ValidationError
    """
    MIN_LEN_USERNAME = 4
    if len(username) < MIN_LEN_USERNAME:
        raise ValidationError('O nome de usuário deve ter no minimo 4 caracteres')

    if not username.isalnum():
        raise ValidationError('O nome de usuário so deve conter letras e números.')


def validate_name_or_lastname(name: str):
    """Valida o nome/sobrenome do usuario contem no minimo 3 caracteres
    e é composto apenas de letras.

    Args:
        name (str): nome ou sobrenome do usuario

    Raises:
        ValidationError: django.core.exeptions.ValidationError
    """
    MIN_LEN_TO_NAME = 3
    name = ''.join(name.strip())
    if not name:
         return
    if not name.isalpha() or len(name) < MIN_LEN_TO_NAME:
        raise ValidationError(
            'O nome precisa ter no minimo 3 carateres '\
            'e ser composto apenas por letras.'
        )


def validate_phonenumber(phone):
    """Valida o numero de telefone do usuario verificando se é uma sequencia
    de numeros iguais ou se há apenas digitos

    Args:
        phone (str): numero de telefone do usuario

    Raises:
        ValidationError: django.core.exeptions.ValidationError
    """
    PHONE_NO_DDD = phone[2:]
    SAME_NUM_SEQUENCE = phone[0] * len(phone)
    NO_DDD_SAME_NUM_SEQUENCE = PHONE_NO_DDD * len(phone)
    if not phone.isnumeric():
        raise ValidationError('Número de telefone inválido.')
    
    if phone == SAME_NUM_SEQUENCE and PHONE_NO_DDD == NO_DDD_SAME_NUM_SEQUENCE:
        raise ValidationError('Número de telefone inválido.')


def validate_new_contact(nome, sobrenome, telefone, email):
    """valida o nome, sobrenome, telefone e email do contato
    usando funções validate_name_or_lastname, validate_name_or_lastname,
    validate_phonenumber e validate_email

    Args:
        nome (str): nome do contato
        sobrenome (str): sobrenome do contato
        telefone (str): telefone do contato
        email (str): email do contato
    raises:
        ValidationError: django.core.exeption.ValidationError
    """
    validate_name_or_lastname(nome)
    validate_name_or_lastname(sobrenome)
    validate_phonenumber(telefone)
    validate_email(email)
    

