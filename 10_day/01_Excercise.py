#1
# Usando for
for i in range(11):
    print(i)
# Usando while
i = 0
while i <= 10:
    print(i)
    i += 1
#2
# Usando for
for i in range(10, -1, -1):
    print(i)

# Usando while
i = 10
while i >= 0:
    print(i)
    i -= 1
#3
for i in range(1, 8):
    print("#" * i)
#4
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
#5
for i in range(11):
    print(f"{i} x {i} = {i * i}")
#6
tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in tecnologias:
    print(tech)
#7
for i in range(0, 101, 2):
    print(i)
#8
for i in range(1, 101, 2):
    print(i)