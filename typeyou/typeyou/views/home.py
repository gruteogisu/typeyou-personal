from django.views.generic import TemplateView
from django.http.response import HttpResponse


class HomeView(TemplateView):
    template_name = "home.html"
