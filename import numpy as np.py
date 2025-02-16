# Datos de la viga
longitud = 5.0  # Longitud de la viga en metros
carga_distribuida = 10.0  # Carga distribuida en kN/m
momento = 20.0  # Momento aplicado en kNm

# Cálculo de las reacciones en los apoyos
reaccion_apoyo_izquierdo = carga_distribuida * longitud / 2
reaccion_apoyo_derecho = carga_distribuida * longitud / 2 + momento

# Cálculo de los momentos en la viga
x = np.linspace(0, longitud, 100)  # Puntos a lo largo de la viga
momento_viga = carga_distribuida * x / 2 - momento * (x - longitud) / longitud

# Visualización de los resultados
import matplotlib.pyplot as plt

plt.plot(x, momento_viga)
plt.xlabel('Distancia a lo largo de la viga (m)')
plt.ylabel('Momento en la viga (kNm)')
plt.title('Diseño de una viga')
plt.grid(True)
plt.show()