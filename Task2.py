#Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inversion(a):
    if a==True:
        a=False
    else: a=True
    return a
def disjunction(a,b):
    if a==False and b==False:
        aVb=False
    else: aVb=True
    return aVb
def conjunction(a,b):
    if a==True and b==True:
        aAb=True
    else: aAb=False
    return aAb
x = int(input('Значение предикат x='))!=0
y = int(input('Значение предикат y='))!=0
z = int(input('Значение предикат z='))!=0

print(inversion(disjunction(disjunction(x,y),z)),"=",conjunction(conjunction(inversion(x),inversion(y)),inversion(z)))

