import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", font_scale=1.0)

np.random.seed(52)

size = 10000
shape = 4.7
scale = 9.768

population = np.random.gamma(shape, scale, size) #General population

n1 = 5
n2 = 50
means1 = []
means2 = []

for i in range(1000): # sample size = 5, we get 1000 different samples
    sample = np.random.choice(population, size=n1)
    mean = np.mean(sample)
    means1.append(mean)

for i in range(1000): # sample size = 50, we get 1000 different samples
    sample = np.random.choice(population, size=n2)
    mean = np.mean(sample)
    means2.append(mean)


fig, axes = plt.subplots(1, 3, figsize=(16, 4))

#General population visualisation
sns.histplot(population, bins=30, kde=True, color='lightcoral', ax = axes[0])
axes[0].set_title('Исходная совокупность\n(Гамма-распределение)')
axes[0].set_xlabel('Значение')
axes[0].set_ylabel('Плотность')

#means of sample with size = 5
sns.histplot(means1, bins=20, kde=True, color='steelblue', ax=axes[1])
axes[1].set_title('Средние (размер выборки = 5)\n1000 выборок')
axes[1].set_xlabel('Среднее значение')
axes[1].set_ylabel('Плотность')

#means of sample with size = 50
sns.histplot(means2, bins=20, kde=True, color='steelblue', ax=axes[2])
axes[2].set_title('Средние (размер выборки = 50)\n1000 выборок')
axes[2].set_xlabel('Среднее значение')
axes[2].set_ylabel('Плотность')


plt.tight_layout()
plt.show()