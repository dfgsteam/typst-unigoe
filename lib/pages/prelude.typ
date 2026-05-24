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

  // Abstract page
  abstractpage(config: config, abstract: abstract)

  // Outline
  if config.at("show_outline", default: true) {
    set outline.entry(fill: repeat(". "))
    outline(depth: 3, indent: auto, title: config.translations.outline_title)
  }
}
