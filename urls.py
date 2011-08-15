from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^friends/?$', 'viz.views.friends'),
    (r'^data_point/(?P<id>\d+)/?$', 'viz.views.data_point_display'),
    (r'^data/?$', 'viz.views.data'),
    (r'^friend/(?P<id>\d+)/?$', 'viz.views.friend'),
    (r'^get/?$', 'viz.views.get'),
    (r'', 'viz.views.index'),
)
