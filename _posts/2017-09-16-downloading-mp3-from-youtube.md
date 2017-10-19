---
layout: post
title:  "Downloading MP3 audio from YouTube"
category: Programming
---

This is a simple tutorial to easily download lots of mp3 audios from YouTube videos. We are going to create a python script that uses [`youtube-dl`](https://rg3.github.io/youtube-dl/) to download and convert to audios the videos we are interested in, from an initial list of videos.

1. Make sure you have [`youtube-dl`](https://rg3.github.io/youtube-dl/) installed;
2. Make a .txt file named `list.txt` where each line corresponds to a link from a YouTube video;
3. Save and run the python script below.

```python
with file('list.txt') as f:
    list_ = f.read()
    f.close()

for l,line in enumerate(list_.split('\n')):
    if len(line) > 0:
        comm = "youtube-dl --extract-audio --audio-format mp3 -l " + line
        res = subprocess.call([comm], shell=True)
        print(res)

```

Example of .txt file:

```
https://www.youtube.com/watch?v=hYZmK46--Mc&index=2&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=0j7dwG1cXc4&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=3
https://www.youtube.com/watch?v=JhV9f1l3H1A&index=4&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=GcNGtZPPSS8&index=5&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=ulam38XpQG4&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=6
https://www.youtube.com/watch?v=rBq-EPieRwU&index=7&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=Pv9Cs3FB2vQ&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=8
https://www.youtube.com/watch?v=WWs6GBwXnmw&index=9&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=GPPdWfoeGbs&index=10&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=ijSng_X9soc&index=11&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=ayEoiU5MOg4&index=12&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=XulpS3cAkOM&index=13&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=2gFLwkeJYB4&index=14&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=sem-8FpR10U&index=15&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=4Eo6zIcEYhk&index=16&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=W7bRGzFt2oE&index=17&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=GfF7EpHXyDY&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=18
https://www.youtube.com/watch?v=5WSlkzz2_Bk&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=19
https://www.youtube.com/watch?v=2_18oWkVq08&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=20
https://www.youtube.com/watch?v=6p6pKehb7Rk&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=21
https://www.youtube.com/watch?v=dSfZgygLjiw&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=22
https://www.youtube.com/watch?v=MJJj0BBrWOE&index=23&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
https://www.youtube.com/watch?v=Fyq8pT8IpCQ&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY&index=24
https://www.youtube.com/watch?v=mggupbkTmWc&index=25&list=PLFfM65xLnO-GvqhGu5vyM1vdm_CGkdQOY
```
