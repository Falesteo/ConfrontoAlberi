# importazione delle librerie grafiche
import networkx as nx


# importazione delle classi dell'albero binario base
from BinaryTree import BinaryTreeNode
from BinaryTree import BinaryTree


# nodo dell'albero AVL
class AVLTreeNode(BinaryTreeNode):
    def __init__(self, key, left=None, right=None, p=None, size=0, layer=0, height=1):
        super().__init__(key, left, right, p, size, layer)
        self.height = height


# classe dell'albero AVL
class AVLTree(BinaryTree):
    def __init__(self):
        super().__init__()


    def get_name(self):
        return 'AVL Tree'


    def get_height(self, x):
        if x is self.null:
            return 0
        return x.height


    def get_balance(self, x):
        if x is self.null:
            return 0
        return self.get_height(x.left) - self.get_height(x.right)


    def update_height(self, x):
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))


    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y


    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x


    # Funzione di inserimento AVL
    def insert(self, key):
        new_node = AVLTreeNode(key, self.null, self.null, self.null)
        self.root = self._insert(self.root, new_node)
        self.update_layers(self.root)


    def _insert(self, root, z):
        if root == self.null:
            return z

        if z.key < root.key:
            root.left = self._insert(root.left, z)
        elif z.key > root.key:
            root.right = self._insert(root.right, z)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # 4 casi di sbilanciamento
        # Sinistra-Sinistra
        if balance > 1 and z.key < root.left.key:
            return self.right_rotate(root)

        # Destra-Destra
        if balance < -1 and z.key > root.right.key:
            return self.left_rotate(root)

        # Sinistra-Destra
        if balance > 1 and z.key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Destra-Sinistra
        if balance < -1 and z.key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    # funzione per il disegno dell'albero
    def plot(self):
        # creo il grafico
        G = nx.DiGraph()

        def add_edges(node, parent=None, pos=None, posx=0.0, layer_spacing=1.0):
            if node is not self.null:
                posy = -node.layer
                if node.left is self.null and node.right is self.null:
                    background_color = '#6666cc'
                else:
                    background_color = '#aaaaff'

                G.add_node(node.key, pos=(posx, posy), color=background_color, border_color='#000')

                if parent is not None:
                    G.add_edge(parent.key, node.key)
                if node.left is not None:
                    add_edges(node.left, node, pos, posx - 1 * layer_spacing, layer_spacing / 2.25)
                if node.right is not None:
                    add_edges(node.right, node, pos, posx + 1 * layer_spacing, layer_spacing / 2.25)

        add_edges(self.root)

        pos = nx.get_node_attributes(G, 'pos')
        node_colors = nx.get_node_attributes(G, 'color')
        node_border_colors = nx.get_node_attributes(G, 'border_color')
        labels = {node: str(node) for node in G.nodes}

        nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000, node_color=list(node_colors.values()),
                font_color='#000', font_size=16, edge_color='#000', edgecolors=list(node_border_colors.values()))

        return G