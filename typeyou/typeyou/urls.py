from django.conf.urls import url
from django.contrib import admin

from typeyou.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name="home"),
]
