.PHONY: all build dev clean build-example dev-example build-all
all: build
build:
	typst compile --pdf-standard a-2b --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ main.typ
dev:
	typst watch --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ main.typ
build-example:
	typst compile --pdf-standard a-2b --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ example.typ
dev-example:
	typst watch --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ example.typ
build-all: build build-example
clean:
	rm -f main.pdf example.pdf
