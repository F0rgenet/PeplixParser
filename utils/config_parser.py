import xml.etree.ElementTree as XMLTree
from loguru import Logger
import os

logger = Logger()


class ConfigParser(object):
    def __init__(self, path: str):
        self.path = path

    def check_file(self):
        if not os.path.isfile(self.path):
            logger.warning(f"Файл конфига '{self.path}' не существует")
            return False
        return True

    def write_base_config(self):
        #x
        XMLTree.

    def create_file(self):
        with open(self.path, "w") as file:
            self.write_base_config()
