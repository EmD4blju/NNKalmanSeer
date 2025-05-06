import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Data_Analyzer():
    def __init__(self, dataset:pd.DataFrame):
        self.set_dataset(dataset=dataset)
    
    def set_dataset(self, dataset:pd.DataFrame) -> None:
        self.dataset = dataset
    
    def visualize(self) -> None:
        sns.lineplot(x='Date', y='Close', data=self.dataset)
        plt.show()
    