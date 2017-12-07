class ModuleElement(object):

    def __init__(self, module):
        self.module = module

    def add_important_date(self, kind, date):
        self.module.dates.append((kind, date))

################################################################################

class Lesson(ModuleElement):

    def __init__(self, module):
        ModuleElement.__init__(self,module)


    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Lesson", date)

################################################################################

class Lab(ModuleElement):

    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Lab Session", date)

################################################################################

class Midterm(ModuleElement):

    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Midterm", date)

################################################################################

class FinalExam(ModuleElement):

    def __init__(self, module):
        ModuleElement.__init__(self, module)


    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Final Exam", date)
