#python_version == '3.7'

def check_sublist(list1, d1, d2):
    lista = []
    listb = []
    listc = []
    for num in list1:
        if num > d1*d2 :
            lista.append(num)
        if num < d1*d2 :
            listb.append(num)
        if num < d1 or num < d2:
            listc.append(num)
    return lista, listb, listc