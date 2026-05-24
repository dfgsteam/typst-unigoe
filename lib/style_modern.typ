// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let apply_style(lang: "en", translations: none, body) = {
    
  // set page style
  set page(margin: (left: 25mm, right: 25mm, top: 25mm, bottom: 25mm), numbering: none)
  // set justify (Blocksatz) and make line-spacing consistent with LaTeX
  set par(justify: true)//, leading: .8em
  // set font
  show text.where(weight: "bold"): set text(weight: "bold")
  set text(font: "New Computer Modern")// or TeX Gyre Schola
  
  // set text(font: "FPL Neu", lang: lang, size: 10pt)
  // style links/references with colorful boxes around them
  show link: it => {
    box(it, stroke: 1pt + red, outset: (bottom:2pt, x:.5pt, y:.5pt))
  }
  show ref: it => {
    box(it, stroke: 1pt + green, outset: (bottom:1.5pt, x:.5pt, y:.5pt))
  }

  // style headings in the document to be consistent with LaTeX
  set heading(numbering: "1.1")
  
  show heading.where(level: 1): it => {
    set heading(supplement: translations.chapter)
    set text(size: 20pt)
    set block(above: 2em, below: 1em)
    // set text(size: 24.88pt)
    // block[
    //   #if it.numbering != none {
    //     text(size: 20.74pt)[Chapter #counter(heading).display()]
    //   }
    //   #v(1em)
    //   #it.body
    // ]
    it
  }
  show heading.where(level: 2): it => [
      #set heading(supplement: translations.section)
      #set text(size: 16pt)
      #set block(above: 1.5em, below: 1em)
      // #set text(size: 14.4pt)
      // #let ex = measure("x").height
      // #set block(above: 3.5*ex, below: 2.3*ex)
      #it
  ]
  show heading.where(level: 3): it => [
      #set heading(supplement: translations.subsection)
      #set text(size: 13pt)
      #set block(above: 1.5em, below: 1em)
      // #set text(size: 12pt)
      // #let ex = measure("x").height
      // #set block(above: 3.25*ex, below: 1.5*ex)
      #it
  ]
  show heading.where(level: 4): it => [
      #set heading(supplement: translations.subsubsection)
      #set block(above: 1.5em, below: 1em)
      // #let ex = measure("x").height
      // #set block(above: 3.25*ex, below: 1.5*ex)
      #it
  ]

  // style outline: chapters as bold and without dots
  show outline.entry: entry => if entry.level != 1 {
    entry
  } else {
    entry.indented(strong(entry.prefix()), strong[#entry.body() #box(width: 1fr, " ") #entry.page()])
  }

  // premium block code styling
  show raw.where(block: true): it => {
    block(
      fill: rgb("f9f9fb"),
      stroke: 0.5pt + rgb("e1e1e8"),
      inset: 12pt,
      radius: 6pt,
      width: 100%,
      clip: true,
    )[
      #set text(size: 8.5pt, font: "DejaVu Sans Mono", weight: "regular")
      #it
    ]
  }

  body
}

#let header(ctx) = context {
  // Suppress running header on pages where a new chapter (level 1 heading) starts
  let has-ch-start = query(heading.where(level: 1)).any(h => h.location().page() == here().page())
  if not has-ch-start {
    align(right)[#ctx.title]
    v(.5em, weak: true)
    line(stroke: .7pt, length: 100%)
  }
}
#let footer(ctx) = {
  line(stroke: 0.7pt, length: 100%)
    v(.5em, weak: true)

  grid(columns: (auto, auto, auto), column-gutter: (1fr, 1fr),
    [#context {
      let headings = query(heading)
      let ch_heading = headings.filter(h => h.level == 1 and h.location().page() <= here().page()).at(-1, default: none)
      if ch_heading == none {
        return none
      }
      if ch_heading.numbering != none {
        let level = counter(heading).at(ch_heading.location()).first()
        [#ctx.translations.chapter #level]
      } else {
        ch_heading.body
      }
    }],
    ctx.author,
    counter(page).display("1"),
  )
}
