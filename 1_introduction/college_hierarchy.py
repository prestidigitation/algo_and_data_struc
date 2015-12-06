class Staff:

    def __init__(self):
        self.employed_by_school = True


class Faculty(Staff):

    def __init__(self):
        Staff.__init__(self)

        self.specialty = input("Professor's specialty: ")

    def lecture(self):
        print("Today I am droning on about %s." % self.specialty)


class Student:
    
    def __init__(self):
        self.employed_by_school = False
