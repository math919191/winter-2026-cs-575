
import math
import random
import numpy as np
import copy



SUSCEPTIBLE = "S"
EXPOSED = "E"
INFECTED = "I"
RECOVERED = "R"

valid_states = {
    SUSCEPTIBLE, EXPOSED, INFECTED, RECOVERED
}

def sample_log_dist(mu, omega):
    # log_normal_distribution()
    # ChatGPT gave this function to me and I modified it. 
    return np.random.lognormal(mean=mu, sigma=omega)

class Agent:
    def __init__(self, initial_state=SUSCEPTIBLE):
        self.countdown_to_infectious = math.ceil(sample_log_dist(mu=1, omega=1))
        self.countdown_to_recovered = math.ceil(sample_log_dist(mu=2.25, omega=.105))
        self.days_spent_infectious = 0
        self.state = initial_state

    def step(self, neighbors):
        if self.state == EXPOSED:
            self.countdown_to_infectious -= 1
            if self.countdown_to_infectious == 0: 
                self.state = INFECTED
        elif self.state == INFECTED:
            self.countdown_to_recovered -= 1
            self.days_spent_infectious += 1

            if self.countdown_to_recovered == 0: 
                self.state = RECOVERED
        elif self.state == SUSCEPTIBLE:
            if self.gets_disease(neighbors):
                self.state = EXPOSED
        # do nothing if you are recovered

    def gets_disease(self, neighbors: list[Agent]):
        for neighbor in neighbors:
            if not neighbor.state == INFECTED:
                continue 
            
            prob_infects = neighbor.get_infectious_level()
            random_num = random.random() 
            if random_num < prob_infects:
                return True

        return False

    def get_infectious_level(self, p1c=0.038, B=-0.0050367):
        if self.state == INFECTED:
            exp = math.exp(B*(self.days_spent_infectious ** 3  -1))
            num = (p1c / (1-p1c)) * exp
            den = (1 + (p1c / (1-p1c) - exp )) * exp
            return num / den
        else:
            print(f"Not infectious level for state {self.state}")
             

class PopulationManager:
    
    def __init__(self, graph, init_S=.9, init_I=.05, init_E=.05):
        if not (init_S + init_E + init_I) == 1:
            print("Error....does not total to 1")
        
        population_size = graph.number_of_nodes()

        self.agents = {} # map id to the agent itself 

        for i in range(population_size):
            if i < init_S * population_size:
                self.agents[i] = Agent(initial_state=SUSCEPTIBLE)
            elif i < ((init_S + init_I) * population_size):
                self.agents[i] = Agent(initial_state=INFECTED)
            else:
                self.agents[i] = Agent(initial_state=EXPOSED)

        self.graph = graph

        self.agent_history = []


    def _get_agent_neighbors(self, agent_id, graph, last_step_agents_dict):
        neighbor_ids = graph.neighbors(agent_id)

        return [last_step_agents_dict[id] for id in neighbor_ids]


    def step_all_agents(self):
        last_step = copy.deepcopy(self.agents)
        self.agent_history.append(last_step)

        for id, agent in self.agents.items():
            # rely on the last set of neighbors and loop over them. 
            curr_agent_neighbors = self._get_agent_neighbors(id, self.graph, last_step)
            agent.step(curr_agent_neighbors) 

    def get_history(self):
        return self.agent_history
    

    def get_history_as_counts(self):
        list1 = [sum(agent.state == SUSCEPTIBLE for agent_id, agent in snapshot.items()) 
                    for snapshot in self.agent_history                
                ]
        list2 = [sum(agent.state == EXPOSED for agent_id, agent in snapshot.items()) 
                    for snapshot in self.agent_history                
                ]
        list3 = [sum(agent.state == INFECTED for agent_id, agent in snapshot.items()) 
                    for snapshot in self.agent_history                
                ]
        list4 = [sum(agent.state == RECOVERED for agent_id, agent in snapshot.items()) 
                    for snapshot in self.agent_history                
                ]       
        return [list1, list2, list3, list4]

    def get_color_map(self, step_num):
        colors = {
            SUSCEPTIBLE : "blue",
            EXPOSED : "yellow",
            INFECTED : "red",
            RECOVERED : "green"
        }

        return [
            colors[agent.state]
            for agent_id, agent in self.agent_history[step_num].items()
        ]
 
    def get_useful_metrics(self):
        susceptible_history, exposed_history, infected_history, recovered_history = self.get_history_as_counts()
        
        def find_steady_time(lst):
            index = len(lst) - 1  
            for i in range(len(lst)-1, -1, -1):
                if lst[i] == lst[-1]:
                    index = i
                else:
                    break

            return index

        return {
            'time to peak infection': infected_history.index(max(infected_history)),
            'peak infections': max(infected_history),
            'time when steady state reached': max(find_steady_time(exposed_history), find_steady_time(infected_history)),
            'number of uninfected individuals at the end of the experiment': susceptible_history[-1]
        }



import networkx as nx
def useful_graph_metrics(G):

    return {
        'maximum degree': max(dict(G.degree()).values()),
        'average degree': sum(dict(G.degree()).values()) / G.number_of_nodes(),
        'diameter': nx.diameter(G),
        'radius': nx.radius(G),
        'density': nx.density(G),
    }

    # a figure or a description of the degree distribution, 
    # the maximum degree, the average degree, the diameter of the graph, the radius of the graph, and the density (connectance) of the graph. 
    # Note that networkx has methods for computing maximum degree, average
    # degree, graph diameter, graph radius, and graph density.

