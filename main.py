import pandas as pd
from week10.Region import Region
from week10.Metric import Metric
from week10.DataMerger import DataMerger
from wekk11.TotalTable import TotalTable
from week12.Sort import Sort
#1zadanie
# def load_metrics(filename):
#     metrics = []
#     with open(filename) as f:
#         next(f)
#         for line in f:
#             region_id, score = line.strip().split(",")
#             metrics.append(Metric(int(region_id), float(score)))
#     return metrics
# def load_regions(filename):
#     regions = []
#     with open(filename) as f:
#         next(f)
#         for line in f:
#             region_id, name = line.strip().split(",")
#             regions.append(Region(int(region_id), name))
#     return regions
# if __name__ == "__main__":
#     metrics = load_metrics("week10/metrics.csv")
#     regions = load_regions("week10/regions.csv")
#     merger = DataMerger(metrics, regions)
#     merger.sort_data()
#     result = merger.merge()
#     for row in result:
#         print(row)
#2zadanie
# metrics_df = pd.read_csv("week10/metrics.csv")
# regions_df = pd.read_csv("week10/regions.csv")
# start = TotalTable
# print(start.merge_metrics_with_regions(metrics_df,regions_df))
#4ZADANIE
start = Sort("week9\metrics.csv")
start.srav()
start.writer()