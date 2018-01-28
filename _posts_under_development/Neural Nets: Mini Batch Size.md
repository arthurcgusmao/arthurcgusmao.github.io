# The mini batch size trade-off in neural networks

When we think about ways of updating the weights of our neural network via gradient descent, there are two extremes we can take:

- **Batch training**: present the entire dataset to the algorithm, sum the weight changes and only then apply them;
- **Online training**: for each example of the dataset, update weights instantly and then move on to the next example (and the next update)



---

ideia geral:

- falar sobre a vantagem de treinar em batch por causa da paralelizacao (velocidade); fazer testes usando o TFLearn para diferentes batch sizes mantendo os outros parametros iguais e ver a velocidade ali no canto superior direito.
- falar sobre a learning rate: faz sentido dizer que ela tem que diminuir quando ja dividimos o update total pelo numero do batch?
- ver e testar se no TFLearn o update dos weights eh feito dividindo a some dos deltas pelo batch size ou se ele simplesmente soma a porra toda
- falar sobre o lance da probabilidade de escapar de um minimo local muito proximo vs ficar pulando de um canto pra outro e nao convergir nunca


---

References tagged as *Batch training* in Zotero.
Also, see [this post](https://www.quora.com/Intuitively-how-does-mini-batch-size-affect-the-performance-of-stochastic-gradient-descent) in quora.
