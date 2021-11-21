"""You can test your functions in this module as in the following code: """


from re import T
from formula import *
from functions import *
from semantics import sat, satisfiability_brute_force, truth_value


formula1 = Atom('p')  # p
formula2 = Atom('q')  # q
formula3 = And(formula1, formula2)  # (p /\ q)
formula4 = And(Atom('p'), Atom('s'))  # (p /\ s)
formula5 = Not(And(Atom('p'), Atom('s')))  # (¬(p /\ s))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)
formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Atom('r')))  # ((¬(p /\ s)) -> (q /\ r))
formula8 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Not(And(Atom('p'), Atom('s')))))
# ((¬(p /\ s)) -> (q /\ (¬(p /\ s))))


print(formula1 == formula3)
print(formula1 == formula2)
print(formula3 == And(Atom('p'), Atom('q')))

print('formula1:', formula1)
print('formula2:', formula2)
print('formula3:', formula3)
print('formula4:', formula4)
print('formula5:', formula5)
print('formula6:', formula6)
print('formula7:', formula7)
print('formula8:', formula8)

print('length of formula1:', length(formula1))
print('length of formula3:', length(formula3))

print('length of formula7:', length(formula7))

print('subformulas of formula7:')
print(subformulas(formula7))
for subformula in subformulas(formula7):
    print(subformula)

print('length of formula8:', length(formula8))
print('subformulas of formula8:')


print("---------------------")
formula7 = Implies(Not(And(Atom('w'), Atom('s'))), And(Atom('w'), Atom('8')))


formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)

print(formula6)
print(length(formula6))
print("+-----------------------------+")
for i in subformulas(formula6):
    print(i)


print("++++++++++++++++++")

print(len(subformulas(formula6)) == (2* number_of_connectives(formula6)) + 1)


print(formula7)
print(rank(formula7))
print(number_of_connectives(formula7))

# print(len(subformulas(formula5)))

# print((2* number_of_connectives(formula5)) + 1)

p = Atom("p")

q = Atom("q")

t = Atom("t")

print("---------------------------------------------")
formula3 = And(Not(p),q)
print(formula3)

print(truth_value(formula3, {'p': False, 'q' : True}))

print(satisfiability_brute_force(formula3))





#  we have shown in class that for all formula A, len(subformulas(A)) <= length(A):
# for example, for formula8:
# print('number of subformulas of formula8:', len(subformulas(formula8)))
# print('len(subformulas(formula8)) <= length(formula8):', len(subformulas(formula8)) <= length(formula8))
