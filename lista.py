from No import No


class Lista:


    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,valor):
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            self.tail.proximo = No(valor)
            self.tail = self.tail.proximo

    def addFirst(self,valor):
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            novo = No(valor)
            novo.proximo = self.head
            self.head = novo

    def size(self):
        cont = 0
        i = x.head
        while i is not None:
            cont += 1
            i = i.proximo
        return cont

    def remove(self,valor):
        p = None
        i = x.head
        if self.tail is None:
            return ("Lista vazia")
        while i is not None:
            if i == valor:
                p.proximo = i.proximo
                i.dado = None
                i = p.proximo
            p = i
            i = i.proximo
            #tem que assumir o próximo do próximo

    def pop(self):
        a = None
        i = x.head
        if self.tail is None:
            return ("Lista vazia")
        if i.proximo is None:
            x.head = None
            x.tail = None
            return i.dado
        while i is not None:
            a = i
            i = i.proximo
            if i.proximo is None:
                e = i.dado
                i = None
                a.proximo = None
                return e

x = Lista()
x.append(1)
x.append(1)
x.append(1)
x.append(1)
x.append(2)
x.append(3)
x.addFirst(14)
x.append(4)
x.addFirst(0)
x.addFirst(-1)
e = x.pop()
x.remove(2)
i = x.head
while i is not None:
    print(i.dado)
    i = i.proximo
i = x.size()
print ("Tamanho: ",i)
print (e)
