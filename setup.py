#!/usr/bin/env python3
import sys
import subprocess
import os
import json

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

def escape_quotes(val):
    if not val:
        return val
    return val.replace('"', '\\"')

def get_existing_file(preferred, fallback):
    if os.path.exists(preferred):
        return preferred
    if os.path.exists(fallback):
        return fallback
    return preferred # fallback to default if neither exists

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

    # Load faculties from JSON
    faculties_file = "presets/faculties.json"
    faculties_data = []
    if os.path.exists(faculties_file):
        try:
            with open(faculties_file, "r", encoding="utf-8") as f:
                faculties_data = json.load(f).get("faculties", [])
        except Exception as e:
            print(f"Warning: Could not load faculties.json: {e}")

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

    # 4. University & Faculty / Universität & Fakultät
    print("4. University & Faculty / Universität & Fakultät")
    uni_name = prompt("University name / Name der Universität", "Georg-August-Universität Göttingen")
    
    print("   Choose Faculty/Department or select Custom:")
    print("   Fakultät/Institut auswählen oder eigene Angabe machen:")
    if faculties_data:
        for idx, fac in enumerate(faculties_data, 1):
            fac_name_disp = fac.get("name_de") if lang == "de" else fac.get("name_en")
            print(f"   [{idx}] {fac_name_disp}")
        custom_idx = len(faculties_data) + 1
        print(f"   [{custom_idx}] {'Eigene Angabe / Custom' if lang == 'de' else 'Custom / Eigene Angabe'}")
    else:
        # Fallback if faculties.json is empty or missing
        print("   [1] Institut für Informatik (default)" if lang == "de" else "   [1] Institute of Computer Science (default)")
        print("   [2] Eigene Angabe / Custom" if lang == "de" else "   [2] Custom / Eigene Angabe")
        custom_idx = 2

    fac_choice_str = prompt("Choose faculty / Fakultät wählen", "1")
    try:
        fac_idx = int(fac_choice_str) - 1
    except ValueError:
        fac_idx = -1
        
    is_goe_cs = False
    fac_contact = None
    if faculties_data and 0 <= fac_idx < len(faculties_data):
        selected_fac = faculties_data[fac_idx]
        fac_name = selected_fac.get("name_de") if lang == "de" else selected_fac.get("name_en")
        is_goe_cs = selected_fac.get("is_goe_cs", False)
        contact_lang_key = "contact_de" if lang == "de" else "contact_en"
        fac_contact = selected_fac.get(contact_lang_key)
    elif not faculties_data and fac_choice_str == "1":
        fac_name = "Institut für Informatik" if lang == "de" else "Institute of Computer Science"
        is_goe_cs = True
    else:
        fac_name = prompt("Enter custom faculty/institute / Eigene Fakultät/Institut eingeben")
        is_goe_cs = False
        
    # Göttingen CS Report Series (ISSN) prompt
    include_issn = "n"
    if is_goe_cs and degree_type in ("bachelor", "master") and uni_name == "Georg-August-Universität Göttingen":
        include_issn_choice = prompt("Is this published in the Göttingen Computer Science Report Series? / Wird dies in den Göttinger Schriften zur Informatik veröffentlicht? (y/n)", "n")
        include_issn = include_issn_choice.lower()
        
    city_name = prompt("City / Stadt des Studienortes", "Göttingen")

    print()

    # 5. Contact Info Page / Kontaktseite
    print("5. Contact Info Page / Kontaktseite")
    print("   [1] Include standard contact info (default)")
    print("   [2] Disable contact info page entirely / Kontaktseite deaktivieren")
    print("   [3] Custom contact info / Eigene Kontaktdaten angeben")
    contact_choice = prompt("Choose contact option / Kontakt-Option wählen", "1")
    
    contact_val = ""
    if contact_choice == "1":
        if fac_contact:
            addr = fac_contact.get("address", "").replace("\n", "\\\\ ")
            contact_val = f"""contact: (
      university: "{escape_quotes(uni_name)}",
      address: [{addr}],
      phone: "{escape_quotes(fac_contact.get("phone", ""))}",
      fax: "{escape_quotes(fac_contact.get("fax", ""))}",
      email: "{escape_quotes(fac_contact.get("email", ""))}",
      website: "{escape_quotes(fac_contact.get("website", ""))}",
    ),"""
        else:
            # Standard contact info will be used automatically (merging defaults)
            contact_val = "// contact: none,"
    elif contact_choice == "2":
        contact_val = "contact: none,"
    else:
        print("   Enter custom contact info / Eigene Kontaktdaten eingeben:")
        c_address = prompt("Address / Adresse (e.g. Goldschmidtstraße 7, 37077 Göttingen)", "Goldschmidtstraße 7, 37077 Göttingen, Germany" if lang == "en" else "Goldschmidtstraße 7, 37077 Göttingen, Deutschland")
        c_phone = prompt("Phone / Telefon", "+49 (551) 39-172000")
        c_fax = prompt("Fax", "+49 (551) 39-14403")
        c_email = prompt("Email", "office@informatik.uni-goettingen.de")
        c_website = prompt("Website / Webseite", "www.informatik.uni-goettingen.de")
        
        contact_val = f"""contact: (
      university: "{escape_quotes(uni_name)}",
      address: [{escape_quotes(c_address)}],
      phone: "{escape_quotes(c_phone)}",
      fax: "{escape_quotes(c_fax)}",
      email: "{escape_quotes(c_email)}",
      website: "{escape_quotes(c_website)}",
    ),"""

    print()

    # 6. Meta Details / Projektdaten
    print("6. Meta Details / Projektdaten")
    title = escape_quotes(prompt("Title of the work / Titel der Arbeit"))
    
    subtitle = escape_quotes(prompt("Subtitle / Untertitel (optional, press Enter to skip)", ""))
    subtitle_val = f'"{subtitle}"' if subtitle else "none"

    translated_title = escape_quotes(prompt("Translated Title / Übersetzter Titel (optional, press Enter to skip)", ""))
    trans_title_val = f'"{translated_title}"' if translated_title else "none"

    author = escape_quotes(prompt("Author name / Name des Autors"))
    
    student_id = escape_quotes(prompt("Student ID / Matrikelnummer (optional, press Enter to skip)", ""))
    student_id_val = f'"{student_id}"' if student_id else "none"

    email = escape_quotes(prompt("E-Mail Address / E-Mail (optional, press Enter to skip)", ""))
    email_val = f'"{email}"' if email else "none"

    first_supervisor = escape_quotes(prompt("First Supervisor / Erstbetreuer", "Prof. Dr. Jane Doe"))
    second_supervisor = escape_quotes(prompt("Second Supervisor / Zweitbetreuer (optional, press Enter to skip)", ""))
    second_sup_val = f'"{second_supervisor}"' if second_supervisor else "none"

    if degree_type == "seminar":
        default_course = "Seminar: Advanced Computer Science" if lang == "en" else "Seminar: Fortgeschrittene Informatik"
    else:
        default_course = "Applied Computer Science" if lang == "en" else "Angewandte Informatik"
        
    course_of_study = escape_quotes(prompt("Course of Study or Seminar / Studiengang oder Seminar", default_course))

    print()

    # 7. Draft Mode / Entwurfsmodus
    print("7. Draft Mode / Entwurfsmodus")
    draft_choice = prompt("Enable draft mode (DRAFT watermark & show todo boxes)? / Entwurfsmodus aktivieren (Wasserzeichen & Todos anzeigen)? (y/n)", "n")
    draft = "true" if draft_choice.lower().startswith("y") else "false"

    # 8. Optional Pages and Sections / Optionale Seiten und Abschnitte
    print("8. Optional Pages and Sections / Optionale Seiten und Abschnitte")
    
    # 8a. Standard Declaration of Independence
    # Default: Yes for thesis, No for seminar/expose
    default_decl_opt = "n" if degree_type in ("expose", "seminar") else "y"
    include_decl_choice = prompt("Include a Declaration of Independence? / Selbstständigkeitserklärung einbinden? (y/n)", default_decl_opt)
    include_declaration = include_decl_choice.lower().startswith("y")
    
    declaration_pos = "beginning"
    if include_declaration:
        print("      Position of Declaration of Independence / Position der Selbstständigkeitserklärung:")
        print("      [1] Beginning / Anfang (default)")
        print("      [2] End / Ende")
        decl_pos_choice = prompt("      Choose position / Position wählen", "1")
        declaration_pos = "end" if decl_pos_choice == "2" else "beginning"
        print()
    
    # 8b. AI Declaration (KI-Erklärung)
    # Default: Yes for thesis, No for seminar/expose
    default_ai_opt = "n" if degree_type in ("expose", "seminar") else "y"
    include_ai_choice = prompt("Include a Declaration on the use of AI? / Erklärung zur KI-Nutzung einbinden? (y/n)", default_ai_opt)
    include_ai_decl = include_ai_choice.lower().startswith("y")
    
    declaration_ai_pos = "beginning"
    if include_ai_decl:
        print("      Position of AI Declaration / Position der Erklärung zur KI-Nutzung:")
        print("      [1] Beginning / Anfang (default)")
        print("      [2] End / Ende")
        ai_pos_choice = prompt("      Choose position / Position wählen", "1")
        declaration_ai_pos = "end" if ai_pos_choice == "2" else "beginning"
        print()
    
    # 8c. Bibliography (Literaturverzeichnis)
    # Default: Yes
    include_bibliography = prompt("Include a Bibliography? / Literaturverzeichnis einbinden? (y/n)", "y").lower().startswith("y")
    
    bib_file_val = "none"
    bib_style_val = "ieee"
    if include_bibliography:
        print("      * Tip: You can auto-sync Zotero using the 'Better BibLaTeX' format and 'Keep updated' option!")
        bib_file = prompt("Bibliography file path / Pfad zur Literaturdatenbank", "content/references.bib")
        bib_style = prompt("Bibliography style / Zitierstil (e.g. ieee, apa, mla, chicago)", "ieee")
        bib_file_val = f'"{escape_quotes(bib_file)}"'
        bib_style_val = f'"{escape_quotes(bib_style)}"'
        
    # 8d. Appendix (Anhang)
    # Default: No
    include_appendix = prompt("Include an Appendix? / Anhang einbinden? (y/n)", "n").lower().startswith("y")
    
    app_file_val = "none"
    if include_appendix:
        preferred_app = "content/appendix.typ"
        app_file = prompt("Appendix file path / Pfad zur Anhangsdatei", preferred_app)
        app_file_val = f'include "{escape_quotes(app_file)}"'
        
    # 8e. Table of Contents Roman page inclusion
    # Default: No
    include_roman_choice = prompt("Include introductory pages (Declaration, Abstract, Acronyms) in Table of Contents? / Einleitende Seiten (Erklärung, Zusammenfassung, Abkürzungen) im Inhaltsverzeichnis aufführen? (y/n)", "n")
    outline_roman_pages = "true" if include_roman_choice.lower().startswith("y") else "false"
    
    # 8f. List of Figures & List of Tables (Abbildungs- und Tabellenverzeichnis)
    # Default: No
    figures_choice = prompt("Include a List of Figures? / Abbildungsverzeichnis einbinden? (y/n)", "n")
    show_list_of_figures = "true" if figures_choice.lower().startswith("y") else "false"
    
    tables_choice = prompt("Include a List of Tables? / Tabellenverzeichnis einbinden? (y/n)", "n")
    show_list_of_tables = "true" if tables_choice.lower().startswith("y") else "false"
    
    # 8g. GitHub Actions CI/CD Pipeline
    # Default: Yes for thesis, No for seminar/expose
    default_pipeline_opt = "n" if degree_type in ("expose", "seminar") else "y"
    include_pipeline_choice = prompt("Include GitHub Actions CI/CD release pipeline? (Auto-builds & releases PDF on version tags like v1.0) / GitHub Actions CI/CD Release-Pipeline einbinden? (y/n)", default_pipeline_opt)
    include_pipeline = include_pipeline_choice.lower().startswith("y")

    print()

    if os.path.exists("main.typ"):
        overwrite = prompt("main.typ already exists. Overwrite? / main.typ existiert bereits. Überschreiben? (y/n)", "y")
        if not overwrite.lower().startswith("y"):
            print("Aborted. No files were changed. / Abgebrochen. Es wurden keine Dateien geändert.")
            sys.exit(0)

    print("Generating main.typ... / Erstelle main.typ...")

    # Determine abstract and declaration defaults with robust file presence checking
    preferred_abstract = "content/abstract_de.typ" if lang == "de" else "content/abstract.typ"
    fallback_abstract = "content/abstract.typ" if lang == "de" else "content/abstract_de.typ"
    abstract_file = get_existing_file(preferred_abstract, fallback_abstract)

    preferred_decl = "content/declaration_de.typ" if lang == "de" else "content/declaration.typ"
    fallback_decl = "content/declaration.typ" if lang == "de" else "content/declaration_de.typ"
    declaration_file = get_existing_file(preferred_decl, fallback_decl)

    preferred_ai = "content/declaration_ai_de.typ" if lang == "de" else "content/declaration_ai.typ"
    fallback_ai = "content/declaration_ai.typ" if lang == "de" else "content/declaration_ai_de.typ"
    declaration_ai_file = get_existing_file(preferred_ai, fallback_ai)

    preferred_content = "content/content_de.typ" if lang == "de" else "content/content.typ"
    fallback_content = "content/content.typ" if lang == "de" else "content/content_de.typ"
    content_file = get_existing_file(preferred_content, fallback_content)

    # For exposé, declaration is usually none and outline false by default
    outline_val = "show_outline: false," if degree_type == "expose" else "// show_outline: true,"

    declaration_val = f'include "{declaration_file}"' if include_declaration else "none"
    declaration_ai_val = f'include "{declaration_ai_file}"' if include_ai_decl else "none"

    if include_bibliography:
        bibliography_val = f'bibliography({bib_file_val}, style: {bib_style_val}, title: none)'
    else:
        bibliography_val = "none"

    # Build translations override if they diverge from default CS Göttingen preset
    translations_override_lines = []
    translations_override_lines.append(f'      institution: "{escape_quotes(fac_name)}",')
    if include_issn.startswith("y"):
        uni_val = f'      university: "Bachelor- und Masterarbeiten\\\\nan der Georg-August-Universität Göttingen\\\\nISSN 1612-6793",' if lang == "de" else f'      university: "Bachelor\'s and Master\'s Theses\\\\nat Georg-August-Universität Göttingen\\\\nISSN 1612-6793",'
    else:
        uni_val = f'      university: "{escape_quotes(uni_name)}",'
    translations_override_lines.append(uni_val)
    translations_override_lines.append(f'      city: "{escape_quotes(city_name)}",')
    translations_override_str = "\n".join(translations_override_lines)

    main_content = f"""#import "/lib/thesis.typ": thesis, todo, acr

#thesis(
  config: (
    
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
    
    // Custom Logo (Default: "/images/ugo-logo.svg")
    // Set to none to hide the logo, or specify an absolute path to a custom SVG/JPG/PNG
    // logo: "/images/ugo-logo.svg", 
    // logo_width: 6.5cm,
    
    // Custom Outline / Table of Contents
    // Set to false to hide the outline page completely (e.g. for exposés or short papers)
    {outline_val}
    
    // Platzierung der Selbstständigkeits- und KI-Erklärung ("beginning" oder "end")
    declaration_position: "{declaration_pos}",
    declaration_ai_position: "{declaration_ai_pos}",
    
    // Sollen einleitende römische Seiten im Inhaltsverzeichnis aufgeführt werden?
    outline_roman_pages: {outline_roman_pages},
    
    // Abbildungs- und Tabellenverzeichnis (List of Figures & List of Tables)
    show_list_of_figures: {show_list_of_figures},
    show_list_of_tables: {show_list_of_tables},
    
    // Custom Translations / Branding override (Dynamically configured)
    translations: (
{translations_override_str}
    ),
    
    // Custom Contact Page (Optional & Dynamic)
    {contact_val}
  ),
  
  // Abstract / Zusammenfassung
  // Can also be a dictionary for dual-language abstracts: (de: include "...", en: include "...")
  abstract: include "{abstract_file}",
  
  // Declaration of independence (Set to none to omit it entirely, e.g. for seminar papers or exposés)
  declaration: {declaration_val},

  // Declaration on the use of AI / Erklärung zur Verwendung von KI (Set to none to omit it entirely)
  declaration_ai: {declaration_ai_val},

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
  bibliography: {bibliography_val},
  
  // Appendix (Set to none to omit it)
  appendix: {app_file_val},
)
"""

    with open("main.typ", "w", encoding="utf-8") as f:
        f.write(main_content)

    # Handle GitHub Actions CI/CD release pipeline creation/deletion
    if include_pipeline:
        os.makedirs(".github/workflows", exist_ok=True)
        pipeline_content = """name: Build and Release Typst PDFs

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Typst
        uses: typst-community/setup-typst@v3

      - name: Compile PDF Documents
        run: |
          make build
          if [ -f example.typ ]; then
            make build-example
          fi

      - name: Create GitHub Release and Upload Assets
        uses: softprops/action-gh-release@v2
        with:
          files: |
            main.pdf
            example.pdf
          fail_on_unmatched_files: false
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""
        with open(".github/workflows/release.yml", "w", encoding="utf-8") as f:
            f.write(pipeline_content)
        print("Created GitHub Actions release pipeline. / GitHub Actions Release-Pipeline wurde erstellt.")
    else:
        # If they chose not to include the pipeline, we can safely delete release.yml if it exists
        if os.path.exists(".github/workflows/release.yml"):
            try:
                os.remove(".github/workflows/release.yml")
                # Clean up empty directories
                if not os.listdir(".github/workflows"):
                    os.rmdir(".github/workflows")
                if not os.listdir(".github"):
                    os.rmdir(".github")
                print("Removed GitHub Actions release pipeline. / GitHub Actions Release-Pipeline wurde entfernt.")
            except Exception:
                pass

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
