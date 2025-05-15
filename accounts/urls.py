from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', onboard),
    path("auth/connect/", auth_connect, name="oauth_connect"),
    path("auth/tokens/", tokens, name="oauth_tokens"),
    path("auth/callback/", callback, name="oauth_callback"),
    path('get-token/', get_token),
    # path("token-refresh/",token_refresh)
]