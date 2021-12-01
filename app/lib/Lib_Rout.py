
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""
Autor: Anderson
Libreria personal para el manejo de rutas del aplicativo,

"""
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#---------------------------------
#           Rutas Pruebas
#---------------------------------
PRUEBAS = '/home/pi/Firmware/appNuevo/Pruebas.txt'

#---------------------------------
#           Rutas Generales
#---------------------------------
FIRM    = '/home/pi/Firmware/'                              # Ruta      Firmware
DATA    = 'db/Data/'                                        # Ruta      Base de datos
STATUS  = 'db/Status/'                                      # Ruta      Estados
COMMA   = 'db/Command/'                                     # Ruta      Comandos
DISP    = '/home/pi/.ID/'                                   # Ruta      Informacion Dispositivo
CONF    = 'db/Config/'                                      # Ruta      Configuraciones
HILS    = 'db/Hilos/'                                       # Ruta      Hilos

#---------------------------------
#           Datos del dispositivo
#---------------------------------
INF_FIRMWARE    = FIRM + 'README.md'                        # Datos y contenido del repositorio git
INF_VERCION     = FIRM + CONF + 'Vercion_Firmware.txt'      #
INF_DISPO       = DISP + 'Datos_Creacion.txt'               # Datos propios del dispositivo pieza 1 UUID

#---------------------------------
#           Rutas Base de datos
#---------------------------------
TAB_USER = FIRM + DATA + 'Tabla_Usuarios.txt'               # Usuarios del servidor o counter
TAB_ENVI = FIRM + DATA + 'Tabla_Enviar.txt'                 # ? posible filtro para mejorar aun no utilizadosd
TAB_AUTO = FIRM + DATA + 'Tabla_Autorizados.txt'            # Registro de usuarios autorizados entrada y salida

TAB_LECTOR = '/home/pi/Firmware/db/Data/Tabla_Lector.txt'            # Registro de usuarios autorizados entrada y salida
TAB_SERVER = '/home/pi/Firmware/db/Data/Tabla_Servidor.txt'            # Registro de usuarios autorizados entrada y salida
#---------------------------------
#           Comandos
#---------------------------------
COM_LED         = FIRM + COMMA + 'Led_RGB/Com_Led.txt'
COM_BUZZER      = FIRM + COMMA + 'Buzzer/Com_Buzzer.txt'
COM_TECLADO     = FIRM + COMMA + 'Teclado/Com_Teclado.txt'
COM_FIRMWARE    = FIRM + COMMA + 'Firmware/Com_Firmware.txt'
COM_TX_RELE     = FIRM + COMMA + 'Rele/Com_Rele.txt'
COM_QR          = '/home/pi/Firmware/db/Status/QR.txt' #FIRM + COMMA + 'Qr/Com_Qr.txt'

#---------------------------------
#           Stados
#---------------------------------
STATUS_USER     = FIRM + STATUS + 'Usuario/Status_User.txt'
STATUS_TECLADO  = FIRM + STATUS + 'Teclado/Status_Teclado.txt'
STATUS_QR       = '/home/pi/Firmware/db/Status/Estado_QR.txt'#FIRM + STATUS + 'Qr/Status_Qr.txt'
STATUS_REPEAT_QR= FIRM + STATUS + 'Qr/Repeat_Qr.txt'

#---------------------------------
#           Configuraciones
#---------------------------------
CONF_TIEM_RELE = FIRM + CONF + 'Rele/Tiempo_Rele.txt'
CONF_DIREC_RELE = FIRM + CONF + 'Rele/Direccion_Rele.txt'

#---------------------------------
#           CONTER_Comunicaciones
#---------------------------------

CONT_AUTORIZADOS = '/home/pi/Firmware/ComCounter/db/datatosend.txt'#  datos autorizados por el dispsotivos         '/home/pi/Data.txt'
CONT_FlAG_AUTORIZADOS = '/home/pi/Firmware/ComCounter/db/flagtosend.txt'#  Bandera de control de escritura              '/home/pi/Flag.txt'

CONT_NEW_TICKET = '/home/pi/Firmware/ComCounter/db/datanewsreceived.txt'#'/home/pi/Data.txt'
CONT_FlAG_NEW_TICKET = '/home/pi/Firmware/ComCounter/db/flagnewsreceived.txt'#'/home/pi/Flag.txt'

CONT_DEL_AUTORIZADOS = '/home/pi/Firmware/ComCounter/db/datadelreceived.txt'        #'/home/pi/Data.txt'
CONT_FlAG_DEL_AUTORIZADOS = '/home/pi/Firmware/ComCounter/db/flagdelreceived.txt'   #'/home/pi/Flag.txt'

CONT_UPDATE_USERS = '/home/pi/Firmware/ComCounter/db/dataupdatereceived.txt'#'/home/pi/Data.txt'
CONT_FlAG_UPDATE_USERS = '/home/pi/Firmware/ComCounter/db/flagupdatereceived.txt'#'/home/pi/Flag.txt'




#---------------------------------
#           Manejo de Hilos  mejorar
#---------------------------------
"""
#-- peticion de usuarios
HILO_OUT_PETI_USERS = FIRM + HILS + 'M_Peticion_Users/Out_Peticion_Users.txt'
HILO_STATUS_PETI_USERS = FIRM + HILS + 'M_Peticion_Users/Status_Peticion_Users.txt'
#-- Procesar QR en el dispositivo
HILO_N_A_Exit_Dis_QR	    = FIRM + HILS + 'QR/Exit_Dispositivos_QR.txt'   #48
HILO_N_A_Status_Dis_QR	    = FIRM + HILS + 'QR/Status_Dispositivos_QR.txt' #49
HILO_N_A_Out_Dis_QR         = FIRM + HILS + 'QR/Out_Dispositivos_QR.txt'    #50

"""
