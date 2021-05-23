---
layout: post
title:  "Evaluation Metrics for Classification"
category: "Machine Learning"
mathjax: true
---
\\(
    \def\TP{\text{TP}}
    \def\FP{\text{FP}}
    \def\TN{\text{TN}}
    \def\FN{\text{FN}}
    \def\Pc{P_\text{correct}}
    \def\Pw{P_\text{wrong}}
    \def\Nc{N_\text{correct}}
    \def\Nw{N_\text{wrong}}
    \newcommand{\prob}{\mathbb{P}}
\\)The motivation for this post is that terms like *False Positive Rate* and *True Negative examples* never felt intuitive to me. As I started to research to understand them better, I found different forms of looking at them that I share here. I hope these different interpretations can make things easier for you too, or increase your understanding at the very least.

Let's start looking at a basic distinction in binary classification tasks: the confusion matrix.

## Confusion matrix

Given a classification algorithm, a confusion matrix is a table where the rows represent the reality (the actual classes) and the columns represent the predictions (the predicted classes). For a binary classification problem, we would have the following:

<style type="text/css">
.tg1  {border-collapse:collapse;border-spacing:0;
    margin-left:auto;
    margin-right:auto;}
.tg1 td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg1 th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg1 .tg1-r6y0{background-color:#efefef;color:#656565;border-color:#000000;text-align:center}
.tg1 .tg1-obcv{border-color:#000000;text-align:center}
.tg1 .tg1-yes0{font-weight:bold;border-color:#000000;text-align:center;background-color:#efefef}
</style>
<div class="overflow-wrapper">
<table class="tg1">
  <tr>
    <th class="tg1-r6y0" colspan="2" rowspan="2"><div style="transform: rotate(-35deg)">Confusion Matrix</div></th>
    <th class="tg1-yes0" colspan="2">Prediction $(\hat Y)$</th>
  </tr>
  <tr>
    <td class="tg1-yes0">False $(\hat Y = 0)$</td>
    <td class="tg1-yes0">True $(\hat Y = 1)$</td>
  </tr>
  <tr>
    <td class="tg1-yes0" rowspan="2">Reality $(Y)$</td>
    <td class="tg1-yes0">False $(Y = 0)$</td>
    <td class="tg1-obcv">True Negatives<br>$\TN$</td>
    <td class="tg1-obcv">False Positives<br>$\FP$</td>
  </tr>
  <tr>
    <td class="tg1-yes0">True $(Y = 1)$</td>
    <td class="tg1-obcv">False Negatives<br>$\FN$</td>
    <td class="tg1-obcv">True Positives<br>$\TP$</td>
  </tr>
</table>
</div>

<!-- <br>where the value of each cell is denoted by its traditional nomenclature: $\TP$, $\TN$, $\FP$, and $\FN$, for True Positives, True Negatives, False Positives, and False Negatives, respectively. -->

<br>where $Y$ represents the ground truth and $\hat Y$ the predicted classes, and the meaning of the four cells correspond to:

<style type="text/css">
.tg2  {border-collapse:collapse;border-spacing:0;
    margin-left:auto;
    margin-right:auto;}
.tg2 td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg2 th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg2 .tg2-l711{border-color:inherit}
.tg2 .tg2-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg2 .tg2-uys7{border-color:inherit;text-align:center}
.tg2 .tg2-us36{border-color:inherit;vertical-align:top}
.tg2 .tg2-i13m{font-weight:bold;background-color:#efefef;border-color:inherit}
</style>
<div class="overflow-wrapper">
<table class="tg2">
  <tr>
    <th class="tg2-i13m" colspan="2">Classifier as reference</th>
    <th class="tg2-i13m" colspan="2">Reality as reference</th>
  </tr>
  <tr>
    <td class="tg2-uys7">$\TP$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of correct positive predictions</span></td>
    <td class="tg2-uys7">$\Pc$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of positive examples predicted correctly</span></td>
  </tr>
  <tr>
    <td class="tg2-uys7">$\FP$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of incorrect positive predictions</span></td>
    <td class="tg2-uys7">$\Nw$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of negative examples predicted incorrectly</span></td>
  </tr>
  <tr>
    <td class="tg2-uys7">$\TN$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of correct negative predictions</span></td>
    <td class="tg2-uys7">$\Nc$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of negative examples predicted correctly</span></td>
  </tr>
  <tr>
    <td class="tg2-c3ow">$\FN$</td>
    <td class="tg2-us36"><span style="font-size: 0.8em;">Number of incorrect negative predictions</span></td>
    <td class="tg2-c3ow">$\Pw$</td>
    <td class="tg2-us36"><span style="font-size: 0.8em;">Number of positive examples predicted incorrectly</span></td>
  </tr>
</table>
</div>


<br>As I have always found the traditional terms (TP, FP, TN, and FN) kind of confusing (sure, they come from the confusion matrix), I extended the table above with a point of view grounded in reality, rather than in the classifier (as it is traditionally done). For some reason, it feels more intuitive to me, maybe because we are used to taking what we consider real as the default point of reference. In the notation adopted, notice that the italic font helps differentiate between the two points of reference.

Also, notice that the new notation does not rely on using *True* and *False* to denote the correctness of a prediction, which can easily be confused by the value of the prediction classes instead.


<!-- In the following sections, we are going to use these different points of view to simplify our line of reasoning and understand the metrics (hopefully) with less mental strain. -->







## Single-Value Measures: summarizing the confusion matrix
<!-- Terms and derivations from the confusion matrix -->

While the confusion matrix presents counts for each possible outcome, it is not straightforward to interpret a classifier's performance based on it. Hence, scientists have designed measures that try to *summarize* the confusion matrix into a single value.

Before we address the measures themselves, let's begin with a comprehensive table that presents different perspectives for each measure, including their relationship with the concepts defined by the confusion matrix. Each double-line border in the table marks a different section, that groups related concepts together.

<!-- In this section we present a comprehensive table with different points of view for concepts derived from the our initial distinctions defined in the confusion matrix. Each double-line border marks the beginning of a new section, composed of concepts that make sense to be grouped together. The table is divided by double-line borders to distinguish what I will call different sections. -->

<style type="text/css">
.tg3 {
    border-collapse: collapse;
    border-spacing:0;
    width: 76em;

    margin-left:auto;
    margin-right:auto;
}
.tg3 td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg3 th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg3 .tg3-j969{font-weight:bold;background-color:#efefef;border-color:inherit}
.tg3 .tg3-hko8{border-color:inherit; text-align:center}
.tg3 .tg3-yzja{border-color:inherit;text-align:center}
.tg3 .double {border-top: 3px double;}
/* .tg3 .darker {background-color: #CCC;} */
</style>
<div class="overflow-wrapper">
<table class="tg3">
  <tr>
    <th class="tg3-j969" colspan="3">Concept</th>
    <th class="tg3-j969" colspan="1">Classifier as reference</th>
    <th class="tg3-j969" colspan="1">Reality as reference</th>
    <th class="tg3-j969" colspan="2">Observations</th>
  </tr>
  <tr>
    <td class="tg3-hko8">Accuracy</td>
    <td class="tg3-hko8">$\text{ACC}$</td>
    <td class="tg3-hko8">$$\prob\left(\hat Y = Y\right)$$</td>
    <td class="tg3-hko8">$$\frac{\TP + \TN}{\TP + \TN + \FP + \FN}$$</td>
    <td class="tg3-hko8">$$\frac{\Pc + \Nc}{\Pc + \Nc + \Pw + \Nw}$$</td>
    <td class="tg3-hko8">$$\frac{\text{correct predictions}}{\text{all examples}}$$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of correct predictions considering all examples</span></td>
  </tr>
  <tr class="double">
    <td class="tg3-hko8">Recall<br><span style="font-size: 0.8em">(Sensitivity)<br>(True Positive Rate)</span></td>
    <td class="tg3-hko8">$\text{TPR}$</td>
    <td class="tg3-hko8">$$\prob\left(\hat Y = 1 \mid Y = 1 \right)$$</td>
    <td class="tg3-hko8">$$\frac{\TP}{\TP + \FN}$$</td>
    <td class="tg3-hko8">$$\frac{\Pc}{\Pc + \Pw}$$</td>
    <td class="tg3-hko8">$$\frac{\text{correct positive predictions}}{\text{all positive examples}}$$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of correct predictions considering only positive examples</span></td>
  </tr>
  <tr>
    <td class="tg3-hko8">Specificity<br><span style="font-size: 0.8em">(True Negative Rate)</span></td>
    <td class="tg3-hko8">$\text{TNR}$</td>
    <td class="tg3-hko8">$$\prob\left(\hat Y = 0 \mid Y = 0 \right)$$</td>
    <td class="tg3-hko8">$$\frac{\TN}{\TN + \FP}$$</td>
    <td class="tg3-hko8">$$\frac{\Nc}{\Nc + \Nw}$$</td>
    <td class="tg3-hko8">$$\frac{\text{correct negative predictions}}{\text{all negative examples}}$$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of correct predictions considering only negative examples</span></td>
  </tr>
  <tr class="darker">
    <td class="tg3-hko8">False Negative Rate</td>
    <td class="tg3-hko8">$\text{FNR}$</td>
    <td class="tg3-hko8">$$\prob\left(\hat Y = 0 \mid Y = 1 \right)$$</td>
    <td class="tg3-hko8">$$\frac{\FN}{\FN + \TP}$$</td>
    <td class="tg3-hko8">$$\frac{\Pw}{\Pw + \Pc}$$</td>
    <td class="tg3-hko8">$= 1 - \text{TPR}$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of incorrect predictions considering only positive examples</span></td>
  </tr>
  <tr class="darker">
    <td class="tg3-hko8">False Positive Rate</td>
    <td class="tg3-hko8">$\text{FPR}$</td>
    <td class="tg3-hko8">$$\prob\left(\hat Y = 1 \mid Y = 0 \right)$$</td>
    <td class="tg3-hko8">$$\frac{\FP}{\FP + \TN}$$</td>
    <td class="tg3-hko8">$$\frac{\Nw}{\Nw + \Nc}$$</td>
    <td class="tg3-hko8">$= 1 - \text{TNR}$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of incorrect predictions considering only negative examples</span></td>
  </tr>
  <tr class="double">
    <td class="tg3-hko8">Precision<br><span style="font-size: 0.8em">(Positive Predictive Value)</span></td>
    <td class="tg3-hko8">$\text{PPV}$</td>
    <td class="tg3-hko8">$$\prob\left(Y = 1 \mid \hat Y = 1 \right)$$</td>
    <td class="tg3-hko8">$$\frac{\TP}{\TP + \FP}$$</td>
    <td class="tg3-hko8">$$\frac{\Pc}{\Pc + \Nw}$$</td>
    <td class="tg3-hko8">$$\frac{\text{number of true positives}}{\text{number of positive calls}}$$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of correct predictions considering only positive predictions</span></td>
  </tr>
  <tr>
    <td class="tg3-hko8">Negative Predictive Value</td>
    <td class="tg3-hko8">$\text{NPV}$</td>
    <td class="tg3-hko8">$$\prob\left(Y = 0 \mid \hat Y = 0 \right)$$</td>
    <td class="tg3-hko8">$$\frac{\TN}{\TN + \FN}$$</td>
    <td class="tg3-hko8">$$\frac{\Nc}{\Nc + \Pw}$$</td>
    <td class="tg3-hko8">$$\frac{\text{number of true negatives}}{\text{number of negative calls}}$$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of correct predictions considering only negative predictions</span></td>
  </tr>
  <tr>
    <td class="tg3-hko8">False Discovery Rate</td>
    <td class="tg3-hko8">$\text{FDR}$</td>
    <td class="tg3-hko8">$$\prob\left(Y = 0 \mid \hat Y = 1 \right)$$</td>
    <td class="tg3-hko8">$$\frac{\FP}{\FP + \TP}$$</td>
    <td class="tg3-hko8">$$\frac{\Nw}{\Nw + \Pc}$$</td>
    <td class="tg3-hko8">$= 1 - \text{PPV}$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of incorrect predictions considering only positive predictions</span></td>
  </tr>
  <tr>
    <td class="tg3-hko8">False Omission Rate</td>
    <td class="tg3-hko8">$\text{FOR}$</td>
    <td class="tg3-hko8">$$\prob\left(Y = 1 \mid \hat Y = 0 \right)$$</td>
    <td class="tg3-hko8">$$\frac{\FN}{\FN + \TN}$$</td>
    <td class="tg3-hko8">$$\frac{\Pw}{\Pw + \Nc}$$</td>
    <td class="tg3-hko8">$= 1 - \text{NPV}$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Proportion of incorrect predictions considering only negative predictions</span></td>
  </tr>
  <tr class="double">
    <td class="tg3-hko8">F1 Score</td>
    <td class="tg3-hko8">$\text{F}_1$</td>
    <td class="tg3-hko8"><span style="">$$H \left( \text{TPR}, \text{PPV} \right)$$</span></td>
    <td class="tg3-hko8">$$\frac{2\TP}{2\TP + \FP + \FN}$$</td>
    <td class="tg3-hko8">$$\frac{2\Pc}{2\Pc + \Nw + \Pw}$$</td>
    <td class="tg3-hko8">$$2\cdot\frac{\text{PPV}\cdot\text{TPR}}{\text{PPV} + \text{TPR}}$$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Harmonic mean of precision and recall</span></td>
  </tr>
  <tr class="double">
    <td class="tg3-hko8">Matthews Correlation Coefficient</td>
    <td class="tg3-hko8">$\text{MCC}$</td>
    <td class="tg3-hko8"><span style="">$$\text{corr}\left( \hat Y, Y \right)$$</span></td>
    <td class="tg3-hko8">$$\tiny{\frac{\TP\cdot\TN - \FP\cdot\FN}{\sqrt{(\TP+\FP)(\TP+\FN)(\TN+\FP)(\TN+\FN)}}}$$</td>
    <td class="tg3-hko8">$$\tiny{\frac{\Pc\cdot\Nc - \Nw\cdot\Pw}{\sqrt{(\Pc+\Nw)(\Pc+\Pw)(\Nc+\Nw)(\Nc+\Pw)}}}$$</td>
    <td class="tg3-hko8">$+ \sqrt{\text{PPV} \cdot \text{TPR} \cdot \text{TNR} \cdot \text{NPV}}$ $- \sqrt{\text{FDR} \cdot \text{FNR} \cdot \text{FPR} \cdot \text{FOR}}$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Correlation coefficient between predictions and reality as two binary variables</span></td>
  </tr>
</table>
</div>

<br>Particularly, the third column of the table above deserves a closer look: there we define some concepts in terms of *probabilities*, motivated by [this great answer](https://stats.stackexchange.com/a/7210/144362).

<!-- As you can see, the table above is separated in sections, divided by the double-line borders. -->

### Accuracy

In the first section there is accuracy, defined by a prior probability (not conditioned on anything). From this, it's easy to see why accuracy is such a common metric: a model with good accuracy tends to perform generally well. And, of course, the price we pay by only looking at accuracy is to risk performing poorly in specific cases, such as when there are class imbalances in the baseline probabilities of the problem we are dealing with.

In contrast to this generality, we can define more specific metrics using conditional probabilities. Section 2 comprises the metrics that are defined by probabilities *conditioned on the examples' true (real) class*, while section 3 comprises metrics that are *conditioned on the classifier's predicted class*. In other words, metrics from section 2 measure performance on examples that belong to a specific class in reality, while metrics from section 3 measure the preciseness of the classifier *after* it predicted a specific class.


### Precision & Recall

In order to better assess the model's performance in datasets with imbalanced classes and where we are more interested in the positive rather than in the negative class, we must move away from accuracy and into metrics from sections 2 and 3 mentioned above. In fact, when we have large class imbalances, accuracy is not a reliable metric at all, since it will be very insensitive to changes in how the algorithm classifies the minority classes.

To illustrate this point, consider the case where the positive examples compose only 1% of our dataset.

Since we are interested in the positive class, we take metrics that give us information about it. Remember:

- **Recall (Sensitivity)** measures positive *coverage*:<br>how many actual positives were predicted positives;
- **Precision** measures positive *exactness*:<br>how many predicted positives were actual positives. [8]

However, when trying to maximize these two metrics we arrive at a compromise: if one cares only about recall, one could predict all examples as positive (e.g., make the threshold in a score-based classifier very low). On the other hand, if one cares only about precision, one could predict an example as positive only when one is 100% sure of that (e.g., make the threshold very high). And it is exactly in trying to find a sweet spot between these two that the F-score comes into play...

@todo: make a reference to the following link, saying it may be interesting to check it out and refer to other definitions of precision
https://en.wikipedia.org/wiki/Accuracy_and_precision


### F-Score

The **F-Score** is a way of representing both precision and recall and finding a balance between them. In order to ensure that the score will be high only when both metrics are high, it uses a weighted *harmonic mean* between precision and recall (remember that the harmonic mean is always closer to the smaller value, differently from the arithmetic mean):

$$
\text{F}_{\beta} = (1 + \beta^2) \cdot \frac{\text{precision}\cdot\text{recall}}{(\beta^2 \cdot \text{precision}) + \text{recall}}
$$

In practice, often this general definition of the F-Score is left aside, and the **F1-Score** (the special case when $\beta = 1$) is used by default. Be aware of this oversimplification, and ask yourself whether different weights between precision and recall can make a difference for your task at hand.

Interestingly, there is a *set theoretic* way of looking at the F-Score: it corresponds to the number of items in the intersection between the set of positive-predicted examples and the set of real positive examples, divided by the average size of the two sets. [1]

<div style="text-align: center"><img src="/images/posts/performance_metrics/set-theoretic-view-on-F-Score_reduced60.png"></div>

Formally, let $\mathcal{\hat P}$ be the set of positive predictions and $\mathcal{P}$ be the set of true examples in a dataset. Then, the F1-Score can be calculated by:

$$
\text{F}_1 = \frac{2\TP}{2\TP + \FP + \FN} = \frac{|\mathcal{\hat P}\cap\mathcal{P}|}{\frac{|\mathcal{\hat P}| + |\mathcal{P}|}{2}}
$$

Despite balancing precision and recall, the F-Score is subject of criticism [1] due to several of its properties. Perhaps the greater one is its neglect of the true negatives, which creates asymmetry: F-Score highly favors correct classification of the positive class.

Motivated by this relevant weakness, let's now look into an interesting alternative.


### MCC: Matthews Correlation Coefficient

> While there is no perfect way of describing the confusion matrix of true and false positives and negatives by a single number, the Matthews correlation coefficient is generally regarded as being one of the best such measures. [6]

To try to best capture the confusion matrix into a single number, the MCC builds on a simple and intuitive idea: use the *correlation* between the observed and predicted binary classifications.

$$
\text{MCC} = \text{corr}\left( \hat Y, Y \right) = \frac{\TP\cdot\TN - \FP\cdot\FN}{\sqrt{(\TP+\FP)(\TP+\FN)(\TN+\FP)(\TN+\FN)}}
$$

Understanding the essence of the MCC is crucial because, knowing it is a correlation, we can easily deduce its properties: it returns a value between $-1$ and $+1$, with the latter corresponding to the perfect prediction (our classifier is completely correlated with the ground truth), and the value $0$ corresponding to random guessing.

From its formula, it is also possible to see that it takes into account all the four classes of the confusion matrix, combining both coverage and exactness in a balanced way [8].

> The advantage of the MCC is that it generates a high score only if your model is able to predict a high percentage of true positives and a high percentage of true negatives, on any balanced or imbalanced dataset. [11]



## Curve Measures: assessing score-based classifiers

Score-based classification methods produce their output by first generating a prediction score (a real number) for each example and then applying a threshold $\tau$ on top of it, to differentiate between negative and positive classes.

Thus, the value defined for the threshold impacts on the predicted classes and, ultimately, on the confusion matrix.

This means that, by exploring all of the possible values the threshold can take, one can construct the set of all possible confusion matrices given a score-based classifier. Moreover, with such set of confusion matrices, one can go even further and plot curves based on single-value measures derived from those confusion matrices.

Based on this idea, scientists have designed measures that try to summarize the classifier's curve, which we call *curve-measures*.

<!-- To better assess the performance of such models, scientists have designed measures that are based on summarizing the curve one can draw by varying the threshold values, which we call *curve-measures*. -->

### ROC Curve

<!-- https://stats.stackexchange.com/questions/225210/accuracy-vs-area-under-the-roc-curve -->

From my experience so far, the area under the ROC curve is strictly related to the separation of the score distributions.


https://stats.stackexchange.com/questions/144070/simple-question-about-roc-curve

The ROC curve is created by plotting TPR x FPR, so it looks on the performance of the model on the actual classes.
The ROC curve shows you how well the algorithm is able to separate true examples from false examples, regardless of their proportion; the ROC curve is *unaffected by class imbalances*.

> ROC analysis provides tools to select possibly optimal models and to discard suboptimal ones independently from (and prior to specifying) the cost context or the class distribution. [10]

This characteristic has a positive and a negative side. The good news is that, since the metric is totally robust to class imbalances,


While this may seem like an advantage (to have a measure robust to class imbalance), the bad news is that it also does not tell you how well the model suits the class imbalances.





Models that separate positives from negatives similarly will have similar AUROC scores. The problem is that, when we have class imbalances, we might want to focus on

In other words, it addresses coverage, but neglects exactness.


Great visualization: http://www.navan.name/roc/
(though incomplete, because it doesn't allow to change class proportions)

#### The AUROC measure

AUROC stands for the *area under the ROC curve*


### Precision x Recall Curve

In other words, it addresses exactness


AUPR can favor models with lower F1 scores [9].


Say that it's a more comprehensive view on the balance between precision (if the model identifies true examples, how well it perform) and recall (is the model good in identifying the true examples?), of which the F1-Score is a specific instance.

!!! RElated to the phrase above: consider adding another column to the main table describing a question that the metric answers. For instance, precision answers the question: "How well does the model perform when it says an example is positive?"



### Other metrics

(get from the mcc-f1 paper)

- Balanced accuracy
- TOC

## References

1. [What the F-measure doesn’t measure...](https://arxiv.org/pdf/1503.06410.pdf)
2. [Performance Metrics for Classification problems in Machine Learning](https://medium.com/greyatom/performance-metrics-for-classification-problems-in-machine-learning-part-i-b085d432082b)
3. [Confusion Matrix -- Wikipedia](https://en.wikipedia.org/wiki/Confusion_matrix)
4. [Positive and Negative Predictive Values -- Wikipedia](https://en.wikipedia.org/wiki/Positive_and_negative_predictive_values)
5. https://stats.stackexchange.com/a/7210/144362
6. https://en.wikipedia.org/wiki/Matthews_correlation_coefficient
7. https://towardsdatascience.com/the-best-classification-metric-youve-never-heard-of-the-matthews-correlation-coefficient-3bf50a2f3e9a
8. https://arxiv.org/abs/2006.11278
9. https://papers.nips.cc/paper/5867-precision-recall-gain-curves-pr-analysis-done-right.pdf
10. https://en.wikipedia.org/wiki/Receiver_operating_characteristic
11. https://biodatamining.biomedcentral.com/articles/10.1186/s13040-017-0155-3
