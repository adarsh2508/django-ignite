from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Home page
    (r'^$', direct_to_template, {'template': 'home.html'}),

    # Presentations
    (r'^presentation/', include('ignite.presentation.urls')),

    # Admin
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/../media' % (settings.PROJECT_PATH)})
    )
