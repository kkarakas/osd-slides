# osd-slides
`osd-slides` is a tool to download Prof. Paine's slides through terminal with one command. 

[![](https://img.shields.io/badge/project-link-green)](https://github.com/kkarakas/osd-slides)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub issues](https://img.shields.io/github/issues/kkarakas/osd-slides)
[![codecov](https://codecov.io/gh/kkarakas/osd-slides/branch/main/graph/badge.svg?token=0TCR1MSIWH)](https://codecov.io/gh/kkarakas/osd-slides)
![build](https://img.shields.io/github/actions/workflow/status/kkarakas/osd-slides/build.yaml)
[![PyPI](https://img.shields.io/pypi/v/osd-slides)](https://pypi.org/project/osd-slides/)

## Overview
- Open Software Development classes slides are hard to turn it to a pdf and download, this tool will help students to download slides easily. 

## Features
- Download osd slides.
- Force download option eventough it already was downloaded

## Install
```sh
pip install osd-slides
```
## Dependencies
- Uses Decktape: https://github.com/astefanutti/decktape

To install decktape, run in osd-slides.
```sh
$ npm install decktape
```
You will need node.js on your computer for above to run.
Check if node.js in your computer by running this. And then check the version of npm.
You might want to restart your terminal/powershell after installing node.js.
```sh
$ Node --version
$ npm --version
```

## How to use
To show downloadable files. 
You must be in directory where `__main__.py` is located.
```sh
$ python ./__main__.py show
```
To download all the files.
You must be in directory where `__main__.py` is located.
It will take 30 minutes to download all the files.
```sh
$ python ./__main__.py download
```
