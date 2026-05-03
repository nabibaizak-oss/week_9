import pandas as pd
import matplotlib.pyplot as plt
class Graff:
    def __init__(self,file1):
        self.file1 = file1
        df = pd.read_csv(self.file1)
        self.df = df
    def bar(self):
        plt.figure(figsize = (6,4))
        plt.barh(self.df["region_id"], self.df["score"])
        plt.title("Top 5 Regions")
        plt.xlabel("Score")
        plt.ylabel("Region")
        plt.savefig("top5plot.png")
        plt.show()
start = Graff(r"..\week12\top5.csv")
start.bar()
start.bar()
