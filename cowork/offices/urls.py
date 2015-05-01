from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OfficeListView.as_view(), name='list'),
    url(r'^add/$', views.OfficeAddView.as_view(), name='add'),
    #url(r'^delete/$', views.OfficeDeleteView.as_view(), name='delete'),
]
