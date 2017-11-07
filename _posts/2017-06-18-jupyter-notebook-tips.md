---
layout: post
#title: "Seeing python's logging messages in a Jupyter Notebook"
title: "Jupyter Notebook Tips"
category: Programming
date: 2017-06-18
---

## Seeing python's logging messages in a Jupyter Notebook

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


## Truncating pandas float display

```python
# changes default formatting of float to 3 decimal places
pd.options.display.float_format = '{:.3f}'.format
```

<!--
## Matplotlib

### Two plots side by side

https://stackoverflow.com/a/42818547/5103881
-->
