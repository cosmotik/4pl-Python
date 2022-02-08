from human import Human

class student(Human):
    """ Initialize student class and extend Human class """

    def __init__(self, name, surname, age, grade):
        super().__init__(name, surname, age)
        self.grade = grade

    def get_student_info(self):
        """ Show all student info """
        self.get_human_info()
        print(f"Grade: \t\t{self.grade}")