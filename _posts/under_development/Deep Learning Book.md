---
header-includes:
    \usepackage{bm}
    \usepackage{/home/arthurcgusmao/GD/Professional/Programming/LaTeX/acgstyle}
---



# Introduction

Deep Learning is a solution to the more intuitive problems in emulating intelligence. The solution involves learning in a hierarchy of concepts, that allows the computer to learn complicated concepts by building them out of simpler ones. This hierarchy has many layers, hence the name Deep Learning.


# Linear Algebra
# Probability and Information Theory
# Numerical Computation


# Machine Learning Basics
## Learning Algorithms
## Capacity, Overfitting and Underfitting

The central challenge in machine learning is **generalization**: we must perform well on *new*, *previously unseen* inputs. What separates machine learning from optimization is that we want the generalization error, also called the test error, to be low as well.

We can only know that performance on the training set will affect the test set if we make the **i.i.d. assumptions** about the **data generating process**. These assumpions are that each example of the dataset is *independent* from any other, and that the train set and test set are **identically distributed**. The same distribution (called the **data generating distribution**) is then used to generate every train example and every test example.

The factors determining how well a machine learning algorithm will perform are its ability to:

1. Make the training error small. (do not *underfit*)
2. Make the gap between training and test error small. (do not *overfit*)

We can control whether a model is more likely to overfit or underfit by altering its **capacity**---its ability to fit a wide variety of functions. One way to control the capacity of a learning algorithm is by choosing its **hypothesis space**, the set of functions that the learning algorithm is allowed to select as being the solution. Since the optimization algorithm does not always find the best function, the **effective capacity** may be less than the **representational capacity** of the model.


### The No Free Lunch Theorem

The no free lunch theorem for machine learning (Wolpert, 1996) states that, averaged over all possible data generating distributions, every classification algorithm has the same error rate when classifying previously unobserved points. In other words, in some sense, no machine learning algorithm is universally any better than any other.

However, if we make assumptions about the kinds of probability distributions we encounter in real-world applications, then we can design learning algorithms that perform well on these distributions.


### Regularization

We can regularize a model that learns a function by adding a penalty called a **regularizer** to the cost function. Expressing preferences for one function over another is a more general way of controlling a model's capacity than including or excluding members from the hypothesis space.

*Regularization is any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error.* The no free lunch theorem has made it clear that there is no best machine learning algorithm, and, in particular, no best form of regularization. We must choose a form of regularization that is well-suited to the particular task.

The philosophy of deep learning in general and this book in particular is that a very wide range of tasks (such as all of the intellectual tasks that people can do) may all be solved effectively using very general-purpose forms of regularization.


## Hyperparameters and Validation Sets

**Hyperparameters** are settings we can use to control the behavior of the learning algorithm, and their values are not adapted by the learning algorithm itself.

Here the author makes a distinction between the training set, the validation set and the test set. The training set is used to train the parameters of the model. The validation set is used to "train" the hyperparameters, by decreasing the validation set error (however, because the validation set ends up influencing the hyperparameters chosen, this estimate of the error tends to be lower than the actual generalization error). After all hyperparameter optimization is complete, the generalization error may be estimated using the test set.


### Cross Validation

*k-fold* cross validation is mentioned.


## Estimators, Bias and Variance

### Point Estimation
(see statistics.pdf)

### Bias
(see statistics.pdf)

### Variance and Standard Error
(see statistics.pdf)

### Trading off Bias and Variance to Minimize Mean Squared Error
(see statistics.pdf)

### Consistency
Tirar dúvida com o Cozman


## Maximum Likelihood Estimation
Are there principles from which we can derive specific functions that are good estimators for
different models? Yes, the ML principle is the most common. It is defined as:
\begin{equation}
\boldsymbol{\theta}_{\text{ML}} = \argmax_{\boldsymbol\theta} p_{\text{model}}( \mathbb{X} ; \boldsymbol\theta )
\end{equation}

(Aqui ele define o ${\boldsymbol\theta_{\text{ML}}}$, tira o log e fala sobre a KL Divergence)

We can see ML as an attempt to make the model distribution match the empirical (observed)
distribution $\hat p_{data}$. Ideally, we would like to match the true data generating
distribution $p_{data}$, but we have no direct access to that.

*** Conditional Log-Likelihood and Mean Squared Error
The conditional LL $\sum \log P(\boldsymbol{y}^{(i)} \mid \boldsymbol{x}^{(i)} ;
\boldsymbol{\theta})$ forms the basis for most supervised learning.

*Example: Linear Regression as Maximum Likelihood.* In this example we see that minimizing the
Mean Squared Error (MSE) is equivalent to maximize the log-likelihood, because both functions
contain the term $\norm{\hat y^(i) - y^(i)}^2$. This justifies the use of the MSE as a maximum
likelihood estimation procedure.

*** Properties of Maximum Likelihood
The main appeal of the ML estimator is that it can be shown to be the best estimator
asymptotically, in terms of its rate of convergence as m increases (tends to infinity).

Under appropriate conditions, the ML estimator has the property of *consistency*. Consistent
estimators can differ in their *statistic efficiency*, meaning that one consistent estimator may
obtain lower generalization error for a fixed number of samples.

For consistency and efficiency, ML is often considered the preffered estimator to use for
machine learning. When the number of examples is small enough to overfit, regularization
strategies may be used to obtain a biased version of ML that has less variance.


** Bayesian Statistics
????????????

*** Maximum /A Posteriori/ (MAP) Estimation
The MAP estimate chooses the point of maximal posteior probability:
\begin{equation}
\boldsymbol\theta_{\text{MAP}} = \argmax_{\boldsymbol\theta} p(\boldsymbol\theta \mid \boldsymbol x) = \argmax_{\boldsymbol\theta} \log p(\boldsymbol x \mid \boldsymbol \theta) + \log p(\boldsymbol \theta).
\end{equation}
This is cheaper than having to integrate over the full distribution of $\boldsymbol\theta$ to
make the predictions. However, we still gain some of the benefits of the Bayesian approach by
allowing the prior to influence the choice of the point estimate.

MAP Bayesian inference has the advantage of leveraging information that is brought by the prior
and cannot be found in the training data, which helps to reduce the variance in the MAP point
estimate (in comparison to the ML estimate). However, it does so at the price of increased bias.

MAP Bayesian inference provides a straightforward way to design complicated yet interpretable
regularization terms. Many regularized estimation strategies (but not all) can be interpreted as
making the MAP approximation to Bayesian inference. This view applies when the regularization
consists of adding an extra term to the objective function that corresponds to $\log
p(\boldsymbol\theta)$.


** Supervised Learning Algorithms
*** Probabilistic Supervised Learning
*** ............
