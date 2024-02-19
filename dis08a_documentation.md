# About this dataset
  ## about me
  **Name:** Patrick Koch
  
  **Matrikelnummer** 11138439
  
# Datenanalyse
## Projektübersicht
Vorliegend sind zwei Datensätze, einer beinhaltet die **Gewerbeanmeldungen von 2011 bis 2019** nach Bundesländern und der andere zeigt den **Anteil der Migranten von 2011 bis 2019 nach Bundesländern**.
Aufgabe der Analyse ist es, herauszufinden, ob diese beiden Entwicklungen einen statistischen Zusammenhang zeigen. Also ist es möglich eine Hypothese beim Vergleich der Daten zu erheben.

### Ausgangsfrage
**Mehr Unternehmensgründungen durch Migration? - Gibt es einen statistischen Zusammenhang zwischen der Neugründungen von Gewerben und dem Anteil der Bevölkerung mit Migrationshintergrund?**
## Analyse
### Cleansing der Datensätze
Im ersten Schritt sollen die Datensätze angeglichen werden um eine leichtere Vergleichbarkeit herzustellen. Dazu werden zwei unterschiedliche Programme verwendet.
#### Datensatz 01 - Gewerbeanzeigenstatistik
1. Datenbereinigung [#11](https://github.com/pkoch12/dis08a/issues/11)
2. Bereinigter Datensatz [dis08_01_out_Gewerbeanzeigenstatistik_bereinigt_utf-8.csv](dataset01/dis08_01_out_Gewerbeanzeigenstatistik_bereinigt_utf-8.csv)

#### Datensatz 02 - Anteil der Bevölkerung mit Migrationsgeschichte
1. Datenbereinigung [#9](https://github.com/pkoch12/dis08a/issues/9)
2. Bereinigter Datensatz [dis08_02_out_cleansing_MA_combined-data.csv](dataset02/dis08_02_out_cleansing_MA_combined-data.csv)

### Kombination der Datensätze
1. Die Kombination der Datensätze erfolgt über ein Skript, welches die Anteile der Einwohner mit Mitgrationshintergrund ins Verhältnis mit den Gewerbeanmeldungen setzt [Analysis-Skript](analysis/dis08_da_w-graph-v.01.py)
2. Hier geht es um die Anteile: Also die Gewerbeanmeldung pro 1000 Einwohner und den Anteil der Migranten in Prozent
3. Das Skript berücksichtigt Jahre (von 2011 bis 2019) und Bundesländer

## Ergebnisse
1. Es scheint, als gäbe es eine korrelation zwischen dem Anteil der Migranten und der Gewerbeanmeldungen
2. Die Analyse ist eindimensional und berücksichtigt nicht alle nötigen Faktoren um eine ausgewogene Interpretation zu ermöglichen

## Fazit und Ausblick
Grundsätzlich lässt sich eine Korrelation von Migration und Gewerbeanmeldungen in den Bundesländern beobachten. Doch schon auf den ersten Blick fällt auf, dass die Stadtstaaten Hamburg und Berlin besonders gründungsfreudig sind und einen vergleichsweise hohen Anteil an Migranten haben. Allein hier gäbe es viele Faktoren für eine detaillierte Begründung. Diese Analyse ist nicht in der Lage ein breites Feld für die Meinungsbildung abzudecken zeigt aber, dass die beiden Datensätze eine Verbindung zu einander zulassen.

