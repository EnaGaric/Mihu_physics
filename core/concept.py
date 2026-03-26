class Concept:
    def __init__(
        self,
        name,
        definition,
        explanation,
        formulas=None,
        terms=None,
        derivation=None,
        deep_dive=None):
        
        self.name = name
        self.definition = definition
        self.explanation = explanation
        self.formulas = formulas or []
        self.terms = terms or {}
        self.derivation = derivation
        self.deep_dive = deep_dive

    def get_deep_dive(self):
        return self.deep_dive