# importazione delle librerie grafiche
import networkx as nx


# importazione delle classi dell'albero binario base
from BinaryTree import BinaryTreeNode
from BinaryTree import BinaryTree


# nodo dell'albero rosso-nero
class RedBlackTreeNode(BinaryTreeNode):
    def __init__(self, key, color, left=None, right=None, p=None, size=0, layer=0):
        super().__init__(key, left, right, p, size, layer)
        self.color = color


# classe dell'albero rosso-nero
class RedBlackTree(BinaryTree):
    def __init__(self):
        super().__init__()
        self.null = RedBlackTreeNode(None, 'black')
        self.root = self.null
        self.height = 0


    def get_name(self):
        return 'Red-Black Tree'


    # algoritmi per la gestione di alberi rosso-neri
    def left_rotate(self, x):
        # Si prende y come il figlio destro di x
        y = x.right

        # Si sposta il sottoalbero sinistro di y a destra di x
        x.right = y.left
        if y.left != self.null:
            y.left.p = x

        # Si collega il padre di x a y
        y.p = x.p
        if x.p == self.null:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        # Si pone x come figlio sinistro di y
        y.left = x
        x.p = y

        y.size = x.size
        x.size = x.left.size + x.right.size + 1


    def right_rotate(self, y):
        # Si prende y come il figlio sinistro di x
        x = y.left

        # Si sposta il sottoalbero destro di y a sinistra di x
        y.left = x.right
        if x.right != self.null:
            x.right.p = y

        # Si collega il padre di x a y
        x.p = y.p
        if y.p == self.null:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x

        # Si pone x come figlio sinistro di y
        x.right = y
        y.p = x

        x.size = y.size
        y.size = y.right.size + y.left.size + 1


    def insert(self, key):
        new_node = RedBlackTreeNode(key, 'none', self.null, self.null, self.null)
        self._insert(new_node)
        self.update_layers(self.root)


    def _insert(self, z):
        y = self.null
        x = self.root

        # Si scende lungo l'albero finché non si giunge a una foglia
        while x != self.null:
            y = x
            y.size = y.size + 1
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        # Si collega l'elemento in posizione
        z.p = y
        z.size = 1
        if y == self.null:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        # Si assegnano dei puntatori nulli come figli
        z.left = self.null
        z.right = self.null
        z.layer = 0

        # Infine si assegna il colore rosso e si chiama la funzione di fixup
        z.color = 'red'
        self.RB_insert_fixup(z)


    def RB_insert_fixup(self, z):
        # Finché il padre è rosso
        while z.p.color == 'red':
            # Si prende lo zio
            if z.p == z.p.p.left:
                y = z.p.p.right
                # Se anche lo zio è rosso
                if y.color == 'red':
                    # Si modificano i colori
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                # Se anche lo zio è rosso
                if y.color == 'red':
                    # Si modificano i colori
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.left_rotate(z.p.p)
        self.root.color = 'black'


    # funzione per il disegno dell'albero
    def plot(self):
        # creo il grafico
        G = nx.DiGraph()

        def add_edges(node, parent=None, pos=None, posx=0.0, layer_spacing=1.0):
            if node is not self.null:
                posy = -node.layer
                if node.color == 'red':
                    background_color = '#FFA6A6'
                else:
                    background_color = '#A5A5A5'
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