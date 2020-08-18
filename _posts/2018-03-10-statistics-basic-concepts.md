---
layout: post
title:  "Statistics basic concepts"
category: "Machine Learning"
mathjax: true
header-includes:
    - \usepackage{bm}
    - \newcommand*\mean[1]{\bar{#1}}
---
This is my personal cheatsheet for statistics. It is far from being a complete introduction.
$$
    \def\mean#1{\bar #1}
    \DeclareMathOperator{\EV}{\mathbb{E}}
$$


## Intro to Research Methods

### Construcs

Something hard to measure, that you'll have to define how to measure.

### Operational Definition

It's how you will measure a given construct.

### Parameters vs Statistics

**Parameters** refer to the whole population. **Statistics** refer to the sample (part of the population).

### Relationships vs Causation

**Relationships** can be shown by observational studies (eg. by seeing a point distribution). **Causation**, however, has to be found through controlled experiments.

## Measures of central tendency

### Mode

*The value at which frequency is highest.*

The mode doesn't really represent the data well because:

-   It's not affected by all scores in the dataset;
-   It changes radically depending on the sample;
-   We can't really describe the mode by an equation.

### Median

*The value in the middle of the distribution.*

(If there are an even number of elements, the median will be the average of the two in the middle.)

The median is more robust to outliers than the mean. It is therefore the best measure of central tendency when dealing with highly skewed distributions.

### Mean (expected value)

*The weighted average, or expected value.*

- Population mean: $\mu$
- Sample mean: $\mean{x}$ (can be used to estimate $\mu$)
- The mean is **affected by outliers**.


![][img:skewed]

[img:skewed]: /images/posts/mode-median-mean-skewed.png

The mean is always pulled towards the longest tail of the distribution, in relation to the median.


## Variability of data

### Range

*Range = MaxValue - MinValue*

### Interquartile Range (IQR)

IQR is the distance between the 25% and the 75% higher measure of the data.

*IQR = Q3 - Q1*

Problem with Range and IQR: neither takes all data into account.

### Outlier

*An observation point that is distant from other observations.*

Values below (Q1 - 1.5\*IQR) or above (Q3 + 1.5\*IQR) are usually considered outliers.

![][img:outlier-boxplot]
Outliers are represented as dots in a boxplot.

[img:outlier-boxplot]: /images/posts/outlier-boxplot.png



## Estimators, Bias and Variance

(from a machine learning point of view)

### Point Estimation

Point estimation is the attempt to provide the single “best” prediction of some quantity of interest. A **point estimator** or **statistic** is any function of the data:

$$
\boldsymbol{\hat \theta}_m = g(\boldsymbol{x}^{(1)},...,\boldsymbol{x}^{(m)}).
$$

The definition does not require that $g$ return a value that is close to the true $\boldsymbol{\theta}$ or even that the range of $g$ is the same as the set of allowable values of $\boldsymbol{\theta}$.

### Bias

Bias measures the expected deviation from the true value of the function or parameter. The bias of an estimator is defined as:

$$
\text{bias}(\boldsymbol{\hat\theta}_m) = \EV(\boldsymbol{\hat\theta}_m) - \boldsymbol{\theta}
$$

where the expectation is over the data (seen as samples from a random variable).

### Variance and Standard Deviation

**Variance** provides a measure of the deviation from the expected estimator value that any particular sampling of the data is likely to cause.

We call *deviation* a measure of difference between the observed value of a variable and some other value, often that variable's mean. We calculate the **variance** by taking the *mean of squared deviations*:

$$
\sigma^2 = \sum_{i=1}^{n} \frac{(x_i - \mean{x})^2}{n}
$$

The **standard deviation** is simply the root square of the variance. One interesting characteristic of the standard deviation is the [68–95–99.7 rule](https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule).

#### Bessel's Correction (unbiased estimator of the population variance)

You use $(n - 1)$ instead of $(n)$ to calculate the standard deviation when estimating the standard deviation for the population from a sample.

$$
\sigma \approx s = \sqrt{\sum_{i=1}^{n} \frac{(x_i - \mean{x})^2}{n - 1}}
$$

Using the *sample standard deviation* (s) corrects the bias in the estimation of the population variance. It also partially corrects the bias in the estimation of the population standard deviation. However, the correction often increases the mean squared error in these estimations.

These [[1](https://www.youtube.com/watch?v=1HmiArFN-EI), [2](https://www.youtube.com/watch?v=9ONRMymR2Eg)] short videos try to bring some intuition on why to use $(n - 1)$ instead of $(n)$.

The problem is that, by using the estimate $(\mean{x})$ instead of the actual population mean $(\mu)$, we create bias in the estimated variance by underestimating it, because $(\mean{x})$ is the value that minimizes $\sum_{i=1}(x_i - \mean{x})^2$, whereas $\mu$ could be any other value that makes it larger.

Using $n-1$ in $s^2$ to estimate $\sigma^2$ fixes this bias, making $s^2$, on average, equals $\sigma^2$ (unbiased estimator).

#### Z-Score
The Z-Score, aka standard score, maps a sample $x_i$ to how many standard deviations $\sigma$ it is from from the mean $\mu$:

$$
z_i = \frac{x_i - \mu}{\sigma}
$$

### Standard Error of the Mean (SEM)

The SEM quantifies the precision of the mean, it is a measure of how far your sample mean is likely to be from the true mean of the population. But how to calculate it without doing lots of experiments and finding many different values for the mean? We can use the estimation:

$$
\text{SEM} = \frac{\sigma}{\sqrt{n}}
$$

Proof of the formula below ([from
here](https://stats.stackexchange.com/questions/89154/general-method-for-deriving-the-standard-error)), the first step is allowed because the $X_i$ are independently sampled, so the variance of the sum is just the sum of the variances.

$$
\text{Var}\bigg(\frac{\sum_{i=1}^{n}{X_i}}{n}\bigg) = \frac{1}{n^2}\text{Var}\bigg(\sum_{i=1}^{n}{X_i}\bigg) = \frac{1}{n^2}\sum_{i=1}^{n}\text{Var}\bigg({X_i}\bigg) = \frac{1}{n^2}\sum_{i=1}^{n}{\sigma^2} = \frac{\sigma^2}{n}
$$

We can use the SEM to interpret different populations and see if there is evidence that they are differences or similarities between them:

![][img:sem]
*How the standard error of the mean helps us interpret populations, from [this YouTube video](https://www.youtube.com/watch?v=3UPYpOLeRJg).*

[img:sem]: /images/posts/interpreting_SEM.png


### The Bias vs Variance Tradeoff

How to choose between two estimators: one with more bias and another with more variance? The most common way to negotiate this trade-off is to use cross-validation. Alternatively, we can also compare the **mean squared error** (MSE) of the estimates:

$$
\begin{align}
\text{MSE} & = \EV \left[ \left( \hat\theta_m - \theta \right)^2 \right] \\
& = \text{Bias} \left( \hat\theta_m \right)^2 + \text{Var} \left( \hat\theta_m \right)^2
\end{align}
$$

The relationship between bias and variance is tightly linked to the machine learning concepts of capacity, underfitting and overfitting.


## Important concepts

### Sampling distribution
The [sampling distribution](https://en.wikipedia.org/wiki/Sampling_distribution) is the probability distribution of the values a statistic (e.g., sample mean or sample variance) can take on.

### Statistical hypothesis testing

The [null hypothesis](https://en.wikipedia.org/wiki/Null_hypothesis) $H_0$ is a default position that there is no relationship between two measured phenomena or no association among groups [Wikipedia]. It is usually contrasted with an [alternative hypothesis](https://en.wikipedia.org/wiki/Alternative_hypothesis) $H_1$, a new theory.

These statistical hypothesis are usually formulated in terms of a [test statistic](https://en.wikipedia.org/wiki/Test_statistic), a one-value numerical summary of a dataset, defined in a way that distinctions between the two hypotheses can be made.

The test statistic must be such that its sampling distribution, and, consequently, [p-values](https://en.wikipedia.org/wiki/P-value), can be calculated.

<!-- Z-test is any statistical  -->


### i.i.d.
[Independent and identically distributed](https://stats.stackexchange.com/questions/89154/general-method-for-deriving-the-standard-error) random variables refers to a collection of random variables that are mutually independent from each other and sampled from the same probability distribution.

### Central limit theorem
The [central limit theorem](central limit theorem) states that, when i.i.d. random variables are summed, the resulting distribution tends toward a normal distribution, as the number of samples grow, even if the original variables themselves are not normally distributed.
