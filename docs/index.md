
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
from osd-slides.osd_slides.main import Downloader
downloader = Downloader()
downloader.searchAndDownloadPdf()
```

Users can view what files can be downloaded by calling showDownloadablePdf()
```python
from osd-slides.osd_slides.main import Downloader
downloader = Downloader()
downloader.showDownloadablePdf()
```
Users can search for keywords in slides and open the exact slide the keyword exists.
```python
from osd-slides.osd_slides.search import Search
url = "https://www.cs.columbia.edu/~paine/4995/lectures/"
search = Search(url, ["22-legal.html","21-econ.html"])
search.lookup("Legal")
search.open(1)
```
 
# How to use Search in Detail

There are two ways of interacting with Search. One is running the program from command line. 
Second is to use it as a library.

### On Command Line

First execute the tool by by running __main__.py with python with search parameter.
```sh
$ python osd-slides/osd_slides/__main__.py search
```
Then you will be prompted with 
```console
Which slides would you like to search in? Please provide slides with spaces between them: 
```
As the output suggests type slides that you would like to search in input with spaces between them. For example type :
```console
22-legal.html 21-econ.html
```
If you want to know what slides you can search, you can run downloader.showDownloadablePdf()
After that, you will be prompted with 
```console
Slides reading completed
What keyword would you like to look up: 
```
Type the keyword you want to look up.
You will receive a list that contains tuples of all the occurrences of the keyword.
Each tuple will contain left-right index and up-down index of slides and name of the slide.

```console
[(1, 0, '22-legal.html'), (1, 1, '22-legal.html'), (2, 0, '22-legal.html')]
Which one would you like to open? please provide the number.
```
Finally select one of them to open on your default browser. 
Indexing starts with 1 so the leftmost one is 1 and the following is 2.
Make sure your input is not out of bounds.


### As a Library 

First import Search class.
```python
from osd-slides.osd_slides.search import Search
```
Then initialize search object by calling it with url and slides.
If url is not given as a argument default one is used.
Slides is given in argument as a list of slide names.
```python
search = Search(slides= ["22-legal.html","21-econ.html"])
```
Then lookup the desired word. 
In the example below we are looking up 'Legal'.
It will print out if it finds any results and 
if found it will print the locations of it.
First number is index of left-right and second number is index of up-down
and the third string is name of slide it was found.
```python
search.lookup("Legal")
```
Finally open the desired result by giving index as an argument.
Without argument, it will open the first one.
```python
search.open(1)
```
Make sure to call lookup(keyword) beforehand. 




[//]: # (# Methods)
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