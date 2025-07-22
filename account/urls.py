from django.urls import path
from account.views import (
    register,
    login,
    dashboard,
    logout,
    acc_home,
    must_authenticate_view
)

urlpatterns =[
    path("", acc_home, name="acc_home"),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("dashboard", dashboard, name="dashboard"),
    path ("logout", logout, name="logout"),
    path("must_authenticate", must_authenticate_view, name="must_authenticate" ),
]
