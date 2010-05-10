from django.conf.urls.defaults import *
from django.conf import settings
from events.models import Season, Location, Event, PreConcertDiscussion, Soloist

import os
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^orch/', include('orch.foo.urls')),
    (r'^$', 'orch.homepage_viewer.views.home'),
    
    (r'^members/$', 'orch.roster.views.all_members'),
    (r'^members/(?P<first_name>.*)_(?P<last_name>.*)/$', 'orch.roster.views.member'),
    
    (r'^season/$', 'events.views.view_current_season'),
	(r'^season/(?P<slug>[-\w]+)/$', 'events.views.view_season'),
    (r'^season/events/(?P<slug>[-\w]+)/$', 'events.views.view_specific_event'),
	(r'^locations/$', 'events.views.all_locations'),
	(r'^locations/(?P<slug>[-\w]+)/$', 'events.views.single_location'),
	(r'^soloists/$', 'events.views.all_soloists'),
	(r'^soloists/(?P<slug>[-\w]+)/$', 'events.views.single_soloist'),
    
    (r'^search/', include('haystack.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': here('site_media') }),
        (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': here("site_media/images") }),
        (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': here("uploads") }),
    )
