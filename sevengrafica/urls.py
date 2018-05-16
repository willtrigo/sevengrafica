from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from sevengrafica.core import views
from sevengrafica.cases import views as viewscases

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^clientes/$', views.clients, name='clients'),
    url(r'^sobrenos/$', views.aboutus, name='aboutus'),
    url(r'^cases/', include('sevengrafica.cases.urls', namespace='cases')),
    url(r'^admin/', admin.site.urls),
    url(r'^newsletter/$', views.redirect_from_newsleter),
    url(r'^newsletter/(?P<newsletter_slug>[\w_-]+)/$', views.redirect_from_newsleter),
    url(r'^newsletter/(?P<newsletter_slug>[\w_-]+)/update/$', views.redirect_from_newsleter),
    url(r'^newsletter/(?P<newsletter_slug>[\w_-]+)/archive/$', views.redirect_from_newsleter),
    url(r'^newsletter/(?P<newsletter_slug>[\w_-]+)/archive/(?P<year>.+)/(?P<month>.+)/(?P<day>.+)/(?P<slug>[\w-]+)/$', views.redirect_from_newsleter),
    url(r'^newsletter/', include('newsletter.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
