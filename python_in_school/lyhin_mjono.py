import random

def etsiLyhin(lista):
    array_for_len = []
    array_for_items = []
    for items in lista:
        pituus = len(items)
        array_for_items.append(items)
        array_for_len.append(pituus)
        print (array_for_len)
        print (array_for_items)




for x in range(0, 5, 1):
    lista = [chr(random.randint(97,110))*random.randint(1,5), chr(random.randint(97,110))*random.randint(1,5), chr(random.randint(97,110))*random.randint(1,5)]
    while len(lista[0]) == len(lista[1]) or len(lista[0]) == len(lista[2]) or len(lista[1]) == len(lista[2]):
        lista[0] = chr(random.randint(97,110))*random.randint(1,5)
        lista[1] = chr(random.randint(97,110))*random.randint(1,5)
        lista[2] = chr(random.randint(97,110))*random.randint(1,5)
    print("Lista on",lista)
    print("Lyhin on",etsiLyhin(lista))