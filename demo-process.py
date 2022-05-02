from functools import partial
import pandas as pd
import numpy as np

import itertools
from multiprocessing.pool import ThreadPool


class ProcessDemo:

    def create_main_columns(self, columns_length):
        length = [f"column{i}" for i in range(columns_length)]
        return length

    def json_dummy_data(self, range_data, columns):
        json_values_data_dummy = np.random.uniform(-100, 100, range_data).tolist()
        dataframe = pd.DataFrame({columns: json_values_data_dummy})
        return dataframe
        

    def process_data_thread(self, thread_data_length, thread_columns_length):
        columns = self.create_main_columns(thread_columns_length)
        with ThreadPool(len(columns)) as processing_pool:
            partials = partial(self.json_dummy_data, thread_data_length)
            result_list = processing_pool.map(partials, columns)
            dataframe = pd.concat(result_list, ignore_index=True, axis=0)

        return dataframe



    def process_data_thread_sample_demo(self, thread_data_length, thread_columns_length):
        columns = self.create_main_columns(thread_columns_length)
        with ThreadPool(len(columns)) as processing_pool:
            partials = partial(self.analytic_sample_demo_process, thread_data_length, thread_columns_length)
            result_list = processing_pool.map(partials, columns)
        return result_list

process = ProcessDemo()

data_length = 3
columns_length = 5
if __name__ == "__main__":
    print((process.process_data_thread(data_length, columns_length)))

