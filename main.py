
num2 = int(input("cual es tu primer numero: "))
errapata = int(input("cual es tu segundo numero: "))

def HastaCien(num):
    while num >= 100:
        num = int(input("numero muy grande, inserte otro: "))

    return num

num2 = HastaCien(num2)
errapata = HastaCien(errapata)

while num2 + errapata <= 150:
    print("tiene que ser mas grande que 150")
    num2 = int(input("Elija otro numero para num2: "))
    num2 = HastaCien(num2) 
    errapata = int(input("Elija otro numero para errapata: "))
    errapata = HastaCien(errapata)
    print (num2)
    print(errapata)

print("muito bem :D")



# def HastaCien(num):
#     while num >= 100:
#         num = int(input("Número muy grande, inserte otro: "))
#     return num

# num2 = int(input("¿Cuál es tu primer número?: "))
# errapata = int(input("¿Cuál es tu segundo número?: "))

# num2 = HastaCien(num2)
# errapata = HastaCien(errapata)

# while num2 + errapata <= 150:
#     print("Tiene que ser más grande que 150")
#     num2 = HastaCien(num2)
#     errapata = HastaCien(errapata)

# print("¡Muito bem! :D")


