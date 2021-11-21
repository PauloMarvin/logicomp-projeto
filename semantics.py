"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from typing import Dict
from formula import *
from functions import atoms


def truth_value(formula: Formula, interpretation : Dict):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    if type(formula) == Atom:
        list_atoms = atoms(formula)
        for atomo in list_atoms:
            if interpretation[str(atomo.name)] == True:
                return True
            elif interpretation[str(atomo.name)] == False:
                return False
            else:
                return "interpretation of atom must be True or False"
        

    if type(formula) == Not:
        valoration = truth_value(formula.inner, interpretation)
        if valoration == True:
            return False
        elif valoration == False:
            return True
        else:
            return "interpretation of atoms must be True or False"

    if type(formula) == And:
        left_formula = truth_value(formula.left, interpretation)
        right_formula = truth_value(formula.right, interpretation)

        if type(left_formula) != bool or type(right_formula) != bool:
            return "interpretation of atoms must be True or False"
        if left_formula and right_formula:
            return True
        else:
            return False

    if type(formula) == Or:
        left_formula = truth_value(formula.left, interpretation)
        right_formula = truth_value(formula.right, interpretation)
        
        if type(left_formula) != bool or type(right_formula) != bool:
            return "interpretation of atoms must be True or False"
        if left_formula or right_formula:
            return True
        else:
            return False

    if type(formula) == Implies:
        left_formula = truth_value(formula.left, interpretation)
        right_formula = truth_value(formula.right, interpretation)
        
        if type(left_formula) != bool or type(right_formula) != bool:
            return "interpretation of atoms must be True or False"
        if left_formula == True and right_formula == False:
            return False
        else:
            return True
        
        



def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def sat(formula: Formula, atoms: set, intepretation: dict):
    
    if not atoms:
        #verifica uma hipótese de valoração.....
        valuation_hypothesis = truth_value(formula, intepretation)
        if valuation_hypothesis:
            #se verdade essa valoração == True ela atende, então a retorne
            return intepretation
        else:
            return False
    #remove um atomo da formula e seta Duas hipoteses True or False
    atom = atoms.pop() 
    new_dict = intepretation
    true_hypothesis_atom = dict(new_dict,**{str(atom.name): True })
    false_hypothesis_atom = dict(new_dict,**{str(atom.name): False })

    formula_valuetion_true = sat(formula,atoms,true_hypothesis_atom)
    if formula_valuetion_true:
        return formula_valuetion_true

    formula_valuation_false = sat(formula,atoms,false_hypothesis_atom)
    if formula_valuation_false:
        return formula_valuation_false

    return "Impossível satisfazer essa formula"
    
    

def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    list_atoms = atoms(formula)
    initial_interpretation = {}
    return sat(formula, list_atoms, initial_interpretation)





