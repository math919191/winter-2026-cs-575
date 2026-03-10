# Project 1 - SEIR Model

### Names

Rebekah Daniels 

I did not work with anyone else on this project. 

### Abstract 

• Abstract: Summarize what you did and what you learned.



### Introduction

The COVID-19 pandemic dramatically influenced life. Better understanding how diseases spread can be useful. 
This report looks at the spread of disease over time using different networks. 
For each network, this report analyzed the network itself, the spread of disease in the network over time, and 
varyied parameters to compare the spread of the disease. 
This report begins by explaning the experiment conditions, then proposes hypotheses about the spread over a network.
Next, it will present results, then it will discuss which hypotheses were correct and incorrect, and finally propose some future work. 
This report also includes figures and tables discussing the results.

### Experiment Conditions


#### First Set 

The first set of experiment conditions were provided to me. They are as follows: 

The parameters I selected for the first set of experiment conditions was the parameter for my scale free networks.
I select ___ because ___. 
Here is an image demonstrating the scale free nature of the graphs I selected.
Note that the trend is largely linear on the log-log plot indicating the scale free nature of the plot. 

Here is a table describing the useful metrics about the graphs. 
The same graphs will be used for the second set of experiment conditions. 

<!-- TODO insert table here of just the graph metrics -->

<!-- TODO verify that the Barabasi ones fit the scale free nature we need -->

                   maximum degree  average degree  diameter  radius   density
Complete Graph                 99       99.000000         1       1  1.000000
Lattice Graph                   4        3.600000        18      10  0.036364
Barabasi Size 100              33        9.500000         4       3  0.095960
Barabasi Size 410              92       19.512195         3       2  0.047707
Dublin Graph                   50       13.487805         9       5  0.032978

#### Second Set 

The second set of experiments conditions I selected. 

Unless otherwise stated, I will use the same experimental conditions specfied in the first set. 

The will conduct the following experiments:

- lower the infectiousness levels (p1c decrease to __ - the equivelant of wearing a mask)
- increase time spent infectious (mu increase to __ - the equivelant of ____ )
- decrease time spent exposed (mu decrease to __ - the equivelant of ___)
- Vary multiple at the same time:
    - lower the infectious level (p1c=)
    - increase time spect infectious (mu=)
    - increase time spent exposed (mu=)

### Hypotheses

• Hypotheses: Make some hypotheses about how the virus will propagate across the different
networks under the different conditions. Give some justification for your hypotheses in terms of
network characteristics (e.g., the metrics in your summary table).

### Results

#### Experimental Conditions 1

Here is a table demonstrating interesting statistics from the simulations with the experimental conditions 1
specified above.  

<!-- TODO - include the table here:  -->

[Interesting Statistics From Simulations With Experimental Conditions 1]() 

<!-- TODO - include interesting figures here:  -->
Here are a few interesting figures from the simulations

[plot 1 - Experimental Conditions 1]() 

[plot 2 - Experimental Conditions 1]() 

[plot 3 - Experimental Conditions 1]() 


#### Experimental Conditions 2

Here is a table demonstrating interesting statistics from the simulations with the experimental conditions 1
specified above.  

<!-- TODO - include the table here:  -->

[Interesting Statistics From Simulations With Experimental Conditions 2]() 

<!-- TODO - include interesting figures here:  -->
Here are a few interesting figures from the simulations

[plot 1]() 

[plot 2]() 

[plot 3]() 


### Discussion

• Discussion: Summarize which hypotheses were supported by data and which were not supported.
Explain why you think the results came out the way they did. If you are speculating about why,
state that you are hypothesizing a possible explanation. If the reason why is justified by the
data, tell me how the data supports your explanation.

### Future Work 


• Future Work: Tell me what you wish you had done or could do now that the project is over.



### ChatGPT

found a `==` v `=` bug for me
did the animation code for me after I tried 

Create code for a time series line plot. I want to have 4 different lines. Demonstrate how I would create the plot given the data for each of the lines

Can you give me code for doing multiple iterations and finding the interquartile range of multiple iterations? 

How can I fix this bug: 


Fill this in with the associated networkx functions where possible. def useful_graph_metrics(G): return { 'the maximum degree': , 'the average degree': , 'diameter of the graph': , 'radius of the graph': , 'density': , }