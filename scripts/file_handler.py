import pandas as pd
from app_logger import App_Logger

class FileHandler():

    def __init__(self):
        self.logger = App_Logger().get_logger(__name__)
        

    def to_csv(self, df, csv_path, index=False):
        try:
            df.to_csv(csv_path, index=index)
            self.logger.info(f'Csv file saved in {csv_path}.')

        except Exception:
            self.logger.exception('File saving failed.')

    def read_csv(self, csv_path, missing_values=["n/a", "na", "undefined"]):
        try:
            df = pd.read_csv(csv_path, na_values=missing_values)
            self.logger.info(f'Csv file read from {csv_path}.')
            return df

        except FileNotFoundError:
            self.logger.exception('File not found.')
  