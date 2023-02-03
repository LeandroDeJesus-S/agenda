from django.shortcuts import render, redirect
from django.contrib import auth
from .validators import validate_password, validate_username
from django.core.validators import validate_email
from django.contrib import messages
from django.contrib.auth.models import User
from homepage.models import Contato, Categoria
from . import validators
from datetime import datetime
from django.db.models import Q, functions, Value
from homepage.recaptcha import ReCaptcha

CAPTCHA = {'captcha': ReCaptcha()}


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', CAPTCHA)

    USERNAME = request.POST.get('username')
    PASSWORD = request.POST.get('password')
    user = auth.authenticate(request, username=USERNAME, password=PASSWORD)
    if user is None:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'login.html', CAPTCHA)

    CAPTCHA_ANSWER = ReCaptcha(request.POST)
    if not CAPTCHA_ANSWER.is_valid():
        messages.error(request, 'Captcha incorreto.')
        return render(request, 'login.html', CAPTCHA)

    auth.login(request, user)
    messages.success(request, f'Você entrou como "{user}"')
    return redirect('homepage')


def cadaster(request):
    if request.method == 'GET':
        return render(request, 'cad.html', CAPTCHA)
    
    USERNAME = request.POST.get('username')
    EMAIL = request.POST.get('email')
    PASSWORD = request.POST.get('password')
    PASSWORD_CONFIRM = request.POST.get('passconfirm')
    CAPTCHA_ANSWER = ReCaptcha(request.POST)
    try:
        validate_username(USERNAME)
        if User.objects.filter(username=USERNAME).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'cad.html')

        validate_email(EMAIL)
        if User.objects.filter(email=EMAIL).exists():
            messages.error(request, 'E-mail já existe.')
            return render(request, 'cad.html')

        validate_password(PASSWORD, PASSWORD_CONFIRM)
        if not CAPTCHA_ANSWER.is_valid():
            messages.error(request, 'Captcha inválido.')
            return render(request, 'cad.html', CAPTCHA)

    except Exception as msg:
        msg = list(msg)
        messages.error(request, msg[0])
        return render(request, 'cad.html', CAPTCHA)

    user = User.objects.create_user(username=USERNAME, password=PASSWORD, email=EMAIL)
    user.save()
    messages.success(request, 'Cadastro realizado, você já pode fazer login.')
    return redirect('login')


@auth.decorators.login_required(redirect_field_name='login')
def add_contact(request):
    context = {'categorias': Categoria.objects.all()}
    context.update(CAPTCHA)
    if request.method == 'GET':
        return render(request, 'add_contact.html', context)
    
    NAME = request.POST.get('nome').strip().title()
    LASTNAME = request.POST.get('sobrenome').strip().title()
    PHONE = request.POST.get('telefone')
    EMAIL = request.POST.get('email')
    DESCRIPTION = request.POST.get('descricao')
    PHOTO = request.FILES.get('foto')
    CATEGORY = Categoria.objects.filter(
        categoria=request.POST.get('categoria')
    ).first()
    context.update({'captcha': ReCaptcha(request.POST)})

    try:
        validators.validate_new_contact(NAME, LASTNAME, PHONE, EMAIL)
    except Exception as msg:
        msg = list(msg)
        messages.error(request, msg[0])
        return render(request, 'add_contact.html', context)
    
    if not context['captcha'].is_valid():
        messages.error(request, 'Captcha incorreto.')
        return render(request, 'add_contact.html', context)


    FULLNAME_FIELD = functions.Concat('Nome', Value(' '), 'Sobrenome')
    FULLNAME_VALUE = NAME + ' ' + LASTNAME
    temp_full_name_contact_field = Contato.objects.annotate(fullname=FULLNAME_FIELD)
    contact_already_exists = temp_full_name_contact_field.filter(
       Q(fullname=FULLNAME_VALUE) | Q(Telefone=PHONE),  User=request.user
    ).exists()

    if contact_already_exists:
        messages.warning(request, 'Contato já existe.')
        return render(request, 'add_contact.html', context)
    
    new_contact = Contato.objects.create(
        User=request.user, Nome=NAME, Sobrenome=LASTNAME, Telefone=PHONE,
        Email=EMAIL, Descrição=DESCRIPTION, Categoria=CATEGORY, foto=PHOTO
    )
    new_contact.save()
    messages.success(request, 'Contato salvo com sucesso.')
    return redirect('homepage')


@auth.decorators.login_required(redirect_field_name='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
