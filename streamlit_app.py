import streamlit as st
import logging
from utils import *

st.set_page_config(
        page_title="Products-Markets",
        page_icon="👋",
    )
logger = logging.getLogger(__name__)

st.header("Products and Markets")


def main():

    st.subheader("Raw Dataset")
    raw_data = load_data('data.csv')
    st.dataframe(raw_data.head())
    

    st.subheader("Processed Dataset")
    processed_dataset = process_dataset(raw_data)
    st.dataframe(processed_dataset.head())


    run_report(processed_dataset)

    # st.subheader("Encoded Dataset")
    # df = load_data('dataset_encoded.csv',index_col=0)
    # st.dataframe(df.head())


if __name__ == '__main__':
    logger.info('hi')    
    main()
