import abc

"""an interface with function 'calc'"""
class Calculable:
    
    @abc.abstractmethod
    def calc(self, vars):
        """calculate expression value"""

class LogicalOperator(Calculable):

    def __init__(self, operator, arg1):  
        self.operator = operator
        self.arg1 = arg1

    def __str__(self):
        return self.operator + '( ' + self.arg1.__str__() + ' )'

"""an abstract class defining formulas"""
class Formula(LogicalOperator):

    def __init__(self, operator, arg1, arg2):        
        super().__init__(operator, arg1)
        self.arg2 = arg2

    def __str__(self):
        return '( ' + self.arg1.__str__() + ' ' + self.operator + ' ' + self.arg2.__str__() + ' )'

"""an abstract class defining constants"""
class Constant(Calculable):
    
    def __init__(self, operator, value):
        self.value = value
        self.operator = operator

    def calc(self, vars):
        return self.value

    def __str__(self):
        return self.operator
