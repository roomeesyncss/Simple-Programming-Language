from tokens import Integer, Float, Reserved

class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.data = base

    def read_INT(self, value):
        return int(value)

    def read_FLT(self, value):
        return float(value)

    def read_VAR(self, id):
        variable = self.data.read(id)
        variable_type = variable.type

        return getattr(self, f"read_{variable_type}")(variable.value)

    def compute_bin(self, left, op, right):
        left_type = "VAR" if str(left.type).startswith("VAR") else str(left.type)
        right_type = "VAR" if str(right.type).startswith("VAR") else str(right.type)
        if op.value in ["=", "equals"]:
            left.type = f"VAR({right_type})"
            self.data.write(left, right)
            return left  # Return the left node which now holds the variable

        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)

        if op.value in ["+", "plus"]:
            output = left + right
        elif op.value in ["-", "minus"]:
            output = left - right
        elif op.value in ["*", "times"]:
            output = left * right
        elif op.value in ["/", "divided by"]:
            output = left / right
        elif op.value in [">", "greater than"]:
            output = 1 if left > right else 0
        elif op.value in [">=", "greater or equal"]:
            output = 1 if left >= right else 0
        elif op.value in ["<", "less than"]:
            output = 1 if left < right else 0
        elif op.value in ["<=", "less or equal"]:
            output = 1 if left <= right else 0
        elif op.value in ["?=", "equal to"]:
            output = 1 if left == right else 0
        elif op.value in ["and"]:
            output = 1 if left and right else 0
        elif op.value in ["or"]:
            output = 1 if left or right else 0

        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)

    def compute_unary(self, operator, operand):
        operand_type = "VAR" if str(operand.type).startswith("VAR") else str(operand.type)

        operand = getattr(self, f"read_{operand_type}")(operand.value)

        if operator.value == "+":
            output = +operand
        elif operator.value == "-":
            output = -operand
        elif operator.value == "not":
            output = 1 if not operand else 0

        return Integer(output) if (operand_type == "INT") else Float(output)

    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        if isinstance(tree, list):
            if isinstance(tree[0], Reserved):
                if tree[0].value == "if":
                    for idx, condition in enumerate(tree[1][0]):
                        evaluation = self.interpret(condition)
                        if evaluation.value == 1:
                            return self.interpret(tree[1][1][idx])

                    if len(tree[1]) == 3:
                        return self.interpret(tree[1][2])

                    else:
                        return
                elif tree[0].value == "while":
                    condition = self.interpret(tree[1][0])

                    while condition.value == 1:
                        print(self.interpret(tree[1][1]))

                        # Checking the condition
                        condition = self.interpret(tree[1][0])

                    return

        # Unary operation
        if isinstance(tree, list) and len(tree) == 2:
            expression = tree[1]
            if isinstance(expression, list):
                expression = self.interpret(expression)
            return self.compute_unary(tree[0], expression)

        # No operation
        elif not isinstance(tree, list):
            return tree

        else:

            left_node = tree[0]
            if isinstance(left_node, list):
                left_node = self.interpret(left_node)


            right_node = tree[2]
            if isinstance(right_node, list):
                right_node = self.interpret(right_node)

            operator = tree[1]
            return self.compute_bin(left_node, operator, right_node)