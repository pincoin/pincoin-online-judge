from allauth.account import forms as allauth_forms


class MemberLoginForm(allauth_forms.LoginForm):
    class Media:
        js = ('https://www.google.com/recaptcha/api.js',)
