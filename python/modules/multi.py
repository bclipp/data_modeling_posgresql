import os
import modules.log_data as log_data
import modules.utils as utils
import modules.song_data as song_data
import pandas as pd
import logging  # type: ignore
import multiprocessing as mp  # type: ignore
from typing import Callable, Optional  # type: ignore



def concurrent_me(size: Optional[int], func: Callable, data: list) -> list:
    logging.info('concurrently running a function')
    pool = mp.Pool(size)
    updated_data: list = pool.map(func, data)
    pool.close()
    pool.join()
    return updated_data
