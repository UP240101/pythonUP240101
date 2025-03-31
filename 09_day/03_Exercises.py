person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# 1. Verificar si existe la clave 'skills' y obtener la habilidad del medio
if 'skills' in person:
    skills_list = person['skills']
    middle_skill = skills_list[len(skills_list) // 2]  # Obtener la habilidad del medio
    print("Middle skill:", middle_skill)
# 2. Verificar si la persona tiene la habilidad 'Python'
if 'skills' in person and 'Python' in person['skills']:
    print("The person has Python skill:", True)
else:
    print("The person has Python skill:", False)
# 3. Determinar el tipo de desarrollador según las habilidades
skills_set = set(person['skills'])
if skills_set == {'JavaScript', 'React'}:
    print("He is a front end developer")
elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
    print("He is a backend developer")
elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
    print("He is a fullstack developer")
else:
    print("Unknown title")
# 4. Verificar si la persona está casada y vive en Finlandia
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
