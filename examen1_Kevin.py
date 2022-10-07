from ast import Return
from cmath import pi
from operator import truediv
import os
from datetime import datetime



invalido = False
valido = True

tarjIngreso = []

class Cliente:
   

    def __init__(self):
        self.tarjeta = None
        self.monto = 0
        self.depos = 0
        self.retir = 0

    def atributos(self):
        self.numSerie = 123231
        self.marca = None
        self.tipo = None
        self.color = None
        self.ubicacion = None

    def depositar(self):
        print(self.tarjeta)
        dep = int(input('Ingrese su monto a depositar: \n'))
        self.depos = dep
        print(f'*******Usted ha depositado: {dep}********** \n')
        print(f'*******Su nuevo monto es de {self.monto + dep}********\n\n')
        self.monto += dep
        self.addInventario('Deposito \n', self.depos)
    

	    
    def Retirar(self):
        print(self.tarjeta)
        
        ret = int(input('¿Que cantidad desea retirar?: '))
        self.retir = ret
        print(f'Su monto actual es, {self.monto}')
        if self.monto >= ret:
            print(f'********Usted a retirado: {ret} , su nuevo monto es {self.monto - ret}********* \n')
            self.monto-=ret
        else:
            print('Monto invalido \n')
        self.addInventario('Retiro \n', self.retir)

    def crearInventario(self, tarjeta, nombre, apellido):
        with open('inventario.txt', 'a+') as inv:
            w = inv.write(str(datetime.today().strftime('%Y-%m-%d')) + ' ' + str(tarjeta) + ' ' + nombre + ' ' + apellido + ': \n')

    def addInventario(self, accion, aMonto):
        with open('inventario.txt', 'a+') as inv:
            a = inv.write(str(datetime.today().strftime('%Y-%m-%d')) + ' ' + accion + ' ' + str(aMonto) + '\n')
           
    def getSaldo(self):
        print(f'********Su saldo es de {self.monto} ********\n')
        self.addInventario('Ver Saldo \n', self.monto)

class CajeroAutomatico(Cliente):

    
    nombre = None
    apellido = None
    pin = None

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
            self.crearInventario(self.tarjeta, self.nombre, self.apellido)

            return True
        else:
            return False

        #Validacion ingreso
        # if ingPass != self.pin:
        #     return False
        # else:
        #     self.tarjeta = tarjPass
        #     
        #     return True
        
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

d = CajeroAutomatico().menu()








