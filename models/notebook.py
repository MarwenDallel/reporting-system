from notebookType import NotebookType


class Notebook:
    def __init__(self, notebook_type: NotebookType):
        self._notebook_type = notebook_type

    @property
    def notebook_type(self) -> NotebookType:
        return self._notebook_type

    @notebook_type.setter
    def notebook_type(self, notebook_type: NotebookType):
        self._notebook_type = notebook_type
