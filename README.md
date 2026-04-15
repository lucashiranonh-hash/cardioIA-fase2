# cardioIA - Fase 2: Diagnóstico Automatizado com IA

Projeto desenvolvido para a **Fase 2** do PBL **CardioIA - A Nova Era da Cardiologia Inteligente**.

Este módulo simula um **estetoscópio digital** com Inteligência Artificial, capaz de:
- Analisar descrições de sintomas relatados por pacientes
- Sugerir diagnósticos cardiológicos com base em um mapa de conhecimento
- Classificar o nível de risco do paciente (**baixo risco** ou **alto risco**) usando Machine Learning

## 🎯 Objetivos da Fase 2

- Extrair informações de texto médico (NLP básico)
- Criar um mapa de associação entre sintomas e doenças
- Desenvolver um classificador de risco com **TF-IDF** + **Logistic Regression**
- Refletir sobre governança de dados e uso responsável de IA na saúde

## 📁 Estrutura do Projeto

```bash
cardioIA-fase2/
├── sintomas_pacientes.txt          # 10 frases de sintomas dos pacientes
├── mapa_conhecimento.csv           # Mapa de sintomas → diagnósticos
├── dataset_risco.csv               # Base de frases rotuladas (baixo/alto risco)
├── diagnostico_basico.py           # Parte 1 - Extração de sintomas e diagnóstico
├── classificador_risco.ipynb       # Parte 2 - Classificador com TF-IDF e ML
├── modelo_risco.pkl                # Modelo salvo (opcional)
├── vectorizer.pkl                  # Vectorizer salvo (opcional)
└── README.md

```

Como executar o projeto
Pré-requisitos

Python 3.8 ou superior
Instale as bibliotecas:Bashpip install pandas scikit-learn joblib

Execução
1. Parte 1 – Diagnóstico básico:
Bashpython diagnostico_basico.py
2. Parte 2 – Classificador de risco:
Abra o arquivo classificador_risco.ipynb no Jupyter Notebook ou VS Code e execute as células.
✅ Funcionalidades Implementadas
Parte 1

Leitura das 10 frases de pacientes
Identificação de sintomas através de palavras-chave
Sugestão automática de diagnósticos (Infarto, Angina, Insuficiência Cardíaca, Arritmia, etc.)

Parte 2

Uso de TF-IDF para vetorização de texto
Treinamento de modelo de Logistic Regression
Classificação do nível de risco
Avaliação de acurácia e relatório de desempenho



Lucas Yuji Nakayama Hirano - RM 563420



⚠️ Considerações sobre IA Responsável
Este projeto é uma simulação educacional e não deve ser utilizado para diagnósticos reais.
Os dados são sintéticos e podem apresentar vieses.
Em sistemas reais de saúde, é fundamental a validação por profissionais médicos, governança de dados e respeito à privacidade do paciente (LGPD).


Validação por médicos
Governança de dados
Proteção à privacidade (LGPD)
