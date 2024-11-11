def inp ():
        while True:
            try:
                tamaño = int(input("¿Cuántos elementos quieres ordenar? "))
                if tamaño > 0:
                    break
                else:
                    print("Por favor, ingresa un número entero positivo.")
            except ValueError:
                print("Por favor, introduce un número entero.")

        lista = []
        print("Introduce los elementos para ordenar (números o palabras):")
        for _ in range(tamaño):
            entrada = int(input("Elemento: "))

            lista.append(entrada)

        return lista


def quicksort(arreg):

    if len(arreg) <= 1:
        print(arreg)
        return arreg
    else:
        apunt = arreg[0]
        left = [i for i in arreg[1:] if i < apunt]
        right = [j for j in arreg[1:] if j >= apunt]
        print(arreg)
        return quicksort(left) + [apunt] + quicksort(right)

def shellsort(lista):

    incremento = len(lista) // 2
    while incremento > 0:
        for i in range(incremento, len(lista)):
            j = i
            temporal = lista[i]
            while j >= incremento and lista[j - incremento] > temporal:
                lista[j] = lista[j - incremento]
                j -= incremento
            lista[j] = temporal
        if incremento == 2:
            incremento = 1
        else:
            incremento = int(incremento / 2.2)
    
    return lista

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1  
    right = 2 * i + 2 

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        print(f"Intercambiando: {arr}")
        heapify(arr, n, largest) 

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"Heap después de heapify en el índice {i}: {arr}")

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        print(f"Intercambiando {arr[0]} y {arr[i]}. Lista después del intercambio: {arr}")
        heapify(arr, i, 0)  
        print(f"Lista después de heapify con tamaño {i}: {arr}")


hi=True
a=inp()
size = len(a)

print(a)
b= quicksort(a)
print(f"Sorted Array in Ascending Order: {b}")

while (hi):
    sort=input("A- Quicksort    B-Shellsort     C-Radix     D-Helix")

    if sort=="A":
        b= quicksort(a)
        print(f"Sorted Array in Ascending Order: {b}")
        
    if sort =="B":
        d= shellsort(a)
        print(f'Sorted Array in Ascending Order:{d}')

    if sort =="C":
        e= radix_sort(a)
        print(f'Sorted Array in Ascending Order:{e}')

    if sort=="D":
        print(f"Lista original: {a}")
        heap_sort(a)
        print(f"Lista ordenada: {a}")
