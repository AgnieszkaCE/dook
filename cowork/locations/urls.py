from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LocationListView.as_view(), name='list'),
    url(r'^add/$', views.LocationAddView.as_view(), name='add'),
    #url(r'^delete/$', views.LocationDeleteView.as_view(), name='delete'),
]
