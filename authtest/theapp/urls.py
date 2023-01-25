from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('authenticated/',views.authentic,name="auth"),
    path('login/',views.login,name='login')
]