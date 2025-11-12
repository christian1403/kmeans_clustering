import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from readData import ReadData
from sklearn.cluster import KMeans

class kmeans:
    data = []
    kmeans_model = None
    labels = None
    centroids = None

    def __init__(self, data):
        self.data = data
    
    def read_dataset(self, data):
        self.data = data
    
    def plot_dataset(self):
        sns.scatterplot(x=self.data[:,0], y=self.data[:,1])
        plt.title("scatter plotting dataset")
        plt.savefig("result/scatter_plotting_dataset.png")
        plt.show()

    def run_kmeans(self, n_clusters=3, random_state=42):
        self.kmeans_model = KMeans(n_clusters=n_clusters, random_state=random_state)
        self.labels = self.kmeans_model.fit_predict(self.data)
        self.centroids = self.kmeans_model.cluster_centers_

        print("K-Means berhasil dijalankan!")
        print("Jumlah Cluster:", n_clusters)
        print("Centroids:")
        print(self.centroids)
    
    def plot_clusters(self):
        sns.scatterplot(x=self.data[:,0], y=self.data[:,1], hue=self.labels, palette="tab10")
        plt.scatter(self.centroids[:,0], self.centroids[:,1], c='red', label='Centroid', marker='X', s=200)
        plt.title("Hasil Clustering dengan K-Means (sklearn)")
        plt.legend()
        plt.savefig("result/hasil_clustering_kmeans.png")
        plt.show()

objData = ReadData("dataset/dataset_kmeans.xlsx")
dataset = objData.readDataExcel()


objkmeans = kmeans(dataset)
objkmeans.read_dataset(dataset)
objkmeans.run_kmeans()
objkmeans.plot_dataset()
objkmeans.plot_clusters()