from django.conf.urls import url, include
from django.contrib import admin

from typeyou.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name="home"),

    url(r'^', include("users.urls", namespace="users")),

    url(r'^community/', include("community.urls", namespace="community")),
]
