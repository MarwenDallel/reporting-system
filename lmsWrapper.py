class lmsWrapper:
    def __init__(self, submission_service):
        self.lms = None
        self.submission = submission_service

    def convert_csv_to_obj(self, csv_file):
        submission.setFeedback