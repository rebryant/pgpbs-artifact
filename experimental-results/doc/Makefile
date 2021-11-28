INTERP=python3
DGEN = $(INTERP) ./gen-data.py
OSRCDATA = ../original-data/csv
RSRCDATA = ../reproduced-data/csv
ODESTDATA = original-data
RDESTDATA = reproduced-data

CTHRESH=100000000
NTHRESH=128

graphs.pdf: graphs.tex 
	pdflatex graphs
	pdflatex graphs


data: odata rdata


odata:
	rm -rf $(ODESTDATA)
	mkdir $(ODESTDATA) 
	# Urquhart
	$(DGEN)  -y $(CTHRESH) < $(OSRCDATA)/urquhart-simon-kissat.csv | sed 's/addplot/addplot[only marks, color=medgreen!60!black, mark=*]/g' \
		> $(ODESTDATA)/urquhart-simon-kissat.tex
	$(DGEN)  -y $(CTHRESH) < $(OSRCDATA)/urquhart-simon-bucket.csv | sed 's/addplot/addplot[only marks, medgreen!80!black, mark=triangle*]/g' \
		> $(ODESTDATA)/urquhart-simon-bucket.tex
	$(DGEN)  -y $(CTHRESH) < $(OSRCDATA)/urquhart-simon-equation.csv | sed 's/addplot/addplot[only marks, medgreen, mark = diamond*]/g' \
		> $(ODESTDATA)/urquhart-simon-equation.tex
	$(DGEN)  -y $(CTHRESH) < $(OSRCDATA)/urquhart-li-bucket.csv | sed 's/addplot/addplot[color=darkred!80!black, mark=triangle*, thick]/g' \
		> $(ODESTDATA)/urquhart-li-bucket.tex
	$(DGEN)  -y $(CTHRESH) < $(OSRCDATA)/urquhart-li-equation.csv |  sed 's/addplot/addplot[color=darkred, mark=diamond*, thick]/g' \
		> $(ODESTDATA)/urquhart-li-equation.tex
	# Chess
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/chess-kissat.csv | sed 's/addplot/addplot[color=medgreen, mark=*, thick]/g' \
		> $(ODESTDATA)/chess-kissat.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/chess-column.csv | sed 's/addplot/addplot[color=darkpurple, mark=triangle*, thick]/g' \
		> $(ODESTDATA)/chess-column.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/chess-equation-integer.csv | sed 's/addplot/addplot[color=midblue, mark=diamond*, thick]/g' \
		> $(ODESTDATA)/chess-equation-integer.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/chess-equation-mod3.csv | sed 's/addplot/addplot[color=clearpurple, mark=diamond*, thick]/g' \
		> $(ODESTDATA)/chess-equation-mod3.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/chess-board-column-randomorder.csv | sed 's/addplot/addplot[color=darkpurple, mark=triangle*, thick]/g' \
		> $(ODESTDATA)/chess-board-column-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/chess-board-equation-randomorder.csv | sed 's/addplot/addplot[color=darkpurple, mark=diamond*, thick]/g' \
		> $(ODESTDATA)/chess-board-equation-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/chess-torus-column.csv | sed 's/addplot/addplot[color=medgreen, mark=triangle*, thick]/g' \
		> $(ODESTDATA)/chess-torus-column.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/chess-torus-equation-randomorder.csv | sed 's/addplot/addplot[color=medgreen, mark=diamond*, thick]/g' \
		> $(ODESTDATA)/chess-torus-equation-randomorder.tex
	# Pigeon
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/pigeon-direct-kissat.csv | sed 's/addplot/addplot[color=redpurple, mark=*, thick]/g' \
		> $(ODESTDATA)/pigeon-direct-kissat.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/pigeon-sinz-kissat.csv | sed 's/addplot/addplot[color=medgreen, mark=*, thick]/g' \
		> $(ODESTDATA)/pigeon-sinz-kissat.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/pigeon-direct-linear-inputorder.csv | sed 's/addplot/addplot[color=clearorange, mark=triangle*, thick]/g' \
		> $(ODESTDATA)/pigeon-direct-linear-inputorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/pigeon-sinz-column-inputorder.csv | sed 's/addplot/addplot[color=darkturquoise, mark=triangle*, thick]/g' \
		> $(ODESTDATA)/pigeon-sinz-column-inputorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/pigeon-sinz-constraint-randomorder.csv | sed 's/addplot/addplot[color=bluegray, mark=diamond*, thick]/g' \
		> $(ODESTDATA)/pigeon-sinz-constraint-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/pigeon-direct-constraint-randomorder.csv | sed 's/addplot/addplot[color=bluegray, mark=diamond*, thick]/g' \
		> $(ODESTDATA)/pigeon-direct-constraint-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/pigeon-sinz-equation-randomorder.csv | sed 's/addplot/addplot[color=browngreen, mark=diamond*, thick]/g' \
		> $(ODESTDATA)/pigeon-sinz-equation-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(OSRCDATA)/pigeon-direct-cook.csv | sed 's/addplot/addplot[color=midblue, mark=pentagon*, thick]/g' \
		> $(ODESTDATA)/pigeon-direct-cook.tex

rdata:
	rm -rf $(RDESTDATA)
	mkdir $(RDESTDATA) 
	# Urquhart
	$(DGEN)  -y $(CTHRESH) < $(RSRCDATA)/urquhart-simon-bucket.csv | sed 's/addplot/addplot[only marks, medgreen!80!black, mark=triangle*]/g' \
		> $(RDESTDATA)/urquhart-simon-bucket.tex
	$(DGEN)  -y $(CTHRESH) < $(RSRCDATA)/urquhart-simon-equation.csv | sed 's/addplot/addplot[only marks, medgreen, mark = diamond*]/g' \
		> $(RDESTDATA)/urquhart-simon-equation.tex
	$(DGEN)  -y $(CTHRESH) < $(RSRCDATA)/urquhart-li-bucket.csv | sed 's/addplot/addplot[color=darkred!80!black, mark=triangle*, thick]/g' \
		> $(RDESTDATA)/urquhart-li-bucket.tex
	$(DGEN)  -y $(CTHRESH) < $(RSRCDATA)/urquhart-li-equation.csv |  sed 's/addplot/addplot[color=darkred, mark=diamond*, thick]/g' \
		> $(RDESTDATA)/urquhart-li-equation.tex
	# Chess
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/chess-column.csv | sed 's/addplot/addplot[color=darkpurple, mark=triangle*, thick]/g' \
		> $(RDESTDATA)/chess-column.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/chess-equation-integer.csv | sed 's/addplot/addplot[color=midblue, mark=diamond*, thick]/g' \
		> $(RDESTDATA)/chess-equation-integer.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/chess-equation-mod3.csv | sed 's/addplot/addplot[color=clearpurple, mark=diamond*, thick]/g' \
		> $(RDESTDATA)/chess-equation-mod3.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/chess-board-column-randomorder.csv | sed 's/addplot/addplot[color=darkpurple, mark=triangle*, thick]/g' \
		> $(RDESTDATA)/chess-board-column-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/chess-board-equation-randomorder.csv | sed 's/addplot/addplot[color=darkpurple, mark=diamond*, thick]/g' \
		> $(RDESTDATA)/chess-board-equation-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/chess-torus-column.csv | sed 's/addplot/addplot[color=medgreen, mark=triangle*, thick]/g' \
		> $(RDESTDATA)/chess-torus-column.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/chess-torus-equation-randomorder.csv | sed 's/addplot/addplot[color=medgreen, mark=diamond*, thick]/g' \
		> $(RDESTDATA)/chess-torus-equation-randomorder.tex
	# Pigeon
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/pigeon-direct-linear-inputorder.csv | sed 's/addplot/addplot[color=clearorange, mark=triangle*, thick]/g' \
		> $(RDESTDATA)/pigeon-direct-linear-inputorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/pigeon-sinz-column-inputorder.csv | sed 's/addplot/addplot[color=darkturquoise, mark=triangle*, thick]/g' \
		> $(RDESTDATA)/pigeon-sinz-column-inputorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/pigeon-sinz-constraint-randomorder.csv | sed 's/addplot/addplot[color=bluegray, mark=diamond*, thick]/g' \
		> $(RDESTDATA)/pigeon-sinz-constraint-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/pigeon-direct-constraint-randomorder.csv | sed 's/addplot/addplot[color=bluegray, mark=diamond*, thick]/g' \
		> $(RDESTDATA)/pigeon-direct-constraint-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/pigeon-sinz-equation-randomorder.csv | sed 's/addplot/addplot[color=browngreen, mark=diamond*, thick]/g' \
		> $(RDESTDATA)/pigeon-sinz-equation-randomorder.tex
	$(DGEN) -y $(CTHRESH) -x $(NTHRESH)  < $(RSRCDATA)/pigeon-direct-cook.csv | sed 's/addplot/addplot[color=midblue, mark=pentagon*, thick]/g' \
		> $(RDESTDATA)/pigeon-direct-cook.tex


clean:

	rm -f *~ *.log

