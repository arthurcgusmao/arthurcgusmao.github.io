---
layout: post
title:  "Performance metrics for classification"
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
\\)The motivation for this post is that whenever I came across terms such as *False Positive Rate*, *True Negative examples*, etc., they never felt very intuitive to me. As I started to search for different forms of looking at them, I found many interesting points of view that I share here. I hope these different interpretations can make things easier for you too!


## The confusion matrix

Given a classification algorithm, a confusion matrix is a table where the rows represent the predictions (the predicted classes) and the columns represent the reality (the actual classes). For a binary classification problem, we would have the following confusion matrix:

<style type="text/css">
.tg1  {border-collapse:collapse;border-spacing:0;
    margin-left:auto;
    margin-right:auto;}
.tg1 td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg1 th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg1 .tg1-r6y0{background-color:#efefef;color:#656565;border-color:#000000;text-align:center}
.tg1 .tg1-obcv{border-color:#000000;text-align:center}
.tg1 .tg1-yes0{font-weight:bold;border-color:#000000;text-align:center}
</style>
<div class="overflow-wrapper">
<table class="tg1">
  <tr>
    <th class="tg1-r6y0" colspan="2" rowspan="2">Confusion Matrix</th>
    <th class="tg1-yes0" colspan="2">Reality</th>
  </tr>
  <tr>
    <td class="tg1-yes0">True</td>
    <td class="tg1-yes0">False</td>
  </tr>
  <tr>
    <td class="tg1-yes0" rowspan="2">Prediction</td>
    <td class="tg1-yes0">True</td>
    <td class="tg1-obcv">$\TP$</td>
    <td class="tg1-obcv">$\FP$</td>
  </tr>
  <tr>
    <td class="tg1-yes0">False</td>
    <td class="tg1-obcv">$\FN$</td>
    <td class="tg1-obcv">$\TN$</td>
  </tr>
</table>
</div>

<br>where the meaning of the four cells are described in the next table:

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
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of positive predictions that are correct</span></td>
    <td class="tg2-uys7">$\Pc$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of positive examples predicted correctly</span></td>
  </tr>
  <tr>
    <td class="tg2-uys7">$\FP$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of positive predictions that are incorrect</span></td>
    <td class="tg2-uys7">$\Nw$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of negative examples predicted incorrectly</span></td>
  </tr>
  <tr>
    <td class="tg2-uys7">$\TN$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of negative predictions that are correct</span></td>
    <td class="tg2-uys7">$\Nc$</td>
    <td class="tg2-l711"><span style="font-size: 0.8em;">Number of negative examples predicted correctly</span></td>
  </tr>
  <tr>
    <td class="tg2-c3ow">$\FN$</td>
    <td class="tg2-us36"><span style="font-size: 0.8em;">Number of negative predictions that are incorrect</span></td>
    <td class="tg2-c3ow">$\Pw$</td>
    <td class="tg2-us36"><span style="font-size: 0.8em;">Number of positive examples predicted incorrectly</span></td>
  </tr>
</table>
</div>


<br>As I have always found the traditional terms (TP, FP, TN and FN) kind of confusing (no doubt they came from the confusion matrix!), I decided to extend the table above with symbols and descriptions that are grounded in reality, instead of grounded in the classifier (as it is traditionally done). For some reason that felt more intuitive to me, maybe because we are used to take whatever we consider as reality as the default point of reference. In the notation adopted here, notice that the italic font helps differentiate between the two points of reference.

<!-- In the following sections, we are going to use these different points of view to simplify our line of reasoning and understand the metrics (hopefully) with less mental strain. -->







### Terms and derivations from the confusion matrix

In this section we present a comprehensive table with different points of view for terms that are derived from the confusion matrix.


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
    <td class="tg3-hko8">$F_1$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">-</span></td>
    <td class="tg3-hko8">$$\frac{2\TP}{2\TP + \FP + \FN}$$</td>
    <td class="tg3-hko8">$$\frac{2\Pc}{2\Pc + \Nw + \Pw}$$</td>
    <td class="tg3-hko8">$$2\cdot\frac{\text{PPV}\cdot\text{TPR}}{\text{PPV} + \text{TPR}}$$</td>
    <td class="tg3-hko8"><span style="font-size: 0.8em">Harmonic mean of precision and recall</span></td>
  </tr>
</table>
</div>

<br>I am not going to discuss each of the concepts in greater depth, but there is one column that I find interesting to highlight: the third one, where we define the concepts in terms of probabilities (motivated by [this great answer](https://stats.stackexchange.com/a/7210/144362) in stackexchange, make sure to do not miss it).

As you can see, the table above is separated in sections, divided by the double-line borders. In the first section there is accuracy, defined by a prior probability (not conditioned on anything). From this, it's easy to see why accuracy is such a common metric: a model with good accuracy tends to perform generally well. And, of course, the price we have to pay if we look only at the accuracy is to risk performing poorly in specific cases, such as when there are class imbalances in the baseline probabilities of the problem we are dealing with.

In contrast to this generality, we can define more specific metrics using conditional probabilities. Section 2 comprises the metrics that are defined by probabilities *conditioned on the examples' true (real) class*, while section 3 comprises metrics that are *conditioned on the classifier's predicted class*. In other words, metrics from section 2 measure performance on examples that belong to a specific class in reality, while metrics from section 3 measure the preciseness of the classifier *after* it predicted a specific class.


### Precision, Recall, and the F1 Score

https://arxiv.org/pdf/1503.06410.pdf

In order to better assess the model's performance in datasets with imbalanced classes and where we are more interested in the positive rather than in the negative class, we must move away from accuracy and into metrics from sections 2 and 3 mentioned above. In fact, when we have large class imbalances, accuracy should *never* be considered a reliable metric, since it will be very insensitive to changes in how the algorithm classifies the minority classes.

To illustrate this point, consider the case where the positive examples compose only 1% of our dataset.

Since we are interested in the positive class, we take metrics that give us information about it. Remember:

- **Recall (Sensitivity)** measures the capacity of the classifier predicting positive examples correctly.
- **Precision** measures the capacity of the classifier being correct after it predicted an examples as positive.

However, when trying to maximize these two metrics we arrive at a compromise: If one cares only about recall, one could predict all examples as positive (e.g., make the threshold in a score-based classifier very low). On the other hand, if one cares only about precision, one could predict an example as positive only when one is 100% sure of that (e.g., make the threshold very high).


The F1 Score is a way of representing both precision and recall and finding a balance between them. In order to ensure that the score will be high only when both metrics are high, it uses the *harmonic mean* between precision and recall (remember that the harmonic mean is always closer to the smaller value, differently from the arithmetic mean).



### ROC Curve

https://stats.stackexchange.com/questions/225210/accuracy-vs-area-under-the-roc-curve

From my experience so far, the area under the ROC curve is strictly related to the separation of the score distributions.


https://stats.stackexchange.com/questions/144070/simple-question-about-roc-curve




## Other resources

- [Performance Metrics for Classification problems in Machine Learning](https://medium.com/greyatom/performance-metrics-for-classification-problems-in-machine-learning-part-i-b085d432082b)
- [Confusion Matrix -- Wikipedia](https://en.wikipedia.org/wiki/Confusion_matrix)
- [Positive and Negative Predictive Values -- Wikipedia](https://en.wikipedia.org/wiki/Positive_and_negative_predictive_values)
