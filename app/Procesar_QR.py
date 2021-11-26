
# Librerias creadas para multi procesos o hilos -------------
import datetime
import time
import commands
import sys
import socket
import os

import lib.Control_Archivos
import lib.Control_Fecha
import lib.Control_Ethernet
import lib.Seguridad
import lib.Control_Torniquete

from lib.Lib_File import *  # importar con los mismos nombres
from lib.Lib_Rout import *  # importar con los mismos nombres

Escrivir_Estados        = lib.Control_Archivos.Escrivir_Estados
Borrar                  = lib.Control_Archivos.Borrar_Archivo
Leer_Estado             = lib.Control_Archivos.Leer_Estado
Escrivir_Enviar         = lib.Control_Archivos.Escrivir_Enviar
Escrivir                = lib.Control_Archivos.Escrivir
Escrivir_Archivo        = lib.Control_Archivos.Escrivir_Archivo
Estado_Usuario 	        = lib.Control_Archivos.Estado_Usuario
Estado_Usuario_Tipo_3   = lib.Control_Archivos.Estado_Usuario_Tipo_3
Verificar_PIN           = lib.Control_Archivos.Verificar_PIN
PIN_Usado               = lib.Control_Archivos.PIN_Usado
ID                      = lib.Control_Archivos.ID

Tiempo                  = lib.Control_Fecha.T_Actual

MD5                     = lib.Seguridad.MD5

Envio                   = lib.Control_Ethernet.envio

Entrar                  = lib.Control_Torniquete.Entrar
Salir                   = lib.Control_Torniquete.Salir



#-------------------------------------------------------
"""
FIRM            = '/home/pi/Firmware/'                      # Ruta Firmware
COMMA           = 'db/Command/'                             # Ruta comandos
CONF            = 'db/Config/'                              # Ruta Configuraciones

COM_LED         =  FIRM + COMMA + 'Led_RGB/Com_Led.txt'     # Archivo de comandos

def Set_File(arch, Text):
    if os.path.exists(arch):
        archivo = open(arch, "w")
        archivo.write(Text)
        archivo.close()
"""
#-------------------------------------------------------
# inicio de variable	--------------------------------------
PP_Mensajes = 1     # 0: NO print  1: Print

Direc_Torniquete = Leer_Estado(13)  #print Direc_Torniquete
Estados = '6' #estados del dispositivos para visualizar en los leds
Estados_Antes = '0'
T_estado = 0


def Registros_autorizaciones(Co, Ti,Qr_Te, I_N_S, Tipo_Acceso):
    Dato =''
    if Tipo_Acceso == 'Access granted-E':   Dato = Co+Ti+'.'+Qr_Te+'.0.'+I_N_S
    else:                                   Dato = Co+Ti+'.'+Qr_Te+'.1.'+I_N_S

    if PP_Mensajes:
        print 'Registro: ' + Dato

    Escrivir(Dato)               #guardar un registro


    #Add_File(CONT_AUTORIZADOS,Dato+'\n')
    #Set_File(CONT_FlAG_AUTORIZADOS,'1')

    #if Qr_Te == '2':    Escrivir_Archivo   (Dato, 27)   #escrivir pin usado
    if I_N_S == '1':	Escrivir_Enviar    (Dato)



#---------------------------------------------------------
#---------------------------------------------------------
def Decision_Torniquete (Res, QR, ID2, Ti,Qr_Te, I_N_S ):

    if Qr_Te == '1'	:	Co = QR+'.'                 #QR

    elif Qr_Te == '2'	:	Co = QR+'.'+ID2+'.'     #PIN
    else :
        if ID2 != -1	:	Co = QR+'.'+ID2+'.'     #RUT
        else		:	Co=''

    #print Co
    Res=Res.rstrip('\n')#se coloca para pruebas
    Res=Res.rstrip('\r')#se coloca para pruebas
    #c
    if Res == 'Access granted-E':
        if PP_Mensajes:
            print "Entrada, estado 3"
        Set_File(COM_LED, 'Access granted-E')

        if Direc_Torniquete == 'D':     Salir()         #Set_File(COM_LED, '4')  #Cambio_Estado_Led('4')
        else :                          Entrar()        #Set_File(COM_LED, '3')  #Cambio_Estado_Led('3')

        #Registros_autorizaciones(Co, Ti,Qr_Te, I_N_S , Res) #registro para todos los formatos
        Set_File(COM_LED, '0')  #Cambio_Estado_Led('0')  #volver a estado de inicio


    elif Res == 'Access granted-S':
        if PP_Mensajes:
            print "Salida, estado 4"

        Set_File(COM_LED, 'Access granted-S')

        if Direc_Torniquete == 'D':     Entrar()        #Set_File(COM_LED, '3')  #Cambio_Estado_Led('3')
        else :                          Salir()         #Set_File(COM_LED, '4')  #Cambio_Estado_Led('4')

        #Registros_autorizaciones(Co, Ti,Qr_Te, I_N_S , Res) #registro para todos los formatos
        Set_File(COM_LED, '0')  #Cambio_Estado_Led('0')  #volver a estado de inicio


    else :
        if PP_Mensajes:
            print "No Esta  activo"
        #print "Sin Acceso o rut equivocado estado 5 0 6"
        Set_File(COM_LED, 'Error')
        #Set_File(COM_LED, '6')  #Cambio_Estado_Led('6')  # realisa un tiempo de visualisacion

def Get_QR_RUT(QR_RUT):

    Pal=''
    if QR_RUT == 'QR':      Pal=Leer_Estado(7)
    Pal=Pal.rstrip('\n')
    Pal=Pal.rstrip('\r')
    return Pal

def Respuesta_Sin_Internet(QR_RUT, T_A,  IDQ_Encrip, QR):

    #global Cantidad_Pines
    if QR_RUT == 'QR':
        if PP_Mensajes:
            print "Respuesta QR, sin internet:"
        Set_File(COM_LED, '7')  #   Cambio_Estado_Led('7')
        # if PP_Mensajes:
        #    print 'ID:'+IDQ_Encrip
        # IDQ_Encrip, Resp = Estado_Usuario(IDQ_Encrip,1)
        # print '----- resolviendo respuesta'
        # print 'Resp:'+ Resp
        #------------------------------------------------------------
        #               NUEVOS FORMATOS
        #------------------------------------------------------------
        puntos = QR.count(".")
        if PP_Mensajes:
            print puntos

        if puntos == 1:
            IDQ_Encrip, Resp = Estado_Usuario(IDQ_Encrip,1)
            if PP_Mensajes:
                print '-----Formato 1: resolviendo respuesta '
                print 'Resp:'+ Resp
            Decision_Torniquete (Resp,QR,"",T_A,'1','1')

        elif puntos == 2:
            IDQ_Encrip, Resp = Estado_Usuario(IDQ_Encrip,1)
            if PP_Mensajes:
                print '-----Formato 2: resolviendo respuesta '
                print 'Resp:'+ Resp
            Decision_Torniquete (Resp,QR,"",T_A,'1','1')

        elif puntos == 3:
            #print 'QR:'+ QR
            SQR = QR.split('.')
            #print SQR[0]
            #print SQR[1]
            inicio = str(int(SQR[2]))
            fin = str(int(SQR[3]))
            #print 'T inicio:' + inicio
            #print 'T inicio:' + str(datetime.datetime.fromtimestamp(int(float(inicio)/1000)))
            #print 'T fin:'    + fin
            #print 'T Actual:' + str(datetime.datetime.fromtimestamp(int(float(T_A)/1000)))
            #print 'T Fin   :' + str(datetime.datetime.fromtimestamp(int(float(fin)/1000)))

            if (inicio <= T_A) and (T_A <= fin):
                if PP_Mensajes:
                    print 'Dentro del rango permitido'
                    print SQR[1]
                IDQ_Encrip, Resp = Estado_Usuario(SQR[1],1)
                print '----- resolviendo respuesta'
                print 'Resp:'+ Resp

                Decision_Torniquete (Resp,QR,"",T_A,'1','1')
            else:
                if PP_Mensajes:
                    print 'finalizo NO esta dentro del rango'
                Decision_Torniquete ('Denegar',QR,"",T_A,'1','1')

        elif puntos == 4:

            SQR = QR.split('.')
            ID =  SQR[1] + '.' + SQR[2]+ '.' + SQR[3]

            #print 'Tipo 3 QR:'
            #print 'ID:'+ ID
            T_inicio = int(SQR[4])
            inicio = str(T_inicio)
            fin = str(int(SQR[3]))
            #print 'T inicio:' + inicio
            #print 'T Actual: ', str(T_A)

            #quemar 60 minutos   3600 segundos
            #ejmeplo de guardado de tikeds
            #MpiC+zaHfumY7muwxRjLSg==.oGGv9bl6U6vpD8HacY7yhg==.5

            if T_A > T_inicio :
                #print 'Ya paso'
                Resta = (int(T_A) -int(SQR[4]))/1000
                #print Resta
                if Resta >=3600 :
                    #print 'vencido'
                    Decision_Torniquete ('Denegar',QR,"",T_A,'1','1')
                else:
                    #print 'a tiempo'
                    IDQ_Encrip, Resp = Estado_Usuario_Tipo_3(ID,1)
                    if PP_Mensajes:
                        print '-----Formato 3: resolviendo respuesta '
                        print 'Resp:'+ Resp

                    Decision_Torniquete (Resp,QR,"",T_A,'1','1')
                    Registros_autorizaciones( QR+'.', T_A,'1','1' , Resp)
            else:
                Decision_Torniquete ('Denegar',QR,"",T_A,'1','1')

        else:
                Decision_Torniquete ('Denegar',QR,"",T_A,'1','1')


def Respuesta_Con_Internet(QR_RUT, T_A,  IDT, Respuesta, QR):

    if QR_RUT == 'QR':
        #Respuesta = Respuesta.text
        if PP_Mensajes:
            print "Respuesta QR, con internet:"+ Respuesta
        Set_File(COM_LED, '1')  #Cambio_Estado_Led('1')
        Decision_Torniquete (Respuesta,QR,"",T_A,'1','0')

def Decision(QR_RUT):

    global Hay_Internet

    T_A = Tiempo()
    if PP_Mensajes:
        print 'Nuevo------------------------------------'
        print 'Tiempo: ', "%s" % T_A
    # Prepararacion de informacion para tratamiento
    if QR_RUT == 'QR':     #else: # QR
        Escrivir_Estados('1',6)# activar sonido por 500*2
        R_Q = Get_QR_RUT('QR')
        #print R_Q
        puntos = R_Q.count(".")
        #if PP_Mensajes:
        #    print puntos
        if puntos == 0:
            IDQ = ''
            QRT = ''
        else:
            s =R_Q.split(".")
            QRT = s[0]
            IDQ = s[1]

        ID_Tratado = IDQ
        Envio_Dato = QRT
        Estado_RQ = 1
        Dato2 = R_Q
        Dato1 = ''

    if PP_Mensajes:
        print QR_RUT+': '+ R_Q

    # Decision dependiendo del estado del internet
    #Hay_Internet =1 # /////////////////////////// hojo comentar
    if Hay_Internet == 0	:   # Hay internet

        Respuesta=Envio(Envio_Dato,T_A, Estado_RQ)
        #print Respuesta
        #print Respuesta.text
        #if Respuesta!='NO': #respuesta del servidor
        if Respuesta.find("Error") == -1:

            Respuesta_Con_Internet(QR_RUT, T_A, Dato1, Respuesta, Dato2)
            Hay_Internet = 0
            Escrivir_Estados('0',28)#estado comunicacion servidor

        elif Respuesta.find("Error :Access denied") != -1:
            Respuesta_Con_Internet(QR_RUT, T_A, Dato1, Respuesta, Dato2)
            Hay_Internet = 0
            Escrivir_Estados('0',28)#estado comunicacion servidor

        else :  # Sin internet Momentanio
            if PP_Mensajes:
                print 'nueva evaluacion'
                print ID_Tratado
            Respuesta_Sin_Internet(QR_RUT,T_A, ID_Tratado, Dato2)
            Hay_Internet = 1
            Escrivir_Estados('1',28)#estado comunicaion servidor
            Estado_Internet = 0


    else :      # Sin internet Permanente
        Respuesta_Sin_Internet(QR_RUT,T_A, ID_Tratado, Dato2)

        #Intento de actualizar usuarios
        #Ping_Intento_Enviar_Usuarios_Autotizados()
#-----------------------------------------------------------------------------------------------
def revicion_QR ():
    if Get_File(STATUS_QR) == '1':   # Hay un QR sin procesar
        #Decision_QR()
        #print 'QR Nuevo'
        Decision('QR')
        Clear_File(STATUS_QR)    #Borrar(8)               #final del proceso

#---------------------------------------------------------
#---------------------------------------------------------
print 'listo'
while 1:

    Hay_Internet = 1
    #---------------------------------------------------------
    #  Proceso 0: Tiempo de espera para disminuir proceso
    #---------------------------------------------------------
    time.sleep(0.05)

    #---------------------------------------------------------
    # Proceso 4: Procesamiento del QR
    #---------------------------------------------------------
    revicion_QR ()
    """
    if Leer_Estado(8) == '1':   # Hay un QR sin procesar
        Decision('QR')
        Borrar(8)               #final del proceso
    """

    #---------------------------------------------------------
    #                           FIN
    #---------------------------------------------------------
