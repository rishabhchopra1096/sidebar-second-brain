```python
class ReviewProcess:
    def __init__(self):
        self.stakeholders = []
        self.users = []
        self.steering_committee = []

    def add_stakeholder(self, stakeholder):
        self.stakeholders.append(stakeholder)

    def add_user(self, user):
        self.users.append(user)

    def add_steering_committee_member(self, member):
        self.steering_committee.append(member)

    def get_feedback(self):
        for stakeholder in self.stakeholders:
            stakeholder.give_feedback()

        for user in self.users:
            user.give_feedback()

    def review_PRD(self):
        for member in self.steering_committee:
            member.review_PRD()

    def approve_PRD(self):
        for member in self.steering_committee:
            member.approve_PRD()

class Stakeholder:
    def __init__(self, name):
        self.name = name

    def give_feedback(self):
        print(f"{self.name} is giving feedback.")

class User:
    def __init__(self, name):
        self.name = name

    def give_feedback(self):
        print(f"{self.name} is giving feedback.")

class SteeringCommitteeMember:
    def __init__(self, name):
        self.name = name

    def review_PRD(self):
        print(f"{self.name} is reviewing the PRD.")

    def approve_PRD(self):
        print(f"{self.name} is approving the PRD.")
```