import numpy as np
import matplotlib.pyplot as plt

a,b = 0.1, 0.5

# Fonction qui définit le champ de vecteurs
def field(x, y):
    # Exemple de champ de vecteurs
    fx = -x+a*y+x**2 *y
    fy = b -a*x -x**2 *y
    return fx, fy

# Fonction pour calculer la trajectoire
def calculate_trajectory(start_x, start_y, num_steps, step_size):
    trajectory_x = [start_x]
    trajectory_y = [start_y]
    x = start_x
    y = start_y

    for _ in range(num_steps):
        fx, fy = field(x, y)
        x += fx * step_size
        y += fy * step_size
        trajectory_x.append(x)
        trajectory_y.append(y)

    return trajectory_x, trajectory_y

# Paramètres de la grille
x_min, x_max = 0, 2  # Plage des valeurs x
y_min, y_max = 0, 3  # Plage des valeurs y
grid_density = 20  # Densité de la grille

# Paramètres de simulation
start_x = 0.5  # Coordonnée x initiale
start_y = 1.2  # Coordonnée y initiale
num_steps = 1000  # Nombre d'étapes de simulation
step_size = 0.1  # Taille de chaque pas

# Création de la grille
x_vals = np.linspace(x_min, x_max, grid_density)
y_vals = np.linspace(y_min, y_max, grid_density)
X, Y = np.meshgrid(x_vals, y_vals)

# Calcul du champ de vecteurs pour chaque point de la grille
U, V = field(X, Y)

# Calcul de l'intensité du champ de vecteurs
intensity = np.sqrt(U ** 2 + V ** 2)

# Normalisation de l'intensité pour une meilleure représentation des couleurs
normalized_intensity = (intensity - intensity.min()) / (intensity.max() - intensity.min())

# Affichage du champ de vecteurs avec des couleurs
plt.streamplot(X, Y, U, V, color=normalized_intensity, cmap='coolwarm')
plt.colorbar(label='Intensité du champ')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Champ de vecteurs avec intensité')
plt.grid(True)

# Calcul de la trajectoire
trajectory_x, trajectory_y = calculate_trajectory(start_x, start_y, num_steps, step_size)

# Affichage de la trajectoire
plt.plot(trajectory_x, trajectory_y, 'r')
plt.show()
