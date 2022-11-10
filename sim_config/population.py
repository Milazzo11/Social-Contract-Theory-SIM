"""
Defines a population (or group) containing many people.

:author: Max Milazzo
"""


from random import randint, uniform
from optimization import GA, DT


class Population:

    def __init__(self, size):
        """
        Population class constructor.
        
        :param size: population size
        :type size: int
        """
        
        # ========================
        # PERSON DATA CONSTRUCTION
        # ========================
        # List Format: [FREQUENCY, WORK_ABILITY, CONSUMPTION_NEEDS]
        # ========================
        
        PDCL = [
        
            [0.05, 0, 0.5]  # no skill, low need
            [0.05, 0.5, 0.5]  # low skill, low need
            [0.1, 1, 0.5]  # med skill, low need
            [0.05, 1.5, 0.5]  # high skill, low need
        
            [0.05, 0, 1]  # no skill, med need
            [0.1, 0.5, 1]  # low skill, med need
            [0.2, 1, 1]  # med skill, med need
            [0.1, 1.5, 1]  # high skill, med need
        
            [0.05, 0, 1.5]  # no skill, high need
            [0.1, 0.5, 1.5]  # low skill, high need
            [0.1, 1, 1.5]  # med skill, high need
            [0.05, 1.5, 1.5]  # high skill, high need
            
        ]
        # population data construction list
        
        self.people = []
        
        # adds people to object list
        for p_types in PDCL:
            for p_count in range(PDCL[0] * size):
            
                infection_state = False
                
                # adds disease infection chance to person construction
                if random() < 0.01:
                    infection_state = True
                    
                self.people.append(Person(age=randint(0, 40), 
                                    sex="R", 
                                    infected=infection_state,
                                    consumption=PDCL[2],
                                    work_ability=PDCL[1]
                )
                
        # public community resources
        self.food = 0
        self.water = 0
        self.shelter = 0
        self.clothing = 0




# ===================
# New Person Creation
# ===================


    def birth(self):
        """
        """


# =======================
# PERSON ACTION FUNCTIONS
# =======================
#
#
# =======================


    def _a_kill(self, killer, victim):
        """
        Kill action.
        
        :param killer: killer
        :param victim: victim being killed
        """
        
        killer.satisfy(uniform(-2, 1))
        
        victim.dissatisy(5)
        victim.die()


# =============================================================================
# =============================================================================


    def _a_sex(self, p1, p2):
        """
        """
        
        p1.satisfy(5)
        p2.satisfy(5)
        
        if p1.infected() != -1:
            p2.infection_progress()
            
        if p2.infected() != -1:
            p1.infection_progress()
            
        if p1.get_sex() != p2.get_sex():  # checks person genders
            self.birth()


# =============================================================================
# =============================================================================


    def _a_steal_per(self, item, robber, victim):
        """
        """
        
        
# =============================================================================
# =============================================================================


    def _a_steal_pop(self, item, robber):
        """
        """
   

# =============================================================================
# =============================================================================


    def _a_donate_per(self, item, giver, receiver):
        """
        """


# =============================================================================
# =============================================================================


    def _a_donate_pop(self, item, giver, receiver):
        """
        """


# ===================================
# PERSON OPTIMIZATION LOGIC FUNCTIONS
# ===================================
#
# ===================================








# =======================
# POPULATION TIME HANDLER
# =======================
# Defines "run" function to move all people forward 1 unit in time
# Additional private functions can be called here as well
# =======================
    
    
    def __get_resource_schema(self):
        return [[]]
        
        
    def __action_manager(self):
        pass
    

    def run(self):
        """
        """
        
        resource_schema = self.__get_resource_schema()
        # defines resource consumption/production decision schema
        
        for per_index in range(len(self.people)):
            self.person[per_index].run(basic_schema[per_index])
            
            self.__action_manager(self.person[per_index])
            # manages person run action
            # person may take 1 additional action per time period