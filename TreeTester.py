# importazione delle librerie
import numpy as np
import matplotlib.pyplot as plt
import random
import time

# importazione delle classi
from NormalBinaryTree import NormalBinaryTree
from RedBlackTree import RedBlackTree
from AVLTree import AVLTree

class TreeTester():
    def __init__(self, treeTypes):
        self.instantiate_trees(treeTypes)
        self.clear_results()


    def instantiate_trees(self, treeTypes):
        self.trees = []
        for treeType in treeTypes:
            match treeType:
                case 'NB':
                    self.trees.append(NormalBinaryTree())
                case 'RB':
                    self.trees.append(RedBlackTree())
                case 'AVL':
                    self.trees.append(AVLTree())


    def clear_results(self):
        self.results = []
        for _ in range(len(self.trees)):
            self.results.append({
                'x': [],
                'y': [],
            })


    def tree_height_test(self, arr_length, num_tests):
        self.clear_results()
        for i in range(num_tests):
            arr = list(range(1, arr_length + 1))
            arr = random.sample(arr, len(arr))

            for index, tree in enumerate(self.trees):
                for value in arr:
                    tree.insert(value)

                self.results[index]['x'].append(i)
                self.results[index]['y'].append(tree.height)
                tree.clear()


    def average_tree_height_test(self, arr_length, num_tests):
        self.clear_results()
        for i in range(1, arr_length + 1):
            for index, tree in enumerate(self.trees):
                sum = 0
                for _ in range(num_tests):
                    arr = list(range(1, i + 1))
                    arr = random.sample(arr, len(arr))

                    for value in arr:
                        tree.insert(value)

                    sum = sum + tree.height
                    tree.clear()

                self.results[index]['x'].append(i)
                self.results[index]['y'].append(sum / num_tests)


    def average_building_time(self, arr_length, num_tests):
        self.clear_results()
        for i in range(0, arr_length + 1):
            for index, tree in enumerate(self.trees):
                sum = 0
                for _ in range(num_tests):
                    arr = list(range(1, i + 1))
                    arr = random.sample(arr, len(arr))

                    start = time.perf_counter()
                    for value in arr:
                        tree.insert(value)
                    end = time.perf_counter()

                    sum = sum + (end - start)
                    tree.clear()

                self.results[index]['x'].append(i)
                self.results[index]['y'].append(sum / num_tests)


    def average_insertion_time(self, arr_length, num_tests):
        self.clear_results()
        for i in range(0, arr_length + 1):
            for index, tree in enumerate(self.trees):
                sum = 0
                for _ in range(num_tests):
                    arr = list(range(1, i + 1))
                    arr = random.sample(arr, len(arr))

                    for value in arr:
                        start = time.perf_counter()
                        tree.insert(value)
                        end = time.perf_counter()
                        sum = sum + (end - start)

                    tree.clear()

                self.results[index]['x'].append(i)
                self.results[index]['y'].append(sum / num_tests / arr_length)


    def average_searching_time(self, arr_length, num_tests):
        self.clear_results()
        for i in range(1, arr_length + 1):
            for index, tree in enumerate(self.trees):
                sum = 0
                for _ in range(num_tests):
                    arr = list(range(1, i + 1))
                    arr = random.sample(arr, len(arr))

                    for value in arr:
                        tree.insert(value)

                    for value in arr:
                        start = time.perf_counter()
                        tree.iterative_search(value)
                        end = time.perf_counter()
                        sum = sum + (end - start)

                    tree.clear()

                self.results[index]['x'].append(i)
                self.results[index]['y'].append(sum / num_tests / i)


    def plot_results(self, xlabel='', ylabel='', save=False, img_name='', offset=False):
        # creo l'immagine che conterrà il grafico
        plt.figure(figsize=(8, 4))
        for index, tree in enumerate(self.trees):
            if offset is True:
                self.results[index]['y'] = np.array(self.results[index]['y']) - (index - 1) * 0.05
            plt.plot(self.results[index]['x'], self.results[index]['y'], marker='o', markersize=4, linestyle='-',
                     label=f'{tree.get_name()}')

        plt.xlabel(xlabel)
        plt.xlim(0)
        plt.ylabel(ylabel)
        plt.ylim(0)

        # Adjust the legend location
        plt.legend(loc='lower right')

        plt.grid(True)
        fig = plt.gcf()
        plt.show()

        if save is True:
            fig.savefig(img_name)

        plt.close()
