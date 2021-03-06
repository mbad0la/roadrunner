from django.conf.urls import url
from django.conf.urls import include
from . import views
import superuser
urlpatterns = [                  
        url(r'^route-search/', views.route_form, name='route_form'),
        url(r'^generate-form/', views.generate_form, name='test'),
        url(r'authorize-form/', views.authorize_form, name='test2'),
        url(r'^password-new/', views.enter_pass, name='new_pass'),
        url(r'^$', views.index, name='index'),
        url(r'^request/stops/', views.send_stops, name='send_stops'),
        url(r'^signup-form/', views.user_signup, name='signup'),
        url(r'^test/', views.test, name='test'),
        url(r'^change-password', views.change_password, name='change_password'),
        url(r'^login-naive/', views.login_form, name='login'),
        url(r'^book-taxi/', views.taxi_form, name='book_taxi'),
        url(r'^user-detail/(?P<id>[0-9][0-9]*)', views.get_user, name='user'),
        url(r'get-user/(?P<id>[0-9][0-9]*)', views.get_user_detail, name='user_detail'),
]
