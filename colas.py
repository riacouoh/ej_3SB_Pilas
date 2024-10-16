from collections import deque
import time

class Cola():
    def __init__(self):
        self.elementos = deque()

    def colas (self):
        d = deque(self.elementos)
        return d

    def mostrar(self):
        d = self.colas()
        for elem in d:
            print(elem, end=" ")
        print()

    def add(self, num):
        res = [int(ele) for ele in num.split()]
        for i in res:
            d= self.elementos.appendleft(i)
            d = self.mostrar()
            time.sleep(.8)
        return d
    
    def elim(self, flag):
        if not self.empty():
            n= self.elementos.pop()
            if flag== True:
                self.mostrar()
        return n
    
    def empty(self):
        if len(self.elementos) ==0:
            return True

def dosColas (c1, c2):
    sumCol = Cola()
    while c1.empty() != True and c2.empty()!= True:
        one = c1.elim(False)
        two = c2.elim(False)
        three= one + two
        sumCol.add(str(three))
        

c1 = Cola()
b= "6 7 8 9"
c1.add(b)
c1.elim(True)
c2 = Cola()
c= "15 10 3 5"
c2.add(c)
c2.elim(True)

dosColas(c1, c2)
exit()