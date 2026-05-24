.PHONY: all build dev clean build-de dev-de build-all
all: build
build:
	typst compile --pdf-standard a-2b --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ main.typ
dev:
	typst watch --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ main.typ
build-de:
	typst compile --pdf-standard a-2b --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ main_de.typ
dev-de:
	typst watch --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ main_de.typ
build-all: build build-de
clean:
	rm -f main.pdf main_de.pdf
