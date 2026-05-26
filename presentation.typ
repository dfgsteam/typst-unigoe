#import "/lib/presentation.typ": presentation, slide

#show: presentation.with(
  title: "Titel der Verteidigung / Presentation Title",
  subtitle: "Verteidigung der Abschlussarbeit / Thesis Defense",
  author: "Vorname Nachname",
  institute: "Institut für Informatik",
  university: "Georg-August-Universität Göttingen",
  date: "2026-05-26",
  logo: "/images/ugo-logo.svg",
  lang: "de", // "de" oder "en"
)

#slide(title: "Einleitung & Motivation")[
  - *Herausforderung*: Komplexe wissenschaftliche Arbeiten erfordern eine hochqualitative Darstellung.
  - *Zielsetzung*: Entwicklung einer dynamischen und flexiblen Vorlage für Göttingen.
  - *Relevanz*: Eine zeitgemäße, modular anpassbare Alternative zu LaTeX.
]

#slide(title: "Wissenschaftlicher Beitrag")[
  - *Dynamic Presets*: Ein einziger Kern-Layoutgenerator für Master, Bachelor, Seminare und Exposés.
  - *Bilingual Abstract*: Automatisch nacheinander gesetzte mehrsprachige Zusammenfassungen.
  - *Dynamic Placement*: Platzierung der offiziellen Erklärungen (Eigenständigkeit, KI) wahlweise am Anfang oder Ende des Dokuments.
]

#slide(title: "Evaluation / Ergebnisse")[
  - Makelloser PDF/A-konformer Export direkt aus der CI/CD-Release-Pipeline.
  - Vollständige Unabhängigkeit von lokalen Schriftarten durch Nutzung von Typst-Webfonts.
  - Zotero-Anbindung über Better BibTeX zur automatischen Real-time-Zitationspflege.
]

#slide(title: "Fazit & Ausblick")[
  - *Zusammenfassung*: Die Vorlage bietet eine spürbare Steigerung der Schreibgeschwindigkeit und Formatierungssicherheit.
  - *Ausblick*: Integration weiterer Universitäts-Presets und fortgeschrittener mathematischer Sätze.
  - *Fragen*: Ich bedanke mich für Ihre Aufmerksamkeit und freue mich auf Ihre Fragen!
]
