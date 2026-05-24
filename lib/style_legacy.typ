// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let apply_style(lang: "en", translations: none, body) = {
  // make pagebreaks fill up with empty pages so content always starts on a left page (of a book) set pagebreak(to: "odd")
  set pagebreak(to: "odd")
  // set page style
  set page(margin: (left: 25mm, right: 25mm, top: 40mm, bottom: 50mm))
  // set justify (Blocksatz) and make line-spacing consistent with LaTeX
  set par(justify: true, leading: .8em)
  // set font
  set text(font: "FPL Neu", lang: lang, size: 10pt)
  // style links/references with colorful boxes around them
  show link: it => {
    box(it, stroke: 1pt + red, outset: (bottom: 2pt, x: .5pt, y: .5pt))
  }
  show ref: it => {
    box(it, stroke: 1pt + green, outset: (bottom: 1.5pt, x: .5pt, y: .5pt))
  }

  // style headings in the document to be consistent with LaTeX
  set heading(numbering: "1.1")
  show heading.where(level: 1): it => {
    set heading(supplement: translations.chapter)
    set block(above: 50pt, below: 40pt)
    set text(size: 24.88pt)
    block[
      #if it.numbering != none {
        text(size: 20.74pt)[Chapter #counter(heading).display()]
      }
      #v(1em)
      #it.body
    ]
  }
  show heading.where(level: 2): it => [
    #set heading(supplement: translations.section)
    #set text(size: 14.4pt)
    #let ex = measure("x").height
    #set block(above: 3.5 * ex, below: 2.3 * ex)
    #it
  ]
  show heading.where(level: 3): it => [
    #set heading(supplement: translations.subsection)
    #set text(size: 12pt)
    #let ex = measure("x").height
    #set block(above: 3.25 * ex, below: 1.5 * ex)
    #it
  ]
  show heading.where(level: 4): it => [
    #set heading(supplement: translations.subsubsection)
    #let ex = measure("x").height
    #set block(above: 3.25 * ex, below: 1.5 * ex)
    #it
  ]

  // style outline: chapters as bold and without dots
  show outline.entry: entry => if entry.level != 1 {
    entry
  } else {
    entry.indented(strong(entry.prefix()), strong[#entry.body() #box(width: 1fr, " ") #entry.page()])
  }

  // increase line spacing in the outline
  show outline: set block(spacing: 1em)
  body
}
// style footer to make page numbers alternate. this get's applied after the introductory pages
#let footer(ctx) = {
  let alignment = if calc.even(here().page()) { right } else { left }
  align(alignment, counter(page).display("1"))
}

#let header(ctx) = {}
