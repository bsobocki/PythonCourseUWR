import itertools as it
import logical_formulas as lf
import consts as c
import variable as v

def isTautology(formula):
    evals = {} 
    vars = []
    getVars(formula, vars)
    perm = list(it.product([True, False], repeat=len(vars)))
    for p in perm:
        i = 0
        e = list(p)
        for name in vars:
            evals[name] = e[i]
            i+=1
        if formula.calc(evals) == False:
            return False
    return True

def getVars(formula, list):
    if type(formula) == v.Variable:
        if formula.name not in list:
            list.append(formula.name)
    if hasattr(formula, 'arg1'):
        getVars(formula.arg1, list)
    if hasattr(formula, 'arg2'):
        getVars(formula.arg2, list)

def printFormula(formula, vars):
    print(formula, ' = ', formula.calc(vars))
    
t = c.T()
f = c.F()
p = v.Variable("p")
q = v.Variable('q')
r = v.Variable('r')

varss = {"p":True, "q":False}

formula1 = lf.And(t, p) # p /\ T 
formula2 = lf.Implication(p ,q) # p => q
formula3 = lf.Equivalence(lf.Implication(p,q), lf.And(p,q)) #  (q => p) <=> (q /\ p)

print('formula 1 :',end='\t')
printFormula(formula1, varss)

printFormula(lf.And(p,q),varss)

print('formula 2 :',end='\t')
printFormula(formula2,varss)
formula2.invert()
print('formula 2 (inverted) :',end='\t')
printFormula(formula2,varss)

printFormula(formula3,varss)

print(formula3, "   is tautology? ", isTautology(formula3))

# p \/ T  v  (~r /\ p) <=> ~(r \/ ~p) 
tautology = lf.Or(
    lf.Or(p, t),
    lf.Equivalence(
        lf.And(
            lf.Negation(r), 
            p), 
        lf.Negation(
            lf.Or(
                r,
                lf.Negation(p)
            ))))
print(tautology, "   is tautology? ", isTautology(tautology))