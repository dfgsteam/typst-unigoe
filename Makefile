.PHONY: all build dev clean
all: build
build:
	typst compile --pdf-standard a-2b --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ main.typ
dev:
	typst watch --font-path lib/fplneu-otf/:lib/Noto_Color_Emoji/ main.typ
clean:
	rm -f main.pdf
