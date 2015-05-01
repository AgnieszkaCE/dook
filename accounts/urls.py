from django.conf.urls import include, url

from accounts import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
