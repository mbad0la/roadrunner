from django.conf.urls import url
from django.conf.urls import include
from . import views
urlpatterns = [
        url(r'^stops/', views.get_stops, name='get_stops'),
        url(r'^routes/', views.get_routes, name='get_routes'),
        url(r'^get-route/(?P<id>[0-9][0-9]*)', views.get_route_detail, name='route_detail'),
]
