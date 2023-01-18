import os
import numpy as np
import pandas as pd

def dump_data(foldername, simulation_data, data):
    """
    Saves data (a dataframe format) as parquet files.

    """
    path = f'../simulations/{foldername}'
    output_path = f'{path}/f_output.parquet'
    input_path = f'{path}/f_input.dat'
    #create save folder
    os.makedirs(path, exist_ok=True)
    file = open(input_path, 'w')
    for key, value in simulation_data.items():
        file.write(f'{key} = {value} ')
    file.close()
    data.to_parquet(output_path, copression='gzip',index=False )
