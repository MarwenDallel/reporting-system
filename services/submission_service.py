from models import Notebook, Feedback


class SubmissionService:
    def __init__(self, notebook: Notebook, feedback: Feedback) -> None:
        self._notebook = notebook
        self._feedback = feedback