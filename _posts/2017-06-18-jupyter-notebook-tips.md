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


## Changing Python's path

It is possible to change the path Python uses to search for files so that you can import modules that otherwise would only be possible by having your notebook file in the same directory. This is useful when you want to have a specific folder for your notebooks in order to be more organized.

To do that, run the following code:

```python
import sys
sys.path.insert(0, '/path/to/application/app/folder')
```

For more details see [this answer](https://stackoverflow.com/a/4383597/5103881).


## Fix installed packages not being imported

Sometimes, when using conda, you may find that you're not able to import installed packages into your notebook. One of the reasons may be because Jupyter is not finding the correct kernel.

To find out what kernel is being used, run (within the notebook):

```python
import sys
sys.path
sys.executable
```

If you find that this is the problem, a simple solution is simply installing jupyter within the conda environment you are using:

```bash
source activate [yourenvname]
conda install jupyter
```

Keep in mind that this will install another instance of jupyter in your machine, occupying space. If you want to save space there are alternatives. See [here](https://github.com/jupyter/notebook/issues/2563).



## Using git to version control jupyter notebooks

[This post](http://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/) explains in a very nice way different ways we can combine jupyter notebook with git tracking only changes in code.


## Tracking time

Jupyter and IPython make it really easy to track time in the cells you execute:

```python
%time print('%time will output the time of running only this line')
```

```python
%%time
print('Jupyter can also track')
print('the time that running an entire cell took')
print('when you use %%time')
```

For more accurate results you may also want to use `timeit` instead of `time`, which Jupyter also allows for. See [this answer](https://stackoverflow.com/questions/17579357/time-time-vs-timeit-timeit) for more details on the difference between the two.
