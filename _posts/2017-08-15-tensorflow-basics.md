---
layout: post
title:  "TensorFlow basics"
category: Machine Learning
---


## Installation

This is what worked best for me, in Ubuntu 16.04.

### Install cuda

Install cuda using apt-get ([instructions here](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#axzz4pToHShYz)). You will need to download a `.deb` package containing repository metadata which can be found in [nvidia's developer platform](https://developer.nvidia.com/cuda-downloads), and then proceed following the steps in the documentation.

Don't forget to perform the mandatory post-installation steps. The step for configuring POWER9 is only necessary if you are using a POWER9 system (Power 9 is a high-end server CPU made by IBM).

Obs: if you installed cuda via apt-get, it may be interesting to put it on hold so that it doesn't get updated automatically and end up breaking down your workflow unexpectedly, since tensorflow binaries are specific to a cuda version:
```bash
sudo apt-mark hold cuda
```

### Install cudnn

Install cudnn *without* using a `.deb` package ([link here](https://developer.nvidia.com/rdp/cudnn-download)). For me, using the `.deb` package provided by nvidia never seemed to get the right paths.

The installation is very simple: after downloaded, uncompress the `.tgz` file:
```bash
cd ~/Downloads/
tar -zxvf cudnn-9.1-linux-x64-v7.1.tgz

# __Output should be:__
# cuda/include/cudnn.h
# cuda/NVIDIA_SLA_cuDNN_Support.txt
# cuda/lib64/libcudnn.so
# cuda/lib64/libcudnn.so.7
# cuda/lib64/libcudnn.so.7.1.3
# cuda/lib64/libcudnn_static.a
```

Next, there will be 2 directories inside the extracted folder: include and lib64. They correspond to the directories with the same name inside /usr/local/cuda where you should move the respective files. That is all that is needed:

```bash
sudo mv ~/Downloads/cuda/include/* /usr/local/cuda/include/
sudo mv ~/Downloads/cuda/lib64/* /usr/local/cuda/lib64/
```


### Install TensorFlow

It's possible to install tensorflow using Anaconda ([instructions here](https://www.tensorflow.org/install/install_linux#InstallingAnaconda)) using [individual whl files](https://github.com/tensorflow/tensorflow/blob/master/README.md). Make sure that the wheel (`.whl`) file you are installing was built for the python, cuda and cudnn versions you have installed.

However, if you want maximum performance, you will want to [build it from source](https://www.tensorflow.org/install/install_sources).


### Testing TensorFlow

```python
import tensorflow as tf

# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)
```





## Variables and Placeholders

[This question](https://stackoverflow.com/questions/36693740/whats-the-difference-between-tf-placeholder-and-tf-variable) describes pretty well the difference between `tf.Variable()` and `tf.placeholder()` and when each should be used.

### Variables

[Doc here](https://www.tensorflow.org/programmers_guide/variables#the_problem). An important point to remember about variables is that they exist outside the context of a single `session.run` call. Be sure to initialize their value by creating an initializer `tf.global_variables_initializer()` and running it through the session.

Variables are usually defined like so:
```python
weights = tf.Variable(tf.truncated_normal([..., ...]))
biases = tf.Variable(tf.zeros([...]))
```

### Placeholders

With placeholders, their values should be passed via a `feed_dict` when running the session.

Since you'll want to feed more than one single example in the input (your batch_size is usually greater than 1), it is common to create the input placeholder like this:
```python
input = tf.placeholder(tf.float32, [None, n_features])
```
which corresponds to a tensor with `None` (i.e., a variable number of) lines and `n_features` columns.

To define a scalar, create a tensor with 0 dimensions:
```python
scalar = tf.placeholder(tf.float32, [])
```



## ReLUs

The ReLU function is provided via `tf.nn.relu()`:
```python
# Hidden Layer with ReLU activation function
hidden_layer = tf.add(tf.matmul(features, hidden_weights), hidden_biases)
hidden_layer = tf.nn.relu(hidden_layer)

output = tf.add(tf.matmul(hidden_layer, output_weights), output_biases)
```


## Convolutions

The functions [`tf.nn.conv2d()`](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d) and [`tf.nn.bias_add()`](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add) help you create a convolutional layer:
```python
conv_layer = tf.nn.conv2d(input, weight, strides=[...], padding='SAME|VALID')
conv_layer = tf.nn.bias_add(conv_layer, bias)
# activation function
conv_layer = tf.nn.relu(conv_layer)
```
`tf.nn.conv2d` requires the input be 4D (batch_size, height, width, depth). The difference between the two types of padding is [nicely explained here](https://stackoverflow.com/a/39371113/5103881).



## Pooling

[`tf.nn.max_pool()`](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool) helps you apply max pooling to the convolutional layer:
```python
conv_layer = tf.nn.max_pool(conv_layer, ksize=[...], strides=[...], padding='SAME|VALID')
```
`ksize` is the filter size. 2x2 filters with a stride of 2x2 are common in practice.



## Dropout

Dropout forces the network to learn **redundant** representations, making things more robust and preventing overfitting. Also, it makes the network act as if taking the consensus of an ensemble of networks, improving performance. See [`tf.nn.dropout()`](https://www.tensorflow.org/api_docs/python/tf/nn/dropout):
```python
keep_prob = tf.placeholder(tf.float32) # probability to keep units

hidden_layer = tf.add(tf.matmul(features, weights[0]), biases[0])
hidden_layer = tf.nn.relu(hidden_layer)
hidden_layer = tf.nn.dropout(hidden_layer, keep_prob)

logits = tf.add(tf.matmul(hidden_layer, weights[1]), biases[1])
```

In order to compensate for dropped units, the function automatically multiplies kept units by $\frac{1}{keep\_prob}$.




## Embedding Layers

[`tf.nn.embedding_lookup()`](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup) does the job of retrieving rows automatically from an embedding layer. In the example below we create an embedding layer for the case of word representation, considering that the number of possible words (or, in general, the number of possible indexes we are going to feed into the network) is `vocab_size` and the number of latent factors in the embedding is `embed_dim`:

```python
embedding = tf.Variable(tf.random_uniform([vocab_size, embed_dim], -1, 1))
embed = tf.nn.embedding_lookup(embedding, ids)
```

`ids` should be a tensor with type `int32` or `int64` containing the ids of the rows to be retrieved.

[This answer](https://stackoverflow.com/a/41922877/5103881) in stackoverflow has a more detailed explanation.


## LSTMs

```python
def build_cell(num_units, keep_prob):
    lstm = tf.contrib.rnn.BasicLSTMCell(num_units)
    drop = tf.contrib.rnn.DropoutWrapper(lstm, output_keep_prob=keep_prob)
    return drop

cell = tf.contrib.rnn.MultiRNNCell([build_cell(num_units, keep_prob) for _ in range(num_layers)])

output, state = tf.nn.dynamic_rnn(cell, embed, sequence_length=source_sequence_length, dtype=tf.float32)
```


## Batch normalization

#### Using `tf.layers.batch_normalization()` (higher level)

First, add batch normalization to the layer (usually before the activation function). A new parameter to the layer will be necessary, indicating if it is training or not. Keep in mind that you will need to create a new placeholder for this boolean value later.
```python
def fully_connected(prev_layer, num_units, is_training):
    layer = tf.layers.dense(prev_layer, num_units, activation=None, use_bias=False)
    layer = tf.layers.batch_normalization(layer, training=is_training)
    layer = tf.nn.relu(layer)
```

Then, you will need to tell tensorflow to update the population statistics while training:
```python
with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS)):
    train_opt = tf.train.AdamOptimizer(learning_rate).minimize(model_loss)
```


#### Using `tf.nn.batch_normalization()` (lower level)

If you want to implement a lower level batch_normalization function, you will use `tf.nn.batch_normalization()`. See the documentation for more details. [This jupyter notebook](https://github.com/arthurcgusmao/dlnd_batch_normalization/blob/master/Batch_Normalization_Solutions.ipynb) can be of help as well.




## Training the network

```python
# define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(epochs):
        for batch in range(num_examples//batch_size):
            ...
            sess.run(optimizer, feed_dict={...})

            loss = sess.run(cost, feed_dict={...})
```
Remember to use `keep_prob = 1` when calculating the loss.




## Save and load progress
`tf.train.Saver` lets you save any `tf.Variable` to your file system.

```python
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # do your stuff
    pass

    saver.save(sess, './model.ckpt')
```
`.ckpt` stands for checkpoint.

To restore the session, do:
```python
saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, './model.ckpt')
    # no need to call the initializer

    # do your stuff
    pass
```

When loading the data tensorflow uses the names it assigns to variables, so be sure to check out the next section.




## Names and Scopes

Tensorflow automatically assings names to each variable. These names are used for reusing the same variables in different contexts (or scopes) and when reloading data. You are able to define the naming structure of the variables (like if it was a namespace) with the functions `tf.name_scope()` and `tf.variable_scope` (their difference is well explained in these answers: [[a1]](https://stackoverflow.com/a/43580096/5103881), [[a2]](https://stackoverflow.com/a/37534656/5103881)), which cause all groups of related objects to have the same naming structure. A good way to do it when defining functions to create the layers is:
```python
def fc_layer(input, channels_in, channels_out, name='fc')
    with tf.name_scope(name):
        w = tf.Variable(tf.zeros([channels_in, channels_out]), name='W')
        b = tf.Variable(tf.zeros([channels_out]), name='B')
        return tf.nn.relu(tf.matmul(input, w) + b)
```

It's possible to set names after the variable was created also, with `tf.identity()`:
```python
weights = tf.Variable(tf.truncated_normal([2,3]))
weights = tf.identity(weights, name='weights')
```


## Shapes and dimensions

To get the [shape as a list of ints](https://stackoverflow.com/a/40666375/5103881), do `tensor.get_shape().as_list()`.


## TensorBoard

[TensorBoard](https://www.tensorflow.org/get_started/summaries_and_tensorboard) is a suite of visualization tools to make debugging, optimization and understading of TF graphs easier.

To use TB we need first write data from TF to disk, using the class `tf.summary.FileWriter()`:
```python
with tf.Session() as sess:
    writer = tf.summary.FileWriter("/tmp/example_name/1")
    writer.add_graph(sess.graph) # this can also be passed in the above statement
```
And then use the command `tensorboard` specifying the logging directory:
```bash
$ tensorboard --logdir /tmp/example_name/1
```
To export condensed information about the model, you use [summaries](https://www.tensorflow.org/api_guides/python/summary):
```python
tf.summary.scalar('accuracy', accuracy)
tf.summary.image('input', x_image, 3)

def fc_layer(...):
    ...
    tf.summary.histogram("weights", w)
    tf.summary.histogram("biases", b)
    tf.summary.histogram("activations", act)
    return ...

# collect summaries
with tf.Session() as sess:
    ...
    merged_summary = tf.summary.merge_all()

    for i in range(2001):
        ...
        if i % 5 ==0:
            s = sess.run(merged_summary, feed_dict={x: batch[0], y: batch[1]})
            writer.add_summary(s, i)
```
Histograms are useful when you have a bunch of numbers (like in a matrix) and you want to look at the distribution of it.

It may be an interesting idea to save different sets of summaries to disk for the varying hyperparameters you may want to experiment with:
```python
# hyperparameter search
for learning_rate in [1e-3, 1e-4, 1e-5]:
    for num_fc_layers in [2, 3]:
        # save a different summary for each configuration
        hparam_str = make_hparam_string(learning_rate, num_fc_layers)
        writer = tf.summary.FileWriter("/tmp/example_name/" + hparam_str)

        # actually run with the new settings
```

A very interesting feature that TB has is the **Embedding Visualizer**, which lets you project high dimensional data into 3 dimensions. Code shown above was taken from [here](https://github.com/dandelionmane/tf-dev-summit-tensorboard-tutorial/blob/master/mnist.py).


## Examples

Lots of Tensorflow examples [here](https://github.com/aymericdamien/TensorFlow-Examples).
