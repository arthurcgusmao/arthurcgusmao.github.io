---
layout: post
title:  "Gradient descent & Backpropagation"
#category: Deep learning
mathjax: true
header-includes:
    \usepackage{bm}
---


This article aims at discussing some of the basics of gradient descent and backpropagation in artificial neural networks (NNs). For newcomers, viewing these concepts from many different perspectives may be a faster way of learning. It's supposed that the reader is already familiar with calculus, linear algebra and basic terminology of NNs.


## Neural networks

Neural networks are a class of *machine learning* models, inspired by how biological neural networks work, that consist of several artificial neurons arranged in specific architectures. Each artificial neuron loosely models a biological neuron in the sense that it is connected to several other neurons and yields an output as a function of its inputs and parameters. By changing either a NN's architecture or its parameters, one is able to modify how the network respond to different inputs, being able to develop networks that better model phenomenons in the real world. Usually, one makes use of optimization algorithms to improve the parameters (also known as weights) of a NN with respect to a set of observations (data points) from the real world, which we call *learning* the weights of a NN.

Learning requires that we find a way to optimize the model weights so that the output gets as close as possible to the ground truth values. In order to do so, we define a *loss (or error) function*, a function that penalizes outputs that differ from the correct values by assigning a higher value to them, and work towards minimizing the results of this loss function by updating the neural network's weights. The most efficient manner of doing so is to have a loss function that is differentiable so that we can employ *gradient descent*, an optimization method to (locally) minimize a function. Gradient descent works by calculating the gradient of a function (the gradient points in the direction of the greatest increase rate of the function) at a given point and changing the function's parameters (in our case, the neural network's weights) in the opposite direction.

In this post, we go through the details of what gradient descent is and how it can be applied in NNs in order to make learning feasible. We do not go through the details of NN architectures or artificial neurons here.


## Gradient descent

### What is gradient descent?

**Gradient descent** is an optimization algorithm that moves us towards a *local minimum* of a function. Intuitively, at each iteraton the algorithm will take a step in the direction that shows the fastest decrease rate of the function, thus minimizing it locally.

![Path that gradient descent would go through for two different starting points][img:gd]

[img:gd]: /images/posts/gradient_descent.png

#### Univariate case

Say we want to minimize a function $y = f(x)$. Gradient descent uses the derivative of the function ($\frac{d f(x)}{dx}$ , which gives us the slope) as a guide so that it knows how a small change $\epsilon$ in $x$ will affect the output $y$:

$$
    f(x + \epsilon) \approx f(x) + \epsilon\ f'(x)
$$


We can thus reduce $f(x)$ by moving $x$ in the opposite direction of the derivative.

#### Multivariate case

The *gradient* of a function generalizes the notion of derivative to the case where the derivative is with respect to a vector. Let $\boldsymbol{x} = [x_1, \dots, x_n]$ and $f:\mathbb{R} ^{n}\rightarrow \mathbb{R}$. Then the gradient of $f$ with respect to $\boldsymbol{x}$ is:

$$
    \boldsymbol{\nabla}_{\boldsymbol{x}}f\left( \boldsymbol{x}\right) =\left[ \begin{matrix} \dfrac {\partial f\left( \boldsymbol{x} \right) } {\partial x_{1}}\\ \vdots \\ \dfrac {\partial f\left( \boldsymbol{x} \right) } {\partial x_{n}}\end{matrix} \right]
$$

Gradient descent for the multivariate case then proposes moving a new point

$$
    \boldsymbol{x}' = \boldsymbol x - \epsilon \boldsymbol{\nabla_x}f(\boldsymbol{x})
$$

where $\epsilon > 0$ is the *learning rate*, a scalar that determines the size of the step we're
going to take in the opposite direction of the gradient of the function to get to the (local)
minimum.

In NNs, the function we're usually trying to minimize is an error (or loss) function, and we can use gradient descent for that. However, how do we do that when our network has more than one layer? How do we propagate the error backwards from the final layers to the initial ones?

### Gradient descent in neural networks





## Backpropagation

Backpropagation is a short expression for "backward propagation of errors". Intuitively, it propagates the output errors of the network backwards, associating a relative value of the error for each unit of the hidden layer. This relative value is then used to update the weights of that unit. The process is repeated for each hidden layer.

More formally, backpropagation attemps to minimize an error function such as

$$
    E = \frac{1}{2}(y - \hat{y})^2
$$

by calculating for each weight $w_{ij}^{(k)}$ the value of $\frac{\partial E}{\partial w_{ij}^{(k)}}$.



.....

- $y$ is the output and $\hat y$ the predicted output
- $f$ is the activation function
- $h$ is the output of the current layer before passing throught the activation function
- $x_i$ is the input of hidden unit $i$
- The *error term* $\delta_j^h$ is the amout of error proportional to the hidden unit $j$ of the hidden layer $h$. It is defined as:

$$
    \delta_j^h = \sum w_{jk} \delta_k^{h+1} f'(h_j)
$$

When the layer is the output the error term is:

$$
    \delta_j^{out} = (y_j - \hat y_j) f'(h_j)
$$

After we have calculated the error term, we calculate the update in the weights by the formula:

$$
    \begin{align*}
        \Delta_{w_{i}} = - \eta \dfrac{\partial E}{\partial w_i} \\
        \Delta_{w_{ij}} = \eta \delta_j^h x_i
    \end{align*}
$$


## Example

Now we are going to calculate one forward pass through the network (inference) and then update the weights by doing backpropagation. Our example is a two layer network which consists of 3 inputs (represented by a vector $\boldsymbol{x}$), 2 hidden units and 1 output unit:

(((figure here)))

$$
    \boldsymbol{x} =
        \begin{bmatrix}
            x_1 \\
            x_2 \\
            x_3
        \end{bmatrix}
$$

The weights from the inputs (layer 0) to the hidden layer (layer 1) are represented by a 2x3 matrix $W^{(0 \rightarrow 1)}$, and the weights from the hidden layer (layer 1) to the output (layer 2) by a 1x2 matrix $W^{(1 \rightarrow 2)}$:

$$
    \boldsymbol{W}^{(0 \rightarrow 1)} =
        \begin{bmatrix}
            w_{11}^{(1)} & w_{12}^{(1)} \\
            w_{21}^{(1)} & w_{22}^{(1)} \\
            w_{31}^{(1)} & w_{32}^{(1)}
        \end{bmatrix}\ ,\ \
    \boldsymbol{W}^{(1 \rightarrow 2)} =
        \begin{bmatrix}
            w_{11}^{(2)} \\
            w_{21}^{(2)}
        \end{bmatrix}
$$

Note that the number of rows in the weight matrix is the same as the number of units in the previous layer, and the number of columns is the number of units the next layer. We adopted this notation because it makes easier to see that the weight $w_{ij}$ is the one that goes from the $i$th node in the previous layer to the $j$th node in the current layer.


### Forward pass

In the forward pass, we start by calculating the input to the hidden unit:

$$
    \boldsymbol{v}_{in}^{(1)} = {\boldsymbol{W}^{(0 \rightarrow 1)}}^T \boldsymbol{x} =
        \begin{bmatrix}
            w_{11}^{(1)} x_1  +  w_{21}^{(1)} x_2  + w_{31}^{(1)} x_3 \\
            w_{12}^{(1)} x_1  +  w_{22}^{(1)} x_2  + w_{32}^{(1)} x_3
        \end{bmatrix} =
        \begin{bmatrix}
            {v_{in}^{(1)}}_{1} \\
            {v_{in}^{(1)}}_{2}
        \end{bmatrix}\ ,
$$

where $h_{i}^{(h)}$ denotes the input to unit $i$ of the hidden layer $h$. Now the hidden layer receives these inputs and yields an output which is the result of the activation function $f$:

$$
    \boldsymbol{v}_{out}^{(1)} = f\left( \boldsymbol{v}_{in}^{(1)} \right) =
        \begin{bmatrix}
            f\left( {v_{in}^{(1)}}_{1} \right) \\
            f\left( {v_{in}^{(1)}}_{2} \right)
        \end{bmatrix} =
        \begin{bmatrix}
            {v_{out}^{(1)}}_{1} \\
            {v_{out}^{(1)}}_{2}
        \end{bmatrix}.
$$

This same process is repeated in the next layer:

$$
    \boldsymbol{v}_{in}^{(2)} = {\boldsymbol{W}^{(1 \rightarrow 2)}}^T \boldsymbol{v}_{out}^{(1)} =
        \begin{bmatrix}
            w_{11}^{(2)} {v_{out}^{(1)}}_{1} + w_{21}^{(2)} {v_{out}^{(1)}}_{2}
        \end{bmatrix} =
        \begin{bmatrix}
            {v_{in}^{(2)}}_{1}
        \end{bmatrix}\ ,\\
    \boldsymbol{v}_{out}^{(2)} = f\left( \boldsymbol{v}_{in}^{(2)} \right) =
        \begin{bmatrix}
            f\left( {v_{in}^{(2)}}_{1} \right)
        \end{bmatrix} =
        \begin{bmatrix}
            {v_{out}^{(2)}}_{1}
        \end{bmatrix}.
$$

And because this is the final layer, the output of our network is:

$$
    \hat y = {v_{out}^{(2)}}_{1}.
$$

We denote the predicted output by $\hat y$ and the real, correct output by $y$. With the prediction value we can now calculate the error $E$ for this example:

$$
    E = y - \hat y
$$


### Backpropagation

Now that we have seen how the forward pass is calculated, we are able to use the error and propagate it backwards.

The error term for the output will be:

$$
    \boldsymbol{\delta}^{(2)} = E \cdot f'(\boldsymbol{v}_{in}^{(2)})
$$

Backpropagating it to the second and first hidden layers:

$$
    \boldsymbol{\delta}^{(1)} = \left( {\boldsymbol{W}^{(1 \rightarrow 2)}} \boldsymbol{\delta}^{(2)} \right) f'(\boldsymbol{v}_{in}^{(1)})^T
$$

$$
    \boldsymbol{\delta}^{(0)} = \left( {\boldsymbol{W}^{(0 \rightarrow 1)}} \boldsymbol{\delta}^{(1)} \right) f'(\boldsymbol{v}_{in}^{(0)})^T
$$

And finally the weight update can be calculated:
