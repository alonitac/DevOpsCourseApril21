# install by: pip install matplotlib
import matplotlib.pyplot as plt


def names_histogram(names, ignore=[]):
    """
    Calculates how frequent each name is
    Hint: use dictionary

    :param names: list of names (strings)
    :param ignore: (Optional) list of names to ignore
    :return: List of tuples in the form ('John', 4)
             Such that 'John' appears 4 times in the list
    """
    names_count = dict()
    for name in names:
        if name not in names_count:
            if name not in ignore:
                names_count[name] = 1
        else:
            names_count[name] += 1

    return list(names_count.items())



    # create a liat
    # iterate over names
    # i = 1
    # iterate again over names
    # if the name from 1st loop equals to current
    # increase i by 1
    # mark this name as visited
    # add (name, i) to the list

    pass   # your code here


def draw_first_n(hist, n=30):
    names = [h[0] for h in hist[:n]]
    freq = [h[1] for h in hist[:n]]
    plt.bar(names, freq)
    plt.show()


if __name__ == '__main__':

    with open('names.txt') as file:
        lines = file.readlines()
        names = [line.rstrip() for line in lines]

    hist = names_histogram(names, ignore=['Jordi', 'Ram'])
    draw_first_n(hist, n=5)
    print('Done')
