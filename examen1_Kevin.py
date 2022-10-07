from cmath import pi
from operator import truediv
import os


invalido = False
valido = True

class CajeroAutomatico:
   

    def __init__(self):
        self.numSerie = None
        self.marca = None
        self.tipo = None
        self.color = None
        self.ubicacion = None
        self.tarjetas = []
        self.monto = 0

    def depositar(self):
        numTarjeta = int(input('Ingrese el numero de su tarjeta: \n'))
        self.tarjetas.append(numTarjeta)
        print(self.tarjetas)
        dep = int(input('Ingrese su monto a depositar: \n'))
        print(f'Usted ha depositado: {dep}')
        print(f'Su nuevo monto es de {self.monto + dep}\n')
        self.monto += dep
	    
    def Retirar(self):
        verTarjeta = int(input('Ingrese su tarjeta: \n'))
        i = 0
        while i < len(self.tarjetas):
            if verTarjeta != self.tarjetas[i]:
                print('Numero de tarjeta incorrecto \n')
            else:
                ret = int(input('¿Que cantidad desea retirar?: '))
                print(f'Su monto actual es, {self.monto}')
                if self.monto >= ret:
                    print(f'Usted a retirado: {ret} , su nuevo monto es {self.monto - ret} \n')
                    self.monto-=ret
                else:
                    print('Monto invalido \n')
            i += 1
   
           
    def getSaldo(self):
        print(f'Su saldo es de {self.monto}')

class Cliente(CajeroAutomatico):
    nombre = 'Kevin'
    apellido = 'Barrantes'
    pin = 1234

    def ingreso(self):
        print('Bienvenido al cajero automatico \n')
        ingPass = int(input('Ingrese su contraseña\n'))

        #Validacion ingreso
        if ingPass != self.pin:
            return False
        else: 
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








