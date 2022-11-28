import os
import numpy as np
import pandas as pd

def load_distribution(folder):
    """
    loads values scattered across multiple .parquet files in a single directory, to produce a unique
    array of values as output.
    """

    params=[]
    file_list=[]
    for root, _, files in os.walk(folder):
        for name in files:
            a=os.path.join(root, name)
            if 'parquet' in a:
                file_list.append(a)
            if '.dat' in a:
                params.append(a)


    territory = np.zeros(1)
    for output in file_list:
        a=pd.read_parquet(output).values
        territory=np.concatenate((territory,a[:,0]))


    territory=territory[1:] 
    
    try:
        params=params[0]
        with open(params) as file :
            l=file.readlines()
        parameters = {ls.split('=')[0].strip() :ls.split('=')[1].strip() for ls in l}    
#        print(parameters)
    except:
        parameters={}
    #print(parameters)
    return territory,parameters
    
def load_2d_values(folder):
    """
    loads values of the form [x0s, f(x0s)],scattered across multiple .parquet files in a single directory, to produce a unique
    array of values as outputof the form [x0s, mean(f(x0s))]
    """

    params=[]
    file_list=[]
    for root, _, files in os.walk(folder):
        for name in files:
            a=os.path.join(root, name)
            if 'parquet' in a:
                file_list.append(a)
            if '.dat' in a:
                params.append(a)

    # load the first info
    first_file=file_list[0]
    pos=(pd.read_parquet(first_file).values)[:,0]

    values=np.zeros(len(pos))
    # average the second info
    for output in file_list:
        a=pd.read_parquet(output).values
        values+=a[:,1]

    values/=len(file_list)
    
    try:
        params=params[0]
        with open(params) as file :
            l=file.readlines()
        parameters = {ls.split('=')[0].strip() :ls.split('=')[1].strip() for ls in l}    
#        print(parameters)
    except:
        parameters={}
    #print(parameters)
    return np.array([pos,values]),parameters
