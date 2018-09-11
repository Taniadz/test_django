from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, TemplateView


class CountriesXMLView(TemplateView):
    content_type='application/xml'
    template_name = 'countries.xml'
