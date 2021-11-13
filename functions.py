"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """


from formula import *

Binary_Elements = {And, Or , Implies}

def length(formula : Formula):
    """Determines the length of a formula in propositional logic."""
    if type(formula) == Atom:
        return 1
    if type(formula) == Not:
        return length(formula.inner) + 1
    if type(formula) in Binary_Elements:
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula : Formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """

    if type(formula) == Atom:
        return {formula}
    if type(formula) == Not:
        return {formula}.union(subformulas(formula.inner))
    if type(formula) in Binary_Elements:
        return {formula}.union(subformulas(formula.left)).union(subformulas(formula.right))

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).


def atoms(formula : Formula):
    """Returns the set of all atoms occurring in a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for atom in atoms(my_formula):
        print(atom)

    This piece of code above prints: p, s
    (Note that there is no repetition of p)
    """
    if type(formula) == Atom:
        return {formula}
    if type(formula) == Not:
        return atoms(formula.inner)
    if type(formula) in Binary_Elements:
        return atoms(formula.left).union(atoms(formula.right))    

def number_of_atoms(formula: Formula):
    """Returns the number of atoms occurring in a formula.
    For instance,
    number_of_atoms(Implies(Atom('q'), And(Atom('p'), Atom('q'))))

    must return 3 (Observe that this function counts the repetitions of atoms)
    """

    if type(formula) == Atom:
        return 1
    if type(formula) == Not:
        return number_of_atoms(formula.inner)
    if type(formula) in Binary_Elements:
        return number_of_atoms(formula.left) + number_of_atoms(formula.right)

def number_of_connectives(formula : Formula):
    """Returns the number of connectives occurring in a formula."""
    if type(formula) == Atom:
        return 0
    if type(formula) == Not:
        return number_of_connectives(formula.inner)
    if type(formula) in Binary_Elements:
        return (number_of_connectives(formula.left) + number_of_connectives(formula.right)) + 1 


def rank(formula : Formula):
    """Returns the number of connectives occurring in a formula."""
    if type(formula) == Atom:
        return 0
    if type(formula) == Not:
        return rank(formula.inner) + 1
    if type(formula) in Binary_Elements:
        return max([rank(formula.left), rank(formula.right)]) + 1
         

def is_literal(formula):
    """Returns True if formula is a literal. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def substitution(formula, old_subformula, new_subformula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_clause(formula):
    """Returns True if formula is a clause. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_negation_normal_form(formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_cnf(formula):
    """Returns True if formula is in conjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_term(formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_dnf(formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_decomposable_negation_normal_form(formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
