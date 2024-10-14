from math import sqrt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

min_number_of_clusters = 2
max_number_of_clusters = 10

def get_inertias(df_rfm):
    inertias = []

    for i in range(min_number_of_clusters, max_number_of_clusters + 1):
        kmeans = KMeans(n_clusters=i, random_state=42, max_iter=500)
        kmeans.fit(df_rfm[df_rfm.columns[1:]])
        inertias.append(kmeans.inertia_)

    return inertias

def plot_elbow_method(inertias):
    plt.plot(range(min_number_of_clusters, max_number_of_clusters + 1), inertias, marker='o')
    plt.title('Método do Cotovelo')
    plt.xlabel('Número de segmentações')
    plt.ylabel('Inércia')
    plt.show()


def get_optimal_number_of_clusters(inertias):
    x1, y1 = min_number_of_clusters, inertias[0]
    x2, y2 = max_number_of_clusters, inertias[-1]
    
    distances = []
    
    for i in range(len(inertias)):
        x0 = i+2
        y0 = inertias[i]

        numerator = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
        denominator = sqrt((y2 - y1)**2 + (x2 - x1)**2)
        distances.append(numerator/denominator)
        
    return distances.index(max(distances)) + 2