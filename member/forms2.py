from allauth.account import forms as allauth_forms


class MemberLoginForm(allauth_forms.LoginForm):
    class Media:
        js = ('https://www.google.com/recaptcha/api.js',)


class MemberResetPasswordForm(allauth_forms.ResetPasswordForm):
    class Media:
        js = ('https://www.google.com/recaptcha/api.js',)


class MemberResetPasswordKeyForm(allauth_forms.ResetPasswordKeyForm):
    pass
