import matplotlib.pyplot as plt
iris.plot()
plt.show()
iris.plot(kind = 'scatter', x = 'petal.length', y = 'sepal.length')
plt.show()
x = iris['petal.length']
y = iris['sepal.length']
a = iris['petal.width']
b = iris['sepal.width']
plt.scatter(x, y, c='green')
plt.scatter(a, b, c='red')
plt.show()
iris['petal.length'].plot(kind = 'hist')
plt.show()

