// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

#let contactpage(config: none) = {
  grid(
    rows: (1fr, auto),
    [],
    [
      #par[Georg-August-Universität Göttingen\
        #config.translations.institution]
      #par[Goldschmidtstraße 7\
        37077 Göttingen\
        Germany
      ]
      #table(
        columns: (auto, auto),
        stroke: none,
        [☎], [+49 (551) 39-172000],
        [📠], [+49 (551) 39-14403],
        [📧], link("mailto:office@informatik.uni-goettingen.de"),
        [🌏], link("https://www.informatik.uni-goettingen.de")[www.informatik.uni-goettingen.de],
      )
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
