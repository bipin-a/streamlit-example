import numpy as np
import pandas as pd
import plotly.express as px

def load_data(file_name, **kwargs):
   df = pd.read_csv(file_name, **kwargs)
   return df

def process_dataset(df):
   return df.groupby(['DIVISION','MARKET_INDUSTRY','UNIQUE_MARKET_ID','PRODUCT_CATEGORY','PRODUCT_ID']).agg(
      total_sold = ('QUANTITY_SOLD',np.sum),
      total_rev = ('PRODUCT_SALES_AMOUNT',np.sum),
      ).sort_values(['UNIQUE_MARKET_ID','total_rev','total_sold']).reset_index()
   
def get_stats(df_, index_cols, agg_col):
  df = df_.copy()
  agg_df = df.groupby(index_cols).agg(
      total = (agg_col, np.sum),
      avg = (agg_col ,np.mean),
      median = (agg_col ,np.median),
      std = (agg_col ,np.std),
  )
  return agg_df

def run_report(df):
   '''
    - Average Sales per Market
    - Total Sales per Market
    - Variance of Sales per Market
    - Number of unique products per Market
    - Best Market
    - Diversity
    - Distribution of Sales
    - Worst Market
    - Which Product Categories do well in which markets
    - Which Market Industy does well with which product categories
    - Distribution of DayPart per Market_ID and Market Industry

   '''
   print(df.info())
   
   sales_per_market = get_stats(df, ['UNIQUE_MARKET_ID'], 'total_rev')
   sales_per_market = sales_per_market.melt()
   print(sales_per_market.info())
