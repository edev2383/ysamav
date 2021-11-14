from stockbox.stockbox.domain.rules.parser.abs_expr import AbstractExpr

class RuleResultOutput:
    resolution: bool
    expression: AbstractExpr
    values: list

    def __init__(self, expression: AbstractExpr, values: list):
        self.expression  = expression
        self.values = values
        self.resolution = values[-1]
