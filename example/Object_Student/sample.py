from datetime import datetime

class Student:
    def __init__(self, name, fam, dr):
        self.name = name
        self.fam = fam
        self.dr = dr
        self.mark = 0

    def get_age(self):
        return (datetime.now() - self.dr).days//365

    def get_mark(self):
        return self.mark

    def add_mark(self, mark):
        self.mark += mark

