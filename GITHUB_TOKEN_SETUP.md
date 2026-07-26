# GitHub Token erstellen für github-readme-terminal

## Schritt-für-Schritt Anleitung

### 1. GitHub Settings öffnen
- Gehe zu: https://github.com/settings/tokens
- Oder: GitHub → Profilbild → Settings → Developer settings → Personal access tokens → Tokens (classic)

### 2. Neuen Token erstellen
- Klicke auf **"Generate new token"** → **"Generate new token (classic)"**
- Gib dem Token einen Namen, z.B. `github-readme-terminal`

### 3. Berechtigungen setzen
Wähle folgende Berechtigung:
- ✅ **public_repo** (Access public repositories)

### 4. Token erstellen
- Klicke auf **"Generate token"**
- **WICHTIG:** Kopiere den Token sofort! Er wird nur einmal angezeigt.
- Der Token sieht so aus: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 5. Token in .env Datei eintragen

Erstelle eine Datei namens `.env` im Hauptverzeichnis deines Projekts:

```bash
# Inhalt der .env Datei:
GITHUB_TOKEN=ghp_dein_token_hier
```

### 6. Skript ausführen
```bash
python3 generate_terminal.py
```

## Sicherheitshinweise

⚠️ **WICHTIG:**
- Teile deinen Token **niemals** öffentlich (nicht in GitHub committen!)
- Die `.env` Datei sollte in `.gitignore` eingetragen sein
- Der Token hat nur Lesezugriff auf öffentliche Repositories (sicher)
- Bei Verlust einfach den Token auf GitHub widerrufen und neu erstellen

## Troubleshooting

Falls der Token nicht funktioniert:
1. Überprüfe, ob der Token korrekt kopiert wurde (keine Leerzeichen)
2. Stelle sicher, dass die Berechtigung `public_repo` aktiviert ist
3. Neu erstellte Tokens können ein paar Minuten brauchen, bis sie aktiv sind