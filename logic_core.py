import string
from sympy import symbols, sympify
from sympy.logic import to_cnf, to_dnf, satisfiable, simplify_logic, Implies
from sympy.logic.boolalg import Equivalent



# Função para converter string → expressão SymPy
def parse_formula(formula: str):
    """
    Converte uma string contendo uma fórmula proposicional em uma
    expressão SymPy.

    Suporta:
    - Negação: ¬, ~, !
    - Conjunção: ∧, &, ^
    - Disjunção: ∨, v, |
    - Implicação: ->, →
    - Parênteses normais
    """

    if not isinstance(formula, str):
        raise ValueError("A fórmula deve ser uma string.")

    all_vars = list(string.ascii_lowercase + string.ascii_uppercase)

    props = symbols(" ".join(all_vars))
    local_dict = {str(p): p for p in props}

    s = formula.lower().strip()

    # Substituições de operadores
    replacements = {
        "¬": "~",
        "!": "~",
        "∧": "&",
        "^": "&",
        "∨": "|",
        " v ": " | ",
        "->": ">>",
        "→": ">>",
    }

    for old, new in replacements.items():
        s = s.replace(old, new)

    if " v " in s:
        s = s.replace(" v ", " | ")

    try:
        expr = sympify(s, locals=local_dict, convert_xor=True)
    except Exception as e:
        raise ValueError(f"Erro ao interpretar a fórmula '{formula}': {e}")

    return expr



# (i) Verificação de equivalência

def are_equivalent(formula1: str, formula2: str) -> bool:
    """
    Retorna True se formula1 e formula2 forem logicamente equivalentes.
    """
    f1 = parse_formula(formula1)
    f2 = parse_formula(formula2)

    try:
        eq_expr = Equivalent(f1, f2)
        simplified = simplify_logic(eq_expr)

        return bool(simplified is True or simplified == True)
    except Exception:
        return False



# (ii) Forma Normal Conjuntiva

def to_cnf_str(formula: str) -> str:
    expr = parse_formula(formula)
    cnf_expr = to_cnf(expr, simplify=True)
    return str(cnf_expr)



# (iii) Forma Normal Disjuntiva

def to_dnf_str(formula: str) -> str:
    expr = parse_formula(formula)
    dnf_expr = to_dnf(expr, simplify=True)
    return str(dnf_expr)



# (iv) Verificar satisfatibilidade (SAT)

def is_satisfiable(formula: str) -> bool:
    expr = parse_formula(formula)
    result = satisfiable(expr)
    return bool(result)
