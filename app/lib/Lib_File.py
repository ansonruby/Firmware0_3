
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""
Autor: Anderson
Libreria personal para manejo de archivos de texto,
 manejo y busqueda de linea como base de Datos
"""
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import os
#from Cns_Rout import *  # importar con los mismos nombres
#-------------------------------------------------------
#----      Funciones para el manejo de archivos     ----
#-------------------------------------------------------

def Clear_File(arch):
    if os.path.exists(arch):
        archivo = open(arch, "w")
        archivo.write("")
        archivo.close()

#-------------------------------------------------------
def Get_File(arch):
    mensaje = ""
    if os.path.exists(arch):
        f = open (arch,'r')
        mensaje = f.read()
        #print(mensaje)
        f.close()
        return mensaje
    else:
        return mensaje

#-------------------------------------------------------
def Set_File(arch, Text):
    if os.path.exists(arch):
        archivo = open(arch, "w")
        archivo.write(Text)
        archivo.close()

#-------------------------------------------------------
def Add_File(arch, Text):
    if os.path.exists(arch):
        archivo = open(arch, "a")
        archivo.write(Text)
        archivo.close()

#-------------------------------------------------------
def Get_Line(arch, Numero):# comienza en 1
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        return lineas[Numero-1] # revisar si comensar en 1 o 0
    else:
        return ""

#-------------------------------------------------------
def Clear_Line(arch, Numero):
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        lineas.pop(Numero-1)
        #print lineas
        f2 =open(arch, "w")
        f2.write(''.join(lineas) )
        f2.close()

#-------------------------------------------------------
def Update_Line(arch, Numero, Dato): #incluir el/n
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        lineas[Numero-1]= Dato
        #print lineas
        f2 =open(arch, "w")
        f2.write(''.join(lineas) )
        f2.close()

#-------------------------------------------------------
def Add_Line_End(arch, Dato): #incluir el/n
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        #print lineas
        f2 =open(arch, "w")
        f2.write(''.join(lineas) )
        f2.write(Dato)
        f2.close()
#-------------------------------------------------------
def Add_Line_Pos(arch, Numero, Dato): #incluir el/n
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        inicio = lineas[0:(Numero-1)]
        fin = lineas[(Numero-1):]

        f2 =open(arch, "w")
        f2.write(''.join(inicio) )
        f2.write(Dato)
        f2.write(''.join(fin) )
        f2.close()
#-------------------------------------------------------
def Num_lines(arch):
    if os.path.exists(arch):
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        return len(lineas)
    else:
        return -1

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------

#Clear_File(TAB_USER)
#Set_File(TAB_USER, 'Hola anderson\ncomensando denuevo\n')
#print Get_File(TAB_USER)
#print Get_Line(TAB_USER,2)
#Clear_Line(TAB_USER,1)
#Update_Line(TAB_USER,2,'OTRA cosa\n')       #incluir el/n
#Add_Line_End(TAB_USER, 'Dato al final\n')   #incluir el/n
#Add_Line_Pos(TAB_USER, 2, 'en posicion 2')  #incluir el/n
#Add_File(TAB_USER, 'mas cosa sin borrar el archivo\n')
#print Get_File(TAB_USER)
#print Num_lines(TAB_USER)


#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
# Clear_File(archivo):
# Get_File(archivo):
# Set_File(archivo, Texto):
# Add_File(archivo, Texto):

# Get_Line(archivo, Numero):
# Clear_Line(archivo, Numero):
# Update_Line(archivo, Numero, Dato): #incluir el/n
# Add_Line_End(archivo, Dato): #incluir el/n
# Add_Line_Pos(archivo, Numero, Dato): #incluir el/n
# Num_lines(a):
