# mihu/models/concept.py

class Concept:
    def __init__(self, name, definition, explanation, formulas=None, terms=None, derivation=None):
        self.name = name
        self.definition = definition
        self.explanation = explanation
        self.formulas = formulas or []
        self.terms = terms or {}
        self.derivation = derivation

    def explain(self):
        return self.explanation

    def get_definition(self):
        return self.definition

    def get_terms(self):
        return self.terms

    def get_derivation(self):
        return self.derivation