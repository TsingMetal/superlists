from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^([1-9]+)/$', views.view_list, name='view_list'),
    url(r'^([1-9]+)/add_item$', views.add_item, name='add_item'),
]
