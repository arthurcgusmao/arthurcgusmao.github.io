---
layout: post
title:  "Markdown and Pandoc for academic writing"
category: Academia
---


## Introduction

In this post we are interested in using Markdown to produce great quality, scientific PDF files. This includes being able to use most of the capabilities that LaTeX has directly in Markdown. In order to do that we resort to a library named Pandoc, which is able to convert documents from one format to another seamlessly.

Before jumping into the technical details though, we first present what are these tools, for the unfamiliar reader, and our motivation.


### Markdown

Wikipedia defines Markdown as a lightweight markup language with plain text formatting syntax.

It lets you easily define headings, use basic text formatting tools such as bold, italics and underlines, place links and images, etc. A quick demonstration can be found [here](http://www.unexpected-vortices.com/sw/rippledoc/quick-markdown-example.html).


### Pandoc

From [its website](https://pandoc.org/MANUAL.html):

> Pandoc is a Haskell library for converting from one markup format to another, and a command-line tool that uses this library.

Examples of the markups that Pandoc handles are HTML (.html), Microsoft Word (.docx), LaTeX and LaTeX Beamer (.tex), Markdown (.md), Org mode (.org), PDF (.pdf), among many, many others.

Looking at the list above, one can see the power of Pandoc. It has everything we need to achieve our proposed writing framework.


## Motivation

Since LaTeX already works the way we want (and does it pretty well), why would we want to mess with that and change an entire framework that has been working great for years?

Well, we are not really giving up LaTeX. Pandoc uses LaTeX to produce the final PDF file, so what we are actually doing is incorporating everything that is good in LaTeX into a simpler markup language, where editing the source code is more visual appealing and easier to understand:

- Commands and markup are simpler than in LaTeX.
- The raw file is more readable.
- You can use LaTeX directly in Markdown.
- It's possible to convert the Markdown input file to LaTeX (or other formats) if necessary, in case it's really not possible to do what you want directly in Markdown.

Now let's see how to configure our desired environment.




## Configuration


### Installing Pandoc

Installing Pandoc is very easy, since they provide package installers for many different platforms. See [this link](https://pandoc.org/installing.html).


### Installing Pandoc filters

The Pandoc command (command line) has an option to pass filters, which are like extensions to the internal representation that Pandoc creates when reading/writing documents. For a more in depth explanation see [the docs](https://pandoc.org/filters.html).

What we need to know here is that there are some functionalities that LaTeX has are not built-in in Pandoc, and we will need filters for that.

Filters are easy to install and they are usually well documented. [A list](https://github.com/jgm/pandoc/wiki/Pandoc-Filters) of third party filters can be found on the wiki.

After you have installed a new filter, remember that it should be in your executable path in order to be easily accessible. If you are using an environment manager for Python such as [conda](https://conda.io/) and installed a filter through pip, consider copying the executable to a more general path. For instance:

```bash
$ sudo cp ~/.anaconda2/bin/pandoc-fignos /usr/local/bin/
```

Below are some of the filters that I personally use:

- [`pandoc-fignos`](https://github.com/tomduck/pandoc-fignos) for figure numbering and referencing.
- [`pandoc-eqnos`](https://github.com/tomduck/pandoc-eqnos) for equation numbers.
- [`pandoc-citeproc`](https://github.com/jgm/pandoc-citeproc) for citations and bibliography.


## Usage

### Executing Pandoc via the command line

Pandoc can be easily executed via the command line. The simplest form would be:

```bash
$ pandoc input.md -o output.pdf
```

Look at how it works smoothly: Pandoc automatically see the format of the output you are trying to produce and generates the correct one.

If you are creating a more complex document, however, you will need to provide more information, such as filters. Keep in mind that the order of the filters matter, since some filters may. An example of a more complex call to the command is:


```bash
pandoc input.md -o output.pdf --filter=pandoc-fignos --filter=pandoc-eqnos --filter=pandoc-citeproc --number-sections
```


### Executing Pandoc in Atom (text editor)

If you write lots of Markdown files, [Atom](http://atom.io) is the number one editor you should try. It has great built-in functionality, such as a Markdown previewer which lets you see how the final document is rendered on the fly.

However, there an extension of the default previewer, named [Markdown Preview Enhanced](https://github.com/shd101wyy/markdown-preview-enhanced) which really makes the experience of writing in Markdown incredible. It has features like auto-syncing the preview with the source code, automatically managing images, applying pandoc filters to the preview, among others.

Once you setup all the Pandoc filters you are using in this package, you will have an almost instantly preview of your document (that sinchronizes even when scrolled), in the same way that it will be produced by Pandoc. This makes the experience of writing really delightful. Since the package is well documented, I am only going to outline some features of it.

What is more relevant for our purposes is that the package is capable of calling Pandoc and producing a pdf file. This is useful because otherwise we would have to open a terminal and execute the command, remembering to pass in all the filters and whatever would be necessary. To create the pdf document, you simply right-click at the preview and select Pandoc. Please look at the package's configurations for more details. It is possible to configure options for how each document will be produced separately, such as export path, table of contents, and even LaTeX options. More details for that in [this link](https://shd101wyy.github.io/markdown-preview-enhanced/#/pandoc-pdf).

Another very interesting thing that Markdown Preview Enhanced helps is in making beautiful presentations. Check out [this introduction](https://rawgit.com/shd101wyy/markdown-preview-enhanced/master/docs/presentation-intro.html) for a glimpse.

There is also a good topic on many other packages that you may find useful in [Atom's discussion forum](https://discuss.atom.io/t/using-atom-for-academic-writing/19222).



## A YAML front matter template

Here is a template of a YAML front matter that I personally use in my documents:

```
---
title: "Your title here"
abstract: "Your abstract here"
author: Arthur


###
### Bibliography settings
###
bibliography:
    - /home/arthurcgusmao/Documents/zotero.bib
#csl: /home/arthurcgusmao/.csl/apa.csl
link-citations: true


###
### Formatting settings
###
documentclass: article
fontsize: 12pt
#geometry: margin=1.0in
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
header-includes:
    - \usepackage{times}
urlcolor: blue


###
### Markdown Preview Enhanced package settings
###
output:
    pdf_document:
        toc: false
        number_sections: true
---
```
