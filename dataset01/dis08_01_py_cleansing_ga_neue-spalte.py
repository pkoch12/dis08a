import pandas as pd

# Pfad zur CSV-Datei
pfad_zur_datei = 'G:/Meine Ablage/Studium/Pätsch/Vorlesung/DIS08 - Data-Modelling/Daten/dis08_01_in_Gewerbeanzeigenstatistik_bereinigt_utf-8.csv'

# Lese die CSV-Datei
df = pd.read_csv(pfad_zur_datei, sep=';', header=None, names=['Bundesland', 'Gewerbeanmeldungen'], encoding='utf-8')

# Initialisiere die Liste für die aktualisierten Daten und eine Variable für die aktuelle Jahreszahl
aktualisierte_daten = []
aktuelle_jahreszahl = None
zeilen_zu_loeschen = []

# Iteriere durch jede Zeile im DataFrame
for index, row in df.iterrows():
    # Prüfe, ob die Zeile eine Jahreszahl enthält
    try:
        # Konvertiere den Wert der ersten Spalte in eine Zahl und prüfe, ob es vierstellig ist
        jahr = int(row['Bundesland'])
        if 1900 < jahr < 2100:  # Einfache Überprüfung, ob es eine plausible Jahreszahl ist
            aktuelle_jahreszahl = jahr  # Aktualisiere die aktuelle Jahreszahl
            zeilen_zu_loeschen.append(index)  # Markiere die Zeile zum Löschen
        else:
            raise ValueError
    except ValueError:
        # Wenn die Zeile keine Jahreszahl ist, füge sie mit der aktuellen Jahreszahl in die neue Liste ein
        if aktuelle_jahreszahl is not None:
            aktualisierte_daten.append([aktuelle_jahreszahl, row['Bundesland'], row['Gewerbeanmeldungen']])

# Erstelle einen neuen DataFrame ohne die Zeilen, die ursprünglich Jahreszahlen enthielten
neuer_df = pd.DataFrame(aktualisierte_daten, columns=['Jahreszahl', 'Bundesland', 'Gewerbeanmeldungen'])

# Pfad für die Ausgabedatei
ausgabe_pfad = 'G:/Meine Ablage/Studium/Pätsch/Vorlesung/DIS08 - Data-Modelling/Daten/dis08_01_out_Gewerbeanzeigenstatistik_bereinigt_utf-8.csv'

# Speichere den aktualisierten DataFrame in einer neuen CSV-Datei
neuer_df.to_csv(ausgabe_pfad, index=False, sep=';', encoding='utf-8')
