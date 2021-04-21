# Overview of this Book

## Run CESM
* Download CESM codebase
* Create a case
* (Modify a component - ex. MARBL)
* Run case

## Apply post-processing workflow
* Convert from history to timeseries files
* Create intake-esm catalog to easily read in data
    * ***If you already have CESM model output, you can start after this point***

## Run Diagnostics/Analysis
* Using various notebooks, read in data, operate on data, cache output
* Individual calcualtions could be used here, using packages such as pop-tools

## Visualize Output
* Output plots to disk
* Generate a catalog with the relevant metadata to create a dashboard
* Create a dashboard visualizing plots, where the plots are stored on a CGD machine or AWS


```{toctree}
:hidden:
:titlesonly:
:caption: Run CESM

BuildCESMcase.ipynb
```


```{toctree}
:hidden:
:titlesonly:
:caption: Apply Post-Processing

post_process.ipynb
```


```{toctree}
:hidden:
:titlesonly:
:caption: Run Diagnostics/Analysis

diagnostics.ipynb
```


```{toctree}
:hidden:
:titlesonly:
:caption: Visualize Output

visualization.ipynb
```
