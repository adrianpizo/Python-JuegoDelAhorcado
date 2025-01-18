
def definirPalabraSecreta():
    defineLaPalabra=input('Escribe una palabra que será Secreta: ').lower()
    return defineLaPalabra

def avanceDelJuego(laPalabraSecreta, coincidenciaEnLetras):
    letrasQueVaAdivinando=''

    for letra in laPalabraSecreta:
        if letra in coincidenciaEnLetras:
            letrasQueVaAdivinando+=letra
        else:
            letrasQueVaAdivinando+="_"

    return letrasQueVaAdivinando

def elJuegoEmpieza():
    laPalabraSecreta=definirPalabraSecreta()
    coincidenciaEnLetras=[]
    intentosDisponibles=5
    finDelJuego=False

    print('¡BIENVENIDOS AL JUEGO DEL AHORCADO!!')
    print(f'...Tienes {intentosDisponibles} intentos para Adivinar...')
    print(avanceDelJuego(laPalabraSecreta, coincidenciaEnLetras), ' tiene', len(laPalabraSecreta), 'letras')

    while not finDelJuego and intentosDisponibles>0:
        letrasParaAdivinar=input('Ingerese una letra del abecedario: ').lower()
        if len(letrasParaAdivinar)!=1 or not letrasParaAdivinar.isalpha():
            print('Ingresar Una Letra Correcta del abecedario!')
        elif letrasParaAdivinar in coincidenciaEnLetras:
            print(f'Ingresar otra letra!. La letra {letrasParaAdivinar} ya la utilizaste!')
        else:
            coincidenciaEnLetras.append(letrasParaAdivinar)

            if letrasParaAdivinar in laPalabraSecreta:
                print(f'PERFECTO!. La letra {letrasParaAdivinar} está en la palabra Secreta')
            else:
                intentosDisponibles-=1
                print(f'¡ERROR!!. La letra "{letrasParaAdivinar}", no está en la palabra')
                print(f'Te quedan "{intentosDisponibles}" intentos')
        
        ComoVaElJuego=avanceDelJuego(laPalabraSecreta, coincidenciaEnLetras)
        print(ComoVaElJuego)

        if '_' not in ComoVaElJuego:
            finDelJuego=True
            laPalabraSecreta=laPalabraSecreta
            print(f'¡GANASTE!!. Completaste la palabra "{laPalabraSecreta}"')

    if intentosDisponibles==0:
        laPalabraSecreta=laPalabraSecreta
        print(f'¡PERDISTE!!. La palabra secreta era "{laPalabraSecreta}"')
elJuegoEmpieza()