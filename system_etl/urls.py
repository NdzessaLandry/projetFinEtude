from django.urls import path
from .views import ETLView, ChargementView, TransformationView, CreerUneTableFaitView, FaitEtDimensionView
#TransformationView, ChargementView

urlpatterns = [
    path('', ETLView.as_view(), name='etl'),
    path("traitement/", ChargementView.as_view(), name="chargement"),
    path("finalize_etl/", TransformationView.as_view(), name="finalize_etl"),
    path("creer_table_fait",CreerUneTableFaitView.as_view(), name="creer_table_fait"),
    path("fait_et_dimension/", FaitEtDimensionView.as_view(), name="fait_et_dimension"),
]
