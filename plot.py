import matplotlib.pyplot as plt


def show(x, y, n):
    plt.style.use('seaborn-v0_8-pastel')
    ax = plt.subplot()
    ax.set(title='Gravitational potential FEM solution', xlabel='n = ' + str(n))
    ax.plot(x, y, color='red')

    plt.show()
