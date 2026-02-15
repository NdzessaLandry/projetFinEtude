from django.urls import path

from .views import AnalyseUnivarieView

urlpatterns = [
    path('', AnalyseUnivarieView.as_view(), name='analyse_univarie'),
]