// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let abstractpage(config: none, abstract: none) = {
  if abstract != none {
    align(center)[
      #heading(
        outlined: false,
        numbering: none,
        text(1em, weight: "bold")[Abstract],
      )
    ]
    v(5pt)
    abstract
    pagebreak()
  }
}
