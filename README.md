# osd-slides
`osd-slides` is a tool to download Prof. Paine's slides through terminal with one command. 

[![](https://img.shields.io/badge/project-link-green)](https://github.com/kkarakas/osd-slides)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub issues](https://img.shields.io/github/issues/kkarakas/osd-slides)

## Overview
- Open Software Development classes slides are hard to turn it to a pdf and download, this tool will help students to download slides easily. 

## Features
- Check if the slide were already downloaded and is the same version.
- Force download option eventough it already was downloaded
- Links that actually work on the slides
- Search through all the documents to find keywords

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