from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('account.urls')),
    url(r'^home/', include('home.urls')),
]