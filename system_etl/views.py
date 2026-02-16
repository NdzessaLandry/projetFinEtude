from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import pandas as pd

class ETLView(TemplateView):
    template_name = 'ETL.html'
# Create your views here.

class ChargementView(TemplateView):
    template_name = 'traitementETL.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajoutez ici les données que vous souhaitez passer à votre template
        return context
    def post(self, request, *args, **kwargs):
        # Traitez les données du formulaire ici
        # Par exemple, vous pouvez récupérer les données du formulaire avec request.POST
        # et effectuer les opérations nécessaires pour le chargement des données
        context=self.get_context_data()
        try:
            if request.method=="POST" and request.FILES['file_source']:
                file=request.FILES['file_source']
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                file_url = fs.url(filename)
                print(file_url)
                extensions_valides = ['.csv', '.xlsx', '.xls', '.txt', ".pdf"]
                extension_fichier = file_url.split('.')[-1].lower()
                if f".{extension_fichier}" in extensions_valides:
                    print("fichier valide")
                else:   
                    print("fichier non valide")
                    return self.render_to_response(context)

                data=pd.DataFrame({'Categorie':['Agriculture','Élévage','Péche','Agriculture','Mine'],'Produit':['Blé','Boeuf','Poisson','Maïs','Fer'],'Prix':[100,200,300,400,500],'Quantite':[10,20,30,40,50],'Exportation':[1000,2000,3000,4000,5000],'Pays':['France','Brésil','Chine','États-Unis','Australie'],'Date':['2020-01-01','2020-02-01','2020-03-01','2020-04-01','2020-05-01']})
                try:
                    context["dataset_preview"]=data.head(5).values.tolist()
                    context["is_dataset_preview"]=True
                except Exception as e:
                    print("Erreur lors de la création de l'aperçu du dataset :", str(e))
                    context["is_dataset_preview"]=False
                context["columns"]=data.columns.tolist()
                return self.render_to_response(context)
            else:
                print("non")
                return self.render_to_response(context)
        except Exception as e:
            print("Erreur lors du chargement du fichier :", str(e))
            return self.render_to_response(context)
    
    

class TransformationView(TemplateView):
    template_name = 'finalize_etl.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajoutez ici les données que vous souhaitez passer à votre template
        return context
    
class CreerUneTableFaitView(TemplateView):
    template_name = 'creer_table_fait.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajoutez ici les données que vous souhaitez passer à votre template
        context["columns"]=["Categorie","Produit","Prix","Quantite","Exportation","Pays","Date"]
        return context

class FaitEtDimensionView(TemplateView):
    template_name = 'fait_et_dimension.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajoutez ici les données que vous souhaitez passer à votre template
        return context
    def post(self, request, *args, **kwargs):
        context=self.get_context_data()
        # Traitez les données du formulaire ici
        # Par exemple, vous pouvez récupérer les données du formulaire avec request.POST
        # et effectuer les opérations nécessaires pour le chargement des données
        return self.render_to_response(context)