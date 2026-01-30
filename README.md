# iCloud/Photos Backup

Sichert die Apple Photos-Bibliothek mit [osxphotos](https://github.com/RhetTbull/osxphotos) nach `/Volumes/Fotos/icloud_fotos`.

## Installation

Virtuelle Umgebung ist bereits eingerichtet (`.venv`). Bei Bedarf neu anlegen:

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

## Berechtigungen (wichtig)

Damit osxphotos die Photos-Bibliothek lesen kann, braucht die App, in der du das Script startest, **Vollständigen Festplattenzugriff**:

1. **Systemeinstellungen** → **Datenschutz & Sicherheit** → **Vollständiger Festplattenzugriff**
2. **+** klicken und **Terminal** (oder **Cursor** / **PyCharm**, je nachdem wo du `python backup_photos.py` ausführst) hinzufügen und aktivieren
3. Terminal/IDE **neu starten**, danach das Script erneut ausführen

Ohne diese Berechtigung erscheint: `PermissionError: Operation not permitted` auf der Photos-Bibliothek.

## Nutzung

1. Virtuelle Umgebung aktivieren (falls noch nicht aktiv):
   ```bash
   source .venv/bin/activate
   ```
2. Externes Laufwerk/Volume **Fotos** an den Mac anschließen (damit `/Volumes/Fotos` existiert).
3. **Fotos-App beenden** (Cmd+Q) – solange Fotos läuft, ist die Bibliothek gesperrt und das Backup schlägt fehl.
4. Script ausführen:

```bash
python backup_photos.py
```

Beim ersten Lauf werden alle Fotos exportiert. Bei weiteren Läufen werden nur **neue oder geänderte** Fotos kopiert (`--update`).

## Optionen im Script

- **Zielpfad:** In `backup_photos.py` ist `BACKUP_PATH = Path("/Volumes/Fotos/icloud_fotos")` – bei Bedarf anpassen.
- **iCloud nachladen:** Wenn Fotos in iCloud sind und noch nicht lokal, kannst du in `backup_photos.py` die Zeile mit `--download-missing` einkommentieren (Photos.app muss dabei geöffnet sein).

## Ordnerstruktur

Fotos liegen unter dem Zielpfad nach Datum sortiert, z. B.:

```
/Volumes/Fotos/icloud_fotos/2024/03/15/IMG_1234.jpg
```
