from django.urls import path
from .views import AnalyseMultidimentionnelleView

urlpatterns = [
    path('', AnalyseMultidimentionnelleView.as_view(), name='analyse_multidimentionnelle'),
]