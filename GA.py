"""
Society Generator genetic algorithm maximizer implementation.

:author: Max Milazzo
"""


from random import random, uniform, randint
# module imports


# GA class
class GA:

    def __init__(self, mutation_chance=0.3, mutation_factor=0.3, crossover_chance=0.1, survival_chance=0.3):
        """
        GA constructor.
        
        :param mutation_chance: chance of mutation for each new child
        :param mutation_factor: defines the relative maximum percent that a gene can be altered during mutation
        :param crossover_chance: chance of genetic crossover occuring for each indidvual gene in all parents
        :param survival_chance: defines the cutoff percentile for parent survival
        :type mutation_chance: float
        :type mutation_factor: float
        :type crossover_chance:float
        :type survival_chance: float
        """
        
        self.data = []
        self.fitness = []
        self.size = 0
        self.mutation_chance = mutation_chance
        self.mutation_factor = mutation_factor
        self.crossover_chance = crossover_chance
        self.survival_num = int(survival_chance * self.size)


    def __select_parents(self):
        """
        Selects the best parents based on which had the highest maximization.
        """
        
        self.data.sort(reverse=True)
        self.data = self.data[:self.survival_num]


    def __breed(self):
        """
        Combines population data to "breed" and create offspring.
        
        :pre: parent data array size is at least 2
        """
        
        children = []
        
        for parent_1_index in range(self.size - 1):
        # loops through parents
        
            for parent_2_index in range(parent_1_index + 1, self.size):
            # selects breeding partner parent
            
                for interior_list_index in range(self.gene_count):
                    
                    child = []
                    parent_1_data = self.data[parent_1_index][interior_list_index]
                    parent_2_data = self.data[parent_2_index][interior_list_index]
                    # gets data
                        
                    if random > 0.5:
                    # 50% chance of getting average of traits, 25% chance of getting trait from each individual parent
                    
                        if random() > 0.5:
                            child.append(parent_1_data)
                        else:
                            child.append(parent_2_data)
                            
                    else:
                        child.append((parent_1_data + parent_2_data) / 2)
                    
                    children.append(child)
        
        self.data = children
        self.size = len(children)
        # sets children as new GA data values


    def __crossover(self):
        """
        Crosses random genes between offspring.
        """
        
        for child_index in range(self.size):
        
            for gene_index in range(self.gene_count):

                if self.crossover_chance > random():
                
                    crossover_child_index = randint(0, self.size)
                    
                    child_temp = self.data[child_index][gene_index]
                    self.data[child_index][gene_index] = self.data[crossover_child_index][gene_index]
                    self.data[crossover_child_index][gene_index] = child_temp
                    # swaps genes at random index


    def __mutate(self):
        """
        Mutates offspring.
        """
        
        for child_index in range(self.size):
        
            for gene_index in range(self.gene_count):
            
                if self.mutation_chance > random():
                
                    self.data[child_index][gene_index] *= (1 + self.mutation_factor) * random.uniform(-1, 1)
                    # mutates random gene
    
        
    def run(self, data, fitness):
        """
        Runs GA and returns its current data.
        
        :param data: a list of properly formatted genetic parents
        :param fitness: fitness values associated with data parents
        :type data: list of list of floats
        :type fitness: list of floats
        :return: GA data
        :rtype: list of list of floats
        """
        
        if (len(data) > 1):
        # parent data array must be of size 2 or greater
        
            self.data = data
            self.size = len(data)
            self.gene_count = len(data[0])
            self.fitness = fitness
            # sets passed data
            
            self.__select_parents()
            self.__breed()
            self.__crossover()
            self.__mutate()
            # runs GA functions
            
            return self.data
            
        else:
        # prints usage message and returns -1 to signify error code
        
            print("GA Error: parent data array must be of size 2 or greater")            
            return -1