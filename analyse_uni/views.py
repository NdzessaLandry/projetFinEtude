from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AnalyseUnivarieView(TemplateView):
    template_name = 'analyse_univarie.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        monDictionnaire={
            "faitPrix":{
                "prix":[100,200,300,400,500],
                "categorie":["Agriculture","Élévage","Péche","Agriculture","Mine"],
                "produit":["Blé","Boeuf","Poisson","Maïs","Fer"],
                "pays":["France","Brésil","Chine","États-Unis","Australie"],
                "date":["2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01"]
            },
            "faitQuantite":{
                "quantite":[10,20,30,40,50],
                "categorie":["Agriculture","Élévage","Péche","Agriculture","Mine"],
                "produit":["Blé","Boeuf","Poisson","Maïs","Fer"],
                "pays":["France","Brésil","Chine","États-Unis","Australie"],
                "date":["2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01"]
            },
            "faitExportation":{
                "exportation":[1000,2000,3000,4000,5000],
                "categorie":["Agriculture","Élévage","Péche","Agriculture","Mine"],
                "produit":["Blé","Boeuf","Poisson","Maïs","Fer"],
                "pays":["France","Brésil","Chine","États-Unis","Australie"],
                "date":["2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01"]
            }
        }
        context['monDictionnaire']=monDictionnaire
        context["categories"]=["Agriculture","Élévage","Péche","Agriculture","Mine"]
        context["Agriculture"]=['Maïs','Blé','Riz']
        context["Élévage"]=['Boeuf','Poulet','Porc']
        context["Péche"]=['Poisson','Crabe','Crevette']
        context["Mine"]=['Fer','Or','Cuivre']
        selection = self.request.GET.get('var_a')
        #print(selection)
        #context["aAfficher"]=context[selection]
        return context

# Investing, Banque mondiale, woe, Trading, WDI