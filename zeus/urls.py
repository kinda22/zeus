from django.conf.urls import include, url
from accounts import urls as accounts_urls
from dashboard import urls as dashboard_urls
from manager import urls as manager_urls
from home import urls as home_urls 

urlpatterns = [
    url(r'^accounts/', include(accounts_urls)),
    url(r'^dashboard/', include(dashboard_urls)),
    url(r'^manager/', include(manager_urls)),
    url(r'^$', include(home_urls)),
]
