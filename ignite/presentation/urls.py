from django.conf.urls.defaults import *
from ignite.presentation.views import presentation_add, presentation_list, presentation_detail

urlpatterns = patterns('',
    url(r'^$', presentation_list, name='presentation_list'),
    url(r'^add/$', presentation_add, name='presentation_add'),
    url(r'^(?P<slug>[\w-]+)/$', presentation_detail, name='presentation_detail'),
)
