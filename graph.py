from cProfile import label
from datetime import datetime
import matplotlib.pyplot as plt

def read(brand):
    a = []
    if brand == "Intermarché":
        brand = "Intermarche"
    with open(f"{brand}/history.dat", "r" , encoding="utf-8") as f:
        code = f.read().replace("None", "0")
        code = code.split(", ")
        for x in code:
            a.append(float(x))
    return a


def graph():
    with open("brands.txt", "r", encoding='utf-8') as f:
        brands = f.read()
    brands = brands.split("\n")
    print(brands)
    data = {}
    for x in brands:
        data[x] = read(x)
    l = []
    for x in data:
        print(x)
        plt.plot(data[x], label=x)
    plt.savefig("graph.png")
