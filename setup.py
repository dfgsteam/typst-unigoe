#!/usr/bin/env python3
import sys
import subprocess
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt(text, default=None):
    if default is not None:
        try:
            val = input(f"{text} [{default}]: ").strip()
            return val if val else default
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            sys.exit(0)
    else:
        try:
            while True:
                val = input(f"{text}: ").strip()
                if val:
                    return val
                print("This field is required. / Dieses Feld ist erforderlich.")
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            sys.exit(0)

def main():
    clear_screen()
    print("=========================================================")
    print("    Typst Georg-August-Universität Göttingen Setup       ")
    print("        Thesis - Seminar Paper - Exposé Template        ")
    print("=========================================================")
    print()
    print("This script will configure your project by generating a customized 'main.typ'.")
    print("Dieses Skript konfiguriert dein Projekt durch Erstellen einer angepassten 'main.typ'.")
    print()

    # 1. Language
    print("1. Language / Sprache")
    print("   [1] German / Deutsch (default)")
    print("   [2] English / Englisch")
    lang_choice = prompt("Choose language / Sprache wählen", "1")
    lang = "de" if lang_choice == "1" else "en"
    
    print()

    # 2. Document Type
    print("2. Document Type / Dokumenttyp")
    print("   [1] Master's Thesis / Masterarbeit (default)")
    print("   [2] Bachelor's Thesis / Bachelorarbeit")
    print("   [3] Seminar Paper / Seminararbeit")
    print("   [4] Exposé")
    doc_choice = prompt("Choose document type / Dokumenttyp", "1")
    
    degree_type = "master"
    if doc_choice == "2":
        degree_type = "bachelor"
    elif doc_choice == "3":
        degree_type = "seminar"
    elif doc_choice == "4":
        degree_type = "expose"

    print()

    # Resolve preset name
    preset_name = f"{lang}_{degree_type}"

    # 3. Styling Style
    print("3. Style / Design-Typ")
    print("   [1] Modern (clean, screen-optimized, default)")
    print("   [2] Legacy (classic double-sided book/LaTeX style)")
    style_choice = prompt("Choose style / Design wählen", "1")
    style = "modern" if style_choice == "1" else "legacy"

    print()

    # 4. Meta Details
    print("4. Meta Details / Projektdaten")
    title = prompt("Title of the work / Titel der Arbeit")
    
    subtitle = prompt("Subtitle / Untertitel (optional, press Enter to skip)", "")
    subtitle_val = f'"{subtitle}"' if subtitle else "none"

    translated_title = prompt("Translated Title / Übersetzter Titel (optional, press Enter to skip)", "")
    trans_title_val = f'"{translated_title}"' if translated_title else "none"

    author = prompt("Author name / Name des Autors")
    
    student_id = prompt("Student ID / Matrikelnummer (optional, press Enter to skip)", "")
    student_id_val = f'"{student_id}"' if student_id else "none"

    email = prompt("E-Mail Address / E-Mail (optional, press Enter to skip)", "")
    email_val = f'"{email}"' if email else "none"

    first_supervisor = prompt("First Supervisor / Erstbetreuer", "Prof. Dr. Jane Doe")
    second_supervisor = prompt("Second Supervisor / Zweitbetreuer (optional, press Enter to skip)", "")
    second_sup_val = f'"{second_supervisor}"' if second_supervisor else "none"

    if degree_type == "seminar":
        default_course = "Seminar: Advanced Computer Science" if lang == "en" else "Seminar: Fortgeschrittene Informatik"
    else:
        default_course = "Applied Computer Science" if lang == "en" else "Angewandte Informatik"
        
    course_of_study = prompt("Course of Study or Seminar / Studiengang oder Seminar", default_course)

    print()

    # 5. Draft Mode
    print("5. Draft Mode / Entwurfsmodus")
    draft_choice = prompt("Enable draft mode (DRAFT watermark & show todo boxes)? / Entwurfsmodus aktivieren (Wasserzeichen & Todos anzeigen)? (y/n)", "n")
    draft = "true" if draft_choice.lower().startswith("y") else "false"

    print()
    if os.path.exists("main.typ"):
        overwrite = prompt("main.typ already exists. Overwrite? / main.typ existiert bereits. Überschreiben? (y/n)", "y")
        if not overwrite.lower().startswith("y"):
            print("Aborted. No files were changed. / Abgebrochen. Es wurden keine Dateien geändert.")
            sys.exit(0)

    print("Generating main.typ... / Erstelle main.typ...")

    # Determine abstract and declaration defaults
    abstract_file = "content/abstract_de.typ" if lang == "de" else "content/abstract.typ"
    declaration_file = "content/declaration_de.typ" if lang == "de" else "content/declaration.typ"
    content_file = "content/content_de.typ" if lang == "de" else "content/content.typ"

    # For exposé, declaration is usually none
    if degree_type == "expose":
        declaration_val = "none"
        outline_val = "show_outline: false,"
    else:
        declaration_val = f'include "{declaration_file}"'
        outline_val = "// show_outline: true,"

    main_content = f"""#import "/lib/thesis.typ": thesis, todo, acr
#import "/lib/presets.typ"

#thesis(
  config: (
    ..presets.{preset_name},
    
    // Core details
    title: "{title}",
    subtitle: {subtitle_val},
    translated_title: {trans_title_val},
    author: "{author}",
    student_id: {student_id_val},
    author_email: {email_val},
    date: none, // Set to none for today's date, or specify a custom date string (e.g. "2026-05-24")
    firstsupervisor: "{first_supervisor}",
    secondsupervisor: {second_sup_val},
    degree_type: "{degree_type}",
    lang: "{lang}",
    course_of_study: "{course_of_study}",
    style: "{style}",
    
    // --- Advanced Customization Options (Dynamic Customization) ---
    
    // Draft Mode (Set to true to show a DRAFT watermark and render all #todo() boxes)
    draft: {draft},
    
    // Custom Logo (Default: "/images/goe-logo.jpg")
    // Set to none to hide the logo, or specify an absolute path to a custom SVG/JPG/PNG
    // logo: "/images/goe-logo.jpg", 
    // logo_width: 6.5cm,
    
    // Custom Outline / Table of Contents
    // Set to false to hide the outline page completely (e.g. for exposés or short papers)
    {outline_val}
    
    // Custom Translations / Branding override
    // You can override individual preset fields without redefining the whole preset!
    // translations: (
    //   institution: "Institute of Computer Science",
    //   university: "Georg-August-Universität Göttingen",
    //   city: "Göttingen",
    // ),
    
    // Custom Contact Page (Optional & Dynamic)
    // Set contact to none to disable the contact info page entirely, or override specific fields:
    // contact: (
    //   university: "Georg-August-Universität Göttingen",
    //   address: [Goldschmidtstraße 7\\ 37077 Göttingen\\ Germany],
    //   phone: "+49 (551) 39-172000",
    //   fax: "+49 (551) 39-14403",
    //   email: "office@informatik.uni-goettingen.de",
    //   website: "www.informatik.uni-goettingen.de",
    // ),
  ),
  
  // Abstract / Zusammenfassung
  // Can also be a dictionary for dual-language abstracts: (de: include "...", en: include "...")
  abstract: include "{abstract_file}",
  
  // Declaration of independence (Set to none to omit it entirely, e.g. for seminar papers or exposés)
  declaration: {declaration_val},

  // Acronyms dictionary (optional)
  // Define your acronyms here: (Key: (English definition, German definition))
  // acronyms: (
  //   API: ("Application Programming Interface", "Schnittstelle zur Anwendungsprogrammierung"),
  //   REST: ("Representational State Transfer", "Zustandsloser Architekturstil"),
  // ),
  
  // Chapters of your document
  chapters: (
    include "{content_file}",
  ),
  
  // Bibliography (Set to none to omit it)
  bibliography: bibliography(
    "content/references.bib",
    style: "ieee",
    title: none,
  ),
  
  // Appendix (Set to none to omit it)
  // appendix: include "content/appendix.typ",
)
"""

    with open("main.typ", "w", encoding="utf-8") as f:
        f.write(main_content)

    print("Success! 'main.typ' has been configured successfully. / Erfolg! 'main.typ' wurde erfolgreich konfiguriert.")
    print()

    # 6. Build compilation option
    build_now = prompt("Would you like to compile your document now? / Möchtest du dein Dokument jetzt übersetzen? (y/n)", "y")
    if build_now.lower().startswith("y"):
        print("Compiling document via 'make build'... / Übersetze Dokument mit 'make build'...")
        try:
            result = subprocess.run(["make", "build"], capture_output=True, text=True)
            if result.returncode == 0:
                print("Compilation successful! 'main.pdf' has been generated. / Übersetzung erfolgreich! 'main.pdf' wurde erstellt.")
            else:
                print("Compilation failed. Error: / Übersetzung fehlgeschlagen. Fehler:")
                print(result.stderr)
        except Exception as e:
            print(f"Could not run make build. Error: / Fehler beim Ausführen von make build: {e}")

if __name__ == "__main__":
    main()
