"""
Defines a whole society containing many people.

:author: Max Milazzo
"""

"""
# defines the different "person types" and their statistics
# FORMAT: PERSON_TYPE = [FREQUENCY, WORK_EFFICIENCY (when compared to arbitrary value 'W'), CONSUMPTION (amount per arbitrary value 'C')]
# Fequency values must add to 1


# IMPORTS (if needed)
# NONE


POPULATION = 10000
# total simulation start population


PEOPLE = [

    no_skill_low_need = [0.05, 0, 0.5],
    low_skill_low_need = [0.05, 0.5, 0.5],
    med_skill_low_need = [0.1, 1, 0.5],

    no_skill_med_need = [0.05, 0, 1],
    low_skill_med_need = [0.1, 0.5, 1],
    med_skill_med_need = [0.2, 1, 1],
    high_skill_med_need [0.1, 1.5, 1],

    no_skill_high_need [0.05, 0, 1.5],
    low_skill_high_need [0.1, 0.5, 1.5],
    med_skill_high_need [0.1, 1, 1.5],
    high_skill_high_need [0.05, 1.5, 1.5]
    
]
# all people types should be help in this global list


# function to convert a person's "work amount" to happiness level decrease
def work_to_happiness_decrease(w):
    if w < 3:
        return 0.5 * w
    else:
        return 2 * (w - 3)


W_to_H = work_to_happiness_decrease
# function alias
"""