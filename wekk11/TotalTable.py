import pandas as pd
class TotalTable():
    @staticmethod
    def merge_metrics_with_regions(metrics_df: pd.DataFrame,regions_df: pd.DataFrame,on: str = "region_id") -> pd.DataFrame:
        result = pd.merge(metrics_df.copy(),regions_df.copy(),how="left",on=on)
        return result
