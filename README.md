Estrai le disponibilità delle varie scuole per l'immissione a ruolo 2022/2023, a partire dal criptico PDF messo a disposizione dal MIUR.

Per calcolare gli indirizzi delle scuole, usiamo i dati pubblici (OpenData) resi disponibili dal MIUR al seguente indirizzo:

- https://dati.istruzione.it/opendata/opendata/catalogo/elements1/?area=Scuole

# Prima di qualsiasi altra cosa

1. Installa le dipendenze: `pip install -r requirements.txt`
2. Scaricati il file CSV con le scuole del MIUR da [questo indirizzo](https://dati.istruzione.it/opendata/opendata/catalogo/elements1/?area=Scuole), e salvalo nella cartella `storage` con nome `scuole-miur.csv`.  Per il download diretto del CSV del 2023-2024, [clicca qui](https://dati.istruzione.it/opendata/opendata/catalogo/elements1/SCUANAGRAFESTAT20232420230901.csv).


# Mostrare le disponibilità delle scuole

1. Crea il database con le scuole del MIUR a partire dal CSV scaricato:
   ```bash
   python3 -m bin.crea_database_scuole_miur
   ```
   Se ha funzionato, troverai nella cartella `storage` un file `scuole-miur.sqlite` che pesa circa 13 MB.
2. Stampa su schermo le scuole con disponibilità, ripartite per disponibilità:
   ```bash
   python3 -m bin.distribuzione_disponibilita 1
   ```

# Visualizzare disponibilità su una mappa

Se vuoi mostrare le scuole su una mappa:

1. Inserisci la tua chiave API di Google Maps in .env
2. Lancia il seguente comando per generare il file `storage/scuole-con-coordinate.csv`:
   ```bash
   python3 -m bin.estrai_csv_con_coordinate 1
   ```
3. Il CSV generato contiene le disponibilità delle scuole e le relative coordinate geografiche
4. Carica il CSV su [Google My Maps](https://mymaps.google.com/) per vedere le scuole su una mappa


# Salva su CSV le scuole filtrate per un criterio

1. Guarda la prima riga del file CSV con le scuole e scegli un criterio per filtrare le scuole. Ad esempio scegli la colonna DESCRIZIONECOMUNE (che contiene il nome del comune) e il valore ROMA.
1. Lancia il comando seguente personalizzando il criterio:
   ```bash
   python3 -m bin.filtra_csv_scuole <scuole-miur.csv> <colonna> <valore> <storage/file-destinazione.csv>
   ```
   dove `scuole-miur.csv` è il file CSV con le scuole del MIUR (vedi sopra).
1. Troverai il file con le scuole filtrate in `file-destinazione.csv`