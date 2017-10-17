from django.conf.urls import url
from django.contrib import admin
from sevengrafica.core import views

urlpatterns = [
    url(r'^$', views.home, name='core'),
    url(r'^admin/', admin.site.urls),
]
