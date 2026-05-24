# Unofficial typst template
for computer science and data science at Georg-August University Göttingen

## Why?

> Typst is like LaTeX but simpler, easier, faster, smaller, based on 40 years of experience but without 40 years of technical decisions. With a syntax reminiccent of Markdown, you can get going within minutes, without much learning nor painful debugging.

Our goals with this template are simple:

- Make writing a thesis fun and easy.
- Get you going immediately. No lengthy onboarding and no cleaning up later.
<!-- - Provide a drop-in replacement for the existing LaTeX templates from the university. -->
- Drop-in replacement: Mimick the look and feel of existing templates. Our experience is: Your supervisors won't notice, nor should they care!
    - The `legacy` preset mimicks [the official template from the CS institute](https://uni-goettingen.de/de/626775.html). This is optimized for double-sided printing.
    - The `modern` present loosley mimicks [this group's template](https://hps.vi4io.org/teaching/ressources/start). It is optimized for screen reading.
- Keep everything hackable / fixable. It's your thesis after all. Unlike LaTeX, fixing stuff is quite reasonable.
    - Note: You don't HAVE TO care! Just ignore everything in `lib/` and be happy.
- Stand-alone and archivable: Your thesis repo should include everything to reproduce your thesis as you wrote it.

We found that forking this repo is a better workflow than the official typst library and template structure. 
We don't plan to publish this template as a typst library + template. Typst libraries are not editable (without forking/copying) and one-shot documents like theses profit little from versioned libaries and their archivability is harmed by external dependencies.

## Getting started

1. Fork this repo. clone your fork
2. Run `make dev`
3. Open `main.typ` in your favorite text editor. Change something, save and `main.pdf` should automatically refresh.

A very convenient setup is VSCodium + [Tinymist Extension](https://open-vsx.org/extension/myriad-dreamin/tinymist).

## Attributions

- “Scroll” icon by Garis Tanam from [Noun Project](https://thenounproject.com/browse/icons/term/scroll/) CC BY 3.0
    - Modified by changing color, inserting text, and slightly moving the quill.

## License

The license for this template is CC0 1.0 but only applies to files where explicitly specified to avoid CC0 becoming the license of your thesis by accident. There are also parts of this repository that are different and even non-free licenses, e.g. fonts and university logos. Note that you might only use the university logos for university purposes. See the individual files and directories for more infomation.

All unspecified files in directories without licensing information, e.g. `content/content.typ`, are licensed as CC0 aswell but only on the `main` branch in the repository under https://gitlab.gwdg.de/glissmann/ugoe-cs-ds-typst-thesis. For your own forks, you may specify a different license.

When contributing to this repository, you do not contribute changes under these licenses but grant us rights e.g. to redistribute and relicense your contributions. See CONTRIBUTING.md.