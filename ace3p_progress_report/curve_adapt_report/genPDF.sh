#!/bin/bash

# showing the list of all the tex files in the folder
texFiles=(*.tex)

if [ ${#texFiles[*]} = 1 ]; then
	job=0
else
	count=1;
	for file in ${texFiles[*]}; do
		echo "$count) $file"
		let "count += 1" 
	done

	# letting the user choose an option
	echo "Enter a number to compile!"
	read job
	let "job -= 1"
fi
# the final file to be compiled 
file=${texFiles[$job]}

# actual compilations

pdflatex $file
bname=$(basename $file .tex)

# echo "Running BibTex"
# bibtex $bname &> /dev/null

echo "Running Index Make"
cmd="makeindex ${bname}.nlo -s nomencl.ist -o ${bname}.nls -t ${bname}.nlg"
eval $cmd

echo "Running Latex Again"
pdflatex $file &> /dev/null

# echo "Creating PS and PDF files"
# dvips "$(basename $file .tex).dvi" &> /dev/null
# ps2pdf "$(basename $file .tex).ps" &> /dev/null
