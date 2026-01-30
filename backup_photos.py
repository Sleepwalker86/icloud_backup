#!/usr/bin/env python3
"""
iCloud/Photos Backup Script mit osxphotos

Sichert alle Fotos aus der Apple Photos-Bibliothek nach /Volumes/Fotos/icloud_fotos.
Verwendet --update für inkrementelle Backups (nur neue/geänderte Fotos).
"""

import subprocess
import sys
from pathlib import Path

# Zielpfad für das Backup
BACKUP_PATH = Path("/Volumes/Fotos/icloud_fotos")


def is_photos_running() -> bool:
    """Prüft, ob die App Fotos (Photos) läuft – die Datenbank ist dann gesperrt."""
    r = subprocess.run(["pgrep", "-x", "Photos"], capture_output=True)
    return r.returncode == 0


def main() -> int:
    if not BACKUP_PATH.parent.exists():
        print(f"Fehler: Volume {BACKUP_PATH.parent} ist nicht eingehängt.")
        print("Bitte externe Festplatte/Volume 'Fotos' verbinden.")
        return 1

    if is_photos_running():
        print("Fehler: Die App 'Fotos' (Photos) läuft noch.")
        print("Die Photos-Datenbank ist gesperrt – osxphotos kann sie nicht lesen.")
        print("Bitte Fotos vollständig beenden (Cmd+Q) und das Script erneut starten.")
        return 1

    BACKUP_PATH.mkdir(parents=True, exist_ok=True)

    # osxphotos export mit sinnvollen Optionen für Backup:
    # --update: nur neue/geänderte Fotos (inkrementell)
    # --export-by-date: Ordnerstruktur Jahr/Monat/Tag
    # --verbose: Fortschritt anzeigen
    cmd = [
        "osxphotos",
        "export",
        str(BACKUP_PATH),
        "--export-by-date",
        "--update",
        "--verbose",
    ]

    # Optional: Fehlende Fotos aus iCloud nachladen (kann Photos.app belasten)
    # Auskommentieren, wenn du keine iCloud-Bibliothek nutzt oder es Probleme macht
    # cmd.append("--download-missing")

    print(f"Starte Backup nach: {BACKUP_PATH}")
    print("Befehl:", " ".join(cmd))
    print("-" * 50)

    try:
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print()
            print("Hinweis: Bei 'Operation not permitted' / PermissionError:")
            print("  Vollständigen Festplattenzugriff für Terminal/Cursor in den Systemeinstellungen")
            print("  erlauben (Datenschutz & Sicherheit → Vollständiger Festplattenzugriff).")
        return result.returncode
    except FileNotFoundError:
        print("Fehler: 'osxphotos' nicht gefunden.")
        print("Installation: pip install osxphotos")
        print("Oder mit uv: uv tool install --python 3.13 osxphotos")
        return 1


if __name__ == "__main__":
    sys.exit(main())
