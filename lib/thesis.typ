// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#import "./pages/prelude.typ": prelude
#import "./presets.typ"

#let draft_state = state("draft", false)

#let todo(color: orange, body) = context {
  if draft_state.get() {
    box(fill: color, width: 100%, inset: 8pt, radius: 5pt, stroke: black)[
      #text(weight: "bold")[TODO:] #body
    ]
  }
}

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
  assert(
    config.lang == "de" or config.lang == "en",
    message: "Only german (de) and english (en) are supported as document languages (lang).",
  )
  assert(
    config.degree_type in ("bachelor", "master", "seminar", "expose"),
    message: "Please set degree_type to one of: bachelor, master, seminar, expose.",
  )

  // dynamic configuration merging
  let default_preset = if config.lang == "de" {
    if config.degree_type == "bachelor" { presets.de_bachelor }
    else if config.degree_type == "master" { presets.de_master }
    else if config.degree_type == "seminar" { presets.de_seminar }
    else { presets.de_expose }
  } else {
    if config.degree_type == "bachelor" { presets.en_bachelor }
    else if config.degree_type == "master" { presets.en_master }
    else if config.degree_type == "seminar" { presets.en_seminar }
    else { presets.en_expose }
  }

  let merged_translations = default_preset.translations + config.at("translations", default: (:))

  let default_contact = (
    university: "Georg-August-Universität Göttingen",
    address: [Goldschmidtstraße 7\ 37077 Göttingen\ Germany],
    phone: "+49 (551) 39-172000",
    fax: "+49 (551) 39-14403",
    email: "office@informatik.uni-goettingen.de",
    website: "www.informatik.uni-goettingen.de",
  )

  let contact = if "contact" in config {
    if config.contact == none {
      none
    } else {
      default_contact + config.contact
    }
  } else {
    default_contact
  }

  let logo = config.at("logo", default: "/images/goe-logo.jpg")
  let logo_width = config.at("logo_width", default: 6.5cm)

  let date = config.at("date", default: none)
  if date == none {
    date = datetime.today().display("[year]-[month repr:long]-[day]")
  }

  let full_config = config
  full_config.insert("date", date)
  full_config.insert("translations", merged_translations)
  full_config.insert("contact", contact)
  full_config.insert("logo", logo)
  full_config.insert("logo_width", logo_width)

  // set documents properties
  set document(author: full_config.author, title: full_config.title, date: datetime.today())
  // set document language
  set text(lang: full_config.lang)

  // apply a style preset
  let apply_style
  let footer
  let header
  if full_config.style == "legacy" {
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
  show: apply_style.with(lang: full_config.lang, translations: full_config.translations)

  // set draft state
  draft_state.update(config.at("draft", default: false))

  // set page background watermark in draft mode
  set page(background: context {
    if draft_state.get() {
      align(center + horizon)[
        #rotate(45deg)[
          #text(80pt, fill: rgb(220, 220, 220, 40%), weight: "bold")[DRAFT]
        ]
      ]
    }
  })

  // import the first few pages (title page, contact info, declaration, abstract, outline)
  prelude(config: full_config, abstract: abstract, declaration: declaration)

  // enable page numbering
  set page(numbering: "1")
  counter(page).update(1)
  let ctx = (title: full_config.title, author: full_config.author, translations: full_config.translations);
  set page(footer: context footer(ctx), header: context header(ctx))

  // include the actual contents
  for ch in chapters {
    ch
  }

  // Bibliography (rendered in standard page style, no appendix footer)
  if bibliography != none {
    pagebreak()
    heading(full_config.translations.bibliography_title)
    v(1em)
    bibliography
  }

  // Appendix (only active and styled if appendix is provided)
  if appendix != none {
    pagebreak()
    set heading(numbering: "A")
    counter(heading).update(0)

    set page(footer: context {
      let head_disp = counter(heading).display("A")
      let app_text = full_config.translations.at("appendix_text", default: "Appendix")
      align(center, [#app_text #head_disp - #counter(page).display("1")])
    })
    appendix
  }
}
