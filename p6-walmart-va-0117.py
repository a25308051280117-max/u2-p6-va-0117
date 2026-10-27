# Matias Lopez NC 0117
import matplotlib.pyplot as plt
import numpy as np

# Matias Lopez NC 0117

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos, precio)
plt.show()

# Personalizar grafica
plt.plot(cant_productos, precio, color="green", marker="o",
         linestyle="dashed", linewidth=2, markersize=12)
plt.title("ventas de walmart 0117")
plt.xlabel("cant prod")
plt.ylabel("precios")
plt.show()
