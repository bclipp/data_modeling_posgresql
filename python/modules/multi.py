import os
import modules.log_data as log_data
import modules.utils as utils
import modules.song_data as song_data
import pandas as pd
import logging  # type: ignore
import multiprocessing as mp  # type: ignore
from typing import Callable, Optional  # type: ignore


def process_files(config:dict, parallel: bool = True):

    file_types = ["../data/song_data", "../data/log_data"]
    files = utils.get_files(file_types[0])
    if parallel():
        concurrent_me(os.cpu_count(), log_data.process_log_data, files) # add config data
    else:
        for file in files:
            log_data.process_log_data(file, config)
    files = utils.get_files(file_types[1])
    if parallel():
        concurrent_me(os.cpu_count(), song_data.process_song_data, files)  # add config data
    else:
        for file in files:
            song_data.process_song_data(file, config)


def concurrent_me(size: Optional[int], func: Callable, data: list) -> list:
    logging.info('concurrently running a function')
    pool = mp.Pool(size)
    updated_data: list = pool.map(func, data)
    pool.close()
    pool.join()
    return updated_data
