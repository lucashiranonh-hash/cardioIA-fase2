import pandas as pd
import os

print("=== CardioIA - Diagnóstico Automatizado ===\n")

# Verifica se os arquivos existem
if not os.path.exists('sintomas_pacientes.txt'):
    print("❌ Erro: Arquivo sintomas_pacientes.txt não encontrado!")
    print("   Coloque ele na mesma pasta.")
    exit()

if not os.path.exists('mapa_conhecimento.csv'):
    print("❌ Erro: Arquivo mapa_conhecimento.csv não encontrado!")
    exit()

# Carrega o CSV
mapa = pd.read_csv('mapa_conhecimento.csv')
print("Colunas encontradas:", list(mapa.columns))

# Função que identifica sintomas
def identificar_sintomas(frase):
    frase = frase.lower()
    diagnosticos = []
    for _, row in mapa.iterrows():
        s1 = str(row['Sintoma1']).lower()
        s2 = str(row['Sintoma2']).lower() if pd.notna(row['Sintoma2']) else ''
        doenca = row['Doenca_Associada']
        
        if s1 in frase or s2 in frase:
            diagnosticos.append(doenca)
    return list(set(diagnosticos))

# Lê as frases
with open('sintomas_pacientes.txt', 'r', encoding='utf-8') as f:
    frases = [linha.strip() for linha in f if linha.strip()]

print(f"{len(frases)} frases de pacientes carregadas.\n")

for i, frase in enumerate(frases, 1):
    diag = identificar_sintomas(frase)
    resultado = ", ".join(diag) if diag else "Não identificado"
    print(f"Paciente {i}:")
    print(f"→ {frase}")
    print(f"Diagnóstico: {resultado}\n")