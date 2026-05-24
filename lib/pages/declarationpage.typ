// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let declarationpage(config: none, declaration: none) = {
  grid(
    rows: (1fr, auto),
    v(1em),
    [
      #line(stroke: 0.4pt, length: 100%)
      #if declaration != none [
        #declaration
      ]
      #if config.style != "legacy" [
        #v(0.2cm)
        #config.translations.city, #config.date
      ]
    ],
  )
  pagebreak()
}
