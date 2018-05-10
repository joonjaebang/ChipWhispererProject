#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys

def plot(filename):
    data = np.load(filename)

    data = data[0]

    x_data = range(0, 25004)
    plt.plot(x_data, data)
    plt.show()

if __name__ == "__main__":
    plot(sys.argv[1])
