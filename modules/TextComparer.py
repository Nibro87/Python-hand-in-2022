import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

from time import time as timer
import matplotlib.pyplot as plt
import numpy as np

class TextComparer():
    
    
       def __init__(self, url_list):
            self.url_list = url_list
    


       def download(self, url, filename):
        response = requests.get(url, allow_redirects=True).json()
        try:
             response.raise_for_status()
        except requests.exceptions.HTTPError as e:
             print (e)
        with open(filename,"w") as f:
             f.write(response.text)  

       
       def multi_download(self):
        start = timer()
        results = ThreadPoolExecutor(8).map(self.download, self.url_list)

        for path in results:
             print(path)

             print(f"Elapsed Time: {timer() - start}")

                