import pandas as pd
import numpy as np

class ReadData:
    data = []
    path = ""

    def __init__(self, path):
        self.path = path
    
    def readDataExcel(self):
        df = pd.read_excel(self.path)
        self.data = df.values.tolist()
        self.data = np.array(self.data)
        return self.data


data = ReadData("dataset/dataset_kmeans.xlsx")
data.readDataExcel()
print(data.data)