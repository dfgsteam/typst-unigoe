# Dynamic & Customizable Typst Thesis Template
for Georg-August-Universität Göttingen (and other Universities/Faculties)

This is a highly dynamic and customizable **unofficial Typst template** for writing Bachelor's and Master's theses. 

## Credits & Attribution

This project is a **fork** of the excellent unofficial Typst template for Computer Science and Data Science at Göttingen, originally created by **Lorenz Glißmann**. 
* Original Creator: [Lorenz Glißmann](https://gitlab.gwdg.de/glissmann/thesis-template)
* Original Repository: [gitlab.gwdg.de/glissmann/ugoe-cs-ds-typst-thesis](https://gitlab.gwdg.de/glissmann/ugoe-cs-ds-typst-thesis)

This fork extends the original design by making all elements (logos, departments, contact pages, localized titles, and cities) completely dynamic and customizable, allowing it to be easily adapted for other faculties (e.g., Physics, Chemistry, Economics) or other universities entirely, while retaining the beautiful original CS/DS style presets as the out-of-the-box defaults.

---

## Why Typst?

> Typst is like LaTeX but simpler, easier, faster, smaller, based on 40 years of experience but without 40 years of technical decisions. With a syntax reminiscent of Markdown, you can get going within minutes, without much learning nor painful debugging.

Our goals with this template are simple:
- **Make writing a thesis fun and easy.**
- **Get you going immediately.** No lengthy onboarding and no cleaning up later.
- **Dynamic Adaptability:** Easily switch between different faculties, universities, or customize branding elements without touching the core styling logic.
- **Drop-in replacement:** Mimic the look and feel of existing templates.
    - The `legacy` preset mimics [the official template from the CS institute](https://uni-goettingen.de/de/626775.html). This is optimized for double-sided printing.
    - The `modern` preset loosely mimics the modern screen-optimized layout.
- **Keep everything hackable / fixable:** It's your thesis after all. Unlike LaTeX, fixing stuff is quite reasonable.
- **Stand-alone and archivable:** Your thesis repo should include everything to reproduce your thesis as you wrote it.

---

## Dynamic Customization Options

You can customize almost every aspect of the thesis via the `config` dictionary in `main.typ`:

1. **Faculties & Institutions:**
   You can easily override individual preset translations (like `institution` or `university` name) directly in your configuration without redefining the preset:
   ```typst
   translations: (
     institution: [Faculty of Physics \ Institute for Astrophysics],
     university: "Georg-August-Universität Göttingen",
   )
   ```

2. **University Logo:**
   Override the default logo by specifying `logo` and `logo_width` in the config:
   ```typst
   logo: "/images/custom_logo.svg",
   logo_width: 5cm,
   ```

3. **Custom Contact Page:**
   The contact page is fully dynamic. If your faculty doesn't require a contact info page, you can disable it by setting `contact: none`. Otherwise, customize any details:
   ```typst
   contact: (
     university: "Georg-August-Universität Göttingen",
     address: [Friedrich-Hund-Platz 1 \ 37077 Göttingen \ Germany],
     phone: "+49 (551) 39-XXXX",
     email: "dekanat@physik.uni-goettingen.de",
     website: "www.physik.uni-goettingen.de",
   )
   ```

4. **Localization:**
   Abstract titles, bibliography titles, and cities are automatically localized based on the selected language (`lang: "de"` or `"en"`), and can also be overridden individually.

---

## Getting started

1. Clone your fork of this repository.
2. Run `make dev` to start hot-reloading compilation.
3. Open `main.typ` in your favorite text editor. Change something, save and `main.pdf` should automatically refresh.

A very convenient setup is VSCodium + [Tinymist Extension](https://open-vsx.org/extension/myriad-dreamin/tinymist).

---

## Attributions

- “Scroll” icon by Garis Tanam from [Noun Project](https://thenounproject.com/browse/icons/term/scroll/) CC BY 3.0 (Modified by changing color, inserting text, and slightly moving the quill).

---

## License

The license for this template is CC0 1.0 but only applies to files where explicitly specified to avoid CC0 becoming the license of your thesis by accident. See the individual files and directories for more information.