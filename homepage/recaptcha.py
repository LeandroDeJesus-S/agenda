from django import forms
from captcha.fields import CaptchaField

class ReCaptcha(forms.Form):
    captcha = CaptchaField()
