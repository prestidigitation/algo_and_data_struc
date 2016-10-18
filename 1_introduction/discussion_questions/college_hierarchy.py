class CollegePerson:

    employed_by_school = False

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Staff(CollegePerson):

    employed_by_school = True


class Faculty(CollegePerson):

    employed_by_school = True

    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

    def get_specialty(self):
        return self.specialty

    def set_specialty(self, specialty):
        self.specialty = specialty

    def lecture(self):
        print("Today I am droning on about %s." % self.specialty)


class Student(CollegePerson):

    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
