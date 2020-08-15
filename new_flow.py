
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# printing the current directory
print(os.getcwd())

def plot():
    plt.scatter(range(10), range(10))
    plt.xlabel('range 1 to 10')
    plt.ylabel('range 1 to 10')