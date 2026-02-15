from django.urls import path
from .views import ETLView

urlpatterns = [
    path('', ETLView.as_view(), name='etl'),
]
