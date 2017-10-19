---
layout: post
title:  "Managing your Bibliography with Zotero and Google Drive"
category: Programming
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

Download and install [ZotFile](http://zotfile.com/) like any other Zotero plugin. Then inside Zotero go to `Tools > ZotFile Preferences > General Settings > Location of Files`. Select *Custom Location* and select the same base directory you used in the step above.

You can also setup ZotFile to store the attachments into subfolders according to rules that depend on the metadata of the files by changing *"Use subfolder defined by"*. For myself, I set it to `/%T` which corresponds to the item type.



### Auto Backup of Zotero Data Directory

Since Zotero metadata are saved at the [Zotero Data Directory](https://www.zotero.org/support/zotero_data), it is important to keep an updated backup of this directory. Otherwise you are at risk of losing all your tags, web links, etc. To accomplish this I set up a cron job to be run every friday:

1. Open a terminal and run `crontab -e`
2. Append the following line to the file:
```bash
0 0 * * FRI zip /path/to/zoterobackup.zip /path/to/Zotero/ -r
```
3. Save the file and make sure the cron is set by running `crontab -l`


## Viewing and annotating your PDFs

Recently I found out that [PDF-XChange Editor](https://www.tracker-software.com/product/pdf-xchange-editor) works gracefully with [Wine](https://en.wikipedia.org/wiki/Wine_(software)). I have tried a lot of PDF editors and viewers for Linux and this one is the best by far. Highly recommended.

For your Android device, you will want a PDF viewer that allows you to annotate the document and that is also capable of syncing with Google Drive, since all the attachments will be there. Unfortunately, the default PDF viewer for Google Drive app is not capable of annotating the document, so we have to resort to an external tool. I tested few of them and the one that worked best for me was [XODO PDF Reader & Annotator](https://www.xodo.com/).
