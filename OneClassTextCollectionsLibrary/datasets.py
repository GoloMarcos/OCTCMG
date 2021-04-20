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

  if not Path('One-Class-News.zip').is_file():
    os.system('gdown --id 19tNpMB_U1GJLXpU1Bo0TL2moQlwUXwAF')
    os.system('unzip One-Class-News.zip') 

  
  basepath = Path('./News/')
  files_in_basepath = basepath.iterdir()
  bases = {}
  for item in files_in_basepath:
    if item.is_file():
      df = pd.read_csv('./News/' + item.name)
      df = df.drop(columns=['Unnamed: 0'])
      bases[item.name.replace('.csv','')] = df

  return bases
