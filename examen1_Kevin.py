from cmath import pi
from curses import noecho
from operator import truediv
import os
from datetime import datetime



invalido = False
valido = True

tarjIngreso = []

class CajeroAutomatico:
   

    def __init__(self):
        self.tarjeta = None
        self.monto = 0

    def atributos(self):
        self.numSerie = 123231
        self.marca = None
        self.tipo = None
        self.color = None
        self.ubicacion = None

    def depositar(self):
        print(self.tarjeta)
        dep = int(input('Ingrese su monto a depositar: \n'))
        print(f'Usted ha depositado: {dep}')
        print(f'Su nuevo monto es de {self.monto + dep}\n')
        self.monto += dep
        self.addInventario('Deposito \n')
    

	    
    def Retirar(self):
        print(self.tarjeta)
        
        ret = int(input('¿Que cantidad desea retirar?: '))
        print(f'Su monto actual es, {self.monto}')
        if self.monto >= ret:
            print(f'Usted a retirado: {ret} , su nuevo monto es {self.monto - ret} \n')
            self.monto-=ret
        else:
            print('Monto invalido \n')
        self.addInventario('Retiro \n')

    def crearInventario(self, tarjeta, nombre, apellido):
        with open('inventario.txt', 'w') as inv:
            w = inv.write(str(datetime.today().strftime('%Y-%m-%d')) + '' + str(tarjeta) + '' + nombre + '' + apellido + ': ')

    def addInventario(self, accion):
        with open('inventario.txt', 'a') as inv:
            a = inv.write(str(datetime.today().strftime('%Y-%m-%d')) + '' + accion + '\n')
           
    def getSaldo(self):
        print(f'Su saldo es de {self.monto}')
        self.addInventario('Ver Saldo \n')

class Cliente(CajeroAutomatico):

    
    nombre = 'Kevin'
    apellido = 'Barrantes'
    pin = 1234

    def ingreso(self):
        print('Bienvenido al cajero automatico \n')

        tarjPass = int(input('Ingrese su numero de tarjeta: '))
        ingPass = int(input('Ingrese su contraseña: '))

        #Validacion ingreso
        if ingPass != self.pin:
            return False
        else:
            self.tarjeta = tarjPass
            self.crearInventario(self.tarjeta, self.nombre, self.apellido)
            return True
        
    def menu(self):
       

        if self.ingreso() != True:
            print('No ha podido ingresar al sistema, intente de nuevo')
            
        else:
            opcMENU = 0
            while opcMENU != 4:
                
                print(f'MENU {self.nombre} {self.apellido}\n'
                    '1. Depositar\n'
                    '2. Retirar\n'
                    '3. Ver saldo\n'
                    '4. Salir\n')
                opcMENU = int(input('Seleccione una opcion: '))
                
                #Validaciones MENU
                if opcMENU == 1:
                    self.depositar()
                if opcMENU == 2:
                    self.Retirar()
                if opcMENU == 3:
                    self.getSaldo()



d = Cliente().menu()








