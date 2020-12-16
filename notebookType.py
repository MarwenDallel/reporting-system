from enum import Enum


class NotebookType(Enum):
    PYTHON_CODE, ML_CODE, EMPTY = range(3)
