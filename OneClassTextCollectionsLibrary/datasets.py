import pandas as pd
from os.path import isdir, isfile
from path import Path

def load(path_files='', only_download = False, dataset = 'All'):

  '''
  this function download and load all datasets, and return a dictionary in which any key represent the dataset
  
  if the directory already exist, to load them, pass the path where the directory are through the path_files parameter
  
  '''
  print('aqqqq')
  if not is_dir(path_files + 'News/'):
    print('oioi')
    if not isfile(path_files + 'News.zip'):
      cmd = 'wget -P ' + path_files +  ' https://zenodo.org/record/5048322/files/News.zip'
      os.system(cmd)
      
    cmd2 = 'unzip ' + path_files + 'News.zip'
    os.system(cmd2)
    
  if not only_download:
    if dataset == 'All':
      basepath = Path(path_files + 'News/')
      files_in_basepath = basepath.iterdir()
      datasets = {}
      for item in files_in_basepath:
        if item.is_file():
          df = pd.read_pickle(path_files + 'News/' + item.name)
          datasets[item.name.replace('.plk','')] = df
    
    else:
      datasets = {}
      datasets[dataset] = pd.read_pickle(path_files + 'News/' + dataset + '.plk')

    return datasets
