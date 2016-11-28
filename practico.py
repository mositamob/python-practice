def cantidad_facturas(cant):
    result = 'Cantidad de facturas: '
    if cant > 12:
        result += 'muchas'
    else:
        result += str(cant)
    return result


print(cantidad_facturas(6))
print(cantidad_facturas(15))


def ambos(s):
    if len(s) > 2:
        result = s[0:2] + s[-2] + s[-1]
        return result


print(ambos('counting'))
print(ambos('py'))


def fix(s):
    first = s[0]
    result = s.replace(first, '*')
    result = result.replace('*', first, 1)
    return result


print(fix('anana'))


def mezclar(a, b):
    return a.replace(a[0], b[0], 1) + " " + b.replace(b[0], a[0], 1)


print(mezclar('mix', 'pai'))


def macheos(lista):
    result = 0
    for i in lista:
        if len(i) > 2 and i[-1] == i[-2]:
            result += 1
    return result


l = ['casa', 'masass', 'el', 'm', 'custee']

print(macheos(l))


def first_x(s):
    return s[0] == 'x'


def front_x(lista):
    x_list = []
    for i in lista:
        if first_x(i):
            x_list.append(i)
            lista.remove(i)
    lista.sort()
    x_list.extend(lista)
    return x_list


lista = ['mix', 'xyz', 'apple', 'xerox', 'bastian', 'aaron']
print(front_x(lista))


def last_t(s):
    return s[0] == 'x'


def sort_last(tuplas):
    return sorted(tuplas, key=lambda tup: tup[-1])


t = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(sort_last(t))


def tabla(n):
    i = 0
    while i <= 10:
        print(str(n) + '*' + str(i) + "=" + str(i * n))
        i += 1


tabla(7)


def mapeo(s):
    d = {}
    l = list(s)
    i = 0
    for _ in l:
        d[l[i]] = i
        i += 1
    print d


mapeo('white')


def busqueda_reversa(d, val):
    for n in d:
        if d[n] == val:
            print(n)


d = {'c': 2, 'e': 1, 's': 2, 'a': 3}
busqueda_reversa(d, 3)


def invitados(lista):
    for n in lista:
        if lista[n] == 'Asistira':
            print(n)


lista_invitados = {'Maria': 'Asistira', 'Luis': 'Asistira',
                   'Angel': 'No Asistira', 'Pedro': 'Asistira',
                   'Carla': 'Asistira'}

invitados(lista_invitados)
