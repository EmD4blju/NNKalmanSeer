from _system import log_config
from _data import data_analyzer, data_manager
import pathlib as pl

def main():
    logger = log_config.setup_logger(__name__)
    logger.info('Neural network aided with Kalman filter')
    dm = data_manager.Data_Manager()
    fetched_data = dm.fetch_data(stock_symbol='SMSN.IL', period='1y')
    dm.save_to_csv(dataset=fetched_data, path=pl.Path('_data', '_saved'), out_name='smsn_dataset.csv')
    logger.info(f'Fetched data type: {type(fetched_data)}')
    da = data_analyzer.Data_Analyzer(dataset=fetched_data)
    da.visualize()
    
    
if __name__ == "__main__":
    main()
