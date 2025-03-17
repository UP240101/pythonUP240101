# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#Encuentra la longitud del conjunto it_companies
print(len(it_companies))
#Añade 'Twitter' a it_companies
new_company = "twitter"
it_companies.add(new_company)
print(it_companies)
#Insertar varias empresas de TI a la vez en el conjunto it_companies
new_companys = {'samnsung', 'AT&T', 'intel', 'Alibaba', 'Dell', 'HP'}
it_companies.update(new_companys)
print(it_companies)
#Eliminar una de las empresas del conjunto it_companies
delete = 'Apple'
it_companies.remove(delete)
print(it_companies)
''''
¿Cuál es la diferencia entre remove y discard?
remove sirve para eliminar un elemento de un conjunto pero si no se encuentra el elemento generara errores
por lo que es bueno verificar si el elemento existe en el conjunto dado y discard no generara ninguno.
'''