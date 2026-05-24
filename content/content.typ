// simple todo blocks. you can also use a library for todo's on the page margins
#let todo(color: orange, body) = {
  box(fill: color, width: 100%, inset: 8pt, radius: 5pt, stroke: black)[#body]
}

= Introduction
#todo[
  - Introducing the topic
  - Motivating the topic
  - Present problem and/or research goals
    - (optional) why other approaches do not work / your work is original
  - Research questions and/or proposed (new) solution
  - (optional) Summary of results/outcomes of the evaluation
]
== Structure of this document
#todo[describe what you do]
= Basics
= Anaysis
== Related Work
== Approach
= Implementation / Case Study
= Results
= Discussion
= Conclusion & Outlook
