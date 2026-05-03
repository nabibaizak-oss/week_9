import pandas as pd
class Sort:
    def __init__(self,file1):
        self.file1 = pd.read_csv(file1)
    def srav(self):
        self.data = self.file1.sort_values(by = "score", ascending = False).head(5)
    def writer(self):
        self.data.to_csv("top5.csv", index = False, encoding = "utf-8")

start = Sort("../wekk11/merged_results.csv")
start.srav()
start.writer()



