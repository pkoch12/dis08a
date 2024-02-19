#!/bin/bash

# Pfad zur CSV-Datei
CSV_PATH="C:/Users/Patsch/Documents/DIS08/Gewerbeanzeigenstatistik_bereinigt_transformiert.csv"

# Markdown-Flag-Check
OUTPUT_MARKDOWN=False
if [[ "$1" == "--markdown" ]]; then
  OUTPUT_MARKDOWN=True
fi

# Python-Skript für Datenanalyse
PYTHON_SCRIPT="analyze_csv.py"

# Python-Skript Inhalt
read -r -d '' PYTHON_CODE <<EOF
import pandas as pd
import sys
import numpy as np  # Importiere NumPy direkt

# CSV-Datei einlesen
df = pd.read_csv("$CSV_PATH", sep=';')


# Markdown Flag
output_markdown = $OUTPUT_MARKDOWN

def print_md(line):
    if output_markdown:
        print(line)
    else:
        print(line.strip('# '))

# Shape der Daten
print_md("# Shape of Dataset")
print_md(f"- Rows with data: {df.dropna().shape[0]}")
print_md(f"- Column count: {df.shape[1]}")

# Spaltennamen
print_md("# Column Names")
for col in df.columns:
    print_md(f"- {col}")

# Datentypen der Spalten
print_md("# Column Data Types")
for col in df.columns:
    dtype = "Numeric" if pd.api.types.is_numeric_dtype(df[col]) else "Textual"
    print_md(f"- {col}: {dtype}")

# Einzigartige Werte pro Spalte
print_md("# Unique Value Count per Column")
for col in df.columns:
    print_md(f"- {col}: {df[col].nunique()}")

# Details zu numerischen Spalten
print_md("# Numeric Column Details")
for col in df.select_dtypes(include=[np.number]).columns:  # Nutze np.number direkt
    max_val = df[col].max()
    min_val = df[col].min()
    mean_val = df[col].mean()
    median_val = df[col].median()
    mode_val = df[col].mode()[0] if not df[col].mode().empty else 'NA'
    print_md(f"- {col}: Max={max_val}, Min={min_val}, Mean={mean_val}, Median={median_val}, Mode={mode_val}")

# Einzigartige Werte, wenn unter Schwellenwert
threshold = 5
print_md("# Values for Columns with Low Unique Value Count")
for col in df.columns:
    unique_values = df[col].nunique()
    if unique_values <= threshold:
        print_md(f"- {col}: {df[col].unique()}")

EOF

# Führe das Python-Skript aus
echo "$PYTHON_CODE" | python -
