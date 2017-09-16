from django.conf.urls import url

from . import views
from accounts.views import LoginView, SignUpView, CeleryView

urlpatterns = [

    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'signup/$', SignUpView.as_view(), name='signup'),
    url(r'logout/$', views.logoutview, name='logout'),
    url(r'test/$', views.testview, name='test'),
    url(r'celery-test/$', CeleryView.as_view(), name='celery-test'),

]