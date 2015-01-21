from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^download/$', 'signups.views.download', name='download'),
    url(r'^aboutus/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^publications/$', 'signups.views.publications', name='publications'),
    url(r'^research/$', 'signups.views.research', name='research'),
    url(r'^contactus/$', 'signups.views.contactus', name='contactus'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)