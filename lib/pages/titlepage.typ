// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let titlepage(config: none) = {
  // Title page
  align(center)[
    #text(size: 14pt)[
      #grid(
        columns: 1fr,
        row-gutter: (1fr, 1fr, 1fr, 1fr, .5fr, 1fr),
        align(left)[
          #if config.logo != none {
            image(config.logo, width: config.logo_width)
          }
        ],
        [
          #text(size: 20pt, weight: "bold", config.translations.degree_text + "\n")
          #config.translations.submitted_text "#config.course_of_study"
        ],
        heading(bookmarked: false, outlined: false, numbering: none, par(leading: .4em)[#config.title]),
        [
          #text(config.author)
          #if config.at("student_id", default: none) != none [
            \ #text(size: 11pt, rgb("555555"))[#config.translations.student_id_text: #config.student_id]
          ]
          #if config.at("author_email", default: none) != none [
            \ #text(size: 11pt, rgb("555555"))[#link("mailto:" + config.author_email)[#config.author_email]]
          ]
        ],
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
