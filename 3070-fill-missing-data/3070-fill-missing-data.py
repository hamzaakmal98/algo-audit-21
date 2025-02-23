import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
   products["quantity"] = products["quantity"].replace("null", 0).fillna(0)  
   return products