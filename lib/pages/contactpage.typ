// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let contactpage(config: none) = {
  if config.contact == none {
    return
  }

  grid(
    rows: (1fr, auto),
    [],
    [
      #if config.contact.university != none [
        #par[#config.contact.university \ #config.translations.institution]
      ]
      #if config.contact.address != none [
        #par[#config.contact.address]
      ]

      #let rows = ()
      #if config.contact.phone != none { rows.push(([☎], config.contact.phone)) }
      #if config.contact.fax != none { rows.push(([📠], config.contact.fax)) }
      #if config.contact.email != none { rows.push(([📧], link("mailto:" + config.contact.email))) }
      #if config.contact.website != none {
        let url = config.contact.website
        if not url.starts-with("http") {
          url = "https://" + url
        }
        rows.push(([🌏], link(url)[#config.contact.website]))
      }

      #if rows.len() > 0 [
        #table(
          columns: (auto, auto),
          stroke: none,
          ..rows.flatten()
        )
      ]
      #v(.5cm)
      #table(
        columns: (auto, auto),
        stroke: none,
        [#config.translations.firstsupervisor_text:], config.firstsupervisor,
        [#config.translations.secondsupervisor_text:], config.secondsupervisor,
      )
    ],
  )
  pagebreak()
}
