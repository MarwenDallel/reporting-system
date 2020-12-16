class Feedback:
    def __init__(self):
        self._student_name = ""
        self._satisfaction_rate = 0
        self._friends_recommendation = 0
        self._effort_level = 0
        self._slack_contribution = 0

    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, student_name):
        self._student_name = student_name

    @property
    def satisfaction_rate(self):
        return self._satisfaction_rate

    @satisfaction_rate.setter
    def satisfaction_rate(self, satisfaction_rate):
        self._satisfaction_rate = satisfaction_rate

    @property
    def friends_recommendation(self):
        return self._friends_recommendation

    @friends_recommendation.setter
    def friends_recommendation(self, friends_recommendation):
        self._friends_recommendation = friends_recommendation

    @property
    def effort_level(self):
        return self._effort_level

    @effort_level.setter
    def effort_level(self, effort_level):
        self._effort_level = effort_level

    @property
    def slack_contribution(self):
        return self._slack_contribution

    @slack_contribution.setter
    def slack_contribution(self, slack_contribution):
        self._slack_contribution = slack_contribution
