import wbgapi as wb

# On récupère toutes les économies
# et on filtre manuellement pour ne garder que les vrais pays
countries = [e['id'] for e in wb.economy.list() if e['aggregate'] == False]

# Maintenant tu peux lancer ta collecte
indicator = 'NY.GDP.MKTP.CD'
data = wb.data.DataFrame(indicator, countries, time=range(1960, 2026))
data.to_csv('gdp_data.csv')
print(f"Nombre de pays collectés : {len(countries)}")