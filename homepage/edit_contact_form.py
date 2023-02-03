from django import forms
from .models import Contato
from captcha.fields import CaptchaField


class AddContatctForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contato
        exclude = ['User']
