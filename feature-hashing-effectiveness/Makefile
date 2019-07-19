LATEXMK = latexmk -r latexmk.rc

all: pydata_london_2019.pdf

%.pdf: %.tex
	$(LATEXMK) -gg -pdf -xelatex -shell-escape -use-make $<
	$(LATEXMK) -c

clean:
	$(LATEXMK) -C
