1. a circulant graph with 20 vertices where each vertex is attached to two neighbors on either side
(nx.circulant graph(20,[1,2,3,4]))
2. a circulant graph with 20 vertices where each vertex is attached to four neighbors on either side
(nx.circulant graph(20,[1,2])
3. a complete graph with 100 vertices (nx.complete graph(100))
4. a 10 × 10 lattice with 100 vertices (nx.grid 2d graph(10,10))
5. a scale-free network with 100 vertices (nx.barabasi albert graph(100,???)
6. a scale-free network with 410 vertices (nx.barabasi albert graph(410,???)
7. infect-dublin network, which has 410 vertices; described and downloadable here:
https://networkrepository.com/ia-infect-dublin.php



animation stuff: 
You do not need to report experiment results for the circulant graphs.
I’m including them in the project because they are really useful for evaluating whether your code is working. 
I suggest using the color-map parameter to animate how the virus spreads over the network. 
I set a color for each state
(for example, blue for susceptible, yellow for exposed, red for infectious, and green for removed) 
and then changed the colors as the infection spread through the network using:

nx.draw(G,pos,with labels=True,node color = color map


How to do the animations / tips for the animation: 


Not for checking code: 

• More agents are infected in the network with the eight nearest neighbors than in the network
with the four nearest neighbors, using the nominal parameters above.
• The rate of infection is faster for the network with eight nearest neighbors than for the network
with four nearest neighbors.
• Most agents get infected.


Notes for complete and lattice graphs

- use code from hw 1
- we should see a difference when there is a larger diamter in the graph
- this is the baseline for what we are doing


The complete and lattice graphs are formed using the same methods you used in Homework 1. They
are to serve as your baseline for your experiment results. The diameter of the complete graph is one
so the disease should propagate most rapidly and most completely through this network. The lattice
graph has larger diameter, so this network should be more resistant to spread than the complete graph.

Scale free with 100 vertices allows for a comparison 


Do scale free with the albert barbasi grpah. 
We are supposed to pick the number of edges parameter and justify why we picked what we did.

This is the Hint for picking the parameter
__Hint: you want your degree distribution to have the signature of a scale-free network, namely the straight line in the log-log plot.__

(will determine this later after I get my code working for the other things)

We can hypthesis about how well the virus would spread in a scale free graph



For dublin, learn a little more about it and then predict it. 

Read a little about the network here https://networkrepository.com/ia-infect-dublin.php (notice the summary of network characteristics) and here
http://www.sociopatterns.org/datasets/infectious-sociopatterns-dynamic-contact-networks/
Given the network characteristics, what would you hypothesize about how the virus would spread over
the network? How are your hypotheses similar to or different from the hypotheses for the complete,
lattice, and scale-free networks?


5 by 2 experiment: 

- 5 provided graphs
- 1 set of parameters provided above and 1 set of parameters that I choose (that would be interesting) 


Time step series = time on the bottom axis and number of people on the y axis
with lines for each type in between 

We average multiple runs but also have the other runs present in lighter colors



- Same time scale
- See it reach a steady state.

Report the stats for the following :
- time-to-peak infection, 
- peak infections, 
- time until no new infections
- number of uninfected individuals at the end of the experiment.


 Figure 5 shows
what I mean by time-to-peak and peak infections. The time to reach steady state is the number of
days until there are no more agents in the infectious or exposed states. The number of uninfected
individuals will be the average number of agents in the susceptible state at the end of the simulation.


Please include the following information about each network: 
- a figure or a description of the degree distribution, 
- the maximum degree, 
- the average degree, 
- the diameter of the graph, 
- the radius of the graph, 
- the density (connectance) of the graph.
Note that networkx has methods for computing maximum degree, average degree, graph diameter, graph radius, and graph density.

Here are the stats I care about. Report it in a table. 

A useful way to present results would therefore be a table with columns {network, max degree,
avg degree, diameter, radius, density, time-to-peak infections, peak infections, time-to-steady-state,
uninfected individuals}. There would be one row per each of the five networks.


Animation: 

--> record everything and then run it
--> only change the colors that need to be changed - NOT everything: nx.draw_networkx_nodes(G, pos, nodelist=changed_nodes, node_color=new_colors)

How to actually create the cool plots? Here is the code: 

plt.fill_between(x, lbounds, ubounds, color=fill_color)
plt.plot(x, means, color=color, label=label)



