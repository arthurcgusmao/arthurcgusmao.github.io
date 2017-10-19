---
layout: post
title: "Seeing python's logging messages in a Jupyter Notebook"
category: Programming
date: 2017-06-18
---

Originally answered [in stackoverflow](https://stackoverflow.com/a/41060201/5103881).

`stderr` is the default stream for the logging module, so in IPython and Jupyter notebooks you
might not see anything unless you configure the stream to `stdout`:

```python
import logging
import sys

logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                     level=logging.INFO, stream=sys.stdout)

logging.info('Hello world!')
```
