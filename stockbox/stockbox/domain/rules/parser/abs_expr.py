from abc import ABC, abstractmethod


class ExprVisitor:
    def visitBinary(self, binary):
        pass

    def visitGrouping(self, grouping):
        pass

    def visitLiteral(self, literal):
        pass

    def visitUnary(self, unary):
        pass


class AbstractExpr(ABC):
    pass

    @abstractmethod
    def accept(self, visitor: ExprVisitor):
        pass
