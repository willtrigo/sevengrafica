from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', cases, name='cases'),
    url(r'^(?P<slug>[\w_-]+)/$', products, name='products'),
]
