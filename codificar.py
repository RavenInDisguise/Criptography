############################################################################
#Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
#Fecha de creación: 14/06/2020 15:25 
#Última modificación: 19/06/2020 21:50
#Versión: 3.8.2
############################################################################

#Importación de librerías:

from codificarLibreria import*
import re
import sys

############################################################################
def validarFraseTildes(frase):
    """
    Funcionalidad: Valida que sea str.
    Entradas: Frase.
    Salidas: True (es correcto) o False (es incorrecto).
    """
    for i in frase:
        if i.isalpha():
            continue
        else:
            return False
    return True
def continuar(abc,abc1):
    """
    Funcionalidad: Saber si continuar o no.
    Entradas: La respuesta (seguir).
    Salidas: Vuelve a ingresar código o acaba.
    """
    while True:
        try:
            seguir=input("\n~¿Desea hacer otra encriptación? (Sí/No) ")
            seguir=seguir.lower().strip()
            if validarFraseTildes(seguir):
                if seguir=="si" or seguir=="sí":
                    return menuPrincipal(abc,abc1)
                elif seguir=="no":
                    print("\n~Gracias por utilizar nuestros servicios, vuelva pronto.~")
                    return False
                else:
                    print("Ingrese Si/No ")
                    continue
            else:
                print("Ingrese una opción válida.")
                continue
        except:
            print("Ingrese una opción válida.")
            continue
    sys.exit()

def validarClave(pclave):
    """
    Funcionalidad: Validar si la clave tiene una palabra.
    Entrada: La clave str(pclave).
    Salida: True/False, dependiendo del resultado. 
    """
    pclave=pclave.split(' ')
    if(len(pclave)==1):
        return True
def validarBin(pbinario):
    """
    Funcionalidad: Valida que el número sea binario.
    Entradas: Frase.
    Salidas: True (es correcto) o False (es incorrecto).
    """
    pbinario=pbinario.split(" ")
    contador=0
    for palabra in pbinario:
        if re.findall("[2-9]+", palabra):
            contador+=1
        if(re.findall("[a-zA-Z]+", palabra)):
            contador+=1
        if(re.findall("[^a-zA-Z0-9_ ^\*]", palabra)):
            contador+=1
    if(contador==0):
        return True
    
def validarCodigo(frase):
    """
    Funcionalidad: Valida que sean números y/o asteriscos.
    Entradas: Frase.
    Salidas: True (es correcto) o False (es incorrecto).
    """
    
    for i in range(len(frase)):
        if re.match(r"([2-9][1-4]\s)",frase):
            frase=frase.replace(frase[:3],"")
        elif frase[0]=="*" and frase[1]==" ":
            frase=frase.replace(frase[:2],"")
        else:
            return False
        if len(frase)==2 and re.match(r"([2-9][1-4])",frase):
            return True

def validarDatos1(pnumero):
    """
    Funcionalidad: Validar que el número sea mayor o igual que 10 y menor que 99.
    Entrada: El número int(pnumero).
    Salida: True/False.
    """
    if(10<=pnumero<=99):
        return True

def validarFrase(frase):
    """
    Funcionalidad: Valida que sea str.
    Entradas: Frase.
    Salidas: True (es correcto) o False (es incorrecto).
    """
    if re.match(r"^[a-zA-Z\s]+$",frase):
        return True
    else:
        return False
def menuDeCifrarMensaje():
    """
    Funcionalidad: Mensaje del menú.
    Entradas: Ninguna.
    Salidas: El mensaje de las opciones.
    """
    print("""\n¿Qué acción desea realizar?\n
        1. Cifrar
        2. Descifrar""")
    
def menuDeCifrar(opcion):  
    """
    Funcionalidad: Menu para cifrar o decifrar.
    Entradas: La opción (1 o 2).
    Salidas: La función correspondiente.
    """
    if (opcion==1 or opcion==2):
        return True, opcion
    else:
        return False, opcion
    
def ingresarDatos1(abc):
    """
    Funcionalidad: Cifrar y descifrar un mensaje según el cifrado César.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase cifrada/descifrada, según desee. 
    """
    flag=True
    while True:
        try:
            print("\n~Bienvenido al programa que encripta y desencripta por cifrado César:")
            menuDeCifrarMensaje()
            opcion=int(input("\nIngrese la acción que desea realizar: "))
            salida=menuDeCifrar(opcion)
            if(salida[0]==True):
                while flag:
                    frase=str(input("\nIngrese su frase únicamente con letras y espacios (sin la ñ): "))
                    frase=frase.lower().strip()
                    if validarFrase(frase):
                        if(salida[1]== 1):
                            print("Su código cifrado es: "+str(cifradoCesar(frase,abc)))
                        else:
                            print("Su código descifrado es: "+str(decifradoCesar(frase,abc)))
                        return False   
                    else:
                        print("Ingrese una frase válida únicamente con sólo letras, sin tildes, caracteres extraños, ni ñ.")
                        continue
            else:
                 print("Opción inexistente. Ingrese otra.")
                 continue
        except:
            print("El valor ingresado es incorrecto, ingrese un número entero.")
            continue
            
def ingresarDatos2(abc):
    """
    Funcionalidad: Cifrar y descifrar un mensaje según el cifrado llave.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase cifrada/descifrada, según desee. 
    """
    flag=True
    flag2=True
    while True:
        try:
            print("\n~Bienvenido al programa que encripta y desencripta por cifrado llave:")
            menuDeCifrarMensaje()
            opcion=int(input("\nIngrese la acción que desea realizar: "))
            salida=menuDeCifrar(opcion)
            if(salida[0]==True):
                while flag:
                        frase=str(input("\nIngrese su frase únicamente con letras y espacios (sin la ñ): "))
                        frase=frase.lower().strip()
                        if validarFrase(frase):
                            while flag2:
                                llave=str(input("\nIngrese su llave (1 palabra): "))
                                llave=llave.lower().strip()
                                if validarClave(llave) and validarFrase(llave):
                                    if(salida[1]== 1):
                                        print("Su código cifrado es: "+str(cifradoLlave(frase,abc,llave)))
                                    else:
                                        print("Su código descifrado es: "+str(decifradoLlave(frase,abc,llave)))
                                    return False
                                else:
                                    print("Ingrese una llave válida de una sola palabra con sólo letras y espacios (sin la ñ).")
                                    flag2=True
                        else:
                            print("Ingrese una frase válida únicamente con sólo letras, sin tildes, caracteres extraños, ni ñ.")
                            flag=True
            else:
                print("Opción inexistente. Ingrese otra.")
                continue
        except:
            print("El valor ingresado es incorrecto, ingrese un número entero.")
            continue

def ingresarDatos3(abc):
    """
    Funcionalidad: Cifrar y descifrar un mensaje según sustitución Vigenére.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase cifrada/descifrada, según desee. 
    """    
    flag=True
    flag2=True
    while True:
        try:
            print("\n~Bienvenido al programa que encripta y desencripta por sustitución Vigeneré:")
            menuDeCifrarMensaje()
            opcion=int(input("\nIngrese la acción que desea realizar: "))
            salida=menuDeCifrar(opcion)
            if(salida[0]==True):
                while flag:
                    numero=int(input("\nIngrese el número de dos cifras positivo con el que desea realizar la encriptación: "))
                    if(validarDatos1(numero)):
                        while flag2:
                            frase=input("\nIngrese su frase únicamente con letras y espacios (sin la ñ): ")
                            frase=frase.strip()
                            if(validarFrase(frase)):
                                frase=frase.lower().split(' ')
                                if(salida[1]== 1):
                                    print("Su código cifrado es: "+str(cifrarVigenere(frase,numero,abc)))
                                else:
                                    print("Su código descifrado es: "+str(descifrarVigenere(frase,numero,abc)))
                            else:
                                print("Ingrese una frase válida únicamente con sólo letras, sin tildes, caracteres extraños, ni ñ.")
                                continue
                            flag2=False
                            return flag2
                        
                        flag=False
                        return flag
                    
                    else:
                        print("Por favor, ingrese un número de dos cifras y positivo.")
                        continue
            else:
                print("Opción inexistente. Ingrese otra.")
                continue
                        
        except ValueError:
            print("El valor ingresado es incorrecto, debe ser un número entero.")
            continue
def ingresarDatos4():
    """
    Funcionalidad: Cifrar y descifrar un mensaje según la sustitución XOR - llave.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase cifrada/descifrada, según desee. 
    """ 
    flag=True
    flag2=True
    while True:
        try:
            print("\n~Bienvenido al programa que encripta y desencripta por sustitución XOR - llave:")
            menuDeCifrarMensaje()
            opcion=int(input("\nIngrese la acción que desea realizar: "))
            salida=menuDeCifrar(opcion)
            if(salida[0]==True):
                while flag:
                    llave=str(input("\nIngrese su llave (1 palabra): "))
                    llave=llave.lower().strip()
                    if (validarClave(llave) and validarFrase(llave)) :
                        while flag2:
                            if(salida[1]==1):
                                frase=str(input("\nIngrese su frase únicamente con letras y espacios (sin la ñ): "))
                                frase=frase.lower().strip()
                                if validarFrase(frase):
                                    print("Su código cifrado con guiones entre caracteres es: "+str(cifrarXOR(frase,llave)))
                                else:
                                    print("Ingrese una frase válida únicamente con letras, sin tildes, caracteres extraños, ni ñ.")
                                    continue
                                
                            elif(salida[1]==2):
                                frase2=str(input("\nIngrese su código con guiones entre caracteres hexadecimales ASCII: "))
                                frase2=frase2.lower().strip()
                                frase2 = frase2.split("-")
                                print("Su código descifrado es: "+str(descifrarXOR(frase2,llave)))
                            flag=False
                            return flag
                    else:
                        print("Ingrese una llave válida de una sola palabra con sólo letras y espacios(sin la ñ).")
                        continue
                    return False
                        
            else:
                print("Opción inexistente. Ingrese otra.")
                continue
        except ValueError:
            print("El valor ingresado es incorrecto, ingrese un número entero.")
            continue
        
def ingresarDatos5():
    """
    Funcionalidad: Cifrar y descifrar un mensaje según la sustitución de la palabra inversa.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase cifrada/descifrada, según desee. 
    """    
    while True:
        try:
            print("\n~Bienvenido al programa que encripta y desencripta por cifrado de palabra inversa:")
            menuDeCifrarMensaje()
            opcion=int(input("\nIngrese la acción que desea realizar: "))
            salida=menuDeCifrar(opcion)
            if(salida[0]==True):
                frase=input("\nIngrese su frase: ")
                frase=frase.split(' ')
                if(salida[1]== 1):
                    print("Su código cifrado es: "+str(cifrarPalabraInverso(frase)))
                else:
                    print("Su código descifrado es: "+str(cifrarPalabraInverso(frase)))
            else:
                print("Opción inexistente. Ingrese otra.")
                continue
        
            return False
       
        except ValueError:
            print("El valor ingresado es incorrecto, ingrese un número entero.")
            continue
def ingresarDatos6():
    """
    Funcionalidad: Cifrar y descifrar un mensaje según la sustitución de mensaje inverso.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase cifrada/descifrada, según desee. 
    """    
    while True:
        try:
            print("\n~Bienvenido al programa que encripta y desencripta por cifrado de mensaje inverso:")
            menuDeCifrarMensaje()
            opcion=int(input("\nIngrese la acción que desea realizar: "))
            salida=menuDeCifrar(opcion)
            if(salida[0]==True):
                frase=input("\nIngrese su frase: ")
                frase=frase.strip()
                if(salida[1]== 1):
                    print("Su código cifrado es: "+str(cifrarMensajeInverso(frase)))
                else:
                    print("Su código descifrado es: "+str(cifrarMensajeInverso(frase)))
            else:
                print("Opción inexistente. Ingrese otra.")
                continue
        
            return False
       
        except ValueError:
            print("El valor ingresado es incorrecto, ingrese un número entero.")
            continue
        
def ingresarDatos7(abc1):
    """
    Funcionalidad: Cifrar y decifrar un mensaje mediante el código telefónico.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase cifrada/descifrada, según desee.
    """
    flag=True
    while True:
        try:
            print("\n~Bienvenido al programa que encripta y desencripta por cifrado telefónico:")
            menuDeCifrarMensaje()
            opcion=int(input("\nIngrese la acción que desea realizar: "))
            salida=menuDeCifrar(opcion)
            if(salida[0]==True):
                while flag:
                    if(salida[1]== 1):
                        frase=input("\nIngrese su frase únicamente con letras y espacios (sin la ñ): ")
                        frase=frase.lower().strip()
                        if(validarFrase(frase)):
                            print("Su código cifrado es: "+str(cifradoTelefono(frase,abc1)))
                        else:
                            print("Ingrese una frase válida únicamente con letras, sin tildes ni ñ.")
                            continue
                    else:
                        frase2=input("\nIngrese su código telefónico con parejas de números y/o asteriscos con espacios entre ellos: ")
                        frase2=frase2.lower().strip()
                        if(validarCodigo(frase2)):
                            print("Su código descifrado es: "+str(decifradoTelefono(frase2,abc1)))
                        else:
                            print("Ingrese un código telefónico válido según lo indicado en las instrucciones.")
                            continue
                    return flag==False
                return False
            else:
                print("Opción inexistente. Ingrese otra.")
                continue
        except ValueError:
            print("El valor ingresado es incorrecto, ingrese un número entero.")
            continue
        
def ingresarDatos8(abc):
    """
    Funcionalidad: Ingresar los datos de la sustitución binaria.
    Entrada: La frase str(frase) y la opción int(opcion).
    Salida: Las frases cifradas y descifradas por sustitución binaria. 
    """
    flag=True
    while True:
        try:
            print("\n~Bienvenido al programa que encripta y desencripta por sustitución binaria:")
            menuDeCifrarMensaje()
            opcion=int(input("\nIngrese la acción que desea realizar: "))
            salida=menuDeCifrar(opcion)
            if(salida[0]==True):
                while flag:
                    if(salida[1]== 1):
                        frase=input("\nIngrese su frase únicamente con letras y espacios (sin la ñ): ")
                        frase=frase.lower().strip()
                        if(validarFrase(frase)):
                            frase=frase.split(' ')
                            print("Su código cifrado es:"+str(cifrarBin(frase,abc)))
                        else:
                            print("Ingrese una frase válida únicamente con letras, sin tildes, caracteres extraños, ni ñ.")
                            continue
                    else:
                        frase2=input("\nIngrese su código binario divido por asteriscos entre palabras y con 5 valores binarios: ")
                        if(validarBin(frase2)):
                           frase2=frase2.split(' ')
                           print("Su código descifrado es: "+str(descifrarBin(frase2,abc)))
                        else:
                            print("Ingrese un número binario válido según lo indicado en las instrucciones.")
                            continue
                    flag=False   
                    return flag
                return False
            else:
                print("Opción inexistente. Ingrese otra.")
                continue
        except ValueError:
            print("El valor ingresado es incorrecto, ingrese un número entero.")
    
def menuPrincipal(abc,abc1):
    """
    Funcionalidad: Mostrar las opciones de tipos de cifrados y permitir elegir una.
    Entradas: La opción.
    Salidas: La función del cifrado deseado.
    """
    while True:
        try:
            print("""
 ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
                       ღ Menú Principal ღ
                                   
                1. Cifrado César.
                2. Cifrado por llave.
                3. Sustitución Vigenére.
                4. Sustitución XOR y llave.
                5. Palabra inversa.
                6. Mensaje inverso.
                7. Cifrado telefónico.
                8. Cifrado binario.
                9. Salir del programa.
 ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃""")
            opcion=int(input("\nIngrese el cifrado que desea realizar: "))
            if opcion==1:
                ingresarDatos1(abc)
                continuar(abc,abc1)
            elif opcion==2:
                ingresarDatos2(abc)
                continuar(abc,abc1)
            elif opcion==3:
                ingresarDatos3(abc)
                continuar(abc,abc1)
            elif opcion==4:
                ingresarDatos4()
                continuar(abc,abc1)
            elif opcion==5:
                ingresarDatos5()
                continuar(abc,abc1)
            elif opcion==6:
                ingresarDatos6()
                continuar(abc,abc1)
            elif opcion==7:
                ingresarDatos7(abc1)
                continuar(abc,abc1)
            elif opcion==8:
                ingresarDatos8(abc)
                continuar(abc,abc1)
            elif opcion==9:
                print("\n~Gracias por utilizar nuestros servicios, vuelva pronto.~")
                return False
            else:
                print("Opción inexistente. Ingrese otra.")
                continue
            return False
        except ValueError:
            print("El valor ingresado es incorrecto, ingrese un número entero.")
            continue
        
print("      ღ Bienvenido al programa de encriptación de mensajes ღ")
abc="abcdefghijklmnopqrstuvwxyz"
abc1=["abc","def","ghi","jlk","mno","pqrs","tuv","wxyz"]
menuPrincipal(abc,abc1)
