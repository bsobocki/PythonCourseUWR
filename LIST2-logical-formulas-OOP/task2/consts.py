import abc
import abstract as abst

class T(abst.Constant):

    def __init__(self):
        super().__init__("T", True)

class F(abst.Constant):

    def __init__(self):
        super().__init__("F", False)
