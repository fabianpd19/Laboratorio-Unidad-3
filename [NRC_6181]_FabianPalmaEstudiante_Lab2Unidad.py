#importamos la siguiente libreria para obtener la fecha y hora actual
from calendar import day_abbr
from datetime import datetime
#funcion que nos retorna la fecha y hora actual
now = datetime.now()

#laboratorio 2 unidad 1
#creación de un sistema de rastreo de contactos simplificado con COVID-19

#declaración de las respectivas clases con sus atributos y métodos
#==========================================
class Cliente:
    def __init__ (self, nombre, telefono, estado):
        #atributos clase cliente
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado
    #registro de la cuenta de un cliente
    def registroCuentaCliente (self, nombreCliente, telefonoCliente):
        #pedimos datos al cliente para llenar las variables
        self.nombreCliente=nombreCliente
        self.telefonoCliente=telefonoCliente
        #nombreCliente = input("Ingrese su nombre: ")
        #telefonoCliente = input("Ingrese su número de télefono: ")
        #creamos un nombre de usuario y contraseña para poder registrarlo 
        #hacemos uso de strings para la creación de las mismas
        self.nombreUsuario=nombreCliente[0:5:1]+telefonoCliente[0:2:1]
        self.contrasena=telefonoCliente[0:3:1]+nombreCliente[0:3:1]+telefonoCliente[3:1:1]
        #mostramos en pantalla el usuario y contraseña
        print("--------------------------------")
        print("¡Bienvenido", nombreCliente,"!")
        print("Su nombre de usuario es:",self.nombreUsuario, "\nSu contraseña es:", self.contrasena)
        print("--------------------------------")
    #inicio de sesion con los datos ingresados
    def iniciDeSesion(self, usuario, contrasena):
        self.usuario=client.nombreUsuario
        #self.contrasena=client.contrasena
        #hacemos una condición para validar el ingreso de sesión del cliente
        usuario=str(input("Ingrese el usuario: "))
        contrasena=str(input("Ingrese la contraseña: "))
        #print(client.contrasena)
        #print(client.nombreUsuario)
        if usuario==client.nombreUsuario and contrasena==client.contrasena:
            #mostramos un mensaje para mostrar que está dentro 
            print("Inicio de sesión exitoso", client.nombre)
        else:
            print("Usuario o contraseña incorrecta")
    def registroTienda(self, horaActual):
        self.estado=client.estado
        horaActual=int(input("Ingrese hora de registro: "))
        if (horaActual<now.hour):
            client.estado="Normal"
        else:
            client.estado="Cercano"
#==========================================
#clase tienda
#==========================================
class Tienda:
    def __init__(self, nombre, telefono, estado, gerente):
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado
        self.gerente=gerente
#==========================================
#clase admin
#==========================================
class Admin:
    def __init__(self, nombre):
        self.nombre=nombre
#instanciamos la clase cliente
client=Cliente("Fabian","0979841987","Normal")
#=======================================
#menu de la clase tienda
#=======================================
#variable clase tienda
#bienvenida del programa
print ("Bienvenido al sistema de contactos de Covid-19:")
print ("¿Qué desea hacer?")
#creación de un switch case para que el usuario pueda realizar las acciones
#==========================================
#declaracion de la variable para el menú principal
opcion=int
#declaracion de las listas para guardar los datos
listaRegistroTienda=[]
while opcion!=6:
    print ("_______________________________________________") 
    print ("    Menú Usuario")
    print ("_______________________________________________") 
    print ("1. Registrarse.")
    print ("2. Iniciar sesión.")
    print ("3. Registrarse en una tienda.")
    print ("4. Ver el historial de tiendas que visitó.")
    print ("5. Ingresar como administrador.")
    print ("6. Salir.")
    print ("_______________________________________________")
    opcion=int(input("Seleccione la opción que desea realizar: "))
    if opcion == 1:
        print('Ingreso de sesión')
        nombre = input("Ingrese su nombre: ")
        telefono = input("Ingrese su número de télefono: ")
        client.registroCuentaCliente(nombre, telefono)
        listaRegistroTienda.append(nombre)
        listaRegistroTienda.append(telefono)
    elif opcion == 2:
        print('Registrarse')
        usuarioCliente=str
        contranaCliente=str
        client.iniciDeSesion(usuarioCliente, contranaCliente)
    elif opcion == 3:
        print('Registro en la tienda')
        horaTiendaRegistro=int
        client.registroTienda(horaTiendaRegistro)
        fecha=str(now.date())
        hora=str(now.time())
        listaRegistroTienda.append(fecha)
        listaRegistroTienda.append(hora)
        listaRegistroTienda.append(client.estado)
        #instanciar objeto
        nombreTienda=str(input("Ingrese nombre de la tienda: "))
        telefonoTienda=str(input("Ingrese telefono de la tienda: "))
        estadoTienda=str("Estado Tienda [Normal] o [Caso]: ")
        gerenteTienda=str(input("Ingrese el nombre del gerente: "))
        listaRegistroTienda.append(nombreTienda)
        storeT=Tienda(nombreTienda, telefonoTienda, estadoTienda, gerenteTienda)
    elif opcion == 4:
        print(listaRegistroTienda)
    elif opcion == 5:
        print(listaRegistroTienda)
    elif opcion == 6:
        print('Saliendo...')
    else:
        print('[!] Opción incorrecta [!]')
        print ("_______________________________________________") 
        print ("1. Iniciar sesión.")
        print ("2. Registrarase.")
        print ("3. Registrarse en una tienda.")
        print ("4. Ver el historial de tiendas que visitó.")
        print ("5. Ingresar como administrador.")
        print ("6. Salir.")
        print ("_______________________________________________")
        opcion=int(input("Seleccione una opción que desea realizar: ")) 