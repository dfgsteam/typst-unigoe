#import "/lib/thesis.typ": thesis
#import "/lib/presets.typ"

#thesis(
  config: (
    ..presets.de_master, // Wähle aus: de_bachelor, de_master, en_bachelor, en_master
    
    // Kerndaten
    title: "Mein Titel der Arbeit",
    author: "Max Mustermann",
    date: none, // Auf none lassen für das heutige Datum, oder ein spezifisches Datum angeben (z. B. "2026-05-24")
    firstsupervisor: "Mein Erstprüfer / meine Erstprüferin",
    secondsupervisor: "Mein Zweitprüfer / meine Zweitprüferin",
    degree_type: "master", // "master" oder "bachelor"
    lang: "de", // "en" oder "de"
    course_of_study: "Angewandte Informatik", // Studiengang
    style: "modern", // "modern" oder "legacy" (legacy ist optimiert für doppelseitigen Druck)
    
    // --- Erweiterte Anpassungsoptionen (Dynamisches Branding) ---
    
    // Eigenes Logo (Standard: "/images/goe-logo.jpg")
    // Auf none setzen, um das Logo auszublenden, oder einen absoluten Pfad zu einem eigenen Logo angeben
    // logo: "/images/goe-logo.jpg", 
    // logo_width: 6.5cm,
    
    // Eigene Übersetzungen / Branding-Überschreibungen
    // Du kannst einzelne Felder der Standard-Voreinstellungen hier überschreiben:
    // translations: (
    //   institution: "Institut für Informatik",
    //   university: "Georg-August-Universität Göttingen",
    //   city: "Göttingen",
    // ),
    
    // Eigene Kontaktseite (Optional & Dynamisch)
    // Auf none setzen, um die Kontaktseite komplett auszublenden, oder Details überschreiben:
    // contact: (
    //   university: "Georg-August-Universität Göttingen",
    //   address: [Goldschmidtstraße 7\ 37077 Göttingen\ Deutschland],
    //   phone: "+49 (551) 39-172000",
    //   fax: "+49 (551) 39-14403",
    //   email: "office@informatik.uni-goettingen.de",
    //   website: "www.informatik.uni-goettingen.de",
    // ),
  ),
  abstract: include "content/abstract_de.typ",
  declaration: include "content/declaration_de.typ",
  chapters: (
    // Sobald du das Template gelesen hast, kannst du den ersten Eintrag auskommentieren:
    include "content/template.typ",
    // include "content/content_de.typ",
  ),
  bibliography: bibliography(
    "content/references.bib",
    style: "ieee",
    title: none,
  ),
  // appendix: include "content/appendix.typ",
)
