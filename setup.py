#!/usr/bin/env python3
import sys
import subprocess
import os
import json
import shutil

# Resolve template root directory (handles setups inside subfolders like expose, seminar, presentation)
def find_template_root():
    current = os.getcwd()
    # Check current directory
    if os.path.exists(os.path.join(current, "lib")) and os.path.exists(os.path.join(current, "presets")):
        return "."
    # Check parent directory
    parent = os.path.dirname(current)
    if os.path.exists(os.path.join(parent, "lib")) and os.path.exists(os.path.join(parent, "presets")):
        return ".."
    # Check grandparent directory
    grandparent = os.path.dirname(parent)
    if os.path.exists(os.path.join(grandparent, "lib")) and os.path.exists(os.path.join(grandparent, "presets")):
        return "../.."
    return "."

template_root = find_template_root()
path_prefix = "" if template_root == "." else template_root + "/"
lib_path = f"{path_prefix}lib/thesis.typ" if template_root != "." else "/lib/thesis.typ"
pres_lib_path = f"{path_prefix}lib/presentation.typ" if template_root != "." else "/lib/presentation.typ"
logo_path_default = f"{path_prefix}images/ugo-logo.svg" if template_root != "." else "/images/ugo-logo.svg"

def copy_template_file(src_name, dest_name=None):
    if dest_name is None:
        dest_name = src_name
    
    src_path = os.path.join(template_root, src_name)
    dest_path = os.path.join(".", dest_name)
    
    if os.path.exists(src_path):
        # Create destination directories if they don't exist
        dest_dir = os.path.dirname(dest_path)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)
        
        # If destination file already exists, don't overwrite it
        if not os.path.exists(dest_path):
            try:
                shutil.copy2(src_path, dest_path)
                print(f"Copied template / Vorlage kopiert: {src_name} -> {dest_name}")
            except Exception as e:
                print(f"Warning: Could not copy {src_name} to {dest_name}: {e}")


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

def read_config_from_main():
    defaults = {
        "title": "Titel der Präsentation / Presentation Title",
        "subtitle": "Verteidigung der Abschlussarbeit / Thesis Defense",
        "author": "Vorname Nachname",
        "institute": "Institut für Informatik",
        "university": "Georg-August-Universität Göttingen",
        "lang": "de"
    }
    if not os.path.exists("main.typ"):
        return defaults
    
    try:
        with open("main.typ", "r", encoding="utf-8") as f:
            content = f.read()
            
        import re
        # Parse fields from the config block
        title_match = re.search(r'title:\s*"([^"]+)"', content)
        if title_match:
            defaults["title"] = title_match.group(1)
            
        subtitle_match = re.search(r'subtitle:\s*"([^"]+)"', content)
        if subtitle_match:
            defaults["subtitle"] = subtitle_match.group(1)
            
        author_match = re.search(r'author:\s*"([^"]+)"', content)
        if author_match:
            defaults["author"] = author_match.group(1)
            
        lang_match = re.search(r'lang:\s*"([^"]+)"', content)
        if lang_match:
            defaults["lang"] = lang_match.group(1)
            
        # Try to parse institution from translations if available
        inst_match = re.search(r'institution:\s*"([^"]+)"', content)
        if inst_match:
            defaults["institute"] = inst_match.group(1)
        else:
            if defaults["lang"] == "de":
                defaults["institute"] = "Institut für Informatik"
            else:
                defaults["institute"] = "Institute of Computer Science"
                
        uni_match = re.search(r'university:\s*"([^"]+)"', content)
        if uni_match:
            defaults["university"] = uni_match.group(1).replace("\\\\n", "\n").replace("\\n", "\n")
            
    except Exception:
        pass
        
    return defaults

def run_presentation_only():
    clear_screen()
    print("=========================================================")
    print("    Typst Georg-August-Universität Göttingen Setup       ")
    print("        Presentation Slide Deck Setup Only              ")
    print("=========================================================")
    print()
    print("This will configure and generate your defense 'presentation.typ' slide deck.")
    print("Dies konfiguriert und erstellt deinen Vortrags-Foliensatz 'presentation.typ'.")
    print()
    
    defaults = read_config_from_main()
    
    lang_choice = prompt("Language / Sprache ([1] German/Deutsch, [2] English/Englisch)", "1" if defaults["lang"] == "de" else "2")
    lang = "de" if lang_choice == "1" else "en"
    
    title = escape_quotes(prompt("Presentation Title / Titel der Präsentation", defaults["title"]))
    subtitle = escape_quotes(prompt("Subtitle / Untertitel", defaults["subtitle"]))
    author = escape_quotes(prompt("Author / Autor", defaults["author"]))
    institute = escape_quotes(prompt("Institute/Faculty / Institut/Fakultät", defaults["institute"]))
    university = escape_quotes(prompt("University / Universität", defaults["university"]))
    
    date_val = prompt("Date / Datum (press Enter for today / Eingabetaste für heute)", "none")
    
    if os.path.exists("presentation.typ"):
        overwrite = prompt("presentation.typ already exists. Overwrite? / presentation.typ existiert bereits. Überschreiben? (y/n)", "y")
        if not overwrite.lower().startswith("y"):
            print("Aborted. No files were changed.")
            sys.exit(0)
            
    pres_content = f"""#import "{pres_lib_path}": presentation, slide

#show: presentation.with(
  title: "{title}",
  subtitle: "{subtitle}",
  author: "{author}",
  institute: "{institute}",
  university: "{university}",
  date: {"none" if date_val == "none" else f'"{escape_quotes(date_val)}"'},
  logo: "{logo_path_default}",
  lang: "{lang}",
)

#slide(title: "Einleitung & Motivation")[
  - *Herausforderung*: Kurze Zusammenfassung der Problemstellung deiner Arbeit.
  - *Zielsetzung*: Was wolltest du mit deiner Arbeit erreichen?
  - *Relevanz*: Warum ist dieses Thema wichtig und wer profitiert davon?
]

#slide(title: "Wissenschaftlicher Beitrag / Kernidee")[
  - *Lösungsansatz*: Wie hast du das Problem gelöst?
  - *Methodik*: Welche wissenschaftlichen Methoden hast du angewendet?
  - *Implementierung*: Kurzer Überblick über deine praktische Arbeit (falls vorhanden).
]

#slide(title: "Evaluation & Ergebnisse")[
  - *Versuchsaufbau*: Wie hast du deine Lösung getestet?
  - *Ergebnisse*: Was sind die wichtigsten Erkenntnisse deiner Arbeit?
  - *Diskussion*: Welche Limitationen oder Sonderfälle gibt es?
]

#slide(title: "Fazit & Ausblick")[
  - *Zusammenfassung*: Das Wichtigste auf den Punkt gebracht.
  - *Ausblick*: Was könnte man als nächstes erforschen?
  - *Fragen*: Ich bedanke mich für Ihre Aufmerksamkeit und freue mich auf Ihre Fragen!
]
"""
    with open("presentation.typ", "w", encoding="utf-8") as f:
        f.write(pres_content)
    print()
    print("Created defense slide deck template. / Foliensatz-Vorlage für die Verteidigung wurde erstellt.")
    print()
    
    build_now = prompt("Would you like to compile your presentation now? / Möchtest du deine Präsentation jetzt übersetzen? (y/n)", "y")
    if build_now.lower().startswith("y"):
        print("Compiling presentation via 'make build-presentation'...")
        try:
            result = subprocess.run(["make", "build-presentation"], capture_output=True, text=True)
            if result.returncode == 0:
                print("Compilation successful! 'presentation.pdf' has been generated. / Übersetzung erfolgreich! 'presentation.pdf' wurde erstellt.")
            else:
                print("Compilation failed. Error: / Übersetzung fehlgeschlagen. Fehler:")
                print(result.stderr)
        except Exception as e:
            print(f"Could not run make build-presentation. Error: / Fehler beim Ausführen von make build-presentation: {e}")
    sys.exit(0)

def main():
    clear_screen()
    print("=========================================================")
    print("    Typst Georg-August-Universität Göttingen Setup       ")
    print("=========================================================")
    print()
    print("What would you like to configure? / Was möchtest du einrichten?")
    print("   [1] Thesis, Seminar Paper, or Exposé (default)")
    print("   [2] Standalone Presentation Slide Deck / Nur Foliensatz (Verteidigung)")
    choice = prompt("Choose setup option / Option wählen", "1")
    
    if choice == "2":
        run_presentation_only()
        return

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
    faculties_file = os.path.join(template_root, "presets/faculties.json")
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
    
    # 8a. Abstract / Zusammenfassung
    # Default: No for expose, Yes for others
    default_abstract_opt = "n" if degree_type == "expose" else "y"
    include_abstract_choice = prompt("Include an Abstract? / Zusammenfassung einbinden? (y/n)", default_abstract_opt)
    include_abstract = include_abstract_choice.lower().startswith("y")
    print()

    # 8b. Standard Declaration of Independence
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
    
    # 8c. AI Declaration (KI-Erklärung)
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
    
    # 8d. Bibliography (Literaturverzeichnis)
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
        
    # 8e. Appendix (Anhang)
    # Default: No
    include_appendix = prompt("Include an Appendix? / Anhang einbinden? (y/n)", "n").lower().startswith("y")
    
    app_file_val = "none"
    if include_appendix:
        preferred_app = "content/appendix.typ"
        app_file = prompt("Appendix file path / Pfad zur Anhangsdatei", preferred_app)
        app_file_val = f'include "{escape_quotes(app_file)}"'
        
    # 8f. Table of Contents Roman page inclusion
    # Default: No
    include_roman_choice = prompt("Include introductory pages (Declaration, Abstract, Acronyms) in Table of Contents? / Einleitende Seiten (Erklärung, Zusammenfassung, Abkürzungen) im Inhaltsverzeichnis aufführen? (y/n)", "n")
    outline_roman_pages = "true" if include_roman_choice.lower().startswith("y") else "false"
    
    # 8g. List of Figures & List of Tables (Abbildungs- und Tabellenverzeichnis)
    # Default: No
    figures_choice = prompt("Include a List of Figures? / Abbildungsverzeichnis einbinden? (y/n)", "n")
    show_list_of_figures = "true" if figures_choice.lower().startswith("y") else "false"
    
    tables_choice = prompt("Include a List of Tables? / Tabellenverzeichnis einbinden? (y/n)", "n")
    show_list_of_tables = "true" if tables_choice.lower().startswith("y") else "false"
    
    # 8h. GitHub Actions CI/CD Pipeline
    # Default: Yes for thesis, No for seminar/expose
    default_pipeline_opt = "n" if degree_type in ("expose", "seminar") else "y"
    include_pipeline_choice = prompt("Include GitHub Actions CI/CD release pipeline? (Auto-builds & releases PDF on version tags like v1.0) / GitHub Actions CI/CD Release-Pipeline einbinden? (y/n)", default_pipeline_opt)
    include_pipeline = include_pipeline_choice.lower().startswith("y")
    
    # 8i. Presentation Slides (Verteidigungspräsentation)
    # Default: Yes for thesis, No for seminar/expose
    default_pres_opt = "n" if degree_type in ("expose", "seminar") else "y"
    include_pres_choice = prompt("Include a Göttingen-branded Slide Deck for your defense? / Foliensatz für die Verteidigung einbinden? (y/n)", default_pres_opt)
    include_presentation = include_pres_choice.lower().startswith("y")

    print()

    if os.path.exists("main.typ"):
        overwrite = prompt("main.typ already exists. Overwrite? / main.typ existiert bereits. Überschreiben? (y/n)", "y")
        if not overwrite.lower().startswith("y"):
            print("Aborted. No files were changed. / Abgebrochen. Es wurden keine Dateien geändert.")
            sys.exit(0)

    print("Generating main.typ... / Erstelle main.typ...")

    # Determine abstract and declaration defaults with robust file presence checking
    if include_abstract:
        preferred_abstract = "content/abstract_de.typ" if lang == "de" else "content/abstract.typ"
        fallback_abstract = "content/abstract.typ" if lang == "de" else "content/abstract_de.typ"
        src_abstract = get_existing_file(os.path.join(template_root, preferred_abstract), os.path.join(template_root, fallback_abstract))
        abstract_basename = os.path.basename(src_abstract)
        local_abstract_path = os.path.join("content", abstract_basename)
        copy_template_file(os.path.relpath(src_abstract, template_root), local_abstract_path)
        abstract_val = f'include "{local_abstract_path}"'
    else:
        abstract_val = "none"

    preferred_decl = "content/declaration_de.typ" if lang == "de" else "content/declaration.typ"
    fallback_decl = "content/declaration.typ" if lang == "de" else "content/declaration_de.typ"
    src_decl = get_existing_file(os.path.join(template_root, preferred_decl), os.path.join(template_root, fallback_decl))
    decl_basename = os.path.basename(src_decl)
    local_decl_path = os.path.join("content", decl_basename)
    copy_template_file(os.path.relpath(src_decl, template_root), local_decl_path)
    declaration_val = f'include "{local_decl_path}"' if include_declaration else "none"

    preferred_ai = "content/declaration_ai_de.typ" if lang == "de" else "content/declaration_ai.typ"
    fallback_ai = "content/declaration_ai.typ" if lang == "de" else "content/declaration_ai_de.typ"
    src_ai = get_existing_file(os.path.join(template_root, preferred_ai), os.path.join(template_root, fallback_ai))
    ai_basename = os.path.basename(src_ai)
    local_ai_path = os.path.join("content", ai_basename)
    copy_template_file(os.path.relpath(src_ai, template_root), local_ai_path)
    declaration_ai_val = f'include "{local_ai_path}"' if include_ai_decl else "none"

    preferred_content = "content/content_de.typ" if lang == "de" else "content/content.typ"
    fallback_content = "content/content.typ" if lang == "de" else "content/content_de.typ"
    src_content = get_existing_file(os.path.join(template_root, preferred_content), os.path.join(template_root, fallback_content))
    content_basename = os.path.basename(src_content)
    local_content_path = os.path.join("content", content_basename)
    copy_template_file(os.path.relpath(src_content, template_root), local_content_path)

    # For exposé, declaration is usually none and outline false by default
    outline_val = "show_outline: false," if degree_type == "expose" else "// show_outline: true,"

    if include_bibliography:
        local_bib_path = os.path.join("content", "references.bib")
        copy_template_file("content/references.bib", local_bib_path)
        bibliography_val = f'bibliography("{local_bib_path}", style: {bib_style_val}, title: none)'
    else:
        bibliography_val = "none"

    if include_appendix:
        local_app_path = os.path.join("content", "appendix.typ")
        copy_template_file("content/appendix.typ", local_app_path)
        app_file_val = f'include "{local_app_path}"'


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

    main_content = f"""#import "{lib_path}": thesis, todo, acr

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
    
    // Custom Logo (Default: "{logo_path_default}")
    // Set to none to hide the logo, or specify an absolute path to a custom SVG/JPG/PNG
    // logo: "{logo_path_default}", 
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
  abstract: {abstract_val},
  
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
          if [ -f presentation.typ ]; then
            make build-presentation
          fi

      - name: Create GitHub Release and Upload Assets
        uses: softprops/action-gh-release@v2
        with:
          files: |
            main.pdf
            example.pdf
            presentation.pdf
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

    # Handle Presentation Slide Deck creation/deletion
    if include_presentation:
        pres_content = f"""#import "{pres_lib_path}": presentation, slide

#show: presentation.with(
  title: "{title}",
  subtitle: "Verteidigung der Abschlussarbeit / Thesis Defense",
  author: "{author}",
  institute: "{fac_name}",
  university: "{uni_name}",
  date: none, // Set to none for today's date
  logo: "{logo_path_default}",
  lang: "{lang}",
)

#slide(title: "Einleitung & Motivation")[
  - *Herausforderung*: Kurze Zusammenfassung der Problemstellung deiner Arbeit.
  - *Zielsetzung*: Was wolltest du mit deiner Arbeit erreichen?
  - *Relevanz*: Warum ist dieses Thema wichtig und wer profitiert davon?
]

#slide(title: "Wissenschaftlicher Beitrag / Kernidee")[
  - *Lösungsansatz*: Wie hast du das Problem gelöst?
  - *Methodik*: Welche wissenschaftlichen Methoden hast du angewendet?
  - *Implementierung*: Kurzer Überblick über deine praktische Arbeit (falls vorhanden).
]

#slide(title: "Evaluation & Ergebnisse")[
  - *Versuchsaufbau*: Wie hast du deine Lösung getestet?
  - *Ergebnisse*: Was sind die wichtigsten Erkenntnisse deiner Arbeit?
  - *Diskussion*: Welche Limitationen oder Sonderfälle gibt es?
]

#slide(title: "Fazit & Ausblick")[
  - *Zusammenfassung*: Das Wichtigste auf den Punkt gebracht.
  - *Ausblick*: Was könnte man als nächstes erforschen?
  - *Fragen*: Ich bedanke mich für Ihre Aufmerksamkeit und freue mich auf Ihre Fragen!
]
"""
        with open("presentation.typ", "w", encoding="utf-8") as f:
            f.write(pres_content)
        print("Created defense slide deck template. / Foliensatz-Vorlage für die Verteidigung wurde erstellt.")
    else:
        if os.path.exists("presentation.typ"):
            try:
                os.remove("presentation.typ")
                print("Removed defense slide deck template. / Foliensatz-Vorlage wurde entfernt.")
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

    print()
    
    # 7. Cleanup template files / Bereinigung der Vorlagendateien
    cleanup_choice = prompt("Clean up template files? (Deletes setup.py, init.sh, example.typ, example.pdf, content/template.typ, and unused presets/content files) / Vorlagendateien bereinigen? (Löscht setup.py, init.sh, example.typ, example.pdf, content/template.typ sowie ungenutzte Vorlagen/Inhalte) (y/n)", "y")
    if cleanup_choice.lower().startswith("y"):
        print("Cleaning up template files... / Bereinige Vorlagendateien...")
        files_to_delete = [
            "init.sh",
            "example.typ",
            "example.pdf",
            "content/template.typ"
        ]
        
        # Unused content files depending on choices, language, and degree type
        
        # 1. Abstract
        if not include_abstract or degree_type == "expose":
            files_to_delete.extend(["content/abstract.typ", "content/abstract_de.typ"])
        else:
            # Delete the abstract in the other language
            if lang == "de":
                files_to_delete.append("content/abstract.typ")
            else:
                files_to_delete.append("content/abstract_de.typ")
                
        # 2. Declaration of Independence
        if not include_declaration or degree_type == "expose":
            files_to_delete.extend(["content/declaration.typ", "content/declaration_de.typ"])
        else:
            # Delete the declaration in the other language
            if lang == "de":
                files_to_delete.append("content/declaration.typ")
            else:
                files_to_delete.append("content/declaration_de.typ")

        # 3. AI Declaration
        if not include_ai_decl:
            files_to_delete.extend(["content/declaration_ai.typ", "content/declaration_ai_de.typ"])
        else:
            # Delete the AI declaration in the other language
            if lang == "de":
                files_to_delete.append("content/declaration_ai.typ")
            else:
                files_to_delete.append("content/declaration_ai_de.typ")
                
        # 4. Appendix
        if not include_appendix:
            files_to_delete.append("content/appendix.typ")
            
        # 5. Bibliography
        if not include_bibliography:
            files_to_delete.append("content/references.bib")

        # 6. Presentation
        if not include_presentation:
            files_to_delete.extend(["presentation.typ", "presentation.pdf", "lib/presentation.typ"])

        # 7. Unused language-specific main content template
        if lang == "de":
            files_to_delete.append("content/content.typ")
        else:
            files_to_delete.append("content/content_de.typ")

        for filename in files_to_delete:
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                    print(f"Deleted / Gelöscht: {filename}")
                except Exception as e:
                    print(f"Could not delete / Fehler beim Löschen von {filename}: {e}")
                    
        # Delete unused preset JSON files (only if local to the setup)
        if template_root == ".":
            active_preset = f"{lang}_{degree_type}.json"
            presets_dir = "presets"
            if os.path.exists(presets_dir):
                try:
                    for f in os.listdir(presets_dir):
                        if f.endswith(".json") and f != active_preset:
                            path = os.path.join(presets_dir, f)
                            os.remove(path)
                            print(f"Deleted unused preset / Gelöscht: {path}")
                except Exception as e:
                    print(f"Could not clean up presets directory / Fehler beim Bereinigen des presets-Verzeichnisses: {e}")
                    
        # Clean up Makefile (copy from template root first if in a subfolder setup)
        makefile_path = "Makefile"
        src_makefile = os.path.join(template_root, "Makefile")
        if os.path.exists(src_makefile) and not os.path.exists(makefile_path):
            copy_template_file("Makefile", makefile_path)
            
        if os.path.exists(makefile_path):
            try:
                with open(makefile_path, "r", encoding="utf-8") as f:
                    makefile_lines = f.readlines()
                
                cleaned_lines = []
                skip_target = False
                for line in makefile_lines:
                    if line.startswith("build-example:") or line.startswith("dev-example:"):
                        skip_target = True
                        continue
                    if line.startswith("build-presentation:") or line.startswith("dev-presentation:"):
                        if not os.path.exists("presentation.typ"):
                            skip_target = True
                            continue
                    if line.startswith("\t"):
                        if skip_target:
                            continue
                    else:
                        skip_target = False
                        
                    # Clean up phony target list
                    if line.startswith(".PHONY:"):
                        phony_targets = [t for t in line.strip().split()[1:] if t not in ("build-example", "dev-example")]
                        if not os.path.exists("presentation.typ"):
                            phony_targets = [t for t in phony_targets if t not in ("build-presentation", "dev-presentation")]
                        cleaned_lines.append(".PHONY: " + " ".join(phony_targets) + "\n")
                        continue
                        
                    # Clean up build-all list
                    if line.startswith("build-all:"):
                        build_targets = ["build"]
                        if os.path.exists("presentation.typ"):
                            build_targets.append("build-presentation")
                        cleaned_lines.append("build-all: " + " ".join(build_targets) + "\n")
                        continue
                        
                    # Clean up clean target rm list
                    if line.startswith("\trm -f"):
                        rm_files = ["main.pdf"]
                        if os.path.exists("presentation.pdf") or os.path.exists("presentation.typ"):
                            rm_files.append("presentation.pdf")
                        cleaned_lines.append("\trm -f " + " ".join(rm_files) + "\n")
                        continue
                        
                    # Adjust command for subfolders if template_root is not current
                    if template_root != ".":
                        # Prefix font paths
                        line = line.replace("lib/", f"{path_prefix}lib/")
                        # Add --root argument to compile/watch commands
                        line = line.replace("typst compile ", f"typst compile --root {template_root} ")
                        line = line.replace("typst watch ", f"typst watch --root {template_root} ")

                    cleaned_lines.append(line)
                    
                with open(makefile_path, "w", encoding="utf-8") as f:
                    f.writelines(cleaned_lines)
                print("Optimized Makefile. / Makefile wurde bereinigt.")
            except Exception as e:
                print(f"Could not update Makefile / Fehler beim Bereinigen der Makefile: {e}")
                
        # Finally, delete setup.py itself
        try:
            os.remove(__file__)
            print("Successfully cleaned up all template setup files. / Einrichtungsdateien wurden erfolgreich bereinigt.")
        except Exception as e:
            print(f"Could not remove setup.py / Fehler beim Löschen von setup.py: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--presentation", "presentation", "-p"):
        run_presentation_only()
    else:
        main()
