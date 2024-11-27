import matplotlib.pyplot as plt
import numpy as np






x = np.linspace(0, 2 * np.pi, 100)  
f = np.sin(x) 
g = np.cos(x)  


plt.figure(figsize=(10,7))
plt.plot(x, f, linewidth=5, label='sin(x)')  
plt.plot(x, g, linewidth=5, label='cos(x)')  
plt.legend()


plt.xlim(0, 2 * np.pi)
plt.ylim(-1, 1)
plt.xticks([0, 2, 4, 6])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de sin(x) e cos(x)')
plt.grid(True)


plt.savefig('Figura.pdf', format='pdf')


plt.show()
