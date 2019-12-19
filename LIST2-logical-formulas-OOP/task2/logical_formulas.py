import abc
import abstract as abst

#   => or <= (able to reverse)
class Implication(abst.Formula):

    def __init__(self, arg1, arg2):
        super().__init__("=>", arg1, arg2)

    def calc(self, vars):
        bool1 = self.arg1.calc(vars)
        bool2 = self.arg2.calc(vars)
        return (True, False)[bool1 and not bool2]
        #return False if bool1 == True and bool2 == False else True

    def invert(self):
        temp = self.arg1
        self.arg1 = self.arg2
        self.arg2 = temp

#   <=>
class Equivalence(abst.Formula):
    
    def __init__(self, arg1, arg2):
        super().__init__("<=>", arg1, arg2)

    def calc(self, vars):
        return self.arg1.calc(vars) == self.arg2.calc(vars)

class And(abst.Formula):
    
    def __init__(self, arg1, arg2):
        super().__init__("/\\", arg1, arg2)

    def calc(self, vars):
        return self.arg1.calc(vars) and self.arg2.calc(vars)

class Or(abst.Formula):
    
    def __init__(self, arg1, arg2):
        super().__init__("\\/", arg1, arg2)

    def calc(self, vars):
        return self.arg1.calc(vars) or self.arg2.calc(vars)

class Negation(abst.LogicalOperator):
    
    def __init__(self, arg1):
        super().__init__("~" ,arg1)
    
    def calc(self, vars):
        return self.arg1.calc(vars)