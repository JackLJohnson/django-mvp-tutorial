from django.conf.urls import patterns, url
from preorder import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='preorder_index'),
                       url(r'^about/$', views.about, name='preorder_about'),
                       url(r'^order/$', views.order, name='preorder_order'),
                       url(r'^thanks/$', views.thanks, name='preorder_thanks'),
                       )