# sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#Unir A y B
c = A.union(B)
print(c)
#Encuentra la intersección A y B
print(A.intersection(B))
#Es A un subconjunto de B
print(A.issubset(B))
#¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B))
#Unir A con B y B con A
print(A.union(B))
print(B.union(A))
#¿Cuál es la diferencia simétrica entre A y B?
print(A.symmetric_difference(B))
#Eliminar los conjuntos por completo
del c