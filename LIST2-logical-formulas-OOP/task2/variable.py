import abstract as abst

class Variable(abst.Calculable):

    def __init__(self, name):
        self.name = name

    def calc(self, vars):
        return vars[self.name]

    def __str__(self):
        return self.name