from collections import deque
import time

class Cola():
    def __init__(self):
        self.elementos = deque()

    def mostrar(self):
        print("Clientes en cola:")
        for elem in self.elementos:
            print(elem, end=" ")
        print()

    def Clientes(self, code):
        print(f"Su código de cliente es: {code}")
        d= self.elementos.appendleft(code)
        d = self.mostrar()
        time.sleep(.8)
        return d
    
    def Atender(self, flag):
        if not self.empty():
            n= self.elementos.pop()
            print(f"El cliente atendido fue {n}")
            if flag== True:
                self.mostrar()
        else:
            print("No hay clientes en cola")
        return n
    
    def empty(self):
        if len(self.elementos) ==0:
            return True
        
def exec ():
    s1 = Cola()
    s2 = Cola()
    s3 = Cola()
    c1=0 
    c2=0
    c3 =0
    
    instrucc = "Para registrarse como cliente escribir C y el código del servicio sin espacio. Para atender presionar A y el código."
    while (True):
        print ("Servicios disponibles: Servicio 01  Servicio 02 Servicio 03")
        print("Para salir presione 0")
        ans= input(instrucc)

        if ans.lower() == "c1":
            c1+=1
            code= "A"+str(c1)
            s1.Clientes(code)
        elif ans.lower() =="c2":
            c2+=1
            code= "A"+str(c2)
            s2.Clientes(code)
        elif ans.lower() == "c3":
            c3+=1
            code="A"+str(c3)
            s3.Clientes(code)
        elif ans.lower() == "a1":
            s1.Atender(True)
        elif ans.lower() == "a2":
            s2.Atender(True)
        elif ans.lower() == "a3":
            s3.Atender(True)
        elif int(ans)==0:
            print("Muchas gracias")
            break

exec()
exit()