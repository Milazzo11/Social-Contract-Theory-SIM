"""
Defines the traits associated with a single person living in a society.

:author: Max Milazzo
"""


from math import log
from random import random, uniform
# module imports


class Person:


# =================
# CLASS CONSTRUCTOR
# =================
# defines base features of a person
# can (if needed) be altered to accomodate more person types
# =================


    def __init__(self, age=0, sex="R", infected=True, consumption=1, work_ability=1, work_intolerance=1, start_satisfaction=1):
        """
        Person class constructor.
        
        :param age: the age of a person, where arbitrary 'N' time is 1
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
        self.rested = 1

        # time-contingent values
        self.age = 0
        
        # infected setter computation
        if infected:
            self.infection = 0
        else:
            self.infection = -1
            
        # resources
        self.food = 0
        self.water = 0
        self.shelter = 0
        self.clothing = 0


# =============================
# PUBLIC VALUE ACCESS FUNCTIONS
# =============================


    @property
    def satisfaction(self):
        return self.satisfaction
        

    @property
    def is_alive(self):
        return self.is_alive
        
    
    @property
    def get_resources(self):
        return (
            self.food,
            self.water,
            self.shelter,
            self.clothing
        )
        
    
    def tax_resources(self, tax_list):
        self.food -= tax_list[0]
        self.water -= tax_list[1]
        self.shelter -= tax_list[2]
        self.clothing -= tax_list[3]


# =======================
# CONSUMPTION DEFINITIONS
# =======================
# conventially these functions will begin with "_c_"
# also defines consumption time functions following base function definitions - returns the time it will take to consume some value 'c'
# defines the "consumption" funtions for each individual person during some arbitrary time period N
# functions take in a consumption amount value 'c' and edits the amount of individual satisfaction gained from that consumption, the amount of resource lost, and other possible person attributes
# must be called for every specified time period
# =======================


    # private function to take age into account for consumption
    def __age_c(self):
        if self.age < 5 or self.age > 70:
            return 0.5
        if self.age < 16 or self.age > 50:
            return 0.7
        else:
            return 1
        
        # returns intolerance and efficiency multiplier based on age
        return eff_mult, int_mult

    
    # food consumption
    def _c_food(self, c):
        
        # subtracts from food
        if self.food >= c:
            self.food -= c
        else:
            return self.food
            # returns food amount on failure
    
        food = 3 * self.consumption_ratio * __age_c() * log(c + 1)
        # relative food based on individual needs
        
        if food >= 0.7:
            self.satisfaction += food
        elif food < 0.7 and food >= 0.2
            self.satisfaction -= 1 / food
        else:
            self.is_alive = False
        
        return -1
        # returns -1 on success
    

    # water consumption
    def _c_water(self, c):
    
        # subtracts from water
        if self.water >= c:
            self.water -= c
        else:
            return self.water
            # returns water amount on failure
            
        water = 3 * self.consumption_ratio * __age_c() * log(10 * c + 1)
        # relative water based on individual needs
        
        if water >= 1:
            self.satisfaction += 3
        elif water < 1 and c >= 0.4:
            self.satisfaction -= 1 / water
        else:
            self.is_alive = False
        
        return -1
        # returns -1 on success


    # shelter "consumption"
    def _c_shelter(self, c):
    
        # personal shelter value does not decrease when used
        if self.shelter < c:
            return self.shelter
            
        shelter = 2 * self.consumption_ratio * log(5 * C + 1)
        # relative shelter based on individual needs
        
        if shelter < 1:
            self.satisfaction -= 3
        elif shelter > 3:
            self.satisfaction += 1
            
        return -1
        # returns -1 on success


    # clothing consumption
    def _c_clothing(self, c):
    
        # subtracts from clothing
        if self.clothing >= c:
            self.clothing -= c
        else:
            return self.clothing
            # returns clothing amount on failure
            
        clothing = 2 * self.consumption_ratio * log(10 * C + 1)
        # relative clothing based on individual needs
    
        if clothing > 1:
            self.satisfaction += clothing
        elif clothing < 0.1:
            self.satisfaction -= 1
            
        return -1
        # returns -1 on success


# ======================
# PRODUCTION DEFINITIONS
# ======================
# conventially these functions will begin with "_p_"
# defines the resources/work functions for some arbitrary time period N for an individual worker
# functions take in a work amount 'w' and sets the amount of resource 'r' produced, the amount of satisfaction lost from completing this work, as well as other possible person attributes
# functions should "match" the consumption functions defined above
# must be called for every specified time period
# =======================


    # private function to take age into account for production
    def __age_p(self):
        if self.age < 5 or self.age > 70:
            return 0, 20
        elif self.age < 16 or self.age > 50:
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


    # FOOD
    
    # food production
    def _p_food(self, w):
        eff_mult, int_mult = __age_p()
        w_int = self.work_intolerance * int_mult * w

        # satisfaction calculations
        if w_int > 1:
            self.satisfaction -= 1.5 * w_int
        elif w_int > 0.5 and w_int <= 1:
            self.satisfaction -= w_int
        else:
            self.satisfaction -= 0.5 * w_int
        
        # production
        self.food = self.work_ability * eff_mult * w


    # water production
    def _p_water(self, w):
        eff_mult, int_mult = __age_p()
        w_int = self.work_intolerance * int_mult * w
        
        # satisfaction calculations
        if w_int > 0.5:
            self.satisfaction -= 2 * w_int
        elif w_int > 0.2 and w_int <= 0.5:
            self.satisfaction -= w_int
        else:
            self.satisfaction -= 0.3 * w_int
        
        # production
        self.water = 10 * self.work_ability * eff_mult * w
    
    
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
        self.shelter = self.work_ability * eff_mult * w / 10
    
    
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
            self.satisfaction -= 1 * w_int
        elif w_int > 0.5 and w_int <= 1:
            self.satisfaction -= 0.7 * w_int
        else:
            self.satisfaction -= 0.5 * w_int
        
        # production
        self.clothing = self.work_ability * eff_mult * w / 2
    

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


# ===============================
# INDIVIDUAL AGENT ACTION EFFECTS
# ===============================
# defines action functions an individual can take and their effects on ONLY him/herself
# corresponding recipient effect function defines actions that can be taken by someone else that effect an individual (if applicable)
# more complex event functions that incorporate multiple actions across individuals are defined in Population class
# functions do not return any values, but may edit these "person" values in various ways
# can optionally take in one or more parameters
# defines time functions relative to time period N=1
# ===============================

    
    # KILL
    
    # kill another person
    def _a_kill(self):
        self.satisfaction += uniform(-1, 1)
    
    # kill time
    def _a_kill_TIME(self):
        return 0.01

    
    # STEAL
    
    # steal from another person
    def _a_steal(self):
        self.satisfaction += random()

    
    # steal time
    def _a_steal_TIME(self):
        return 0.01

    
    # AID
    
    # aid another person
    def _a_aid(self):
        self.satisfaction += uniform(-1, 1)
    
    # aid time
    def _a_aid_TIME(self):
        return 0.1 * random()

    
    # SEX
    
    # have sex with another person
    def _a_sex(self):
        self.satisfaction += 10 * random()
        
    def _a_sex_TIME(self):
        return 0.05 * random()

    
    # RELAX
    
    # relax
    def _a_relax(self):
        self.satisfaction += 0.5 * random()
        self.rested *= 2
    
    # relax time
    def _a_relax_TIME(self):
        return 0.5


# ===================================
# INDIVIDUAL RECIPIENT ACTION EFFECTS
# ===================================
# defines actions that can be taken by someone else and their effects on this individual
# more complex interactions with agent effect functions dealt with in Population class event functions
# can optionally take in one or more parameters
# functions do not return any values, but may edit these "person" values in various ways
# defines time functions relative to time period N=1
# ===================================

    
    # KILL
    
    # get killed by another person
    def _r_kill(self):
        self.is_alive = False
        
    # killed time
    def _r_kill_TIME(self):
        return 0

    
    # STEAL
    
    # get stolen from by another person
    def _r_steal(self):
        self.satisfaction -= 2 * random()
        
    # stolen time
    def _r_steal(self):
        return 0


    # AID
    
    # get aided by another person
    def _r_aid(self):
        self.satisfaction += random()
        
    def _r_aid_TIME(self):
        return 0

    
    # SEX
    
    # another person has sex with individual
    def _r_sex(self, consent=True):
        if consent:
            self._a_sex()
        else:
            self.satisfaction -= 20 * random()
    
    # sex time
    def _r_sex_TIME(self):
        return self._a_sex_TIME()


# =========================================
# ACTION EFFECT GLOBAL ACCESS (DO NOT EDIT)
# =========================================


    def action_funcs(self):
        """
        Returns action functions used.
        
        :return: tuple of action functions
        :rtype: tuple
        """
        
        return (
            ((self._a_kill, _a_kill_TIME), (self._r_kill, _r_kill_TIME)),
            ((self._a_steal, _r_steal_TIME), (self._r_steal, _r_steal_TIME)),
            ((self._a_aid, _a_aid_TIME), (self._r_aid, _r_aid_TIME)),
            ((self._a_sex, _a_sex_TIME), (self._r_sex, _r_sex_TIME)),
            ((self._a_relax, _a_relax_TIME, None)
        )
        # action agent and recipient functions are linked (if recipient function exists)
        # each function is also linked with associated time function
        # FORMAT: ( ... ((action, action_time), (recipient_event, recipient_event_time) or None ... )


# =====================================
# INDIVUAL TIME ACTION -> EVENT HANDLER
# =====================================
# Defines "next" function to move person formward 1 unit in time
# Additional private functions can be called here as well
# =====================================
    
    
    # handles death possibility based on age
    def __death_age_chance(self):
        if random() < (self.age ** 2) / 100000:
            self.is_alive = False


    # handles sleep
    def __sleep_handle(self):
        if self.rested < 0.1:
            self.is_alive = False
            
        self.rested /= 2

    
    # handles infection
    def __infection_handle(self):
        if self.infection != -1:
        
            self.infection += 1:
            self.satisfaction -= self.infection
            
            # death
            if random() * 5 < self.infection:
                self.is_alive = False
            
            # recovery
            elif random() * 3 > self.infection:
                self.infection = -1
                
                
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
            
            self.resource_func_list[index][0](schema_list[index][0])
            # consume resources
    
    
    def __action_manager(self, action_list):
        """
        """
        
        ### NEED TO REWORK PERSON-PERSON INTERACTION
        # probably put all functions that affect multiple people in "People" class
        # person class will only contain individual actions
        

    def next(self, schema_list, action_list):
        """
        "Moves" person through time and changes their values accordingly.
        
        :param schema_list: holds resource management production and consumption schema
        [
          [ consumption_func1_val, production_func1_val], 
          [ consumption_func2_val, production_func2_val],
          ...
        ]
        :param action_list: holds list of action functions
        :type schema_list: list
        """
        
        self.age += 1
        
        self.__death_age_chance()
        self.__sleep_handle()
        self.__infection_handle()
        
        self.__resource_manager(schema_list)
        self.__action_manager(action_list)