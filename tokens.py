class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})"

# Numeric tokens
class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)

# Operation tokens
class Operation(Token):
    def __init__(self, value):
        super().__init__("OP", value)

# Declaration tokens for "create a variable"
class Declaration(Token):
    def __init__(self, value):
        super().__init__("DECL", value)

# Variable tokens, for example "x" in "create a variable named 'x'"
class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR", value)

# Boolean tokens (true/false or other boolean values)
class Boolean(Token):
    def __init__(self, value):
        super().__init__("BOOL", value)

# Comparison operators, e.g., ">", "<", "=="
class Comparison(Token):
    def __init__(self, value):
        super().__init__("COMP", value)

# Reserved keywords for special commands such as 'if', 'else'
class Reserved(Token):
    def __init__(self, value):
        super().__init__("RSV", value)

# Emoji tokens for special commands, e.g., 📋 for copying or 🔢 for list generation
class Emoji(Token):
    def __init__(self, value):
        super().__init__("EMOJI", value)

# String tokens for representing string literals
class String(Token):
    def __init__(self, value):
        super().__init__("STR", value)

# Keyword tokens representing specific operations (e.g., "repeat", "print")
class Keyword(Token):
    def __init__(self, value):
        super().__init__("KEY", value)

# New token class for natural language commands like "create a variable named"
class Command(Token):
    def __init__(self, value):
        super().__init__("CMD", value)

# Alias tokens for user-defined keywords, i.e., when users define their own shorthand for commands
class Alias(Token):
    def __init__(self, value):
        super().__init__("ALIAS", value)

