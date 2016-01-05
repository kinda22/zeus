from django.conf.urls import include, url
from .views import login_view, logout_view, register 

urlpatterns = [
    url(r'login/',  login_view, name="accounts_login"),
    url(r'logout/',  logout_view, name="accounts_logout"),
    url(r'register/', register, name="accounts_register"),
]
