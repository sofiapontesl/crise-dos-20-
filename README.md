# 🧠 Crise dos 20 Anos: Uma Análise de Dados com Python

Este projeto tem como objetivo analisar as percepções de jovens sobre a chamada **"crise dos 20 anos"**. Usamos dados coletados por um formulário do Google Forms com perguntas sobre idade, gênero, estudo, trabalho, produtividade e o conhecimento da expressão "crise dos 20".

---

## 📊 Objetivos

- Coletar e analisar dados de jovens entre 18 e 30 anos sobre temas relacionados à vida adulta.
- Investigar a relação entre variáveis como gênero, idade, estudo, trabalho e a percepção de cobrança produtiva.
- Divulgar achados relevantes para discussão social ou acadêmica.
- Praticar análise de dados com Python (Pandas, Matplotlib, Seaborn, etc).

---

## 🗃️ Estrutura do Projeto

crise-dos-20/
├── data/
│ └── respostas.csv # Dados exportados ou atualizados da API
├── notebooks/
│ └── eda.ipynb # Análise exploratória dos dados
├── src/
│ ├── fetch_sheets.py # Script para puxar dados via API Google Sheets
│ ├── clean.py # Limpeza e padronização de colunas
│ ├── analysis.py # Cálculos estatísticos e cruzamentos
│ └── visualize.py # Geração de gráficos
├── outputs/
│ └── figuras/ # Gráficos salvos
├── README.md # Este arquivo
├── requirements.txt # Dependências do projeto
└── .gitignore # Arquivos ignorados pelo Git

