import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta


def display(vector, name="USD", vis=0):
    # matplotlib default window configuration
    if vis == 0:
        plt.style.use('classic')
    else:
        plt.style.use('_mpl-gallery')

    # inverting dates to make sure that today's info is on the right
    x = []
    for i in range(len(vector)):
        x.append(vector[len(vector) - i - 1])

    # converting numeration to date, then invert it
    y = []
    curdate = datetime.date(datetime.now())
    for i in range(len(vector)):
        # y.append(curdate - timedelta(days=(len(vector) - i - 1)))
        y.append(len(vector) - i - 1)

    # error checks
    if len(x) != len(y):
        print('error: length does not match!')
        y = list(range(len(x)))
        if len(x) == 0:
            print('error: no data received!')
            return -1

    # plotting
    fig, axs = plt.subplots(1, 1, figsize=(18, 6))
    ys = [str(el) for el in y]
    axs.plot(ys, x)
    plt.xlabel(" Dates ")
    plt.ylabel(" RUB ")
    plt.grid()
    plt.title(name)
    # save tmp image in the directory
    try:
        plt.savefig("tmp_img/export_img.png")
    except FileNotFoundError:
        os.mkdir("tmp_img")
        plt.savefig("tmp_img/export_img.png")

    directory = os.getcwd()
    return os.path.join(directory, os.path.normpath("tmp_img/export_img.png"))


def delete(place):
    try:
        os.remove(place)
        print("image removed")
        return 0
    except OSError:
        print("not possible to delete an not existent file")
        return 1


display([1,2,3,4,5])