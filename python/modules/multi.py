import logging  # type: ignore
import multiprocessing as mp  # type: ignore
from typing import Callable, Optional  # type: ignore


def concurrent_me(size: Optional[int],
                  func: Callable,
                  data: list,
                  output: bool = True) -> Optional[list]:
    logging.info('concurrently running a function')
    pool = mp.Pool(size)
    updated_data: list = pool.map(func, data)
    pool.close()
    if output:
        pool.join()
        return updated_data
