from typing import Dict, List, Tuple
from copy import deepcopy
import random

def intro() -> Tuple[str, str]:
    """
    Mostra la informació del joc. Explica com s'hi juga i què s'ha de fer.
    Demana el nom als jugadors i els retorna

    Retorna: Una parella de noms dels jugadors
    """
    jugador_1=''
    jugador_2=''
    jugador=[]
    print('Benvolguts al joc de les xifres. Pimerament els dos jugadors haureu de escollir dos files cada u. Seguidament us donarà 6 nombres que pertanyen en aquestes perspectives llistes ja escollides. A continuació us donarà un nombre aleatori que serà el objectiu al que heu de arribar fent qualsevol operació matemàtica i no podreu repetir cap dels 6 nombres. El jugador que més es apropi guanya. Us desitjo molta sort i que guanyi el millor.')
    jugador_1=input('Hola, jugador com et dius?')
    jugador_2=input('Benvolgut, com es diu vostè?')
    jugador=(jugador_1, jugador_2)
    return tuple(jugador)
def crea_files() -> List[List[int]]:
    """
    Crea una llista de quatre llistes de nombres. Les tres primeres contenen nombres de l'1 fins al 9.
    I la quarta conté els nombres 10, 10, 25, 50, 75, 100.
    Les files estan ordenades.
    
    Retorna: Llista de llistes amb els nombres que hi haurà a cadascuna de les files.
    """
    fila_1=[1,2,3,4,5,6,7,8,9]
    fila_2=[1,2,3,4,5,6,7,8,9]
    fila_3=[1,2,3,4,5,6,7,8,9]
    fila_4=[10,10,25,50,75,100]
    llista_llistes_nombres=[fila_1,fila_2,fila_3,fila_4]
    return llista_llistes_nombres
    

def escull_fila(jugador, llista_llistes_nombres: List[List[int]]) -> Tuple[int, List[List[int]]]:
    """
    Demana al jugador que esculli una fila entre la 1a i la 4a.
    
    Retorna: - Un nombre a l'atzar de la fila escollida de llista_llistes_nombres.
             - La llista de llistes amb els nombres que quedin per escollir.   
    """
    #MIRA RANDRANGE
    # Aquestes són les dues maneres que havíem comentat de copiar les llistes dins d'una llista element a element.
    # Per fer-ho fins al nivell que sigui i amb l'estructura que sigui, s'ha de utilitzar la funció deepcopy del mòdul copy.
    # A més a més, preserva les identitats entre les llistes, és a dir, si hi ha una llista [a, a], crearà una nova llista
    # que contingui una sola còpia duplicada del que sigui que contingui la variable a.
    #
    #files_copiades = [
    #    llista_llistes_nombres[0][:],
    #    llista_llistes_nombres[1][:],
    #    llista_llistes_nombres[2][:],
    #    llista_llistes_nombres[3][:]
    #    ]
    #files_copiades = [llista_llistes_nombres[i][:] for i in range(len(llista_llistes_nombres))]
    from random import randrange
    jugador_1=jugador[0]
    files_copiades = deepcopy(llista_llistes_nombres)
    llista_escollida_1=int(input(f'Hola {jugador_1} escull una fila entre la 1a i la 4a:'))
    
    llista_nombres = 0
    fila_1=[1,2,3,4,5,6,7,8,9]
    fila_2=[1,2,3,4,5,6,7,8,9]
    fila_3=[1,2,3,4,5,6,7,8,9]
    fila_4=[10,10,25,50,75,100]
    
    if llista_escollida_1 == 1:
        llista_nombres=fila_1.pop(randrange(0,9))
        
    elif llista_escollida_1==2:
        llista_nombres=fila_2.pop(randrange(0,9))
        
    elif llista_escollida_1==3:
        llista_nombres=fila_3.pop(randrange(0,9))
        
    else:
        llista_nombres=fila_4.pop(randrange(0,5))
  
    return llista_nombres
    

def escolliu_nombres(jugador) -> List[int]:
    """
    Fa que els jugadors escullin els nombres a partir de les respectives files.
    Cada jugador anirà escollint una fila per torn fins que hagin escollit 6 nombres.

    Retorna: Una llista de 6 nombres enters
    """
    nombres_escollits=[]
    files = crea_files()
    jugador_1=jugador[0]
    jugador_2=jugador[1]
    i=0
    while i<6:
        if i%2:
            nombre_escollit,files = escull_fila(jugador_1, files)
            nombres_escollits.append(nombre_escollit)
            i+=1
        else:
            nombre_escollit,files = escull_fila(jugador_2, files)
            nombres_escollits.append(nombre_escollit)
            i+=1
        
    return nombres_escollits
    

    
def crea_num_objectiu() -> int:
    """
    Crea un nombre a l'atzar de tres xifres entre el 100 i el 999.
    
    Retorna: Un enter entre 100 i 999 a l'atzar
    """
    from random import randrange
   
    centenes=random.randrange(100,999)
    return centenes
def mostra_enunciat(llista_nombres: List[int], nombre_objectiu: int) -> None:
    """
    Mostra als jugadors els nombres disponibles i el nombre objectiu.
    
    Retorna: -
    """
    return print(f'Ara procedirem a ensenyar-te una sèrie de nombres, {llista_nombres} aquests són els nombres que has de arribar per tal de arribar al nombre objectiu {nombre_objectiu}. Molta sort i que guanyi el millor')

def espera(temps: int) -> None:
    """
    S'espera un determinat temps i després segueix amb l'execució del programa.
    
    Retorna: -
    """
    import time
    for i in range(1,temps):
        time.sleep(1)
        return demana_respostes()
    
def demana_respostes(jugador) -> Tuple[str, str]:
    """
    Demana als dos jugadors que escriguin les seves respostes i les retorna en una parella d'strings.
    
    Retorna: Una parella d'strings amb les respostes dels dos jugadors.
    """
    jugador_1=jugador[0]
    jugador_2=jugador[1]
    resposta_1= input(f'{jugador_1} ensenyem el teu procediment si us plau:')
    resposta_2= input(f'{jugador_2} demostrem el teu procediment si us plau:')
    
    respostes=(resposta_1,resposta_2)
    return respostes
def corregeix_respostes(respostes: Tuple[str, str], llista_nombres: List[int]) -> Tuple[bool, bool]:
    """
    Mira si les respotes són correctes, és a dir si es poden fer amb els nombres que hi ha a la llista de nombres i les operacions permeses.
    
    Retorna: Una parella de variables booleanes que indiquen si les respectives respostes són correctes.
    """
    xifra=''
    numero=''
    jugador_1=True
    jugador_2=True
    copia=deepcopy(llista_nombres)
    resposta_be_1=[]
    resposta_be_2=[]
    resposta_1=respostes[0] + " "
    resposta_2=respostes[1] + " "
    for num in resposta_1:
        if num=='1':
            pass
        elif num=='2':
            pass
        elif num=='3':
            pass
        elif num=='4':
            pass
        elif num=='5':
            pass
        elif num=='6':
            pass
        elif num=='7':
            pass
        elif num=='8':
            pass
        elif num=='9':
            pass
        elif num=='0':
            pass
        elif num=='+':
            pass
        elif num=='*':
            pass
        elif num=='-':
            pass
        elif num =='(':
            pass
        elif num==')':
            pass
        elif num=='^':
            pass
        elif num=='/':
            pass
        elif num==' ':
            pass
        else:
            jugador_1=False
            
    for num in resposta_2:
        if num=='1':
            pass
        elif num=='2':
            pass
        elif num=='3':
            pass
        elif num=='4':
            pass
        elif num=='5':
            pass
        elif num=='6':
            pass
        elif num=='7':
            pass
        elif num=='8':
            pass
        elif num=='9':
            pass
        elif num=='0':
            pass
        elif num=='+':
            pass
        elif num=='*':
            pass
        elif num=='-':
            pass
        elif num =='(':
            pass
        elif num==')':
            pass
        elif num=='^':
            pass
        elif num=='/':
            pass
        elif num==' ':
            pass
        else:
            jugador_2=False
    
    for num in '+*-()^/':
        resposta_1=resposta_1.replace(num,' ')
    for num in '+*-()^/':
        resposta_2=resposta_2.replace(num,' ')

  
    while len(resposta_1)!=0:
        for element in resposta_1:
            if element==' ':
                if xifra!= '':
                    resposta_1=resposta_1[1:]
                    resposta_be_1.append(int(xifra))
                    xifra=''
                    break
                else:
                    resposta_1=resposta_1[1:]
                    break
            else:
                xifra=xifra+element
                resposta_1=resposta_1[1:]
                
    while len(resposta_2)!=0:
        for i in resposta_2:
            if i==' ':
                if numero!= '':
                    resposta_2=resposta_2[1:]
                    resposta_be_2.append(int(numero))
                    numero=''
                    break
                else:
                    resposta_2=resposta_2[1:]
                    break
            else:
                numero=numero+i
                resposta_2=resposta_2[1:]
        
    for num in resposta_be_1:
        if num in copia:
            numss=copia.index(num)
            copia.pop(numss)
            
        else:
            jugador_1=False
            
    for n in resposta_be_2:
        if n in llista_nombres:
            nums=llista_nombres.index(n)
            llista_nombres.pop(nums)
            
        else:
            jugador_2=False
    
    
    return (jugador_1,jugador_2)

corregeix_respostes(["2 + 3-4+8+8", "5+8+1+1+7"], [1, 2, 3, 4, 5, 8, 8, 7])


def puntua_respostes(respostes: Tuple[str, str], respostes_correctes: Tuple[bool, bool], nombre_objectiu: int) -> Tuple[int, int]:
    """
    Puntua les respostes a partir de la seva proximitat al nombre objectiu.
    
    Retorna: Una parella d'enters que es corresponen a la puntuació del primer i el segon jugador respectivament.
    """
    comptador_1=0
    comptador_2=0
    resposta_1=respostes[0]
    resposta_2=respostes[1]
    
    if resposta_1==nombre_objectiu:
        resposta_1=comptador_1+1
    elif resposta_2==nombre_objectiu:
        resposta_2==comptador_2+1

    
    return tuple[comptador_1,comptador_2]
def torn_xifres(puntuacions_anteriors,jugador) -> Tuple[int, int]:
    """
    Fa un torn sencer de xifres i retorna les puntuacions_anteriors actualitzades amb la puntuació de la nova ronda.
    
    Retorna: Una parella d'enters amb les puntuacions_anteriors actualitzades.
    """
    comptador_1=puntuacions_anteriors[0]
    comptador_2=puntuacions_anteriors[1]
    jugador_1=jugador[0]
    jugador_2=jugador[1]
    resposta_2=''
    resposta_2=input(f'Us animeu a jugar una altre ronda? De moment la puntuació està així; el {jugador_1} consta de {comptador_1} i el {jugador_2} té {comptador_2} punts.')
    if resposta_2=='si':
        return crea_files()
    else:
        return print(f'Dacord, gràcies per jugar-hi.')
