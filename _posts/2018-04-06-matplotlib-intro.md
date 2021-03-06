---
layout: post
title:  "Matplotlib intro (pyplot)"
category: "Programming"
---

A very simple introduction to Matplotlib in Python. It tries to present fundamental concepts without clinging to many details. If you have time I highly recommend you another post which is much more conceptual, detailed and illustrated than mine: ["Artist" in matplotlib](https://dev.to/skotaro/artist-in-matplotlib---something-i-wanted-to-know-before-spending-tremendous-hours-on-googling-how-tos--31oo).

```python
import matplotlib.pyplot as plt
```

## Basics: Figures and Axes

The most important thing that you have to know is that Matplotlib has two main classes for plotting curves and setting up configurations: [`Figure`](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) and [`Axes`](https://matplotlib.org/api/axes_api.html). In this section we present these objects and its main methods.

### Figure

The [`Figure`](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) object is a major object that contains all of the plot elements (including the [`Axes`](https://matplotlib.org/api/axes_api.html) object, which we will see next). It can be accessed in the following manners:

```python
fig = plt.figure() # returns a Figure instance
```

The last line is a shortcut for getting the current figure and its axes; see [these answers](https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python) for more details.

Configurations such as saving and displaying the figure are set at the figure-level:

```python
fig.savefig('filepath.png') # saves figure
fig.show() # displays figure
```



### Axes

[`Axes`](https://matplotlib.org/api/axes_api.html) are the objects that have plotting methods. Each figure can contain multiple axes, thus allowing you to make multiple plots on the same figure. They are created and accessed from the figure object:

```python
# create new axes
ax1 = fig.subplots() # add a set of subplots to this figure (default 1)

# get existing axes
axs = fig.axes # list of axes in `fig`
```

Once you have the axis object that you want to plot a curve into, the only thing you need to do is to call the plotting method:

```python
ax1.plot(x, y)
```

There are many different kinds of plotting methods (which we will not cover), here are a few:

- [`ax.plot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html) Lines and/or Markers
- [`ax.bar`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html) Bars chart
- [`ax.hist`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html) Histogram
- [`plt.scatter`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html) Scatter (has capability to render a different size and/or color for each point, in contrast to plot)


### Shortcuts: the Pyplot interface

To make things easier, Matplotlib has shortcuts for the methods mentioned above directly through `pyplot`. That is, lots of methods can be called from `pyplot`, regardless of whether they would normally be called from a Figure or an Axis object:

```python
import matplotlib.pyplot as plt

# Example 1
plt.plot([1,2,3])
plt.savefig('filepath.png')
plt.show()

# Example 2
fig, ax1 = plt.subplots() # get figure and 1 axes (already added to fig)
...
```




## Axis labels, Legends, and Title

Legend, title and axis labels should be set in the axis object:
```python
# TITLE AND AXIS LABELS
ax.set(title='title', xlabel='xlabel', ylabel='ylabel')
# or
ax.set_title('title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

# LEGEND
# add labels to curves
ax.plot(xa, ya, label='Algorithm A')
ax.plot(xb, yb, label='Algorithm B')

# call legend function
ax.legend()
```

Of course, Matplotlib has shortcuts for these methods directly through `pyplot` as well, in the case you are dealing with a single plot:
```python
# shortcuts
plt.title('title')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.legend()
```


## Subplots

In Matplotlib, the subplot functionality allows you to specify where the axes should be situated (in the figure) according to a subplot grid.

```python
ax1 = fig.add_subplot(221) # creates an axis in the position specified (row-col-num)
ax2 = fig.add_subplot(222) # creates an axis in the position specified (row-col-num)
ax3 = fig.add_subplot(223) # creates an axis in the position specified (row-col-num)
ax4 = fig.add_subplot(224) # creates an axis in the position specified (row-col-num)
# or
[[ax1, ax2], [ax3, ax4]] = fig.subplots(nrows=2, ncols=2) # add a set of subplots to this figure
# or
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2) # shortcut for getting both figure and (all) axes
```

After getting the axes, you can call the plotting method of your choice for each one.

#### Breaking out of the grid

In addition, these functions do not impose a fixed grid, they simply create new axes that occupy specific positions. Because of that, you can create subplots with varying widths and heights in the same figure.
<!-- Some examples are covered in [this tutorial](https://plot.ly/matplotlib/subplots/). -->

An option for a very flexible plotting scheme is the following: specify a starting position `(x0,y0)` and the size of your new axis `(width,height)` by passing the quadruple `(x0,y0,width,height)` to [`add_subplot`](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_subplot) via the `position` keyword argument:
```python
ax1 = fig.add_subplot(position=(x0,y0,width,height))
```

Alternatively, you can use the [`add_axes`](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_axes) method, whose calling signature is the same quadruple. Its differences to `add_subplot` method are well discussed [here](https://stackoverflow.com/a/43330553/5103881).


## Decoration

Usually configuration of the curves, bars, histograms, etc. are done in the respective plotting function:

```python
plt.plot(x, y, color='green', marker='o', linestyle='dashed',
         linewidth=2, markersize=12)
```

Check out the docs for more details:

- [Colors](https://matplotlib.org/2.0.2/api/colors_api.html)
- [Lines](https://matplotlib.org/2.0.1/api/lines_api.html)
- [Markers](https://matplotlib.org/api/markers_api.html)


## Specific tips

- The parameter `alpha` is usually the transparency of the curve.
- Use `plt.tight_layout()` when your subplots have titles

#### Varying colors w/ custom colormap
Say you want to plot a set of lines with their colors varying according to some criteria.
Matplotlib define a set of [colormaps](https://matplotlib.org/3.3.0/tutorials/colors/colormaps.html) via `matplotlib.cm`, that returns a color from the colormap given your input (which can be in the range [0,1] or [0, 255]):
```python
import matplotlib.pyplot as plt
from matplotlib import cm

ys = ([1,2,3], [2,3,4], [3,4,5], [4,5,6])

for i,y in enumerate(ys):
    plt.plot(y, color=cm.summer(i/len(ys)))
```
![Varying colors with colormap][img:varying_colors]

[img:varying_colors]: /images/posts/matplotlib/varying_colors_with_colormap.png

## Other resources

- [DataCamp Matplotlib Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)



## Examples


#### Highlighting specific data points in a scatter plot

![Highlighting specific data points in a scatter plot][img:data_points_scatter]

[img:data_points_scatter]: /images/posts/matplotlib/specific_data_points_vs_dataset.png


#### Color warmth in scatter plot

![Color warmth in scatter plot][img:color_warmth]

[img:color_warmth]: /images/posts/matplotlib/linear_regression.png


#### True vs predicted data points

![True vs predicted data points][img:true_vs_predicted]

[img:true_vs_predicted]: /images/posts/matplotlib/true_vs_predicted _data_points.png
