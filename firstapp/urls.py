from django.conf.urls import include, url
from django.contrib import admin
from mysite import views
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^projects', views.projects, name='projects'),
	url(r'^about', views.about_us, name='about'),
	url(r'^send', views.send_message, name='message')
]
if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()
#if settings.DEBUG:
#	urlpatterns += staticfiles_urlpatterns() + static(
#	settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
#)
