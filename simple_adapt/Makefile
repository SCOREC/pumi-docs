simple_adapt.pdf : simple_adapt.tex \
edge_split.png edge_collapse.png edge_swap.png

%.pdf : %.tex
	pdflatex $<

%.png : %.mp
	mpost $<

