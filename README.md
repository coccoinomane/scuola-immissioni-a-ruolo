Estrai le disponibilità delle varie scuole per l'immissione a ruolo 2022/2023, a partire dal criptico PDF messo a disposizione dal MIUR.

Per calcolare gli indirizzi delle scuole, usiamo i dati pubblici (OpenData) resi disponibili dal MIUR al seguente indirizzo:

- https://dati.istruzione.it/opendata/opendata/catalogo/elements1/?area=Scuole

# Come usare

1. Scaricati il file CSV con le scuole del MIUR da [questo indirizzo](https://dati.istruzione.it/opendata/opendata/catalogo/elements1/SCUANAGRAFESTAT20222320220901.csv), e salvalo nella cartella `storage` con nome `scuole-miur.csv`.
2. Crea il database con le scuole del MIUR a partire dal CSV scaricato:
   ```bash
   python3 -m bin.crea_database_scuole_miur
   ```
   Se ha funzionato, troverai nella cartella `storage` un file `scuole-miur.sqlite` che pesa circa 13 MB.
3. Stampa su schermo le scuole con disponibilità, ripartite per disponibilità:
   ```bash
   python3 -m bin.distribuzione_disponibilita 1
   ```