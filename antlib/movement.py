""" Movement method for the ant library

This module consists of a method which will be useful to move the ants.

The functions in this module are:
    * generate_movement

"""

import numpy as np


def generate_movement(ants):
    """
    Generate random movements for ants based on their type.

    Args:
        ants (list): List of Ant objects

    Returns:
        None
    """
    for ant in ants:
        if (ant.ant_type == 'queen'):
            speed = np.random.uniform(0.01, 0.05)
        elif (ant.ant_type == 'worker'):
            speed = np.random.uniform(0.05, 0.1)
        elif (ant.ant_type == 'drone'):
            speed = np.random.uniform(0.1, 0.2)
        movement_direction = np.random.rand(2) - 0.5
        movement_direction /= np.linalg.norm(movement_direction)  # Normalize

        ant.start_pos = ant.get_pos() + speed * movement_direction

