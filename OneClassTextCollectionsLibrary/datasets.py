import pandas as pd
import os
from pathlib import Path

def load(path_files=''):

  '''
  this function download and load all datasets, and return a dictionary in which any key represent the dataset
  
  if the directory already exist, to load them, pass the path where the directory are through the path_files parameter
  
  this function changes the current directory, remember to go back to the directory you were in
  '''

  if path_files != '':
    os.chdir(path_files)

  if not Path('News.zip').is_file():
    os.system('gdown --id 1-20ozBt8NjnN1X_F_HkXVMlDl67CUYNW')
    os.system('unzip News.zip') 

  
  basepath = Path('./News/')
  files_in_basepath = basepath.iterdir()
  datasets = {}
  for item in files_in_basepath:
    if item.is_file():
      df = pd.read_pickle('./News/' + item.name)
      datasets[item.name.replace('.plk','')] = df

  return datasets
