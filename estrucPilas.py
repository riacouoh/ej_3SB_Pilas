import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         if len(self.items) <=8:
            self.items.append(item)
         else:
            print("Max capacity exceeded.")

     def extraer(self):
         if len(self.items) !=0:
            self.items.pop()
         elif len(self.items) ==0:
            return IndexError
    
     def dataframe(self):
        # initialize list of lists
        data = [self.items]
        # Create the pandas DataFrame
        df = pd.DataFrame(data)
        print(df)

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)
     
p = Pila()

print(p.estaVacia())
p.incluir("X")
p.incluir("Y")
p.extraer()
p.extraer()
p.extraer()
p.incluir("V")
p.incluir("W")
p.extraer()
p.incluir("R")
p.dataframe()