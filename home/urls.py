from django.contrib import admin
from django.conf.urls import url, include
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_question/$', views.create_question, name='create_question'),
    url(r'^(?P<question_id>[0-9]+)/create_answer/$', views.create_answer, name='create_answer'),
    url(r'^(?P<question_id>[0-9]+)/$', views.all_answers, name='all_answer'),
    url(r'^(?P<question_id>[0-9]+)/delete_answer/(?P<answer_id>[0-9]+)/$', views.delete_answer, name='delete_answer'),
    url(r'^(?P<question_id>[0-9]+)/delete_question/$', views.delete_question, name='delete_question'),
    url(r'^(?P<question_id>[0-9]+)/update_question/', views.update_question, name='update_question'),
]
