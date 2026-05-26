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
  // style links and references in a sleek, modern, borderless way
  show link: set text(fill: rgb("1a5fb4"))
  show ref: set text(fill: rgb("0f766e"))

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
    let headings = query(heading)
    // Find active chapter (level 1)
    let active_ch = headings.filter(h => h.level == 1 and h.location().page() <= here().page()).at(-1, default: none)
    // Find active section (level 2)
    let active_sect = headings.filter(h => h.level == 2 and h.location().page() <= here().page()).at(-1, default: none)
    
    // Ensure section belongs to current chapter
    if active_sect != none and active_ch != none and active_sect.location().page() < active_ch.location().page() {
      active_sect = none
    }
    
    let left_text = if active_ch != none {
      if active_ch.numbering != none {
        let level = counter(heading).at(active_ch.location()).first()
        [#ctx.translations.chapter #level: #active_ch.body]
      } else {
        active_ch.body
      }
    } else {
      none
    }
    
    let right_text = if active_sect != none {
      if active_sect.numbering != none {
        let num = counter(heading).at(active_sect.location())
        [#num.map(str).join(".") #active_sect.body]
      } else {
        active_sect.body
      }
    } else {
      none
    }
    
    grid(
      columns: (1fr, 1fr),
      align(left)[#text(size: 8.5pt, fill: rgb("555555"))[#left_text]],
      align(right)[#text(size: 8.5pt, fill: rgb("555555"))[#right_text]],
    )
    v(.4em, weak: true)
    line(stroke: .5pt + rgb("dddddd"), length: 100%)
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
