# 🎓 Dynamic & Customizable Typst Thesis, Seminar & Exposé Template
### For Georg-August-Universität Göttingen (and other Universities/Faculties)

This repository provides a modern, highly flexible, and **unofficial Typst template** for writing Bachelor's/Master's theses, seminar papers, or exposés (research proposals). 

This project is a **fork and extension** of the excellent unofficial Typst template for Computer Science and Data Science at Göttingen, originally created by [Lorenz Glißmann](https://gitlab.gwdg.de/glissmann/thesis-template). It extends the original design by making branding elements, degree presets, frontmatter layouts, and contact details completely dynamic, allowing it to be easily adapted for any university, faculty, or short-form academic paper.

---

## 🌟 Key Features

* 🏫 **Comprehensive Formats**: Built-in, localized presets for **Master's Theses**, **Bachelor's Theses**, **Seminar Papers**, and **Exposés** in both **German** (`de`) and **English** (`en`).
* 🛠️ **Interactive Setup Wizard**: Configure your entire project in seconds by running `python3 setup.py`.
* 🖊️ **Draft & Smart Todo Mode**: Enable `draft: true` to display a subtle `DRAFT` watermark across all pages and render custom `#todo("...")` blocks. Setting `draft: false` hides all watermark and todo boxes automatically for a clean final release.
* 📑 **Multi-Language Abstracts**: Pass a dictionary of abstracts (e.g. `(de: include "...", en: include "...")`) to automatically generate consecutive English and German abstract pages with correct localized headings.
* 📖 **Fully Optional Frontmatter**: Hide the Table of Contents (`show_outline: false`), skip the declaration page (`declaration: none`), or omit the contact page (`contact: none`) to perfectly suit short seminar papers or exposés.
* 📌 **Clean Appendix & Bibliography**: The bibliography compiles in standard format, while the appendix-specific formatting (e.g., heading numbering `A` and `Appendix A - 1` footers) only triggers if an `appendix` is actually supplied.
* ⚡ **CI/CD Automated Release Pipeline**: The repository is fully optimized to be slim and binary-free. All generated PDFs are ignored locally, and a **GitHub Actions Release Pipeline** compiles and attaches the compiled PDFs (`main.pdf` and `example.pdf`) directly to the GitHub Release on every pushed version tag (`v*`)!

---

## 📂 Repository Layout

```bash
├── main.typ          # Clean, ready-to-write starter document
├── example.typ       # Feature-rich preview showcase (compiled with draft mode on)
├── setup.py          # Interactive Python wizard to configure main.typ
├── Makefile          # Commands for local compilation and watching
├── lib/
│   ├── presets.typ   # Built-in German and English presets for all document types
│   ├── thesis.typ    # Main document layout, draft state, and todo logic
│   ├── style_*.typ   # Modern (screen-optimized) and Legacy (book-style) formats
│   └── pages/        # Dynamic layouts for title page, contact, declaration, abstract
├── content/
│   ├── content*.typ  # Actual chapter source files
│   ├── template.typ  # Comprehensive template guide showing math, figures, and formatting
│   ├── references.bib# Bibliography references in bibtex format
│   └── *.typ         # Abstract and declaration source files
└── images/           # Logos and branding assets
```

---

## 🚀 Getting Started

### 1. Initialize Your Document

You can initialize a brand new project in a fresh directory with a single terminal command:
```bash
curl -fsSL https://raw.githubusercontent.com/dfgsteam/typst-unigoe/main/init.sh | bash
```

Alternatively, you can manually clone this repository and run the setup script:
```bash
git clone https://github.com/dfgsteam/typst-unigoe.git my-thesis
cd my-thesis
python3 setup.py
```
The wizard will guide you through configuring your language, paper format, title, subtitle, author, student ID, and supervisors, generating a pristine `main.typ` instantly.

### 2. Local Compilation & Watching
Compile your document locally using the provided `Makefile`:
* **Compile main starter:** `make build` (Generates `main.pdf`)
* **Compile feature example:** `make build-example` (Generates `example.pdf`)
* **Live preview watching:** `make dev` (or `make dev-example`) watches files and recompiles instantly on save.

> **Convenience Tip**: We highly recommend using VSCodium/VS Code with the [Tinymist Typst Extension](https://open-vsx.org/extension/myriad-dreamin/tinymist) for an outstanding live-rendering side-by-side editing experience.

---

## 🤖 GitHub Actions CI/CD Pipeline

To keep your git history slim and fast, **pre-compiled binary PDFs are excluded from version control** (via `.gitignore`). 

When you are ready to publish a new version of your work:
1. Create a version tag and push it:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
2. The **GitHub Release Workflow** will automatically trigger, checkout the repository, install Typst, compile both `main.typ` and `example.typ`, and attach `main.pdf` and `example.pdf` as assets to a new GitHub Release.

---

## 📜 License

The license for this template is **CC0 1.0 Universal** (Public Domain), allowing you to modify, distribute, and use it freely for any purpose. 

*(Attribution to Lorenz Glißmann's original institute template is highly appreciated!)*