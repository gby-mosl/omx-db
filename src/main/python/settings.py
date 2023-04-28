import json
import logging
from pathlib import Path

import mysql.connector

# CONSTANTS
MYSQL_ERRORS = (mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.DataError
                )
class Configuration:
    def __init__(self):
        self.settings_file = Path(__file__).parent.parent / "settings" / "settings.json"
        self.log_file = Path(__file__).parent.parent / "error.log"

        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(filename)s (%(funcName)s) -- %(message)s',
                            filename=self.log_file,
                            filemode="a",
                            level=logging.DEBUG)

    def getSettings(self, params: str) -> dict:
        try:
            with open(self.settings_file, "r") as f:
                settings = json.load(f)
                return settings[params]
        except KeyError as e:
            logging.error(f"{type(e)}: Parameter {e} does not exist.")
        except FileNotFoundError as e:
            logging.error(f"{type(e)}: {e}")
            return None
