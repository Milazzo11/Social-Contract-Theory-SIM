"""
Defines the traits associated with a single person living in a society.

:author: Max Milazzo
"""


from math import log
from random import random
# module imports


class Person:


# =================
# CLASS CONSTRUCTOR
# =================
# defines base features of a person
# can (if needed) be altered to accomodate more person types
# =================


    def __init__(self, consumption=1, work_ability=1, work_intolerance=1, start_satisfaction=1):
        """
        Person class constructor.
        
        :param consumption: the amount that a person "needs" to consume relative to a "standard" value of 1 (larger value = more consumption needed)
        :param work_ability: how well a perosn can perform work to produce resources (larger value = more efficiency, value of 1 is "standard")
        :param work_intolerance: the rate at which a person loses satisfaction from having to work (larger value = greater dislike of work, value of 1 is "standard")
        :type consumption: float
        :type work_ability: float
        :type work_intolerance: float
        """
        
        self.satisfaction = start_satisfaction
        self.is_alive = True
        self.consumption_ratio = 1 / consumption
        self.work_ability = work_ability
        self.work_intolerance = work_intolerance


# =======================
# PUBLIC GETTER FUNCTIONS
# =======================


    @property
    def satisfaction(self):
        return self.satisfaction
        

    @property
    def is_alive(self):
        return self.is_alive


# =======================
# CONSUMPTION DEFINITIONS
# =======================
# conventially these functions will begin with "_c_"
# defines the "consumption" funtions for each individual person during some arbitrary time period N
# functions take in a consumption amount value 'c' and edits the amount of individual satisfaction 's' gained from that consumption and other possible person attributes
# =======================


    # food
    def _c_food(self, c):
        food = 3 * self.consumption_ratio * log(c + 1)
        
        if food >= 0.7:
            self.satisfaction += food
        elif food < 0.7 and food >= 0.2
            self.satisfaction -= 1 / food
        else:
            self.is_alive = False


    # water
    def _c_water(self, c):
        water = 3 * self.consumption_ratio * log(10 * c + 1)
        
        if water >= 1:
            self.satisfaction += 3
        elif water < 1 and c >= 0.4:
            self.satisfaction -= 1 / water
        else:
            self.is_alive = False


    # shelter
    def _c_shelter(self, c):
        shelter = 2 * self.consumption_ratio * log(5 * C + 1)
        
        if shelter >= 1:
            self.satisfaction += 2
        else:
            self.satisfaction -= 3


    # clothing
    def _c_clothing(self, c):
        clothing = 2 * self.consumption_ratio * log(10 * C + 1)
    
        if clothing > 1:
            self.satisfaction += clothing
        elif clothing < 0.1:
            self.satisfaction -= 1


# =======================================
# CONSUMPTION GLOBAL ACCESS (DO NOT EDIT)
# =======================================


    def consumption(self):
        """
        Returns consumption functions used.
        
        :return: consumption functions
        :rtype: tuple
        """
        
        return (
            self._c_food,
            self._c_water,
            self._c_shelter,
            self._c_clothing
        )
        

# ======================
# PRODUCTION DEFINITIONS
# ======================
# conventially these functions will begin with "_p_"
# defines the resources/work functions for some arbitrary time period N for an individual worker
# functions take in a work amount value 'w' and return the amount of resource 'r' produced and edit the amount of satisfaction lost from completing this work 's' as well as other possible person attributes
# functions should "match" the consumption functions defined above
# =======================


    # food
    def _p_food(w):
        w_int = self.work_intolerance * w

        # satisfaction calculations
        if w_int > 1:
            self.satisfaction -= 1.5 * w_int
        elif w_int > 0.5 and w_int <= 1:
            self.satisfaction -= w_int
        else:
            self.satisfaction -= 0.5 * w_int
        
        # production
        return self.work_ability * w


    # water
    def _p_water(w):
        w_int = self.work_intolerance * w
        
        # satisfaction calculations
        if w_int > 0.5:
            self.satisfaction -= 2 * w_int
        elif w_int > 0.2 and w_int <= 0.5:
            self.satisfaction -= w_int
        else:
            self.satisfaction -= 0.3 * w_int
        
        # production
        return 10 * self.work_ability * w


    # shelter
    def _p_shelter(w):
        w_int = self.work_intolerance * w
        
        # satisfaction calculations
        if w_int > 0.7:
            self.satisfaction -= 2 * w_int
        elif w_int > 0.5 and w_int <= 0.7:
            self.satisfaction -= w_int
        else:
            if random() < 0.1:
                self.is_alive = False
                # too much construction work leads to the possibility of death
                
            else:
                self.satisfaction -= 0.3 * w_int

        # production
        return self.work_ability * w / 10


    # clothing
    def _p_clothing(w):
        w_int = self.work_intolerance * w
        
        # satisfaction calculations
        if w_int > 1:
            self.satisfaction -= 1 * w_int
        elif w_int > 0.5 and w_int <= 1:
            self.satisfaction -= 0.7 * w_int
        else:
            self.satisfaction -= 0.5 * w_int
        
        # production
        return self.work_ability * w / 2


# =======================================
# CONSUMPTION GLOBAL ACCESS (DO NOT EDIT)
# =======================================


    def production(self):
        """
        Returns production functions used.
        
        :return: production functions
        :rtype: tuple
        """
        
        return (
            self._p_food,
            self._p_water,
            self._p_shelter,
            self._p_clothing
        )
        # production functions must match corresponding consumption function indicies returned in "consumption"


# ==================
# ACTION DEFINITIONS
# ==================
#
#
#
# ==================

"""
# defines action functions that individuals can take and their effects
# functions take in an "agent" value 'a' represnting the person performing the action and 'r' representing the person "recieving" the action
# functions do not return any values, but may edit these "person" values in various ways

def kill(a, r):
    pass


def steal(a, r):
    pass


def aid(a, r):
    pass


def sex(a, r):
    pass


ACTIONS = [




]
"""