def prog32():
    print('==================')
    print(' tipo de licencia')
    print('==================')

    edad =int(input('ingrese edad:'))

    print()

    if 16 == edad == 17 :
        print('-> licencia de menor')
        
    elif 18<= edad <= 65 :
        print('-> licencia de adulto')
           
    elif edad > 65 :
        print('-> licencia de adulto mayor')
        
    else:
        print('-> espere la edad')
           
           
    
    