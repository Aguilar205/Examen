def prog51():
    print('_________________________________________')
    print(' Sumar los primeros N números naturales')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')

    val = int(input('ingrese un valor entero: '))
    print()

    can = 0
    for i in range(1, val + 1):
        can += i
        print('=> lo numeros',can)

    print()
    print(f"La suma de los primeros {val} números naturales es: {can}")
    print('____________________________________________________________')
