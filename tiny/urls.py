from django.conf.urls import patterns, include, url
from shorturls.views import LinkCreate
from shorturls.views import LinkShow
from shorturls.views import RedirectToLongURL

urlpatterns = patterns('',
    url(r'^$', LinkCreate.as_view(), name='home'),
    url(r'^link/(?P<pk>\d+)$', LinkShow.as_view(), name='link_show'),
    url(r'^r/(?P<short_url>\w+)$', RedirectToLongURL.as_view(),
              name='redirect_short_url'),
)
