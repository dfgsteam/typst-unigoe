#import "/lib/thesis.typ": thesis
#import "/lib/presets.typ"

#thesis(
  config: (
    ..presets.en_master, // Choose from: de_bachelor, de_master, en_bachelor, en_master, de_seminar, en_seminar, de_expose, en_expose
    
    // Core details
    title: "My title",
    author: "Jane Doe",
    date: none, // Set to none for today's date, or specify a custom date string (e.g. "2026-05-24")
    firstsupervisor: "My first supervisor",
    secondsupervisor: "My second supervisor",
    degree_type: "master", // "master", "bachelor", "seminar", or "expose"
    lang: "en", // "en" or "de"
    course_of_study: "Applied Computer Science",
    style: "modern", // "modern" or "legacy"
    
    // --- Advanced Customization Options (Dynamic Customization) ---
    
    // Custom Logo (Default: "/images/goe-logo.jpg")
    // Set to none to hide the logo, or specify an absolute path to a custom SVG/JPG/PNG
    // logo: "/images/goe-logo.jpg", 
    // logo_width: 6.5cm,
    
    // Custom Outline / Table of Contents
    // Set to false to hide the outline page completely (e.g. for exposés or short papers)
    // show_outline: true,
    
    // Custom Translations / Branding override
    // You can override individual preset fields without redefining the whole preset!
    // translations: (
    //   institution: "Institute of Computer Science",
    //   university: "Georg-August-Universität Göttingen",
    //   city: "Göttingen",
    // ),
    
    // Custom Contact Page (Optional & Dynamic)
    // Set contact to none to disable the contact info page entirely, or override specific fields:
    // contact: (
    //   university: "Georg-August-Universität Göttingen",
    //   address: [Goldschmidtstraße 7\ 37077 Göttingen\ Germany],
    //   phone: "+49 (551) 39-172000",
    //   fax: "+49 (551) 39-14403",
    //   email: "office@informatik.uni-goettingen.de",
    //   website: "www.informatik.uni-goettingen.de",
    // ),
  ),
  abstract: include "content/abstract.typ",
  // Set to none to omit the declaration of independence completely (e.g. for seminar papers or exposés)
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



