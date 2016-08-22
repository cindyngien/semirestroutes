from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='myindex'),
    url(r'^products/new$', views.new, name='newproduct'),
    url(r'^products/create$', views.create, name ='addproduct'),
    url(r'^products/(?P<product_id>[0-9]+)$', views.show, name = 'showproduct'),
    url(r'^products/(?P<product_id>[0-9]+)/edit$', views.edit, name = 'editproduct'),
    url(r'^products(?P<product_id>[0-9]+)$', views.update, name = 'updateproduct'),
    url(r'^products/(?P<product_id>[0-9]+)/destroy$', views.destroy, name = 'destroyproduct'),
]
