from django.conf.urls import include, url

from cowork import views

urlpatterns = [
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^locations/', include('cowork.locations.urls', namespace='locations')),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
]
