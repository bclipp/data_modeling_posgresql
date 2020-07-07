import os
import glob
from typing import TypedDict  # type: ignore
from typing import Callable, Optional  # type: ignore
import pandas as pd
from modules import log_data, song_data, multi


def iterate_paths(file_paths: list):
    for path in file_paths:
        if path.find("log"):
            process_files(config,
                          True,
                          log_data.process_log_data(),
                          path["location"])
        else:
            process_files(config,
                          True,
                          song_data.process_song_data(),
                          path["location"])


def process_files(config: dict, function: Callable, file_path, parallel: bool = True):
    files = get_files(file_path)
    data_frame: pd.DataFrame = pd.DataFrame({"location": files})
    data_frame: pd.DataFrame = data_frame.append(config, ignore_index=True)
    files: list = data_frame.to_dict()
    if parallel():
        multi.concurrent_me(os.cpu_count(), function, files)
    else:
        for file in files:
            function(file, config)


def get_files(file_path):
    all_files = []
    for root, _, files in os.walk(file_path):
        files = glob.glob(os.path.join(root, '*.json'))
        for file in files:
            all_files.append(os.path.abspath(file))
    return all_files


class ConfigVars(TypedDict):
    db_ip_address: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    intergration_test: Optional[str]


def get_variables() -> ConfigVars:
    try:
        db_ip_address = os.environ['DB_IP_ADDRESS']
        postgres_db = os.environ['POSTGRES_DB']
        postgres_user = os.environ['POSTGRES_USER']
        postgres_password = os.environ['POSTGRES_PASSWORD']
        intergration_test = os.environ.get('INTERGRATION_TEST', default=None)
    except KeyError:
        raise KeyError("Please verify that the needed env variables are set")
    return {"db_ip_address": db_ip_address,
            "postgres_db": postgres_db,
            "postgres_user": postgres_user,
            "postgres_password": postgres_password,
            "intergration_test": intergration_test}
