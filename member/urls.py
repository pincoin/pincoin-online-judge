from django.urls import (
    path, re_path
)

from . import views

urlpatterns = [
    # Account
    path('login/',
         views.MemberLoginView.as_view(), name="account_login"),
    path('logout/',
         views.MemberLogoutView.as_view(), name="account_logout"),
    path('signup/',
         views.MemberLoginView.as_view(), name="account_signup"),

    # Password Change

    # Password Reset
    path('password/reset/',
         views.MemberLoginView.as_view(), name="account_reset_password"),

    # Email Confirmation
    path('confirm-email/',
         views.MemberLoginView.as_view(), name="account_email_verification_sent"),
    re_path(r'^confirm-email/(?P<key>[-:\w]+)/$',
            views.MemberLoginView.as_view(), name="account_confirm_email"),
    path('email/',
         views.MemberLoginView.as_view(), name="account_email"),

    # Site Terms and Conditions / Privacy Policy

    # Profile

    # Social Providers

]
