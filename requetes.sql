SELECT prix,categorie, pays, date_complete from fait_prix as fp INNER JOIN dim_zone as dz ON dz.id=fp.id_zone INNER JOIN 
dim_produit as dp ON dp.id=fp.id_produit INNER JOIN dim_date as dd ON dd.id=fp.id_date ORDER BY date_complete; 

SELECT quantite,categorie, pays, date_complete from fait_quantite as fp INNER JOIN dim_zone as dz ON dz.id=fp.id_zone INNER JOIN 
dim_produit as dp ON dp.id=fp.id_produit INNER JOIN dim_date as dd ON dd.id=fp.id_date ORDER BY date_complete; 

SELECT quantite_exportee,prix_exportation,categorie, pays, date_complete from fait_exportation as fp INNER JOIN dim_zone as dz ON dz.id=fp.id_zone INNER JOIN 
dim_produit as dp ON dp.id=fp.id_produit INNER JOIN dim_date as dd ON dd.id=fp.id_date ORDER BY date_complete; 

SELECT quantite_importee,prix_importation,categorie, pays, date_complete from fait_importation as fp INNER JOIN dim_zone as dz ON dz.id=fp.id_zone INNER JOIN 
dim_produit as dp ON dp.id=fp.id_produit INNER JOIN dim_date as dd ON dd.id=fp.id_date ORDER BY date_complete; 

