class Node:
    def __init__(self, data):
        self.data = data
        self.prox = None

class listaEncadeada:
    def __init__(self):
        self.head = None

    def insert(self, data):
        novono = Node(data)
        novono.prox = self.head
        self.head = novono

    def insertion_sort(self):
        if not self.head or not self.head.prox:
            return

        sorted_head = self.head
        current = self.head.prox
        sorted_head.prox = None

        while current:
            temp = current
            current = current.prox

            if temp.data < sorted_head.data:
                temp.prox = sorted_head
                sorted_head = temp
            else:
                search = sorted_head
                while search.prox and search.prox.data < temp.data:
                    search = search.prox
                
                temp.prox = search.prox
                search.prox = temp

        self.head = sorted_head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.prox
        print()


lista5 = listaEncadeada()
lista5.insert(5)
lista5.insert(6)
lista5.insert(7)
lista5.insert(8)
lista5.insertion_sort()
print("lista ja ordenada")
lista5.print_list()

lista1 = listaEncadeada()
lista1.insert(4)
lista1.insert(3)
lista1.insert(2)
lista1.insert(1)
lista1.insertion_sort()
print("ordem inversa:")
lista1.print_list()

lista3 = listaEncadeada()
lista3.insert(1)
lista3.insert(2)
lista3.insert(1)
lista3.insert(2)
lista3.insertion_sort()
print("duplicados:")
lista3.print_list()

lista4 = listaEncadeada()
lista4.insert(9)
lista4.insert(9)
lista4.insert(9)
lista4.insert(9)
lista4.insertion_sort()
print("sem repetição:")
lista4.print_list()
