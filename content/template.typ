// Copyright (c) 2025 Lorenz Glißmann
// Creative Commons Zero v1.0 Universal

= First steps
1. Read the following chapters
2. Configure this template. Put your thesis data into the `main.typ`.
3. Decide on a chapter structure, comment out this file in `main.typ` and put your chapters in there.


= How to structure your thesis
We first discuss the structure of your thesis and then give you an introduction into typst and this template.

Structuring your thesis can be confusing at first but it is actually easier than you think. No matter where you write your thesis, the structure is always very similar. Different disciplines just use different titles and have a slightly different focus. The kind of work you do, e.g. proof, case study, benchmark, also has an impact on wording and focus.

A thesis is generally written in present tense with a few exceptions. We typically present an evaluation and/or case study in past tense, referring to _what happened_. Similarly abstract, parts of the introduction and the conclusion may also other tenses. We can write a thesis in different persons. There is no consensus on what is best but the options are generally:

- the scientific "we": Modern and increasingly common, also in papers. It might feel awkward to use if you write the thesis by yourself, but you get used to this rather quickly and then it is (subjectively) easy to read.
- "I": This is the most accurate but often also feels rather personal. Some people think this is too personal and you should put the your thesis in the center instead of yourself.
- passive: Definitively puts the content in the center but also often seems uncommited and like you don't want to take responsiblity for your work and your decisions. It is also often harder to understand.

You should probably discuss this with your supervisors.

== Introduction
Every thesis has an introduction. The introduction typically has multiple uses:

- it introduces the reader to the topics of the thesis
- it _motivates_ the work (not you personal motivation but rather why the topic is interesting/relevant)
- it defines _goals_ and depending on your field also either _research questions_ or _problems_ that the work is attempting to solve
- it gives an overview over the _structure_ of the document

We generally start by introducing the reasearch area and why it is relevant. Then we explain the specific problem/challenge. If there are existing/common solutions in that area, we briefly mention them and especially their limitations. Following this, we propose our new solution/approach. Depending on your area, we also summarize how we evaluated this approach

== Basics / Foundations
The basics chapter presents foundational knowledge on which the work is based. It also provides the opportunity to define terminology and introduce the reader to domain knowledge that might not be common knowledge.

This chapter is also sometimes named "Foundations".

== Analysis / Related Work
The analysis chapter typically does what it says: Problem analysis. This also includes presenting and discussion other research that is related to the thesis' topics.

This chapter is sometimes called "Related work" and only presents / relates other research in the area of your topic. If it is called "Related work", a part of the analysis is usually shifted into the next chapter or a dedicated chapter. You might also have a section on "Related Work" in you analysis chapter.

== Design / Approach / Methods
This chapter presents the design of your research. This _can_ include software design but the focus is on *research design* i.e. how your research solves problems / answers it's research questions.

The design chapter is also often called "Approach" and presents how you approach reaching your goal / answering your research questions. It is also sometimes called "Methods" and discusses the research methodology of your work.

There are some differences in what this chapter aims to achieve. A case study design often discusses the _approach_, empirical studies generelly discuss _methods_ and a focus on problem solving or software design usually make the _design_ the center of this chapter.

== Implementation / Case Study / Evaluation / Results / Discussion
Depending on the focus in the previous chapter and the type of work, this chapter might actually be multiple chapters or contain multiple sections in the following order:

- *Implementation*: when software design or a reference implementation / proof of concept is important for your work.
  - Although _implementation_ seems to imply a focus on software engineering, this is *only true in very few edge cases*. Depending on your area source code snippets may be required or highly undesirable!
- *Case Study*: then the work includes a case study.
  - This may present how your study was conducted be written in past tense (while all other chapters typically use present tense).
  - The core is: usage/application of your approach for answering the research
question.
  - This may include presenting results and discussing their validity.
- *Evaluation* / *Results*: You may present your data / results here.
  - _How_ you evaluate is part of the previous chapter!
- *Discussion* / *Interpretation*: Discuss your results, critically analyze your approach and discuss limitations.

There is a lot of variation in here. An example: A case study where users use a software and answer a questionnaire about that. We
- might have just the "Case Study" chapter which tells the story of conducting the case study (incl. the actual procedure and the results). The discussion might be put into *Conclusion*.
- might have a seperate chapter on the (software) *Implementation*, the *Case Study*, presenting *Results* and a *Discussion*.

Having the optimal structure here is not the most important thing but there should always be:

- a clear separation between design/approach and case study/implementation and
- a clear separation between presenting results and discussing/interpreting results


== Conclusion
This chapter actually has three different functions:

- summarize the results
- finally answer your research questions or summarizing that, depending on the previous chapters
- discuss the validity and limitations of your work
- give an outlook (also called future work) how your work could/should be continued

It is possible to make separate sections or chapters for some of these.

= Using typst and this template to write your thesis
<document-structure>
The rest of this introduction chapter shows basic usage of some #strike[latex] typst features that can be used in the document. Of course there is a lot more to typst that what can be covered here.

The document structure is defined by `main.typ` which applies the template in `template.typ`. When you apply the template, you should enter your data there. You also have the choice between two styles:

- `legacy` looks like the classic LaTeX template and is optimized for printing and binding your thesis.
- `modern` looks more modern and is optimized for on computer screens.

== Document structure

Depending on your preference, you can distribute your chapters over multiple files or put everything into one file. Instead of one compact file with all chapter, you can e.g. create one file per chapter. A tip for later: The convention is that a file is not closed with a `#pagebreak()` but leaves this to the importing file. You can import files with a command like this (see main.typ):

```typst
#include "content/content.typ"
```

You can create headings (chapter, section, subsection, ...) like this:

```typst
= A Chapter
== A Section
=== A Subsection
==== A Subsubsection
```
These shorthand commands are equivalent to calling the `heading` function. By default all headings are numbered and outlined. The `heading` function takes arguments, e.g.:

- `depth`: e.g. 1 for chapter and 3 for subsection.
- `numbering`: How the heading should be numbered or `none` it numbering should be ommitted for this heading.
- `outlined`: `true` or `false`, whether the heading should appear in the table of contents

The heading function also takes _`content`_ (the heading's title) as a _positional_ argument:

```typst
#heading(depth: 2, outlined: false, numbering: none, "Invisible Section")
```

Many typst functions take content and passing content along as a bare string is limited so there is a shorthand for providing functions with content:

```typst
#heading(depth: 2, outlined: false, numbering: none)[Invisible Section"]
```
You can use the same syntax as in `.typ` files inside `[ ]`.

=== Formatting text

A common example for passing `content` into a function is centering:
#align(center)[
  This text appears centered on the page.
]

Typst comes with a simple markdown-like syntax for many common problems. Text can be made *\*bold\** , _\_italic\__ or #raw("`monospaced`"). Formatting text is generally exposed via typst's `text` function that #text(weight: "thin", size: 12pt, font: "New Computer Modern", fill: red)[can do a lot]:

```typst
#text(weight: "thin", size: 12pt, font: "New Computer Modern", fill: red)[can do a lot]
```

The function that generated monospaced content is called `raw` and can also display syntax-highlighted code. It also has a shorthand for multiline code-like content:

#grid(columns: (1fr, 1fr), [
#raw("```c
#include<stdio.h>

int main() {
    printf(\"Hello World\\n\");
    return 0;
}
```")
], [
  ... becomes this code block when rendered:
  ```c
#include<stdio.h>

int main() {
    printf(\"Hello World\\n\");
    return 0;
}
```
])

The function `link` is used to generate clickable #link("https://en.wikipedia.org/wiki/Hyperlink")[hyperlinks]. By default links look like regular text and we could manually wrap each link in a `#underline[...]` but there is a better way. Typst has a flexible system for styling content.

==== Changing styling behavior
Typst has two kinds of rules:
- `set` rules can globally set some parameters, e.g. #raw(lang: "typst", "#set align(center)") makes everything centered (until another another alignment is set)
- `show` rules can change how something is rendered

In the case of styling hyperlinks we can use a `show` rule to make all hyperlinks underlined and italic:
```typst
#show link: l => text(style: "italic", underline(l))
```

#show link: l => text(style: "italic", underline(l))
From now on all Links are italic and underlined:

#link("https://en.wikipedia.org/wiki/Hyperlink")[https://en.wikipedia.org/wiki/Hyperlink]

=== Lists, Tables, Formulas & more

Typst has unordered list:

#grid(columns: (1fr, 1fr), [
  ```typst
  - One
  - Two
  - Three
  ```
], [
  - One
  - Two
  - Three
])

And ordered lists:
#grid(columns: (1fr, 1fr), [
  ```typst
  + One
  + Two
  + Three
  ```
], [
  + One
  + Two
  + Three
])

Of course lists can also be nested:

#grid(columns: (1fr, 1fr), [
  ```typst
  + One
    + alpha
    + beta
  + Two
  + Three
  ```
], [
  + One
    + alpha
    + beta
  + Two
  + Three
])

=== Grids and Tables
<tables>

Other forms of lists can often be done as a `grid`:

#grid(columns: (1fr, 1fr), [
  ```typst
  #grid(columns: 2,column-gutter: .5em, row-gutter: .5em, align: (right, left),
    [First:], [One],
    [Second:], [Two],
    [Third:], [Three],
  )
  ```
], [
  #grid(columns: 2,column-gutter: .5em, row-gutter: .5em, align: (right, left),
    [First:], [One],
    [Second:], [Two],
    [Third:], [Three],
  )
])

And if you have looked at the source code to this document, you have seen that `grid` can also be used to do much more e.g. figures with a two-column layout.

The `table` function act similarly to `grid` and can be used to create a simple table. It is usually best to wrap tables and images into a `figure` with a caption.

#grid(columns: (1fr, 1fr), [
  ```typst
  #figure(kind: table,
    caption: "A simple centered table with some of my favorite numbers",
    align(center)[#table(
      columns: 4,
      align: (left,center,left,right,),
      [1], [2], [3], [4],
      [5], [6], [7], [8],
      [9], [10], [11], [12],
    )]
  ) 
  ```
], [
  #figure(kind: table,
    caption: "A simple centered table with some of my favorite numbers",
    align(center)[#table(
      columns: 4,
      align: (left,center,left,right,),
      [1], [2], [3], [4],
      [5], [6], [7], [8],
      [9], [10], [11], [12],
    )]
  )
])

=== Figures and including graphics
<using-graphics>
The `image` function can be used to include graphics in the document.
The vector-based graphic formats i.e. `svg` (but unfortunately not yet `pdf`) are preferred, while the pixel-based `jpg` and `png` can also be included. 

#grid(columns: (60%, 1fr), [
  ```typst
  #figure(caption: "The modern university logo", 
   image("../images/ugo-logo.svg", width: 100pt)
  )
  <fig:uni_logo>
  ```
], [
  #figure(caption: "The modern university logo", 
   image("../images/ugo-logo.svg", width: 100pt)
  )
  <fig:uni_logo>
])

Relative units (`em`, `pt` are relative to text size and `%` is relative to the available space) are generally prefered for `width`. If you include labels like `<fig:uni_logo>` with your figures, you can easily reference e.g. as "@fig:uni_logo" by writing `@fig:uni_logo`.

=== Citing
<citing>
One of the most important things in scientific work is the citing. 
Citing, incl. numbering and formatting is easy since everything is automatically managed by #strike[latex] typst. For example (look into the source code):

John Doe@doe2013 proposes is his paper a new approach on XYZ.

Meyer et al.@meyer2014[p. 100] suggest a new method to XYZ.

The `cite` function is used to reference to an item by its key but we also have shorthands for that. The references are stored in a separate `references.bib` file that contains
all references in the `bibtex` format.

The bibliography is also automatically generated.

For good practices in scientific writing you can make use of the following documents:

- #link("https://www.hochschulverband.de/fileadmin/redaktion/download/pdf/resolutionen/Gute_wiss._Praxis_Fakultaetentage.pdf")
  (only in german)
- #link("https://www.sub.uni-goettingen.de/en/learning-teaching/academic-work-tools-and-methods/academic-writing/")

=== Footnotes
<footnotes>
Footnotes can be easily inserted using the `footnote` function#footnote[Make sure to use footnotes but only when necessary.].

```typst
#footnote[Make sure to use footnotes but only when necessary.]
```

=== Math
<math>
Typst can display math formulas. The syntax is similar but also a little different from latex: #link("https://typst.app/docs/reference/math/")

=== Acronyms
<acronyms>
There are packages for making acronyms easy and fun, e.g.: #link("https://typst.app/universe/package/acrostiche/")

=== PDF/A validation
<pdfa-validation>
The thesis has to be in PDF/A format for archiving. This template automatically generates your file according to the PDF/A standard. It can be that this is violated by changing the document, for example by inserting non-compliant graphics. Please check, whether your final
version of the document is PDF/A compliant, e.g., by using a freely
available tool like #emph[veraPDF]#footnote[https:\/\/verapdf.org/home/].