#import "/lib/thesis.typ": thesis, todo, acr
#import "/lib/presets.typ"

#thesis(
  config: (
    ..presets.de_master, // Choose from: de_bachelor, de_master, en_bachelor, en_master, de_seminar, en_seminar, de_expose, en_expose
    
    // Core details
    title: "Titel der Arbeit",
    subtitle: none, // Untertitel (optional)
    translated_title: none, // Übersetzter Titel (optional)
    author: "Vorname Nachname",
    student_id: none, // Deine Matrikelnummer (optional, z. B. für Seminararbeiten)
    author_email: none, // Deine E-Mail (optional)
    date: none, // Auf none lassen für das heutige Datum, oder ein Datum angeben (z. B. "2026-05-24")
    firstsupervisor: "Erstprüfer*in",
    secondsupervisor: "Zweitprüfer*in",
    degree_type: "master", // "master", "bachelor", "seminar" oder "expose"
    lang: "de", // "de" oder "en"
    course_of_study: "Angewandte Informatik",
    style: "modern", // "modern" oder "legacy"
    
    // --- Erweiterte Optionen (Advanced Options) ---
    
    // Entwurfs-Modus (auf true setzen, um "DRAFT"-Wasserzeichen anzuzeigen und Todos zu rendern)
    draft: false,
    
    // Custom Logo (Standard: "/images/ugo-logo.svg")
    // Auf none setzen, um das Logo auszublenden, oder einen Pfad zu einer SVG/JPG/PNG angeben
    // logo: "/images/ugo-logo.svg", 
    // logo_width: 6.5cm,
    
    // Inhaltsverzeichnis (auf false setzen, um das Verzeichnis auszublenden, z. B. bei Exposés)
    // show_outline: true,
    
    // Eigene Übersetzungs- und Marken-Overrides
    // translations: (
    //   institution: "Institut für Informatik",
    //   university: "Georg-August-Universität Göttingen",
    //   city: "Göttingen",
    // ),
    
    // Custom Kontakt-Seite (Standardmäßig aktiviert, zum Deaktivieren auf none setzen)
    // contact: (
    //   university: "Georg-August-Universität Göttingen",
    //   address: [Goldschmidtstraße 7\ 37077 Göttingen\ Deutschland],
    //   phone: "+49 (551) 39-172000",
    //   fax: "+49 (551) 39-14403",
    //   email: "office@informatik.uni-goettingen.de",
    //   website: "www.informatik.uni-goettingen.de",
    // ),
  ),
  
  // Zusammenfassung / Abstract
  // Kann auch ein Dictionary sein für zweisprachige Abstracts: (de: include "...", en: include "...")
  abstract: include "content/abstract_de.typ",
  
  // Selbstständigkeitserklärung (auf none setzen, falls nicht benötigt, z. B. bei Exposés)
  declaration: include "content/declaration_de.typ",

  // Erklärung zur Verwendung von KI (auf none setzen, falls nicht benötigt)
  // declaration_ai: include "content/declaration_ai_de.typ",

  // Abkürzungen (optional, zum Aktivieren auskommentieren und anpassen)
  // acronyms: (
  //   API: ("Application Programming Interface", "Schnittstelle zur Anwendungsprogrammierung"),
  //   REST: ("Representational State Transfer", "Zustandsloser Architekturstil"),
  // ),
  
  // Kapitel deiner Arbeit
  chapters: (
    include "content/content_de.typ",
  ),
  
  // Literaturverzeichnis (auf none setzen, falls nicht benötigt)
  bibliography: bibliography(
    "content/references.bib",
    style: "ieee",
    title: none,
  ),
  
  // Anhang (auf none setzen, falls nicht benötigt)
  // appendix: include "content/appendix.typ",
)
