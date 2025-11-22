# Ferramenta Interativa de Lógica Proposicional

Este projeto implementa uma aplicação interativa para manipulação e análise de sentenças da lógica proposicional utilizando Python, SymPy e Streamlit.  
O objetivo é oferecer uma ferramenta simples e funcional para auxiliar estudantes na compreensão de equivalência lógica, formas normais e satisfatibilidade.

## Funcionalidades

1. **Verificação de Equivalência (i)**  
   Dadas duas sentenças, o sistema verifica se elas são logicamente equivalentes com base em transformações algébricas.

2. **Geração da Forma Normal Conjuntiva – FNC (ii)**  
   Converte qualquer sentença válida da lógica proposicional em uma fórmula equivalente na Forma Normal Conjuntiva.

3. **Geração da Forma Normal Disjuntiva – FND (iii)**  
   Converte a sentença em uma forma equivalente na Forma Normal Disjuntiva.

4. **Verificação de Satisfatibilidade – SAT (iv)**  
   Com base na sentença original ou em sua FNC, o sistema verifica se há alguma valoração que a torna verdadeira.

## Estrutura do Projeto

logica_streamlit/
├── app.py # Interface construída com Streamlit
├── logic_core.py # Implementação das operações lógicas
├── requirements.txt
├── .gitignore 
└── README.md

## Como Executar o Projeto

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar a aplicação

```bash
streamlit run app.py
```

