#import "/lib/thesis.typ": thesis
#import "/lib/presets.typ"

#thesis(
  config: (
    ..presets.en_master,
    title: "My title",
    author: "Jane Doe",
    date: none, // TODO: Insert date
    firstsupervisor: "My first supervisor",
    secondsupervisor: "My second supervisor",
    degree_type: "master", // "master" or "bachelor"
    lang: "en", // "en" or "de"
    course_of_study: "Applied Computer Science",
    style: "modern", // "modern" or "legacy"
  ),
  abstract: include "content/abstract.typ",
  declaration: include "content/declaration.typ",
  chapters: (
    // once you have read it, you can comment out the template
    include "content/template.typ",
    // include "content/content.typ",
  ),
  bibliography: bibliography(
    "content/references.bib",
    style: "ieee",
    title: none,
  ),
  // appendix: include "content/appendix.typ",
)



