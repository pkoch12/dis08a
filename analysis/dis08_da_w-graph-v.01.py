import pandas as pd
import matplotlib.pyplot as plt

def korrelationsanalyse_und_graph_pro_jahr(daten1_pfad, daten2_pfad):
    # Daten laden
    df1 = pd.read_csv(daten1_pfad, delimiter=';')  # Gewerbeanmeldungen
    df2 = pd.read_csv(daten2_pfad, delimiter=';')  # Migrationshintergrund
    
    # Daten zusammenführen
    df_merged = pd.merge(df1, df2, left_on=["Jahreszahl", "Bundesland"], right_on=["Jahr", "Bundesland"])
    
    # Korrekturen für die Berechnungen: Werte in 'Einwohner *1.000' und 'mit Migrationshintergrund' sind um Faktor 1000 zu erhöhen
    df_merged["Gewerbeanmeldungen pro 1.000 Einwohner"] = (df_merged["Gewerbeanmeldungen"] / (df_merged["Einwohner *1.000"] * 1000)) * 1000
    df_merged["Migrantenanteil in Prozent"] = (df_merged["mit Migrationshintergrund"] * 1000 / (df_merged["Einwohner *1.000"] * 1000)) * 100
    
    # Jahre im Datensatz
    jahre = df_merged['Jahr'].unique()
    
    for jahr in sorted(jahre):
        df_jahr = df_merged[df_merged['Jahr'] == jahr]
        
        # Korrelationsanalyse für das Jahr
        korrelation = df_jahr[["Migrantenanteil in Prozent", "Gewerbeanmeldungen pro 1.000 Einwohner"]].corr()
        print(f"Korrelation für {jahr}:")
        print(korrelation)
        
        # Graph erzeugen für das Jahr
        plt.figure(figsize=(10, 6))
        plt.scatter(df_jahr["Migrantenanteil in Prozent"], df_jahr["Gewerbeanmeldungen pro 1.000 Einwohner"])
        plt.title(f'Migrantenanteil vs. Gewerbeanmeldungen pro 1.000 Einwohner ({jahr})')
        plt.xlabel('Migrantenanteil in Prozent')
        plt.ylabel('Gewerbeanmeldungen pro 1.000 Einwohner')
        plt.grid(True)
        
        # Für jedes Bundesland das Label hinzufügen
        for i, txt in enumerate(df_jahr["Bundesland"]):
            plt.annotate(txt, (df_jahr["Migrantenanteil in Prozent"].iloc[i], df_jahr["Gewerbeanmeldungen pro 1.000 Einwohner"].iloc[i]))
        
        plt.show()

# Beispiel für den Aufruf der Funktion
daten1_pfad = 'G:/Meine Ablage/Studium/Pätsch/Vorlesung/DIS08 - Data-Modelling/analysis/dis08_01_out_Gewerbeanzeigenstatistik_bereinigt_utf-8.csv'
daten2_pfad = 'G:/Meine Ablage/Studium/Pätsch/Vorlesung/DIS08 - Data-Modelling/analysis/dis08_02_out_cleansing_MA_combined-data.csv'
korrelationsanalyse_und_graph_pro_jahr(daten1_pfad, daten2_pfad)
