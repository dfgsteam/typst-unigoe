// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let declarationpage(config: none, title: none, declaration: none) = {
  if title != none {
    heading(level: 1, numbering: none, outlined: config.at("outline_roman_pages", default: false))[#title]
    v(1.5em)
  }
  if declaration != none [
    #declaration
  ]
  if config.style != "legacy" [
    #v(0.8cm)
    #config.translations.city, #config.date
  ]
  pagebreak()
}
