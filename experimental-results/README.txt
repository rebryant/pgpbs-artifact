This directory includes the original data from the paper, plus the
ability to reproduce a portion of this data.

Makefile options:

data:
  Regenerate a portion of the results and combine the data into a
  set of graphs comparing the original results to the regenerated ones.

clean:
  Remove extraneous files

superclean:
  Remove generated result files

Subdirectories:

  original-results:
      The data files used in the paper.  These are organized into
      files fig4, fig5, fig6, and fig7, corresponding to the figure
      numbers in the paper.

  reproduced-results:

      The files needed to reproduce a portion of the experimental
      results.  These are organized into
      files fig4, fig5, fig6, and fig7, corresponding to the figure
      numbers in the paper.

  doc:
      The files required to generate the graph document
