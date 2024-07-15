import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("iris.csv")
iris.head(5)
iris.tail(5)
iris.describe()
iris.info()
iris.plot()
plt.show()
