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
  if declaration != none {
    declarationpage(config: config, declaration: declaration)
  }

  // AI Declaration
  if declaration_ai != none {
    declarationpage(config: config, declaration: declaration_ai)
  }

  // Abstract page
  abstractpage(config: config, abstract: abstract)

  // Outline
  if config.at("show_outline", default: true) {
    set outline.entry(fill: repeat(". "))
    outline(depth: 3, indent: auto, title: config.translations.outline_title)
    pagebreak()
  }

  // List of Abbreviations (Acronyms)
  if acronyms != none and acronyms.len() > 0 {
    let title = if config.lang == "de" { "Abkürzungsverzeichnis" } else { "List of Abbreviations" }
    heading(level: 1, numbering: none, outlined: true)[#title]
    v(1.5em)
    grid(
      columns: (3cm, 1fr),
      row-gutter: 1.5em,
      column-gutter: 1.5em,
      ..acronyms.pairs().map(((key, val)) => (
        strong(key),
        if val.len() > 1 and config.lang == "de" { val.at(1) } else { val.first() }
      )).flatten()
    )
    pagebreak()
  }
}
