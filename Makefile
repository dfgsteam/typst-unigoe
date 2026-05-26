.PHONY: all build dev clean build-example dev-example build-presentation dev-presentation build-all
all: build
build:
	typst compile --pdf-standard a-2b --font-path lib/fplneu-otf/ --font-path lib/Noto_Color_Emoji/ main.typ
dev:
	typst watch --font-path lib/fplneu-otf/ --font-path lib/Noto_Color_Emoji/ main.typ
build-example:
	typst compile --pdf-standard a-2b --font-path lib/fplneu-otf/ --font-path lib/Noto_Color_Emoji/ example.typ
dev-example:
	typst watch --font-path lib/fplneu-otf/ --font-path lib/Noto_Color_Emoji/ example.typ
build-presentation:
	typst compile --pdf-standard a-2b --font-path lib/fplneu-otf/ --font-path lib/Noto_Color_Emoji/ presentation.typ
dev-presentation:
	typst watch --font-path lib/fplneu-otf/ --font-path lib/Noto_Color_Emoji/ presentation.typ
build-all: build build-example build-presentation
clean:
	rm -f main.pdf example.pdf presentation.pdf
