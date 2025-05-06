import pathlib as pl
from _system import log_config
import yfinance as yf
import pandas as pd

class Data_Manager():
    def __init__(self):
        self.logger = log_config.setup_logger(__name__)
        self.logger.info(f'{self} created')
        
    def fetch_data(self, stock_symbol:str, period:str):
        ticker = yf.Ticker(ticker=stock_symbol)
        dataset = ticker.history(period=period)
        self.logger.info('Data fetched successfully')
        return dataset['Close'].reset_index()
    
    def save_to_csv(self, dataset:pd.DataFrame, path:pl.Path, out_name:str) -> None:
        dataset.to_csv(
            path_or_buf=pl.Path(path, out_name),
            sep=';'
        )
        
    def __str__(self):
        return f'Data_Loader[{id(self)}]'
    