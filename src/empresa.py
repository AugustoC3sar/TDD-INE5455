import re
from typing import List

class Empresa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    