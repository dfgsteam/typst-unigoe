#!/bin/bash
set -e

# Clear screen for a neat welcome
clear
echo "========================================================="
echo "    Typst Georg-August-Universität Göttingen Bootstrap   "
echo "========================================================="
echo ""

read -p "Enter project directory name / Projektordner Name (press Enter for 'my-thesis' or type '.' for current directory): " DEST_DIR < /dev/tty
DEST_DIR=${DEST_DIR:-my-thesis}

if [ "$DEST_DIR" = "." ]; then
  # Initialize in current directory
  # Check if directory contains non-git files
  if [ "$(ls -A | grep -v '^\.git$')" ]; then
    echo "Warning: Current directory contains files. / Warnung: Aktuelles Verzeichnis enthält Dateien."
    read -p "Do you want to proceed? / Trotzdem fortfahren? (y/n): " PROCEED < /dev/tty
    if [[ ! "$PROCEED" =~ ^[Yy]$ ]]; then
      echo "Aborted."
      exit 0
    fi
  fi
  
  echo "Cloning template to temporary directory... / Klone Vorlage in temporäres Verzeichnis..."
  # Cross-platform compatible mktemp
  TEMP_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'typst-unigoe')
  git clone --depth 1 https://github.com/dfgsteam/typst-unigoe.git "$TEMP_DIR"
  
  # Delete the cloned git config so we don't overwrite the user's existing remote git config
  rm -rf "$TEMP_DIR/.git"
  
  echo "Copying files... / Kopiere Dateien..."
  cp -r "$TEMP_DIR"/. .
  rm -rf "$TEMP_DIR"
  
  # Only initialize git if it's not already a git repository
  if [ ! -d ".git" ]; then
    echo "Initializing fresh Git repository... / Initialisiere neues Git-Repository..."
    git init
  fi
  
else
  # Initialize in new directory
  if [ -d "$DEST_DIR" ]; then
    echo "Error: Directory '$DEST_DIR' already exists. / Fehler: Verzeichnis '$DEST_DIR' existiert bereits."
    exit 1
  fi
  echo "Cloning template... / Klone Vorlage..."
  git clone --depth 1 https://github.com/dfgsteam/typst-unigoe.git "$DEST_DIR"
  cd "$DEST_DIR"
  echo "Initializing fresh Git repository... / Initialisiere neues Git-Repository..."
  rm -rf .git
  git init
fi

# Make sure setup.py is executable
chmod +x setup.py

echo ""
echo "Starting interactive setup... / Starte interaktive Einrichtung..."
python3 setup.py < /dev/tty
