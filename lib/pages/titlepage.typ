// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let titlepage(config: none) = {
  // Title page
  align(center)[
    #text(size: 14pt)[
      #grid(
        columns: 1fr,
        row-gutter: (1fr, 1fr, 1fr, 1fr, .5fr, 1fr),
        align(left)[#image("../../images/goe-logo.jpg", width: 6.5cm)],
        [
          #text(size: 20pt, weight: "bold", config.translations.degree_text + "\n")
          #config.translations.submitted_text "#config.course_of_study"
        ],
        heading(bookmarked: false, outlined: false, numbering: none, par(leading: .4em)[#config.title]),
        par(text(config.author)),
        [#config.translations.institution],
        [
          #config.translations.university
          #v(0.2cm)
          #config.date
        ],
      )
    ]
  ]
  pagebreak(weak: true)
}
