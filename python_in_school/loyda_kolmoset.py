import random


alku = random.randint(5,20)
loppu = alku + random.randint(25,50)

print("Alku:",alku)
print("Loppu:",loppu)

print("Parittomat kolmella jaolliset:")

for x in range(alku, loppu):
    jaakolmella = str(x/3) # Jaetaan kolmella jotta saadaan kolmella jaolliset numerot, muutetaan float to str

    if len(jaakolmella) <= 4: # Kaikki kolmella jaolliset ovat max len 4, joten otetaan ne talteen. Tämä mahdollista, koska loppuluku aina alle 100
        kerrotaankolmella = float(jaakolmella) * 3 # Muutetaan luvut takaisin alkuperäiseksi kolmella jaolliseksi
        jaetaankahdella = kerrotaankolmella / 2 # Jaetaan nämä luvut kahdella
        loyda_kolmelliset = str(jaetaankahdella).find(".5") # Missä ".0" niin parillisia, poistetaan ne, ottamalla vain ".5" loppuiset talteen
        print(loyda_kolmelliset)
        if loyda_kolmelliset >= 0:
            print(loyda_kolmelliset)
        else:
            continue
    else:
        continue




