from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from ignite.settings import PROJECT_PATH, DEBUG

urlpatterns = patterns('',

    # Home page
    (r'^$', direct_to_template, {'template': 'home.html'}),

    # Presentations
    (r'^presentation/', include('ignite.presentation.urls')),

    # Admin
    (r'^admin/', include('django.contrib.admin.urls')),
)

if DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/../media' % (PROJECT_PATH)})
    )
