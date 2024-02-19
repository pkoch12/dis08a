import tkinter as tk
from tkinter import filedialog
import pandas as pd
import re

def process_csv(file_path):
    # CSV-Datei lesen
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Extrahiere Jahreszahl aus der ersten Zeile
    year = re.findall(r'\d{4}', content.split('\n')[0])[0]
    
    # Konvertiere den CSV-Inhalt in ein DataFrame
    df = pd.read_csv(file_path, delimiter=";", header=None, skiprows=4)
    
    # Füge Jahreszahl als erste Spalte hinzu
    df.insert(0, 'Jahr', year)
    
    # Lösche spezifizierte Zeilen und Spalten
    df = df.iloc[:16].drop(columns=[2, 3, 6, 7])
    
    # Setze Spaltennamen für jeden DataFrame
    df.columns = ['Jahr', 'Bundesland', 'Einwohner *1.000', 'mit Migrationshintergrund', 'Anteil in Prozent']
    
    return df

def combine_csv_files(file_paths):
    combined_df = pd.DataFrame(columns=['Jahr', 'Bundesland', 'Einwohner *1.000', 'mit Migrationshintergrund', 'Anteil in Prozent'])
    for file_path in file_paths:
        df = process_csv(file_path)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    return combined_df

# Interaktive Dateiauswahl
root = tk.Tk()
root.withdraw()  # Wir verstecken das Tkinter-Hauptfenster
file_paths = filedialog.askopenfilenames(title="Wählen Sie die CSV-Dateien aus", filetypes=[("CSV-Dateien", "*.csv")])  # Mehrere Dateien auswählen

if file_paths:  # Überprüfe, ob Dateien ausgewählt wurden
    combined_df = combine_csv_files(file_paths)
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV-Dateien", "*.csv")], title="Speichern als")
    if save_path:  # Überprüfe, ob ein Speicherort ausgewählt wurde
        combined_df.to_csv(save_path, index=False, sep=';')
    else:
        print("Speichern abgebrochen.")
else:
    print("Keine Dateien ausgewählt.")
