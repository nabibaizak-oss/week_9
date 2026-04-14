class DataMerger:
    def __init__(self, metrics: list, regions: list):
        self.metrics = metrics
        self.regions = regions
    def sort_data(self):
        self.metrics.sort(key=lambda x: x.region_id)
        self.regions.sort(key=lambda x: x.region_id)
    def merge(self):
        i, j = 0, 0
        result = []
        while i < len(self.metrics) and j < len(self.regions):
            m = self.metrics[i]
            r = self.regions[j]
            if m.region_id == r.region_id:
                result.append({
                    "region_id": m.region_id,
                    "name": r.name,
                    "score": m.score
                })
                i += 1
                j += 1
            elif m.region_id < r.region_id:
                i += 1
            else:
                j += 1
        return result


