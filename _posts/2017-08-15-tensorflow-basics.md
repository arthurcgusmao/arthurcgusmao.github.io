# Tensorflow basics

## Installation

This is what worked best for me, in Ubuntu 16.04.


1. Install cuda using apt-get [link here](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#axzz4pToHShYz).
2. Install cudnn without using a .deb package [link here](https://developer.nvidia.com/rdp/cudnn-download). There will be 2 directories inside the folder when you uncompress the .tar file: include and lib64. They correspond to the respective directories with the same name inside /usr/local/cuda. The only version of cudnn I tried which made the build be successful was the 5. Installing the .deb package provided by nvidia never seemed to get the right paths.
3. For maximum performance, [build tensorflow from source](https://gist.github.com/Brainiarc7/6d6c3f23ea057775b72c52817759b25c).


Testing:

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

[This question](https://stackoverflow.com/questions/36693740/whats-the-difference-between-tf-placeholder-and-tf-variable) describes pretty well the difference between `tf.Variable()` and `tf.placeholder()` and when each should be used. When using variables, you should initialize their value via `tf.global_variables_initializer`. With placeholders, be sure to pass their values via a `feed_dict`.

Since you'll want to feed more than one single example in the input, it is common to create the input placeholder like this:
```python
input = tf.placeholder(tf.float32, [None, n_features])
```
which corresponds to a tensor with `None` (i.e., a variable number of) lines and `n_features` columns.


## ReLUs

The ReLU function is provided by tensorflow via `tf.nn.relu()`:
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


## Pooling

[`tf.nn.max_pool()`](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool) helps you apply max pooling to the convolutional layer:
```python
conv_layer = tf.nn.max_pool(conv_layer, ksize=[...], strides=[...], padding='SAME|VALID')
```
2x2 filters with a stride of 2x2 are common in practice.



## Dropout

Dropout forces the network to learn **redundant** representations, making things more robust and preventing overfitting. Also, it makes the network act as if taking the consensus of an ensemble of networks, improving performance. `tf.nn.dropout()` is provided by tensorflow:
```python
keep_prob = tf.placeholder(tf.float32) # probability to keep units

hidden_layer = tf.add(tf.matmul(features, weights[0]), biases[0])
hidden_layer = tf.nn.relu(hidden_layer)
hidden_layer = tf.nn.dropout(hidden_layer, keep_prob)

logits = tf.add(tf.matmul(hidden_layer, weights[1]), biases[1])
```

In order to compensate for dropped units, the function automatically multiplies kept units by $\frac{1}{keep\_prob}$.



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

Tensorflow automatically assings names to each variable and it'll use it when loading the data. To avoid errors you may want to set the names manually:
```python
weights = tf.Variable(tf.truncated_normal([2,3]), name='weights')
```

## Tensorflow examples
Lots of Tensorflow examples [here](https://github.com/aymericdamien/TensorFlow-Examples).
