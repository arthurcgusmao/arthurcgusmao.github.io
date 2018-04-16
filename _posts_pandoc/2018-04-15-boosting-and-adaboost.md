---
final_post_front_matter:
    layout: post
    title: Boosting and AdaBoost
    category: Machine Learning
    mathjax: true

###
### Bibliography settings
###
bibliography:
    - /home/arthurcgusmao/Documents/zotero.bib
    - ./bibfiles/adaboost.bib
#csl: /home/arthurcgusmao/.csl/apa.csl
link-citations: true

---

## Introduction

*Boosting* is an approach to machine learning based on the idea of
creating a highly accurate prediction rule by combining many relatively
weak and inaccurate rules. Since it uses the output of
other learning algorithms, it may be referred to as a
meta-algorithm. Methods that use multiple learning algorithms to obtain
better predictive performance are called *ensemble methods*, and boosting is a particular case. In
this text we briefly discuss boosting in general, with a more intuitive
explanation, and focus on the very traditional *AdaBoost* algorithm, with
some practical considerations at the end.


## Some history and concepts

The idea of boosting was motivated when Micheal Kearns and Leslie
Valiant introduced the concept of *weak learnability* and posed what is
known as the *hypothesis boosting problem* in 1988.

A class of concepts
is (strongly) *learnable* if there exists a polynomial-time algorithm
that achieves low error with high confidence for all concepts in the
class. Weak learnability drops the requirement that the learner be able
to achieve arbitrarily high accuracy; a weak learning algorithm only need to be able to output a hypothesis that performs (slightly) better than random
guessing [@Schapire1989].

The *hypothesis boosting problem* asked the following question: "Can a
set of weak learning algorithms be combined into an arbitrarily strong
learner?" Robert Schapire answered it with a yes on his 1990 paper
called *The Strength of Weak Learnability*. That paper presented the
first provable polynomial-time boosting algorithm. A year later, Yoav
Freund developed a more efficient algorithm, but it still had some
practical issues. Then in 1995 Freund and Schapire developed the AdaBoost
algorithm, which solved many of the practical difficulties that the
earlier boosting algorithms had [@Ehlen2007], winning the Gödel Prize.


## What is boosting

The concept of boosting lies on the idea that we can combine many
relatively weak and inaccurate rules to create a highly accurate
prediction. The way AdaBoost does that is by combining the output of the
other learning algorithms (the weak learners) into a weighted sum that
represents the final output of the algorithm. AdaBoost is adaptive in
the sense that subsequent weak learners are tweaked in favor of those
instances misclassified by previous classifiers [@wiki:AdaBoost].

Schapire proved that it is possible to build a learner which error can
be *arbitrarily* small (i.e., a strong learner) by combining the
prediction of many different weak learners.


## Some intuition on why boosting works

We can metaphorically reformulate the hypothesis boosting problem in the
following manner: "Can we make a crowd arbitrarily smart in a specific
topic by adding to it as many individuals (specialists) as we want?"
Apparently the answer is yes, but this won't always work. Note that we
have to make sure that the new specialist should be correct more than
50%, otherwise we are decreasing our chances of getting the right
answer. Another essential thing to do is to make sure that the new
specialist included is better covering an area of the domain which we
weren't getting quite right yet, otherwise we could stay a long time
adding new specialists with very little or no improvement.

The first issue is surely covered by assuring that the learners are at
least weak learners (they should each have error below 1/2). Given this
assumption and sufficient data, a boosting algorithm can provably
produce a final hypothesis with arbitrarily small generalization error
[@Schapire2013].

The second issue is a more practical one, and is handled quite well by
AdaBoost by its adaptative property. AdaBoost tweaks each new generated
hypothesis (in each iteration) in favor of those instances misclassified
by previous classifiers. As explained by him, "The proof of this result
was based on the filtering of the distribution in a manner causing the
weak learning algorithm to eventually learn nearly the entire
distribution" [@Schapire1989].


## The AdaBoost Algorithm

![AdaBoost Algorithm](/images/posts/adaboost_alg.png)

The pseudocode for AdaBoost is shown the figure above. We are given $m$
labeled training examples $(x_1,y_m), ..., (x_m,y_m)$. On each round
$t = 1, ..., T$, a distribution $D_t$ is computed as in the figure over
the $m$ training examples, and a given weak learner is applied to find a
*weak hypothesis* $h_t$, where the aim of the weak learner is to find a
weak hypothesis with low weighted error $\epsilon_t$ relative to $D_t$.
The final or combined hypothesis $H$ computes the sign of a weighted
combination of weak hypotheses

$$
    F(x) = \sum^{T}_{t=1} \alpha_t h_t(x).
$$

As already mentioned, this is equivalent to saying that $H$ is computed
as a weighted majority vote of the weak hypotheses $h_t$ where each is
assigned weight $\alpha_t$ [@Schapire2013].

Application of the VC Theory (Vapnik and Chervonenkis) to AdaBoost predicts
that it will *always* overfit. In practice, however, one can see that
the algorithm has a quite strong resistance to overfitting. This has
been tried to be explained in many forms. Schapire came with the
*margins explanation*: in summary, AdaBoost will succeed without overfitting if the weak-hypothesis
accuracies are substantially better than random (since this will lead to
large margins), and if provided with enough data relative to the
complexity of the weak hypotheses [@Schapire2013]. We won't get into more
details here, but his hypothesis can be better understood by reading his 2013 essay "Explaining AdaBoost".

Besides resistance to overfitting, AdaBoost has many advantages: it is
fast, simple and easy to program; it has only one parameter to tune (the
number of rounds); it requires no prior knowledge about the weak
learner [@Ehlen2007].

AdaBoost also has an ability to identify outliers. Because it focuses
its weights on the hardest examples, the examples with the highest weight
often turn out to be outliers. However, when the number of outliers is
very large, the emphasis placed on the hard examples can become
detrimental to the performance of the algorithm. This was demonstrated
in practice, and a variant of the algorithm called "Gentle AdaBoost",
which puts less emphasis on outliers, was proposed [@Ehlen2007].

A paper published by Phillip Long and Rocco A. Servedio in 2008
suggested that many boosting algorithms, including AdaBoost, are
probably flawed. They concluded that "convex potential boosters cannot
withstand random classification noise" [@Long:2010:RCN:1713649.1713653],
therefore making the applicability of such algorithms for real world
with noisy datasets questionable. The paper shows that if any fraction
of the training data is mis-labeled, the boosting algorithm tries
extremely hard to correctly classify these training examples, and fails
to produce a model with accuracy much better than random guessing [@wiki:boosting
].

## Conclusion

We have seen some key concepts in understanding boosting in general and
AdaBoost in particular. Some historical context was presented. An
intuitive vision on why boosting works was favored, and then the
AdaBoost Algorithm was analysed. Advantages and disadvantages were
discussed, together with some proposed explanations on how and why
AdaBoost works and practical considerations.

------------------------------------------------------------------------

oq da pra melhorar:

-   falar sobre o que eu respondi naquele topico do stackoverflow


## References
