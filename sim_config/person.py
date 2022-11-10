"""
Holds person-specific state and defines needs/abilities.
Configures person lifetime increment events.

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


    def __init__(self, age=0, sex="R", infected=True, consumption=1, work_ability=1, work_intolerance=1, start_satisfaction=1, rest_init=10):
        """
        Person class constructor.
        
        :param age: the age of a person, iterated for every single time period
        :param sex: defines the sex (as in gender, not the action of sexual intercourse) of a person
        :param infected: is the person infected with disease
        :param consumption: the amount that a person "needs" to consume relative to a "standard" value of 1 (larger value = more consumption needed)
        :param work_ability: how well a perosn can perform work to produce resources (larger value = more efficiency, value of 1 is "standard")
        :param work_intolerance: the rate at which a person loses satisfaction from having to work (larger value = greater dislike of work, value of 1 is "standard")
        :type age: int
        :type sex: str (functionally of type chr)
        :type infected: bool
        :type consumption: float
        :type work_ability: float
        :type work_intolerance: float
        """

        # constant person values
        self.consumption_ratio = 1 / consumption
        self.work_ability = work_ability
        self.work_intolerance = work_intolerance
        self.rest_init = rest_init
        
        # sex (gender) setter computation
        if sex.upper() == "M" or sex.upper() == "F":
            self.sex = sex
        else:
            if random() > 0.5:
                self.sex = "M"
            else:
                self.sex = "F"
        
        # non-constant
        self.satisfaction = start_satisfaction
        self.is_alive = True
        self.rested = self.rest_init

        # time-contingent values
        self.age = 0
        
        # infected setter computation
        if infected:
            self.infection = 0
        else:
            self.infection = -1
            
        # personal resources
        self.food = 0
        self.water = 0
        self.shelter = 0
        self.clothing = 0


# =============================
# PUBLIC VALUE ACCESS FUNCTIONS
# =============================


    @property
    def get_satisfaction(self):
        return self.satisfaction

    
    @proprty
    def get_age(self):
        return self.age
        
        
    @property
    def get_sex(self):
        return self.sex
    
    
    @satisfy.setter
    def satisfy(self, amount):
        self.satisfaction += amount
        
        
    @dissatisfy.setter
    def dissatisfy(self, amount):
        self.satisfaction -= amount


    @property
    def is_alive(self):
        return self.is_alive
        
        
    @property
    def infected(self):
        return self.infected
        
    
    @proprty
    def rest(self, amount):
        self.rested += amount
        
        
    @tire.setter
    def tire(self, amount):
        self.rested -= amount
        
        
    @die.setter
    def die(self):
        self.is_alive = False
        
        
    @infection_progress.setter
    def infection_progress(self):
        self.infection += 1
        
        
    @infection_state.setter
    def infection_recover(self):
        self.infection = -1


# =========================
# RESOURCE ACCESS FUNCTIONS
# ==========================


    @property
    def get_food(self):
        return self.food
        
    
    @property
    def get_water(self):
        return self.water
        
        
    @property
    def get_shelter(self):
        return self.shelter
        

    @property
    def get_clothing(self):
        return self.clothing
        
        
    @gain_food.setter
    def gain_food(self, amount):
        self.food += amount
    
    
    @gain_water.setter
    def gain_water(self, amount):
        self.water += amount
    
    
    @gain_shelter.setter
    def gain_shelter(self, amount):
        self.shelter += amount


    @gain_clothing.setter
    def gain_clothing(self, amount):
        self.clothing += amount
        
        
    @lose_food.setter
    def lose_food(self, amount):
        self.food -= amount
        
    
    @lose_water.setter
    def lose_water(self, amount):
        self.water -= amount
    
    
    @lose_shelter.setter
    def lose_shelter(self, amount):
        self.shelter -= amount
    
    
    @lose_clothing.setter
    def lose_clothing(self, amount):
        self.clothing -= amount
   

# ================================
# RESOURCE CONSUMPTION DEFINITIONS
# ================================
# conventially these functions will begin with "_c_"
# defines the "consumption" funtions for each individual person during single time period
# functions take in a consumption amount value 'c' and edits the amount of individual satisfaction gained from that consumption, the amount of resource lost, the amount of "rest" lost, and other possible person attributes
# must be called for every specified time period
# ================================


    # private function to take age into account for consumption
    def __age_c(self):
        if self.get_age() < 5 or self.get_age() > 70:
            return 0.5
        if self.get_age() < 16 or self.get_age() > 50:
            return 0.7
        else:
            return 1
        
        # returns intolerance and efficiency multiplier based on age
        return eff_mult, int_mult


# =============================================================================
# =============================================================================

    
    # food consumption
    def _c_food(self, c):
        
        # subtracts from food
        if self.food >= c:
            self.lose_food(c)
        else:
            return self.get_food()
            # returns food amount on failure
    
        food = 3 * self.consumption_ratio * __age_c() * log(c + 1)
        # relative food based on individual needs
        
        if food >= 0.7:
            self.satisfy(food)
        elif food < 0.7 and food >= 0.2
            self.dissatisfy(1 / food)
        else:
            self.dissatisfy(10 / food)
            self.die()
        
        return -1
        # returns -1 on success
    

# =============================================================================
# =============================================================================


    # water consumption
    def _c_water(self, c):
    
        # subtracts from water
        if self.water >= c:
            self.lose_water(c)
        else:
            return self.get_water()
            # returns water amount on failure
            
        water = 3 * self.consumption_ratio * __age_c() * log(10 * c + 1)
        # relative water based on individual needs
        
        if water >= 1:
            self.satisfy(3)
        elif water < 1 and c >= 0.4:
            self.dissatisfy(1 / water)
        else:
            self.dissatisfy(10 / water)
            self.die()
        
        return -1
        # returns -1 on success


# =============================================================================
# =============================================================================


    # shelter "consumption"
    def _c_shelter(self, c):
    
        # personal shelter value does not decrease when used
        if self.shelter < c:
            return self.get_shelter()
            
        shelter = 2 * self.consumption_ratio * log(5 * C + 1)
        # relative shelter based on individual needs
        
        if shelter < 1:
            self.dissatisfy(3)
        elif shelter > 3:
            self.satisfy(1)
            
        return -1
        # returns -1 on success


# =============================================================================
# =============================================================================


    # clothing consumption
    def _c_clothing(self, c):
    
        # subtracts from clothing
        if self.clothing >= c:
            self.lose_clothing(c)
        else:
            return self.get_clothing()
            # returns clothing amount on failure
            
        clothing = 2 * self.consumption_ratio * log(10 * C + 1)
        # relative clothing based on individual needs
    
        if clothing > 1:
            self.satisfy(clothing)
        elif clothing < 0.1:
            self.dissatisfy(1)
            
        return -1
        # returns -1 on success


# ===============================
# RESOURCE PRODUCTION DEFINITIONS
# ===============================
# conventially these functions will begin with "_p_"
# defines the resources/work functions for a single time period
# functions take in a work amount 'w' and sets the amount of resource 'r' produced, the amount of satisfaction lost from completing this work, as well as other possible person attributes
# functions should "match" the consumption functions defined above
# must be called for every specified time period
# ===============================


    # private function to take age into account for production
    def __age_p(self):
        if self.get_age() < 5 or self.get_age() > 70:
            return 0, 20
        elif self.get_age() < 16 or self.get_age() > 50:
            return 0.3, 4
        else:
            return 1, 1

    
    # private function to take sex (gender) into account for production in male-dominated fields
    def __sex_p_M(self):
        if self.sex == "M":
            return 1, 1
        else:
            return 0.7, 0.7


    # private function to take sex (gender) into account for production in female-dominated fields
    def __sex_p_F(self):
        if self.sex == "F":
            return 1, 1
        else:
            return 0.7, 0.7


# =============================================================================
# =============================================================================

    
    # food production
    def _p_food(self, w):
        eff_mult, int_mult = __age_p()
        w_int = self.work_intolerance * int_mult * w

        # satisfaction calculations
        if w_int > 1:
            self.dissatisfy(1.5 * w_int)
            self.tire(1.5 * w_int)
        elif w_int > 0.5 and w_int <= 1:
            self.dissatisfy(w_int)
            self.tire(w_int)
        else:
            self.dissatisfy(0.5 * w_int)
            self.tire(0.5 * w_int)
        
        # production
        self.gain_food(self.work_ability * eff_mult * w)


# =============================================================================
# =============================================================================


    # water production
    def _p_water(self, w):
        eff_mult, int_mult = __age_p()
        w_int = self.work_intolerance * int_mult * w
        
        # satisfaction calculations
        if w_int > 0.5:
            self.dissatisfy(2 * w_int)
            self.tire(w_int)
        elif w_int > 0.2 and w_int <= 0.5:
            self.dissatisfy(w_int)
            self.tire(0.5 * w_int)
        else:
            self.dissatisfy(0.3 * w_int)
            self.tire(0.1 * w_int)
        
        # production
        self.gain_water(10 * self.work_ability * eff_mult * w)
    
    
# =============================================================================
# =============================================================================
    
    
    # shelter production
    def _p_shelter(self, w):
    
        # multiplier calculations
        eff_mult_A, int_mult_A = __age_p()
        eff_mult_S, int_mult_S = __sex_p_M()
        eff_mult = eff_mult_A * eff_mult_S
        int_mult = int_mult_A * int_mult_S
        
        w_int = self.work_intolerance * int_mult * w
        
        # satisfaction calculations
        if w_int > 0.7:
            self.dissatisfy(2 * w_int)
            self.tire(4 * w_int)
            
            if random() < 0.1:
                self.die()
                # too much construction work leads to the possibility of death
            
        elif w_int > 0.5 and w_int <= 0.7:
            self.dissatisfy(w_int)
            self.tire(2 * w_int)
        else:
            self.dissatisfy(0.3 * w_int)
            self.tire(w_int)

        # production
        self.gain_shelter(self.work_ability * eff_mult * w / 10)


# =============================================================================
# =============================================================================

    
    # clothing production
    def _p_clothing(self, w):
    
        # multiplier calculations
        eff_mult_A, int_mult_A = __age_p()
        eff_mult_S, int_mult_S = __sex_p_F()
        eff_mult = eff_mult_A * eff_mult_S
        int_mult = int_mult_A * int_mult_S

        w_int = self.work_intolerance * int_mult * w
        
        # satisfaction calculations
        if w_int > 1:
            self.dissatisfy(w_int)
            self.tire(0.5 * w_int)
        elif w_int > 0.5 and w_int <= 1:
            self.dissatisfy(0.7 * w_int)
            self.tire(0.3 * w_int)
        else:
            self.dissatisfy(0.5 * w_int)
            self.dissatisfy(0.1 * w_int)
        
        # production
        self.gain_clothing(self.work_ability * eff_mult * w / 2)
    

# ==================================================
# CONSUMPTION/PRODUCTION GLOBAL ACCESS (DO NOT EDIT)
# ==================================================


    def resource_funcs(self):
        """
        Returns consumption and production functions used.
        
        :return: tuple of consumption functions and production functions
        :rtype: tuple
        """
        
        return (
            (self._c_food, self._p_food),
            (self._c_water, self._p_water),
            (self._c_shelter, self._p_shelter),
            (self._c_clothing, self._p_clothing)
        )
        # consumption and production functions are linked


# =====================
# INDIVUAL TIME HANDLER
# =====================
# Defines "run" function to move person forward 1 unit in time
# Additional private functions can be called here as well
# =====================
    
    
    # handles death possibility based on age
    def __death_age_chance(self):
        if random() < (self.get_age() ** 2) / 100:
            self.die()


    # handles sleep
    def __rest_handle(self):
        if self.rested < 0:
            self.die()

    
    # handles infection
    def __infection_handle(self):
        if self.infection() != -1:
        
            self.infection_progress
            self.dissatisfy(self.infection())
            
            # death
            if random() * 5 < self.infection():
                self.die()
            
            # recovery
            elif random() * 3 > self.infection():
                self.infection_recover()
                
                
    def __resource_manager(self, schema_list):
        """
        Manages person resources for time period.
        
        :param schema_list: holds resource management production and consumption schema
        :type schema_list: list
        """
        
        resource_func_list = self.resource_funcs()
        
        for index in range(len(resource_func_list)):
            self.resource_func_list[index][1](schema_list[index][1])
            # produce resources
            
            res = self.resource_func_list[index][0](schema_list[index][0])
            # consume resources
            
            # handle if insufficient resources and consume all available
            if res != -1:
                self.resource_func_list[index][0](res)

        
# =============================================================================
# =============================================================================


    def run(self, schema_list):
        """
        "Moves" person through time and changes their values accordingly.
        
        :param schema_list: holds resource management production and consumption schema
        [
          [ consumption_func1_val, production_func1_val], 
          [ consumption_func2_val, production_func2_val],
          ...
        ]
        :type schema_list: list
        """
        
        self.rest()
        # simulates person's rest
        
        if self.is_alive:
            self.age += 0.003
            self.__death_age_chance()
            # age iteration
            # currently set so each iteration accounts for about 1 day of a person's lifespan
            
        if self.is_alive:
            self.__rest_handle()
            # person rest effect handler
        
        if self.is_alive:
            self.__infection_handle()
            # person infection handler
        
        if self.is_alive:        
            self.__resource_manager(schema_list)
            # manage daily required resource consumption
            
        return self.is_alive()
        # returns whether or not person is still alive