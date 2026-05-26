#import "/lib/thesis.typ": thesis, todo, acr, theorem, definition, proof

#thesis(
  config: (
    // Core details
    title: "A Dynamic and Customizable Typst Template for Theses, Seminar Papers, and Exposés",
    subtitle: "A modern alternative to LaTeX for university students",
    translated_title: "Eine dynamische und anpassbare Typst-Vorlage für Abschlussarbeiten, Seminararbeiten und Exposés",
    author: "Jane Doe",
    student_id: "12345678",
    author_email: "jane.doe@stud.uni-goettingen.de",
    date: none, // Set to none for today's date, or specify a custom date string (e.g. "2026-05-24")
    firstsupervisor: "Prof. Dr. First Supervisor",
    secondsupervisor: "Dr. Second Supervisor",
    degree_type: "master", // "master", "bachelor", "seminar", or "expose"
    lang: "en", // "en" or "de"
    course_of_study: "Applied Computer Science",
    style: "modern", // "modern" or "legacy"
    
    // --- Advanced Customization Options (Dynamic Customization) ---
    
    // Draft Mode (Set to true to show a DRAFT watermark and e.g. render all #todo() boxes)
    draft: true,
    
    // Custom Logo (Default: "/images/ugo-logo.svg")
    // Set to none to hide the logo, or specify an absolute path to a custom SVG/JPG/PNG
    // logo: "/images/ugo-logo.svg", 
    // logo_width: 6.5cm,
    
    // Custom Outline / Table of Contents
    // Set to false to hide the outline page completely (e.g. for exposés or short papers)
    // show_outline: true,
    
    // Position of Declaration of Independence and AI Declaration ("beginning" or "end")
    declaration_position: "end",
    declaration_ai_position: "end",
    
    // Include Roman page numbered sections in Table of Contents
    outline_roman_pages: true,
    
    // Abbildungs- und Tabellenverzeichnis (List of Figures & List of Tables)
    show_list_of_figures: true,
    show_list_of_tables: true,
    
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
    //   address: [Goldschmidtstraße 7\ 37077 Göttingen\ Germany],
    //   phone: "+49 (551) 39-172000",
    //   fax: "+49 (551) 39-14403",
    //   email: "office@informatik.uni-goettingen.de",
    //   website: "www.informatik.uni-goettingen.de",
    // ),
  ),
  
  // Dual-language abstracts (English & German) in a dictionary!
  abstract: (
    en: include "content/abstract.typ",
    de: include "content/abstract_de.typ",
  ),
  
  declaration: include "content/declaration.typ",

  declaration_ai: include "content/declaration_ai.typ",

  acronyms: (
    API: ("Application Programming Interface", "Schnittstelle zur Anwendungsprogrammierung"),
    REST: ("Representational State Transfer", "Zustandsloser Architekturstil"),
    JSON: ("JavaScript Object Notation", "JavaScript-Objekt-Notation"),
  ),
  
  chapters: (
    // Comprehensive template demo showing formatting, math, figures, etc.
    include "content/template.typ",
  ),
  
  bibliography: bibliography(
    "content/references.bib",
    style: "ieee",
    title: none,
  ),
  
  appendix: include "content/appendix.typ",
)
