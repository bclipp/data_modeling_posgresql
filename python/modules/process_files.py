import os
from typing import Callable # type: ignore
import pandas as pd
from modules import log_data, song_data, multi, utils


def iterate_paths(file_paths: list,
                  config: dict):
    for path in file_paths:
        if path.find("log"):
            process_files(config,
                          True,
                          log_data.process_log_data(path),
                          path["location"])
        else:
            process_files(config,
                          True,
                          song_data.process_song_data(path),
                          path["location"])


def process_files(config: dict,
                  function: Callable,
                  file_path: str):
    par: bool = config["parallel"]
    files = utils.get_files(file_path)
    data_frame: pd.DataFrame = pd.DataFrame({"location": files})
    data_frame: pd.DataFrame = data_frame.append(config, ignore_index=True)
    files: list = data_frame.to_dict()
    if par:
        multi.concurrent_me(os.cpu_count(),
                            function,
                            files,
                            False)
    else:
        for file in files:
            function(file, config)
