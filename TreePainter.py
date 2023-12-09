# importazione delle librerie
import numpy as np
import matplotlib.pyplot as plt
import random

# importazione delle classi
from NormalBinaryTree import NormalBinaryTree
from RedBlackTree import RedBlackTree
from AVLTree import AVLTree


class TreePainter():
    def __init__(self, trees_info):
        self.trees = []
        for tree_info in trees_info:
            tree = self.instantiate_tree(tree_info['treeType'])
            self.build_tree(tree, tree_info['build_mode'], tree_info['num_values'])
            self.trees.append(tree)

        self.max_height = 0
        for tree in self.trees:
            self.max_height = max(tree.height, self.max_height)


    def instantiate_tree(self, treeType):
        match treeType:
            case 'NB':
                return NormalBinaryTree()
            case 'RB':
                return RedBlackTree()
            case 'AVL':
                return AVLTree()


    def build_tree(self, tree, list_mode, list_length):
        match list_mode:
            case 'ordered':
                arr = list(range(1, list_length + 1))
            case 'random':
                arr = list(range(1, list_length + 1))
                arr = random.sample(arr, len(arr))

        for value in arr:
            tree.insert(value)


    # mostro l'immagine finale
    def draw(self):
        # creo l'immagine che conterrà gli alberi
        if len(self.trees) == 1:
            self.fig, self.axes = plt.subplots(figsize=(16, 10))
            for y in range(1, self.max_height + 1):
                self.axes.axhline(-y, color='#ddd', linestyle='--', zorder=0)
            self.trees[0].plot()
        else:
            self.fig, self.axes = plt.subplots(1, len(self.trees), figsize=(16 * len(self.trees), 10), sharey=True)
            plt.subplots_adjust(top=.95, bottom=.05, left=0, right=1, hspace=0, wspace=0)

            # aggiungo linee orizzontali per evidenziare i livelli degli alberi
            for i in range(len(self.trees)):
                for y in range(1, self.max_height + 1):
                    self.axes[i].axhline(-y, color='#ddd', linestyle='--', zorder=0)

            # aggiungo i disegni degli alberi all'immagine
            for index, tree in enumerate(self.trees):
                plt.sca(self.axes[index])
                tree.plot()

        plt.show()

    # salvo i grafi in immagini singolarmente
    def save_subplots(self):
        for index, tree in enumerate(self.trees):
            fig, ax = plt.subplots(figsize=(16, 10))
            tree.plot()
            for y in range(1, self.max_height + 1):
                ax.axhline(-y, color='#ddd', linestyle='--', zorder=0)

            ax.set_ylim(self.axes[index].get_ylim())

            plt.savefig(f'tree_{index + 1}.png')
            plt.close()