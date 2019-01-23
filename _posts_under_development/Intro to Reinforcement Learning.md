This is meant to be an extremely simple introduction to reinforcement learning (RL). Let's dive in.

### The Markov Decision Process (MDP) setting

In RL, we want an agent to learn an optimal set of actions so that it can succeed in a given environment. Usually, we have the scenario where the agent can sense the whole environment (i.e., the environment is fully observable), but it doesn't know how the environment works, neither the results of the actions.
We describe the agent's current situation as its state, denoted by $s$. After taking an action, the agent is led to a new state $s'$ (which may even be the same initial state, i.e., after taking the given action the situation hasn't changed).
Also, we assume that a single action may result in several different outcomes, given an unknown probabilistic mapping from actions to outcomes. Hence, we model how the environment works by a *transition model* $P(s^{'} \mid s, a)$. In order to 'tell' the agent how well it is performing, for each state the agent receives a reward, determined in our model by a *reward function* $R(s)$, that maps states to a scalar that represents the respective reward value. With the setting described above the agent faces a *Markov Decision Process* (MDP). This name origins from the fact that by defining the problem in this way we are dealing with a *Markovian process*: the probability of going to a state $s'$ does not depend on any state previous to $s'$s immediate previous state $s$.

### Policy: a solution to the MDP

A *policy*, denoted by $\pi(s)$, is a solution for the MDP that maps states to actions. Another way to put that we want the agent to learn an optimal set of actions is to say that we want it to learn an *optimal policy* $\pi^*$.

== old ==

To solve this problem, we consider three types of agent design:

| Reflex agent              | Q-learning (model free)             | Model based                   |
|---------------------------+-------------------------------------+-------------------------------|
| <>                        | <>                                  | <>                            |
| Searches the policy space | Learns an action → utility function | Learns the *transition model* |
|                           |                                     | and the *reward function*     |
