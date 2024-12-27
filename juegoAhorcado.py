import random


def palabraSecretasMarcas() ->str:
    listaDePalabraSecreta=['fruco','aromatel','barrigon','3d','coco','dove','fab','vasenol','ego','savital','savital']
    return random.choice(listaDePalabraSecreta)

def mostrarAvance(palabraSecreta, letrasQueCoinciden):
    LoQueVaAdivinando=''

    for letras in palabraSecreta:
        if letras in letrasQueCoinciden:
            LoQueVaAdivinando+=letras
        else:
            LoQueVaAdivinando+='_'
    return LoQueVaAdivinando


def empezarJuego():
    palabraSecreta=palabraSecretasMarcas()
    letrasQueCoinciden=[]
    intentosARealizar=5
    juegoTerminado=False

    print('BIENVENIDO AL JUEGO DEL AHORCADO!!')
    print(f'Tienes {intentosARealizar} intentos para Adivinar!')
    print(mostrarAvance(palabraSecreta, letrasQueCoinciden), 'Tiene', len(palabraSecreta), 'letras')

    while not juegoTerminado and intentosARealizar > 0:
        letraIngresaadaParaAdvinar=input('Por favor, ingrese una letra: ').lower()

        if len(letraIngresaadaParaAdvinar) != 1 or not letraIngresaadaParaAdvinar.isalpha():
            print('Ingrese una letra válida (A-Z)')
        elif letraIngresaadaParaAdvinar in letrasQueCoinciden:
            print(f'La letra "{letraIngresaadaParaAdvinar}" ya la has utilizado. Ingresa otra!! ')
        else:
            letrasQueCoinciden.append(letraIngresaadaParaAdvinar)

            if letraIngresaadaParaAdvinar in palabraSecreta:
                print(f'¡CORRECTO!. La letra "{letraIngresaadaParaAdvinar}", está dentro de la palabra Secreta')
            else:
                intentosARealizar-=1
                print(f'MAL Hecho!. La letra "{letraIngresaadaParaAdvinar}", no está en la palabra secreta')
                print(f'Te quedan solo {intentosARealizar} intentos')

        avanceActual=mostrarAvance(palabraSecreta, letrasQueCoinciden)
        print(avanceActual)

        if '_' not in avanceActual:
            juegoTerminado = True
            palabraSecreta=palabraSecreta.upper()
            print(f'FELICITACIONES!!. La palabra completa es: "{palabraSecreta}"')
    
    if intentosARealizar==0:
        palabraSecreta=palabraSecreta.upper()
        print(f'PERDISTE!. La palabra correcta era: "{palabraSecreta}"')

empezarJuego()