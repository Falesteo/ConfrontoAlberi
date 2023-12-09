# importazione delle classi
from NormalBinaryTree import NormalBinaryTree
from RedBlackTree import RedBlackTree
from AVLTree import AVLTree

# importazione delle classi
from TreePainter import TreePainter
from TreeTester import TreeTester


# main function
def main():
    trees_info = [{
        'treeType': 'NB',
        'build_mode': 'random',
        'num_values': 31,
    }, {
        'treeType': 'RB',
        'build_mode': 'random',
        'num_values': 31,
    }, {
        'treeType': 'AVL',
        'build_mode': 'random',
        'num_values': 31,
    }]

    treePainter = TreePainter(trees_info)
    # treePainter.draw()
    # treePainter.save_subplots()


    treeTester = TreeTester(['RB', 'NB', 'AVL'])

    # treeTester.tree_height_test(31, 50, True, True)
    # treeTester.plot_results('# Test', 'Altezza dell\'albero', True, 'Altezza alberi', True)
    #
    # treeTester.average_tree_height_test(64, 1000, True, True)
    # treeTester.plot_results('Dimensione dell\'albero', 'Altezza media',  True, 'Altezza media')
    #
    # treeTester.average_building_time(64, 1000, True, True)
    # treeTester.plot_results('Dimensione dell\'albero', 'Tempo medio di costruzione dell\'albero', True, 'Tempo medio di costruzione')
    #
    # treeTester.average_insertion_time(64, 1000, True, True)
    # treeTester.plot_results('Dimensione dell\'albero', 'Tempo medio di inserimento di un elemento',  True, 'Tempo medio di inserimento')

    treeTester.average_searching_time(64, 1000, True, True)
    treeTester.plot_results('Dimensione dell\'albero', 'Tempo medio di ricerca un elemento',  True, 'Tempo medio di ricerca')


if __name__ == '__main__':
    main()