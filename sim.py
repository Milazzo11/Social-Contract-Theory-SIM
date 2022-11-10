"""
Society Generator simulation.

:author: Max Milazzo
"""


import sim_config
from time import sleep


def run_handle(sim_society):
    """
    """
    
    sim_society.run()
    sleep(0.1)
    
    # statistics can be printed here
    # GUI code could be placed here if user wants a display


def main():
    """
    Entry point to simulation execution.
    """
    
    sim_society = Society()
    sim_society.optimize(runs=1000)
    
    count = input("Enter desired simulation run time > ")
    
    for _ in range(count):
        run_handle(sim_society)


if __name__ == "__main__":
    main()