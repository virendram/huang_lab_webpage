from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^index/$', 'signups.views.home', name='home'),
    url(r'^research/$', 'signups.views.research', name='research'),
    url(r'^contact_us/$', 'signups.views.contact_us', name='contact_us'),
    url(r'^publications/$', 'signups.views.publications', name='publications'),
    url(r'^download/$', 'signups.views.download', name='download'),
    url(r'^verify_user/$', 'signups.views.verify_user', name='verify_user'),
    url(r'^confirmation_expired/$', 'signups.views.confirmation_expired', name='confirmation_expired'),
    url(r'^register_confirm/(?P<activation_key>\w+)/$', ('signups.views.register_confirm'), name='register_confirm'),
    
    
    #url(r'^gestational_week_33wg_b0/$', 'signups.views.gestational_week_33wg_b0', name='gestational_week_33wg_b0'),
   # url(r'^downloads1/$', 'signups.views.downloads1', name='downloads1'),
    #url(r'^aboutus/$', 'signups.views.aboutus', name='aboutus'),
    
    
    
    
    
    #url(r'^signup/$', 'signups.views.login', name='login'),
    
    
)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)