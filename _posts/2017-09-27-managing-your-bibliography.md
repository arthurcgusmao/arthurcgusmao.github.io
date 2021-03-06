---
layout: post
title:  "Managing your Bibliography with Zotero and Google Drive"
category: Academia
---

This post is a guide for setting up a bunch of softwares that will allow you to have a great free tool for managing bibliography in your computer (Zotero) together with a complete backup of all your data, including metadata like tags and notes, and access to all PDFs in another mobile device like Android. To accomplish this, we are going to use the following tools:

- Google Drive
- Zotero
- ZotFile plugin for Zotero
- Zotero Connector for Google Chrome
- PDF-XChange Editor
- Xodo PDF Reader & Editor

The role of Google Drive here is to sync your attachments (usually the PDF of the papers you saved) across all your devices and also assure you have a free backup in the cloud. The great win of this setup is that you probably will have a lot more space free in your Google Drive that the free storage limit that Zotero allows for. Then Zotero will be used only for managing the bibliography itself. ZotFile is a plugin that will help us with saving the attachments to the right location, so they can be in a place synced with Google Drive. The last three tools really depend on your operating systems and browser of choice, they were put here thinking of someone that uses Linux with Google Chrome and Android.


## Zotero configuration


### Saving the PDFs outside Zotero Data Directory

We are going to use Google Drive to keep a copy of each PDF in the cloud. Therefore, we must configure Zotero to use relative paths for linked file attachments. It can be done by, inside Zotero, going to `Edit > Preferences > Advanced > Linked Attachment Base Directory` and choosing the Base Directory where you'll want to save your files.

However, this only guarantees that Zotero will be able to find attached files that are located in the selected directory above, but will *not* automatically save new downloaded files there (e.g., files downloaded via the [Zotero Connector for Google Chrome](https://chrome.google.com/webstore/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc?hl=en) will still be saved into the Data Directory). To change this behavior, we'll use a Zotero plugin named ZotFile.


### Setting up ZotFile

Download and install [ZotFile](http://zotfile.com/) like any other Zotero plugin. Then inside Zotero go to `Tools > ZotFile Preferences > General Settings > Location of Files`. Select *Custom Location* and select the same base directory you used in the step above. Be sure to uncheck the option `Automatically rename attachments files using parent metadata` in Zotero (same location as in *automatic saving of snapshots* --- see *Other configurations* section below), I found that when this was checked ZotFile would not be able to move the file to the desired location.

You can also setup ZotFile to store the attachments into subfolders according to rules that depend on the metadata of the files by changing *"Use subfolder defined by"*. For myself, I set it to `/%T` which corresponds to the item type.



### Auto Backup of Zotero Data Directory

Since Zotero metadata are saved at the [Zotero Data Directory](https://www.zotero.org/support/zotero_data), it is important to keep an updated backup of it. Otherwise you are at risk of losing all your tags, web links, etc. To make sure a backup would be run everyday I used anacron, following the steps proposed by [this answer](https://askubuntu.com/a/235090). The anacron command I used was:
```bash
1   5   zotero.backup   zip /path/to/zoterobackup.zip /path/to/Zotero/ -r
```




## Viewing and annotating your PDFs

Recently I found out that [PDF-XChange Editor](https://www.tracker-software.com/product/pdf-xchange-editor) works gracefully with [Wine](https://en.wikipedia.org/wiki/Wine_(software)). I have tried a lot of PDF editors and viewers for Linux and this one is the best by far. Highly recommended. From my personal experience, I found that the newest version (7.0.324.3) was somewhat buggy in the 64 bit version, so I installed the 32 bit one and the problems were gone.

Edit 2020-11-15: Recently I came across [Master PDF](https://code-industry.net/free-pdf-editor/), an alternative PDF editor that runs natively on Linux, without the need for Wine. I have been using it for the last weeks successfully instead of PDF-XChange.

<!-- An interesting thing for you to do if you want to default the opening of PDF files to evince but make an exception to open them with PDF-XChange when in a specific directory is [this script](https://gist.github.com/slowkow/8834315):
```bash
#!/bin/bash

# Check if the pdf is in the Zotero folder.
if [[ "$1" == */Bibliography/* ]]
then
    wine '/home/arthurcgusmao/.wine/drive_c/Program Files (x86)/PDF Editor/PDFXEdit.exe' "$1"
else
    evince "$1"
fi
```
Place the script above into `~/.local/bin/` and set it as the default PDF program:

1. Open `~/.local/share/applications/defaults.list`
2. Add `application/pdf=scriptabove` -->

For your Android device, you will want a PDF viewer that allows you to annotate the document and that is also capable of syncing with Google Drive, since all the attachments will be there. Unfortunately, the default PDF viewer for Google Drive app is not capable of annotating the document, so we have to resort to an external tool. I tested few of them and the one that worked best for me was [XODO PDF Reader & Annotator](https://www.xodo.com/).


## Other configurations

### Recursive subcollections in Zotero

By default Zotero does not list items of sub-collections in the item-list. You can modify that through the [recursive collections](https://forums.zotero.org/discussion/3317/recursive-display-of-all-items-of-a-collection-and-its-subcollections/#Comment_14225) advanced option:


![Set the custom variable `extensions.zotero.recursiveCollections` to true by double clicking over the Value column in the respective line.][img:zotsubcol]

[img:zotsubcol]: /images/posts/zotero_recursivecollections.png


### Disable automatic saving of snapshots

One feature that can be annoying is that the Zotero connector for chrome will automatically save a snapshot from sites like arxiv. This can be disabled in `Preferences > General > File Handling`:

![Uncheck the checkbox to disable automatic saving of snapshots.][img:zotdissnap]

[img:zotdissnap]: /images/posts/zotero_disable_snapshots.png


### Automate `.bib` file generation

[zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex) is a plugin that can automate bibtex exporting, among other utilities. This is crucial for removing the distraction of having to regenerate your `.bib` file every time you add another item to your library.
