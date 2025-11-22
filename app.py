import streamlit as st
from logic_core import (
    are_equivalent,
    to_cnf_str,
    to_dnf_str,
    is_satisfiable,
    parse_formula,
)
from sympy import sympify


def detect_equivalence_used(f1, f2):
    try:
        e1 = parse_formula(f1)
        e2 = parse_formula(f2)
    except:
        return "Equivalência logicamente válida (não foi possível identificar a regra específica)."

    s1 = str(e1)
    s2 = str(e2)

    if "Implies" in s1 or ">>" in f1:
        if "Or" in s2 or "|" in s2:
            return "Eliminação da implicação (p → q ≡ ¬p ∨ q)"

    if "Not(And" in s1 and "Or" in s2:
        return "Lei de De Morgan (¬(p ∧ q) ≡ ¬p ∨ ¬q)"

    if "Not(Or" in s1 and "And" in s2:
        return "Lei de De Morgan (¬(p ∨ q) ≡ ¬p ∧ ¬q)"

    if "Not(Not" in s1:
        return "Dupla negação (¬¬p ≡ p)"

    if ("And" in s1 and "Or" in s2) or ("Or" in s1 and "And" in s2):
        return "Distributividade"

    return "Equivalência lógica válida (sem regra específica identificada)"



st.set_page_config(
    page_title="Lógica Proposicional – Ferramenta Interativa",
    layout="wide",
)

st.title("Ferramenta Interativa de Lógica Proposicional")

st.markdown(
    """
Esta aplicação oferece quatro funcionalidades principais:

1. Verificar se duas sentenças são logicamente equivalentes.  
2. Converter sentenças para a Forma Normal Conjuntiva (FNC).  
3. Converter sentenças para a Forma Normal Disjuntiva (FND).  
4. Verificar se uma sentença é satisfatível.  

### Sintaxe aceita
- Proposições: p, q, r, s, ...
- Negação: ~p, ¬p, !p  
- Conjunção: p & q, p ∧ q, p ^ q  
- Disjunção: p | q, p v q, p ∨ q  
- Implicação: p -> q, p → q  
- Parênteses: (p v q) -> r
"""
)

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Equivalência (i)",
        "FNC (ii)",
        "FND (iii)",
        "Satisfatibilidade (iv)",
    ]
)

# (i) Verificação de equivalência
with tab1:
    st.header("Verificar equivalência entre duas sentenças")

    col1, col2 = st.columns(2)

    with col1:
        formula1 = st.text_input("Sentença 1", value="p -> q")
    with col2:
        formula2 = st.text_input("Sentença 2", value="¬p v q")

    if st.button("Verificar equivalência", key="btn_equiv"):
        try:
            eq = are_equivalent(formula1, formula2)
            if eq:
                st.success("As sentenças são logicamente equivalentes.")
                regra = detect_equivalence_used(formula1, formula2)
                st.info(f"Equivalência utilizada: {regra}")
            else:
                st.warning("As sentenças NÃO são logicamente equivalentes.")
        except Exception as e:
            st.error(f"Erro ao analisar as fórmulas: {e}")

# (ii) FNC
with tab2:
    st.header("Gerar Forma Normal Conjuntiva (FNC)")

    formula = st.text_input(
        "Digite uma sentença qualquer",
        value="(p v q) -> r",
        key="fnc_input",
    )

    if st.button("Gerar FNC", key="btn_fnc"):
        try:
            cnf_str = to_cnf_str(formula)
            st.write("FNC equivalente:")
            st.code(cnf_str, language="text")
        except Exception as e:
            st.error(f"Erro ao gerar a FNC: {e}")

# (iii) FND
with tab3:
    st.header("Gerar Forma Normal Disjuntiva (FND)")

    formula = st.text_input(
        "Digite uma sentença qualquer",
        value="(p & q) v r",
        key="fnd_input",
    )

    if st.button("Gerar FND", key="btn_fnd"):
        try:
            dnf_str = to_dnf_str(formula)
            st.write("FND equivalente:")
            st.code(dnf_str, language="text")
        except Exception as e:
            st.error(f"Erro ao gerar a FND: {e}")

# (iv) Satisfatibilidade
with tab4:
    st.header("Verificar satisfatibilidade")

    formula = st.text_input(
        "Digite uma sentença (em qualquer forma)",
        value="p & ~p",
        key="sat_input",
    )

    if st.button("Verificar SAT", key="btn_sat"):
        try:
            sat = is_satisfiable(formula)
            if sat:
                st.success("A sentença é satisfatível (existe uma valoração que a torna verdadeira).")
            else:
                st.error("A sentença é insatisfatível (contradição).")
        except Exception as e:
            st.error(f"Erro ao verificar satisfatibilidade: {e}")
