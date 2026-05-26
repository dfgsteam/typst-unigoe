// Göttingen Slide Presentation Template
// Aspect Ratio: 16:9

#let slide(title: none, body) = {
  pagebreak(weak: true)
  if title != none {
    block(width: 100%, below: 1.2em)[
      #text(size: 22pt, weight: "bold", fill: rgb("1a5fb4"))[#title]
      #v(-0.5em)
      #line(length: 100%, stroke: 1.5pt + rgb("1a5fb4"))
    ]
  }
  body
}

#let presentation(
  title: "Presentation Title",
  subtitle: none,
  author: "Author Name",
  institute: "Institute of Computer Science",
  university: "Georg-August-Universität Göttingen",
  date: none,
  logo: "/images/ugo-logo.svg",
  logo_width: 5cm,
  lang: "de",
  body
) = {
  // Page setup
  set page(
    paper: "presentation-16-9",
    margin: (top: 1.8cm, bottom: 1.2cm, left: 1.2cm, right: 1.2cm),
    header: context {
      // Suppress header on title slide (first page)
      if here().page() > 1 {
        v(3em)
        grid(
          columns: (1fr, auto),
          align(left + horizon)[
            #text(size: 10pt, fill: rgb("555555"), weight: "medium")[#title]
          ],
          align(right + horizon)[
            #if logo != none {
              image(logo, width: 2.8cm)
            }
          ]
        )
        v(0em)
        line(length: 100%, stroke: 0.5pt + rgb("dddddd"))
      }
    },
    footer: context {
      if here().page() > 1 {
        line(length: 100%, stroke: 0.5pt + rgb("dddddd"))
        v(-0.8em)
        grid(
          columns: (1fr, 1fr, 1fr),
          align(left)[
            #text(size: 8.5pt, fill: rgb("777777"))[#author]
          ],
          align(center)[
            #text(size: 8.5pt, fill: rgb("777777"))[#date]
          ],
          align(right)[
            #text(size: 8.5pt, fill: rgb("777777"))[
              #let current = here().page()
              #let total = counter(page).final().first()
              #if lang == "de" [Folie #current von #total] else [Slide #current of #total]
            ]
          ]
        )
        v(0.5em)
      }
    }
  )

  // Text formatting
  set text(font: "New Computer Modern", size: 18pt, lang: lang)
  set par(justify: true, leading: 0.8em)
  
  // Style lists for presentation slides
  set list(marker: ([#text(fill: rgb("1a5fb4"))[•]], [#text(fill: rgb("0f766e"))[‣]]))

  // Title Slide Layout
  
  align(center + horizon)[
    #grid(
      columns: 1fr,
      row-gutter: 1.5em,
      align(left)[
        #if logo != none {
          image(logo, width: logo_width)
        }
      ],
      [
        #v(1em)
        #text(size: 28pt, weight: "bold", fill: rgb("1a5fb4"))[#title]
        #if subtitle != none [
          #v(0.5em)
          #text(size: 18pt, weight: "medium", fill: rgb("555555"))[#subtitle]
        ]
      ],
      [
        #line(length: 100%, stroke: 1.5pt + rgb("1a5fb4"))
      ],
      [
        #grid(
          columns: (1fr, 1fr),
          align(left)[
            #text(size: 13pt, weight: "bold")[#author] \
            #text(size: 11pt, fill: rgb("555555"))[#institute]
          ],
          align(right)[
            #text(size: 12pt)[#university] \
            #text(size: 11pt, fill: rgb("555555"))[#date]
          ]
        )
      ]
    )
  ]

  body
}
