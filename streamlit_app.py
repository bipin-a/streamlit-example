import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st
import logging
st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
logger = logging.getLogger(__name__)

"""
# Products and Markets
"""

def load_data(file_name):
   df = pd.read_csv(file_name)
   return df


def get_stats(df_, index_cols, agg_col):
  df = df_.copy()
  agg_df = df.groupby(index_cols).agg(
      total = (agg_col, np.sum),
      avg = (agg_col ,np.mean),
      median = (agg_col ,np.median),
      std = (agg_col ,np.std),
  )
  return agg_df


def run_report():
   
   data = get_stats()
   sales_per_market = get_stats(data, ['UNIQUE_MARKET_ID'], 'PRODUCT_SALES_AMOUNT')
   sales_per_market = sales_per_market.melt()
   g = sns.FacetGrid(sales_per_market, col="variable", height=3.5, aspect=.65, sharex=False, sharey=False)
   g.map(sns.histplot, "value")
   st.pyplot(g.fig)




def main():
    df = load_data('dataset_encoded.csv')

if __name__ == '__main__':


    logger.info('hi')

    print('hi')
    
    main()
