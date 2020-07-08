import os
import glob
from typing import TypedDict  # type: ignore
from typing import Callable, Optional  # type: ignore


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
        integration_test = os.environ.get('INTEGRATION_TEST', default=None)
    except KeyError:
        raise KeyError("Please verify that the needed env variables are set")
    return {"db_ip_address": db_ip_address,
            "postgres_db": postgres_db,
            "postgres_user": postgres_user,
            "postgres_password": postgres_password,
            "intergration_test": integration_test}
