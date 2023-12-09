# importazione delle librerie grafiche
import networkx as nx


# importazione delle classi dell'albero binario base
from BinaryTree import BinaryTreeNode
from BinaryTree import BinaryTree


class NormalBinaryTree(BinaryTree):
    def __init__(self):
        super().__init__()


    def get_name(self):
        return 'Normal Binary Tree'


    def insert(self, key):
        new_node = BinaryTreeNode(key, self.null, self.null, self.null)
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


    # cancellazione di un elemento data la chiave
    def delete(self, key):
        z = self.tree_search(self.root, key)
        if z != None:
            if z.left == self.null:
                self.trapianto(z, z.right)
            elif z.right == self.null:
                self.trapianto(z, z.left)
            else:
                y = self.tree_minimum(z.right)
                if y.p != z:
                    self.trapianto(y, y.right)
                    y.right = z.right
                    y.right.p = y
                self.trapianto(z, y)
                y.left = z.left
                y.left.p = y
        else:
            print("\nImpossibile effettuare cancellazione: nodo con chiave fornita non trovato.")


    # funzione per il disegno dell'albero
    def plot(self):
        # creo il grafico
        G = nx.DiGraph()

        def add_edges(node, parent=None, pos=None, posx=0.0, layer_spacing=1.0):
            if node is not self.null:
                posy = -node.layer
                G.add_node(node.key, pos=(posx, posy), color='#c8e0d2', border_color='#000')

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
                font_color='#000', font_size=16, edge_color='#000',
                edgecolors=list(node_border_colors.values()))
        return G