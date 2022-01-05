########################################################################
#Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
#Fecha de creación: 17/06/20 21:00 
#Última modificación: 17/06/2020 21:05
#Versión: 3.8.2
########################################################################

#Funciones de la tarea programada 1 - criptografía de datos 

########################################################################

#Funciones reto 1 - Cifrado César:

def decifradoCesar(frase, abecedario):
    """
    Funcionalidad: Devuelve tres letras el código para saber la frase inicial.
    Entradas: La frase codificada y el abecedario.
    Salidas: La frase de una forma entendible.
    """
    fraseNueva="" #Se crea la frase nueva
    for letra in frase: #Para cada letra en la frase
        if letra==" ": #Si es un espacio
            fraseNueva=fraseNueva+letra #Agrega el espacio a la frase cifrada
        else: #Si es una letra
            posicion=abecedario.find(letra) #Encuentra la posición de la letra actual del mensaje en el abecedario
            if posicion<=2: #Si la posición es menor o igual a 2, significa que se sale del rango de posiciones del abecedario
                nueva=letra.replace(letra,abecedario[posicion+23]) #Suma 23 para quedar en una posición válida
            else: #Si está dentro del rango de posiciones del abecedario
                nueva=letra.replace(letra,abecedario[posicion-3]) #Corre la posición de la letra 3 lugares hacia atrás
            fraseNueva=fraseNueva+nueva #Le agrega a la frase nueva la letra decifrada
    return fraseNueva #Retorna la frase decifrada

def cifradoCesar(frase,abecedario):
    """
    Funcionalidad: Avanza tres letras el código para cifrarlo.
    Entradas: La frase y el abecedario.
    Salidas: La frase codificada.
    """
    fraseNueva="" #Se crea la frase nueva
    for letra in frase: #Para cada letra en la frase
        if letra==" ": #Si es un espacio
            fraseNueva=fraseNueva+letra #Agrega el espacio a la frase cifrada
        else: #Si es una letra
            posicion=abecedario.find(letra) #Encuentra la posición de la letra actual del mensaje en el abecedario
            if posicion>=23: #Si la posición es mayor o igual a 23, significa que se sale del rango de posiciones del abecedario
                nueva=letra.replace(letra,abecedario[posicion-23]) #Resta 23 para quedar en una posición válida
            else: #Si está dentro del rango de posiciones del abecedario
                nueva=letra.replace(letra,abecedario[posicion+3]) #Corre la posición de la letra 3 lugares hacia adelante
            fraseNueva=fraseNueva+nueva #Le agrega a la frase nueva la letra cifrada
    return fraseNueva #Retorna la frase cifrada

########################################################################

#Funciones reto 2 - Cifrado llave:

def decifradoLlave(frase,abc,llave):
    """
    Funcionalidad: Utiliza la llave y el texto codificado para saber el mensaje real.
    Entradas: La frase codificada, la llave y el abecedario.
    Salidas: La frase de una forma entendible.
    """
    iLlave=0 #Se le asigna 0 a iLlave
    fraseNueva="" #Se crea fraseNueva
    for letra in frase: #Para cada caracter en la frase
        if letra==" ": #Si es igual a un espacio
            iLlave=0 #iLlave en 0, para iniciar de nuevo la palabra llave
            fraseNueva+=letra #A la frase nueva se le agrega el espacio
        else: #Si es una letra
            valorLetra=abc.find(letra)+1 #Encuentra el valor de la letra actual del mensaje
            valorLlave=abc.find(llave[iLlave])+1 #Encuentra el valor de la letra actual de la llave
            resta=valorLetra-valorLlave #Suma ambos valores
            if resta<1: #Si el valor se sale del rango de valores posibles dentro del abecedario
                resta=resta+26 #Le suma 26 para encontrar un valor válido
                fraseNueva+=abc[resta-1] #Agrega al mensaje la letra con el valor nuevo
            else: #Si el valor está dentro del rango
                fraseNueva+=abc[resta-1] #Agrega al mensaje la letra con el valor 
            iLlave+=1 #Aumenta en 1 la posición de la llave
        if iLlave==len(llave): #Si ya se llegó al final de la llave
            iLlave=0 #Vuelve a iniciar en la posición 0 de la llve
    return fraseNueva #Retorna el mensaje decifrado

def cifradoLlave(frase,abc,llave):
    """
    Funcionalidad: Utiliza la llave y el texto para codificarlo.
    Entradas: La frase codificada, la llave y el abecedario.
    Salidas: La frase codificada.
    """
    iLlave=0 #Se le asigna 0 a iLlave
    fraseNueva="" #Se crea fraseNueva
    for letra in frase: #Para cada caracter en la frase
        if letra==" ": #Si es igual a un espacio
            iLlave=0 #iLlave en 0, para iniciar de nuevo la palabra llave
            fraseNueva+=letra #A la frase nueva se le agrega el espacio
        else: #Si es una letra
            valorLetra=abc.find(letra)+1 #Encuentra el valor de la letra actual del mensaje
            valorLlave=abc.find(llave[iLlave])+1 #Encuentra el valor de la letra actual de la llave
            suma=valorLetra+valorLlave #Suma ambos valores
            if suma>26: #Si el valor se sale del rango de valores posibles dentro del abecedario
                suma=suma-26 #Le resta 26 para encontrar un valor válido
                fraseNueva+=abc[suma-1] #Agrega al mensaje la letra con el valor nuevo
            else: #Si el valor está dentro del rango
                fraseNueva+=abc[suma-1] #Agrega al mensaje la letra con el valor 
            iLlave+=1 #Aumenta en 1 la posición de la llave
        if iLlave==len(llave): #Si ya se llegó al final de la llave
            iLlave=0 #Vuelve a iniciar en la posición 0 de la llve
    return fraseNueva #Retorna el mensaje cifrado

########################################################################

#Funciones reto 3 - Cifrado vigeneré:

def cortarNumero(pnumero):
    """
    Funcionalidad: Dividir el número en dos partes. 
    Entrada: El número int(pnumero).
    Salida: El número cortado int(num1, num2).
    """
    contador=0
    num1=0
    num2=0
    div=0
    while pnumero>0:
        contador+=1
        div=pnumero%10
        if(contador==1):
            num2=div
        else:
            num1=div
        pnumero //= 10
    return num1, num2

def descifrarVigenere(pfrase,pnumero,abecedario):
    """
    Funcionalidad: Descifrar el código mediante el método Vigenere.
    Entrada: La frase str(pfrase) y el número int(pnumero).
    Salida: La nueva frase descifrada list[fraseL].
    """
    frase=" "
    contador2=0
    for palabra in pfrase: #Recorre la lista con las palabras.
        numero=cortarNumero(pnumero) #Función que divide el número en dos.
        valor1=numero[0]
        valor2=numero[1]
        contador=0
        for letra in palabra: #Recorre cada letra de la palabra.
             indice=abecedario.find(letra)    
             if(contador==0): #Si el contador está en cero.
                indice-=valor1 #Al índice se le resta el valor que es el número [0].
                contador=1 #Se le suma uno a contador.
             else:
                indice-=valor2 #Al índice se le resta el valor que es el número [1].
                contador=0 #Se iguala a 0 el contador.
             if(indice<0):
                 indice=25+indice
             frase+=abecedario[indice] #Iguala a frase la letra con el índice definido anteriormente.
        frase=frase+" "
    return frase

def cifrarVigenere(pfrase,pnumero,abecedario):
    """
    Funcionalidad: Cifrar el código mediante el método Vigenere.
    Entrada: La frase str(pfrase) y el número int(pnumero).
    Salida: La nueva frase cifrada list[fraseL].
    """
    frase=" "
    for palabra in pfrase: #Recorre la lista con las palabras.
        numero=cortarNumero(pnumero) #Función que divide el número en dos.
        valor1=numero[0]
        valor2=numero[1]
        contador=0
        for letra in palabra: #Recorre cada letra de la palabra.
                indice=abecedario.find(letra)
                if(contador==0): #Si el contador está en cero.
                    indice+=valor1 #Al índice se le suma el valor que es el número [0].
                    contador=1 #Se le suma uno a contador.
                else: 
                    indice+=valor2 #Al índice se le suma el valor que es el número [1].
                    contador=0 #Se iguala a 0 el contador.
                if(indice>25): #Si el índice es mayor a 25.
                    indice=indice-25 #Le resta 25 al índice.
                frase+=abecedario[indice] #Iguala a frase la letra con el índice definido anteriormente.
        frase+=" "
    return frase

########################################################################

#Funciones reto 4 - XOR:

def encontrarASCII(plista):
    """
    Funcionalidad: Encuentra la letra asignada a ese valor númerico.
    Entrada: La lista (plista).
    Salida: La lista final con las letras asignadas y guiones en medio (listaFinal).
    """
    listaFinal="" 
    guion=""
    for indice in plista: #Recorre cada índice almacenado de la lista.
        indice=chr(indice) #Lo convierte a ASCII hexadecimal.
        listaFinal+=guion+indice #Se adjunta el valor a listaFinal.
        guion="-"
    return listaFinal

def descifrarXOR(pfrase,pclave):
    """
    Funcionalidad: Descifrar el código mediante el método XOR
    Entrada: La frase str(pfrase) y la palabra clave (pclave).
    Salida: La nueva pfrase descifrada.
    """
    frase=""
    indice=0
    ejemploXOR="\x5C"+"\x78"
    for letra in pfrase:
        try:
            if(letra[0]+letra[1]==ejemploXOR): #Si el primer y segundo caracter coincide con "\x" entonces:
                letra = letra[2]+letra[3] #La letra toma los valores numéricos posicionados en [2],[3].
                letra = chr(int(letra,16)) #Convierte el valor númerico hexadecimal a decimal y saca su valor alfabético.
                letra = int(ord(letra)) #Este caracter alfabético se procesa con el ord y se saca su valor númerico. 
            elif(letra[1]=="n"):        #Si el segundo caracter coincide con la "n".
                letra = int(ord('\n'))  #Este caracter alfabético se procesa con el ord y se saca su valor númerico.
            elif(letra[1]=="r"):        #Si el segundo caracter coincide con la "r".
                letra = int(ord('\r'))  #Este caracter alfabético se procesa con el ord y se saca su valor númerico. 
        except:
            letra = list(letra)     #Si es únicamente una letra
            letra = letra[0]        #Letra es igual a letra[0] 
            letra = int(ord(letra)) ##Este caracter alfabético se procesa con el ord y se saca su valor númerico.
            
        num=ord(pclave[indice])#Este caracter alfabético se procesa con el ord y se saca su valor númerico, de acuerdo al índice de la palabra clave.
        caracter = letra^num    #Se saca el XOR. 
        indice+=1               #Se suma uno al índice. 
        if(indice==len(pclave)):#Si el índice es más grande que el largo de la palabra clave.
            indice=0            #El índice se iguala a cero.     
        frase+=str(chr(caracter))
    return frase
        
def cifrarXOR(pfrase,pclave):
    """
    Funcionalidad: Cifrar el código mediante el método XOR.
    Entrada: La frase str(pfrase) y la palabra clave (pclave).
    Salida: La nueva frase cifrada listaFinal.
    """
    index=0
    indiceXOR=0
    indiceLista=[]
    listaFinal=[]
    for letra in pfrase:            #Para cada letra de la frase.
        indice=ord(letra)           #Convierte al valor númerico ASCII.
        indice2=ord(pclave[index])  #Convierte al valor númerico ASCII a la letra de la clave según el índice.
        indiceXOR=(indice ^ indice2) #Saca el XOR.
        indiceLista.append(indiceXOR)#Adjunta el valor del XOR a una lista.
        index+=1                     #Le suma uno al índice para que que pclave avance letra por letra.
        if(index==(len(pclave))):    #Si el índice es igual al largo de la clave, entonces se reinicia.
            index=0 
    listaFinal.append(encontrarASCII(indiceLista)) #Se adjunta a la lista los valores ASCII hexadecimales convertidos
                                                   #por la funcion encontrarASCII.
    return (str(listaFinal).strip('[]').strip("''")) #Se le quitan paréntesis cuadrados y comillas.

########################################################################

#Funciones reto 5 - Palabra inversa:

def cifrarPalabraInverso(pfrase):
    """
    Funcionalidad: Cifrar y descifrar el mensaje de forma inversa.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase inversa. 
    """
    inverso="" 
    inverso2=""
    for palabra in pfrase: #Recorre la frase palabra, por palabra.
        inverso=" "+inverso #Se le adjunta un espacio e inverso a la variable string inverso.
        for letra in palabra: #Recorre cada letra de cada palabra.
            inverso=letra+inverso #Se le adjunta la letra a la variable string inverso.
    inverso=inverso.split(' ') #Se divide el string por cada espacio vacío.
    for valor in inverso: #Se recorre cada uno de los valores inversos.
            inverso2=valor+" "+inverso2 #Se le da vuelta a los valores adjuntando a una variable string inverso2.
    return inverso2

########################################################################

#Funciones reto 6 - Mensaje inverso:

def cifrarMensajeInverso(mensaje):
    """
    Funcionalidad: Darle vuelta a una frase o palabra entera.
    Entrada: La frase o palabra.
    Salida: El mensaje entero invertido.
    """
    fraseNueva="" #Se crea la frase nueva
    for letra in mensaje: #Para cada letra en el mensaje ingresado
            fraseNueva=letra+fraseNueva #Agrega la letra actual al frente de frase nueva
    return fraseNueva #Retorna la frase nueva
 
########################################################################

#Funciones reto 7 - Cifrado telefónico:

def decifradoTelefono(mensaje,abecedario):
    """
    Funcionalidad: Reemplaza las combinaciones de números por las letras correspondientes.
    Entradas: El mensaje cifrado.
    Salidas: El mensaje decifrado.
    """
    codigo="" #Se crea el mensaje
    contador=0 #Se inicia un contador en 0 para las posiciones del código
    while contador<len(mensaje): #Mientras que el contador sea menor al largo del código ingresado
        if mensaje[contador]=="*": #Si lo de la posición es un asterisco
            codigo+=" " #Agregar como un espacio al mensaje
            contador+=1 #Aumenta en 1 el contador para continuar con la siguiente posición
        elif mensaje[contador]==" ": #Si lo de la posición es un espacio
            contador+=1 #Aumenta en 1 el contador para continuar con la siguiente posición
        else: #Si es un número
            posicion=int(mensaje[contador])-2 #Encuentra la posición de la lista del abecedario en la que se encuentran las letras de ese número
            letras=abecedario[posicion] #Saca el grupo de letras
            letra=int(mensaje[contador+1])-1 #Encuentra la posición de la letra que corresponde al número siguiente
            codigo+=letras[letra] #Agrega la letra que corresponde al mensaje
            contador+=2 #Aumenta en 2 el contador para continuar con el siguiente número que corresponde a una tecla del teléfono
    return codigo #Retorna el mensaje decifrado

def cifradoTelefono(mensaje,abecedario):
    """
    Funcionalidad: Reemplaza las letras por las combinaciones de números correspondientes.
    Entradas: El mensaje.
    Salidas: El mensaje cifrado.
    """
    codigo="" #Se crea el código
    for letraMensaje in mensaje: #Para cada letra o espacio en el mensaje
        if letraMensaje==" ": #Si lo de la posición es un espacio
            codigo+="*"+letraMensaje #Agrega un asterisco y un espacio al código
        else: #Si es una letra
            for letra in abecedario: #Para cada grupo de letras en la lista abecedario
                tecla=letra.find(letraMensaje) #Busca la letra actual en el grupo de letras actual
                if tecla>=0: #Si la letra se encuentra en el grupo de letras actual
                    posicion=str(abecedario.index(letra)+2) #Encuentra el número de la posición
                    #del grupo de letras en el abecedario y le suma dos para indicar la tecla
                    veces=str(tecla+1) #Define la cantidad de veces que hay que presionar esa tecla 
                    codigo+=posicion+veces+" " #Le agrega al código la tecla, las veces que se debe presionar y un espacio
    return codigo #Retorna el mensaje cifrado

########################################################################

#Funciones reto 8 - Binario:

def cifrarBin(pfrase,abecedario):
    """
    Funcionalidad: Cifrar el código mediante el binario.
    Entrada: La frase ingresada (pfrase).
    Salida: La frase convertida a binario letra por letra. 
    """
    binario=""
    asterisco=""
    for palabra in pfrase: #Recorre palabra por palabra la frase.
        binario=binario+asterisco #Se adjunta a la variable binario la variable asterisco por cada palabra nueva.
        for letra in palabra: #Se recorre cada letra de cada palabra.
            indice=abecedario.find(letra) #Busca la letra encontrada y devuelve el índice.
            if(indice!=-1):
                binario=binario+" "+bin(indice)[2:].zfill(5) #Se adjunta el número binario modificado a 5 cifras. 
                asterisco=" * " #Se iguala asterisco a " * ".
    return binario

def descifrarBin(pfrase,abecedario):
    """
    Funcionalidad: Descifra el mensaje en binario.
    Entrada: La frase ingresada (pfrase) en binario.
    Salida: La frase decodificada del binario (frase).
    """
    frase=""
    for binario in pfrase: #Recorre palabra por palabra la frase.
        if(binario != "*" and binario != ""): #Si binario es diferente a asterisco y el espacio.
            binario=int(binario,2) #Convierte el binario a un entero decimal.
            for indice,letraABC in enumerate(abecedario): #Recorre la lista abecedario con su índice.
                if(binario==indice): #Compara el número con el índice.
                   frase+=abecedario[indice] #Muestra la frase decodificada.
                if(binario>25 or binario<0):
                    frase="ninguno. El valor binario ingresado es diferente los índices del abecedario."         
        else:
            frase+=" "       
    return frase

