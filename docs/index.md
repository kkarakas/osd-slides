
Welcome to osd-slides's documentation!
======================================
```{eval-rst}
.. toctree::
   :maxdepth: 2
   :caption: Contents
      
```
# How to Install

Install osd-slides by running below in shell.
```sh
pip install osd-slides
```
This library uses [Decktape](https://github.com/astefanutti/decktape).
To install decktape, run below in shell.
```sh
$ npm install decktape
```
You will need node.js on your computer for above to run.
Check if node.js in your computer by running this below in shell. And then check the version of npm.
You might want to restart your terminal/powershell after installing node.js.
```sh
$ Node --version
$ npm --version
```
# How to use

Users can download files by calling searchAndDownloadPdf().
```python
import osd-slides
downloader = osd-slides.Downloader()
downloader.searchAndDownloadPdf()
```

Users can view what files can be downloaded by calling showDownloadablePdf()
```python
import osd-slides
downloader = osd-slides.Downloader()
downloader.showDownloadablePdf()
```

# Example
Running this below will printout all the files available for download.
```python
import osd-slides
downloader = osd-slides.Downloader()
downloader.showDownloadablePdf()
```

# Methods
```{eval-rst}
.. autofunction:: osd_slides.main.searchAndDownloadPdf
.. autofunction:: osd_slides.main.showDownloadablePdf
```

```{eval-rst}
.. note: 
   Blah Blah blah
```

```{eval-rst}
.. toctree::
   :maxdepth: 1
   :caption: Contents

   modules
 ```