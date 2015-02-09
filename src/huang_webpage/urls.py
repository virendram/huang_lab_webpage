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
    #url(r'^account/', include('django.contrib.auth.urls')),
    #url(r'^password_reset/',  'signups.views.cust_password_reset'),
    #url(r'^password_reset/done/', 'signups.views.cust_password_reset_done'),
    #url(r'^reset/([0-9A-Za-z]+)-(.+)/', 'signups.views.cust_password_reset_confirm'),
    #url(r'^reset/done/', 'signups.views.cust_password_reset_complete'),
    
    
    url(r'^index/$', 'signups.views.home', name='home'),
    url(r'^research/$', 'signups.views.research', name='research'),
    url(r'^contact_us/$', 'signups.views.contact_us', name='contact_us'),
    url(r'^publications/$', 'signups.views.publications', name='publications'),
    url(r'^download/$', 'signups.views.download', name='download'),
    url(r'^verify_user/$', 'signups.views.verify_user', name='verify_user'),
    url(r'^confirmation_expired/$', 'signups.views.confirmation_expired', name='confirmation_expired'),
    url(r'^login/$', 'signups.views.login', name='login'),
    url(r'^signup/$', 'signups.views.signup', name='signup'),
    url(r'^thankyou/$', 'signups.views.thank_you', name='thank_you'),
    url(r'^forgot_password/$', 'signups.views.forgot_password', name='forgot_password'),
    url(r'^password_changed_successfully/$', 'signups.views.password_changed_successfully', name='password_changed_successfully'),
    url(r'^check_email_password_reset/$', 'signups.views.check_email_password_reset', name='check_email_password_reset'),
    
    url(r'^mass_email/(?P<permission_key>\w+)/$', ('signups.views.mass_email'), name='mass_email'),
    url(r'^register_confirm/(?P<activation_key>\w+)/$', ('signups.views.register_confirm'), name='register_confirm'),
    url(r'^reset_password/(?P<activation_key>\w+)/$', ('signups.views.reset_password'), name='reset_password'),
    
    
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