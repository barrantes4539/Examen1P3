"""Imports"""
from ast import Return
from cmath import pi
from operator import truediv
import os
from datetime import datetime

"""Variables booleanas"""
invalido = False
valido = True

"""Clase referente a las operaciones del cajero automatico y manejo de archivos"""
class CajeroAutomatico:
   
    """Metodos de atribucion"""

    def __init__(self):
        self.tarjeta = None
        self.monto = 0
        self.deposito = 0
        self.retiro = 0
        self.montoCajero = 0

    """Metodos de calculo"""

    def depositar(self):
        dep = int(input('Ingrese su monto a depositar: \n'))
        self.deposito = dep
        self.montoCajero = self.montoCajero + dep
        print(f'*******Usted ha depositado: {dep}********** \n')
        print(f'*******Su nuevo monto es de {self.monto + dep}********\n\n')
        self.monto += dep
        self.addInvCliente('Deposito \n', self.deposito)
        self.crearInvCajero('121212', 'Full', 'LENOVO', 'Azul', 'Costado Oeste de Metrocentro')
        self.addInvCajero(self.montoCajero)
     
    def Retirar(self):
        ret = int(input('¿Que cantidad desea retirar?: '))
        self.retiro = ret
        self.montoCajero = self.montoCajero - ret
        print(f'Su monto actual es, {self.monto}')
        if self.monto >= ret:
            print(f'********Usted a retirado: {ret} , su nuevo monto es {self.monto - ret}********* \n')
            self.monto-=ret
        else:
            print('Monto invalido \n')
        self.addInvCliente('Retiro \n', self.retiro)
        self.crearInvCajero('121212', 'Full', 'LENOVO', 'Azul', 'Costado Oeste de Metrocentro')
        self.addInvCajero(self.montoCajero)

    def getSaldo(self):
        print(f'********Su saldo es de {self.monto} ********\n')
        self.addInvCliente('Ver Saldo \n', self.monto)


    """Metodos manejo de archivos"""

    def crearInvCliente(self, tarjeta, nombre, apellido):
        with open('clientes.txt', 'a+') as inv:
            w = inv.write(str(datetime.today().strftime('%Y-%m-%d')) + ' ' + str(tarjeta) + ' ' + nombre + ' ' + apellido + ': \n')

    def addInvCliente(self, accion, aMonto):
        with open('clientes.txt', 'a+') as inv:
            a = inv.write(str(datetime.today().strftime('%Y-%m-%d')) + ' ' + accion + ' ' + str(aMonto) + '\n')
    
    def crearInvCajero(self, serie, tipo, marca, color, ubicacion):
        with open('cajeros.txt', 'a+') as inv:
            w = inv.write(str(datetime.today().strftime('%Y-%m-%d')) + ' ' + serie + ' ' + tipo + ' ' + marca + ' ' + color + ' ' + ubicacion +': \n')

    def addInvCajero(self, montoTotal):
        with open('cajeros.txt', 'a+') as inv:
            a = inv.write(str(datetime.today().strftime('%Y-%m-%d')) + ' ' + str(montoTotal) + '\n')
           
    

"""Clase de cliente referente a la interfaz del cliente y las entradas del mismo"""
class Cliente(CajeroAutomatico):

    """Variables usuario"""
    nombre = None
    apellido = None
    pin = None

    """Metodo de registro de usuario"""
    def registro(self):
        print('\n Registro')

        tarjReg = int(input('Ingrese su numero de tarjeta: '))
        nomReg = input('Ingrese su nombre: ')
        apellReg = input('Ingrese su apellido: ')
        passReg = int(input('Ingrese su pin: '))
        opcReg = input('¿Desea registrarse? s/n \n')

        if opcReg == 's':
            self.tarjeta = tarjReg
            self.nombre = nomReg
            self.apellido = apellReg
            self.pin = passReg
            self.crearInvCliente(self.tarjeta, self.nombre, self.apellido)

            return True
        else:
            return False

    """Metodo de interfaz de usuario(Menu)"""
    def menu(self):
       
            ing = None
            opcMENU = 0
            while opcMENU != 5:
                
                print(f'MENU \n'
                    '1. Registrarse \n'
                    '2. Depositar\n'
                    '3. Retirar\n'
                    '4. Ver saldo\n'
                    '5. Salir\n')
                opcMENU = int(input('Seleccione una opcion: '))

                #Validaciones MENU
                if opcMENU == 1:
                    self.registro()
                    self.tarjeta = None
                    self.nombre = None
                    self.apellido = None
                    self.pin = None
                    self.monto = 0
                    ing = True
                if opcMENU == 2 and ing == True:
                    self.depositar()
                if opcMENU == 3 and ing == True:
                    self.Retirar()
                if opcMENU == 4 and ing == True:
                    self.getSaldo()
                if ing != True:
                    print('*******No esta registrado, intente de nuevo******* \n')

"""Llamada al metodo interfaz"""
d = Cliente().menu()








