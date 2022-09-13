#Menu
def menu():
    consulta = input("\nEscoja que desea hacer: \n"
                     + "1 - Binario a decimal \n"
                     + "2 - Decimal a binario \n"
                     + "0 - Salir \n")
    
    if int(consulta) == 1:
        convertir_bin_dec()
    elif int(consulta) == 2:
        convertir_dec_bin()
    elif int(consulta) == 0:
        return
    else:
        menu()

#Convertir binario a decimal
def binario_a_decimal(numero_binario):
    suma = 0
    contador = len(numero_binario)

    for c in numero_binario:
        contador -= 1
        suma += (2**contador) * int(c)
        
    return suma

def convertir_bin_dec():
    numero_binario = input("\nIngrese el numero en forma binario: ")
    resultado = binario_a_decimal(numero_binario)
    print(resultado)
    menu()


#Convertir decimal a binario
def decimal_a_binario(numero_decimal):
    
    contador = 0
    bandera = True
    
    while(bandera == True):
        if((2**contador) >= numero_decimal):
            bandera = False
        else:
            contador += 1
        
    numero = numero_decimal
    resultado = ''
    
    if contador != 0:
        contador -= 1
    
    while(contador >= 0):
        
        if(numero >= 2**contador):
            numero = numero - (2**contador)
            resultado += '1'
        elif(numero<2**contador):
            resultado += '0'
        
        contador -=1
    
    return resultado

def convertir_dec_bin():
    numero_decimal = int(input("\nIngrese el numero en decimal: "))
    resultado = decimal_a_binario(numero_decimal)
    print(resultado)
    menu()

#Ejecutable
menu()