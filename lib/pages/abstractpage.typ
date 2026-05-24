// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let abstractpage(config: none, abstract: none) = {
  if abstract != none {
    if type(abstract) == dictionary {
      for (lang_key, content) in abstract {
        let title = if lang_key == "de" { "Zusammenfassung" } else if lang_key == "en" { "Abstract" } else { config.translations.abstract_title }
        align(center)[
          #heading(
            outlined: false,
            numbering: none,
            text(1em, weight: "bold")[#title],
          )
        ]
        v(5pt)
        content
        pagebreak()
      }
    } else {
      align(center)[
        #heading(
          outlined: false,
          numbering: none,
          text(1em, weight: "bold")[#config.translations.abstract_title],
        )
      ]
      v(5pt)
      abstract
      pagebreak()
    }
  }
}
