// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#import "./pages/prelude.typ": prelude

#let thesis(
  config: none,
  titlepage: none,
  abstract: none,
  declaration: none,
  chapters: none,
  bibliography: none,
  appendix: none,
) = {
  // validate and clean up arguments
  if config.date == none {
    config.date = datetime.today().display("[year]-[month repr:long]-[day]")
  }
  assert(
    config.lang == "de" or config.lang == "en",
    message: "Only german (de) and english (en) are supported as document languages (lang).",
  )
  assert(
    config.degree_type == "bachelor" or config.degree_type == "master",
    message: "Please set degree_type to either bachelor or master.",
  )

  // set documents properties
  set document(author: config.author, title: config.title, date: datetime.today())
  // set document language
  set text(lang: config.lang)

  // apply a style preset
  let apply_style
  let footer
  let header
  if config.style == "legacy" {
    import "/lib/style_legacy.typ"
    apply_style = style_legacy.apply_style
    footer = style_legacy.footer
    header = style_legacy.header
  } else {
    import "/lib/style_modern.typ"
    apply_style = style_modern.apply_style
    footer = style_modern.footer
    header = style_modern.header
  }
  show: apply_style.with(lang: config.lang, translations: config.translations)

  // import the first few pages (title page, contact info, declaration, abstract, outline)
  prelude(config: config, abstract: abstract, declaration: declaration)

  // enable page numbering
  set page(numbering: "1")
  counter(page).update(1)
  let ctx = (title: config.title, author: config.author, translations: config.translations);
  set page(footer: context footer(ctx), header: context header(ctx))

  // include the actual contents
  for ch in chapters {
    ch
  }

  pagebreak()
  set heading(numbering: "A")
  counter(heading).update(0)

  set page(footer: {
    context align(center, counter(heading).display("A - ")+ counter(page).display("1"))
  })

  // set page(numbering: "I")
  //Bibliography
  if bibliography != none {
    heading("Bibliography")
    v(1em)
    bibliography
  }
  if appendix != none {
    pagebreak()
    appendix
  }
}
