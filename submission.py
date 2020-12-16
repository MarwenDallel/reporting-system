from models import Notebook
from models import Feedback


class Submission:
    def __init__(self, notebook: Notebook, feedback: Feedback) -> None:
        self._notebook = notebook
        self._feedback = feedback

    @property
    def notebook(self) -> Notebook:
        return self._notebook

    @notebook.setter
    def notebook(self, notebook: Notebook):
        self._notebook = notebook

    @property
    def feedback(self) -> Feedback:
        return self._feedback

    @feedback.setter
    def feedback(self, feedback: Feedback):
        self._feedback = feedback





