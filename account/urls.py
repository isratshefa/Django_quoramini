from django.conf.urls import url, include

from . import views
app_name = 'account'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^logout/$', views.logout_user, name='logout'),
]
