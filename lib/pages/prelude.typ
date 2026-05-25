// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

// Title page .. Contents
#import "./titlepage.typ": titlepage
#import "./contactpage.typ": contactpage
#import "./abstractpage.typ": abstractpage
#import "./declarationpage.typ": declarationpage

#let prelude(
  config: none,
  abstract: none,
  declaration: none,
  declaration_ai: none,
  acronyms: none,
) = {
  // disable page numbering for the first few pages
  set page(numbering: none)

  // Title page
  titlepage(config: config)

  // Contact info page
  contactpage(config: config)

  // Enable page numbering from here on
  set page(numbering: "I")

  // Declaration
  if declaration != none and config.at("declaration_position", default: "beginning") == "beginning" {
    let title = config.translations.at("declaration_title", default: if config.lang == "de" { "Selbstständigkeitserklärung" } else { "Declaration of Authorship" })
    declarationpage(config: config, title: title, declaration: declaration)
  }

  // AI Declaration
  if declaration_ai != none and config.at("declaration_ai_position", default: "beginning") == "beginning" {
    let title = config.translations.at("declaration_ai_title", default: if config.lang == "de" { "Erklärung zur Verwendung von KI" } else { "Declaration on the Use of AI" })
    declarationpage(config: config, title: title, declaration: declaration_ai)
  }

  // Abstract page
  abstractpage(config: config, abstract: abstract)

  // Outline
  if config.at("show_outline", default: true) {
    set outline.entry(fill: repeat(". "))
    outline(depth: 3, indent: auto, title: config.translations.outline_title)
    pagebreak()
  }

  // List of Figures (Abbildungsverzeichnis)
  if config.at("show_list_of_figures", default: false) {
    let title = if config.lang == "de" { "Abbildungsverzeichnis" } else { "List of Figures" }
    set outline.entry(fill: repeat(". "))
    show heading: set heading(outlined: config.at("outline_roman_pages", default: false))
    outline(title: title, target: figure.where(kind: image))
    pagebreak()
  }

  // List of Tables (Tabellenverzeichnis)
  if config.at("show_list_of_tables", default: false) {
    let title = if config.lang == "de" { "Tabellenverzeichnis" } else { "List of Tables" }
    set outline.entry(fill: repeat(". "))
    show heading: set heading(outlined: config.at("outline_roman_pages", default: false))
    outline(title: title, target: figure.where(kind: table))
    pagebreak()
  }

  // List of Abbreviations (Acronyms)
  if acronyms != none and acronyms.len() > 0 {
    let title = if config.lang == "de" { "Abkürzungsverzeichnis" } else { "List of Abbreviations" }
    heading(level: 1, numbering: none, outlined: config.at("outline_roman_pages", default: false))[#title]
    v(1.5em)
    let sorted-acronyms = acronyms.pairs().sorted(key: ((key, val)) => key)
    grid(
      columns: (3cm, 1fr),
      row-gutter: 1.5em,
      column-gutter: 1.5em,
      ..sorted-acronyms.map(((key, val)) => (
        strong(key),
        if val.len() > 1 and config.lang == "de" { val.at(1) } else { val.first() }
      )).flatten()
    )
    pagebreak()
  }
}
