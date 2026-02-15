from django.shortcuts import render
from django.views.generic import TemplateView

class ETLView(TemplateView):
    template_name = 'ETL.html'
# Create your views here.
