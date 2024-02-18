#so this code should force you to put two numbers that added together give 150 or more, and it won't stop unitl you get it right.
#blame me if u dare bitshes
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
    
print("muito bem :D")
print("your number should be dis uan: ", num2 + errapata)


















































































































































#easteregg hola jejejjjJEJjejEJJejejo2JEO2JE OJIV1IV1OX1pk10100010101011-. . ...- . .-. / --. --- -. .- / --. .. ...- . / -.-- --- ..- / ..- .--.
