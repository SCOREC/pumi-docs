target=hps
outdir=build
${target}.pdf: ${target}.tex
	pdflatex -output-directory=${outdir} $<
	bibtex ${outdir}/${target}
	pdflatex -output-directory=${outdir} $<
	pdflatex -output-directory=${outdir} $<
clean:
	rm -rf ${outdir}/*
