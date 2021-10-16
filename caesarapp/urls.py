from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^encrypt/$', views.encryptcaesar, name='encrypt'),
    url(r'^encrypthill/$', views.encrypthill, name='encrypthill'),
    url(r'^(?P<userInput_id>[0-9]+)/encrypted/$', views.encrypted, name='encrypted'),
    url(r'^(?P<userInput_id>[0-9]+)/encryptedhill/$', views.encryptedhill, name='encryptedhill'),
    url(r'^history/$', views.history, name='history'),
]
