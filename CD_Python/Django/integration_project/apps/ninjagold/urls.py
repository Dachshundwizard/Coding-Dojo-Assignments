from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^processgold/(?P<place>(cave)|(house)|(farm)|(casino))$', views.processgold, name='processgold'),
    url(r'^reset$', views.reset, name='reset')
]
