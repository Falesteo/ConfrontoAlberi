# nodo dell'albero binario di ricerca
class BinaryTreeNode:
    def __init__(self, key, left=None, right=None, p=None, size=0, layer=0):
        self.key = key
        self.left = left
        self.right = right
        self.p = p
        self.size = size
        self.layer = layer


# albero binario di ricerca
class BinaryTree:
    def __init__(self):
        self.null = BinaryTreeNode(None)
        self.root = self.null
        self.height = 0


    # operazioni comuni a tutti i tipi di alberi binari
    # operazioni di ricerca
    def recursive_search(self, x, key):
        if x != self.null:
            if key == x.key:
                return x
            elif key < x.key:
                return self.recursive_search(x.left, key)
            elif key > x.key:
                return self.recursive_search(x.right, key)
        else:
            print(f'L\'elemento con chiave {k} non è presente nell\'albero')
            return None


    def iterative_search(self, k):
        x = self.root
        while True:
            if x == self.null:
                print(f'L\'elemento con chiave {k} non è presente nell\'albero')
                return None
            elif k == x.key:
                return x
            elif k < x.key:
                x = x.left
            elif k > x.key:
                x = x.right


    def minimum(self, x):
        while x.left != self.null:
            x = x.left
        return x


    def maximum(self, x):
        while x.right != self.null:
            x = x.right
        return x


    def predecessor(self, x):
        if x.left != self.null:
            return maximum(x.left)
        y = x.p
        while y != self.null and x == y.left:
            x = y
            y = y.p
        return y


    def successor(self, x):
        if x.right != self.null:
            return minimum(x.right)
        y = x.p
        while y != self.null and x == y.right:
            x = y
            y = y.p
        return y


    # operazioni di ottenimento di informazioni
    def get_size(self, x):
        if x is self.null:
            return 0
        else:
            return self.get_size(x.left) + self.get_size(x.right) + 1


    def get_rank(self, x):
        rank = x.left.size + 1
        y = x
        while y is not self.root:
            if y is y.p.right:
                rank += y.p.left.size + 1
            y = y.p

        return rank


    def select_nth(self, x, n):
        # calcolo il rango di x
        rank = x.left.size + 1

        # se corrisponde all'elemento cercato lo restituisco
        if n is rank:
            return x

        # altrimenti lo confronto con i e scendo lungo l'albero
        elif n < rank:
            return self.select_nth(x.left, n)
        else:
            return self.select_nth(x.right, n - rank)


    # operazioni di aggiornamento degli attributi dei nodi
    def update_layers(self, x, layer = 1):
        x.layer = layer
        self.height = max(self.height, layer)

        if x.left != self.null:
            self.update_layers(x.left, layer + 1)
        if x.right != self.null:
            self.update_layers(x.right, layer + 1)


    # operazioni di stampa
    def inorder_walk(self, x):
        if x != self.null:
            self.inorder_walk(x.left)
            print(str(x.key) + ", ", end='')
            self.inorder_walk(x.right)


    def preorder_walk(self, x):
        if x != self.null:
            print(str(x.key) + '(', end='')
            self.preorder_walk(x.left)
            print(',', end='')
            self.preorder_walk(x.right)
            print(')', end='')
        else:
            print('_', end='')


    # operazioni con modifica
    def trapianto(self, u, v):
        if u.p == self.null:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v

        if v != self.null:
            v.p = u.p


    def clear(self):
        self.root = self.null
        self.height = 0