

import commands
import socket
import fcntl
import struct
import time
import requests


from lib.Lib_File import *  # importar con los mismos nombres
from lib.Lib_Rout import *  # importar con los mismos nombres

import lib.Control_Archivos  as Ca
#import lib.Control_Ethernet  as Ce

#----------------------------------------------
#                   definiciones
#----------------------------------------------

Escrivir_Estados        = Ca.Escrivir_Estados
Generar		            = Ca.Generar_ID_Tarjeta
Escrivir_Archivo        = Ca.Escrivir_Archivo
Leer_Archivo            = Ca.Leer_Archivo
Leer_Lineas             = Ca.Leer_Lineas
Borrar                  = Ca.Borrar_Archivo
Link_servidor           = Ca.Mejor_Opcion_link
Escrivir_nuevo          = Ca.Escrivir_nuevo
Verificar_ID_Tipo_3     = Ca.Verificar_ID_Tipo_3

#Get_Post_try_catch     =Ce.Get_Post_try_catch   #(peticion, CE_url, CE_datos, CE_cabeceras, tout):


"""
g2yt1.6ebe76c9fb411be97b3b0d48b791a7c9
gqyt3.3c7849bc28d281f187156af8ec4c882b
g2zdk.9a97ba14cb334d71cceffc84244f5d9c
"""
"""
def Verificar_ID_Tipo_3(Pal): #mejorar por que podia pasa cualquiera
    #global N_A_Servidor
    #print Pal
    archivo = open('/home/pi/Firmware/db/Data/Tabla_Servidor.txt', 'r')
    archivo.seek(0)
    for linea in archivo.readlines():
        s=linea.rstrip('\n')
        s=s.rstrip('\r')
        #s2 =s.split(".")
        #print 'ID: '+ s2[0] + ' RUT: '+s2[2]
        #print  s
        #Rut = ''#s2[0]
        if 	s ==	Pal:
            archivo.close()
            return s2[0]
    archivo.close()
    return -1
"""

def add_user_counter(usuario):

    puntos = usuario.count(".")
    print puntos

    if puntos == 3:
        s = usuario.split(".")
        #ID =s[0]
        #print s[0]
        #print s[1]
        #print s[2]
        #print s[3]
        #print s[4]
        #print IDPrueba
        #ID='12dsad'
        ID = s[1] + '.' + s[2] + '.' + s[3]

        Respuesta = Verificar_ID_Tipo_3(ID)
        #print Respuesta

        if Respuesta == -1:
            #Comando = usuario.strip('\n')
            Escrivir_Archivo(ID,0)
            print 'Usuario agregado'
        else:
            print 'ya existe'
    else:
        print 'No cumple parametros'




def Resolver_Comando_Counter():

    global Comando_Antes
    #print CONT_FlAG_NEW_TICKET
    flag = Get_File(CONT_FlAG_NEW_TICKET)
    #print flag
    if  flag == '1':
        #print 'dentro'


        Comando =  Get_File(CONT_NEW_TICKET) #Leer_Archivo(48)}
        #print Comando
        if len(Comando) >= 1 :
            Usuarios = Comando.split("\n")
            for linea in Usuarios:
                s=linea.rstrip('\n')
                if len(s) > 0:
                    #print s
                    add_user_counter(s)

        Clear_File(CONT_NEW_TICKET) #Borrar(48)

        Clear_File(CONT_FlAG_NEW_TICKET)



#Resolver_Comando_Counter()

"""
def Nuevos_Usuarios_conter():
    IP_conter = Leer_Archivo(49)
    IP_conter = IP_conter.replace('',"\n")
"""
#payload = {'Dato': 'g2yt1asd12343.6ebe76c9fb411be97b3b0d48b791a7c9'}
#print Get_Post_try_catch('GET_PARAM', 'http://192.168.0.14/Prueba/new_user.php', payload, '', 2)

"""
dat = '"g2yt1asd12343.6ebe76c9fb411be97b3b0d48b791a7c9","g2yt1asd123435.6ebe76c9fb411be97b3b0d48b791a7c9"'
#dat = '"g2yt1asd12343.6ebe76c9fb411be97b3b0d48b791a7c9","g2yt1asd123435.6ebe76c9fb411be97b3b0d48b791a7c9' # con error
CE_datos ='{"data":['+dat+']}'

r = requests.post('http://192.168.0.14/api/new_user/index.php', data=CE_datos, headers='', timeout=2)

print r
print 'Texto: ' + r.text

time.sleep(1.05)
"""
#print 'listo'
#Resolver_Comando_Counter()

#print Get_Post_try_catch('POST', 'http://192.168.0.14/Prueba/new_user.php', CE_datos, '', 2)
#print Get_Post_try_catch('POST', 'http://192.168.0.14/api/counter/new_user/index.php', CE_datos, '', 2)



#while 1:

    #---------------------------------------------------------
    #  Proceso 0: Tiempo de espera para disminuir proceso
    #---------------------------------------------------------
    #time.sleep(1.05)
    #Resolver_Comando_Counter()
