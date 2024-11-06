# Segundo entregable
# Convertidor de relog de manecillas a hora normal.
def inputs(pregunta):
    ask = input(pregunta)
    x = False
    while x == False:
        try:
            ask = int(ask)
            x = True
        except:
            x == False
        if x == True:
            return(ask)
        else:
            ask = input("Lo anteriormente digitado no es un numero. Intente de nuevo: ")

def leer_hora():
    man_corta = inputs("A donde apunta la manecilla corta: ")
    while man_corta > 12 or man_corta <= 0 :

        man_corta = inputs("El numero que usted digito no existe en un relog de manecillas. Intente de nuevo: ")
    return(man_corta)

def leer_min():
    man_larga = inputs("A donde apunta la manecilla larga: ")
    while man_larga > 12 or man_larga <= 0 :
        print("El numero que usted digito no existe en un relog de manecillas.")
        man_larga = inputs("A donde apunta la manecilla larga: ")
    minutos = man_larga*5
    if minutos == 60:
        minutos = "00"
    elif minutos == 5:
        minutos = "05"
    return minutos

def main():
    print("Digite lo que se le solicita")
    hora = leer_hora()
    minutos = leer_min()
    print(f"La hora es: {hora}:{minutos}")
    
main()