# CardioIA - Fase 2: Diagnóstico Automatizado com IA

Projeto desenvolvido para a **Fase 2** do PBL CardioIA - A Nova Era da Cardiologia Inteligente.

Este módulo simula um **estetoscópio digital** com Inteligência Artificial, capaz de:
- Analisar descrições de sintomas relatados por pacientes
- Sugerir diagnósticos cardiológicos com base em um mapa de conhecimento
- Classificar o nível de risco do paciente (baixo risco ou alto risco) usando Machine Learning

##  Objetivos da Fase 2

- Extrair informações de texto médico (NLP básico)
- Criar um mapa de associação sintomas × doenças
- Desenvolver um classificador de risco usando TF-IDF + Logistic Regression
- Refletir sobre governança de dados e responsabilidade em IA na saúde

##  Estrutura do Projeto
cardioia-fase2/
├── sintomas_pacientes.txt          # 10 frases de sintomas dos pacientes

├── mapa_conhecimento.csv           # Mapa de sintomas → diagnósticos

├── dataset_risco.csv               # Base de frases rotuladas (baixo/alto risco)

├── diagnostico_basico.py           # Parte 1 - Extração de sintomas e diagnóstico

├── classificador_risco.ipynb       # Parte 2 - Classificador com TF-IDF e ML

├── modelo_risco.pkl                # Modelo salvo (opcional)

├── vectorizer.pkl                  # Vectorizer salvo (opcional)

└── README.md

##  Como executar o projeto

### Pré-requisitos
- Python 3.8 ou superior
- Bibliotecas necessárias:
  ```bash
  pip install pandas scikit-learn joblib


  Execução
1. Diagnóstico básico (Parte 1):
Bashpython diagnostico_basico.py
2. Classificador de risco (Parte 2):
Abra o arquivo classificador_risco.ipynb no Jupyter Notebook ou execute as células.
 Funcionalidades
Parte 1 - Diagnóstico por sintomas

Lê 10 frases de pacientes
Identifica sintomas usando palavras-chave
Sugere possíveis diagnósticos (Infarto, Angina, Insuficiência Cardíaca, Arritmia, etc.)

Parte 2 - Classificador de Risco

Utiliza TF-IDF para transformar texto em vetores numéricos
Treina um modelo de Logistic Regression
Classifica frases como "alto risco" ou "baixo risco"
Avaliação com acurácia e relatório de classificação


Lucas Yuji Nakayama Hirano - RM  563420
