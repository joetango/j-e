class studyGroup:

    def __init__(self):
        self.members = {}

    def add(self, name, number):
        self.members[name] = number
    
    def get_roster(self):
        return list(self.members.keys())
    

group = studyGroup()

group.add("Evvyg", 27)
group.add("JOerizzy", 17)

roster = group.get_roster()

print(roster)