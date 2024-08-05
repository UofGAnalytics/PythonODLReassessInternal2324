""" Movement method for the ant library

This module consists of a method which will be useful to move the ants.

The functions in this module are:
    * generate_movement

"""

import numpy as np
from sklearn.ensemble import IsolationForest
from copy import deepcopy

def generate_movement(ants):
    """
    Generate random movements for ants based on their type.

    ant_type may include 'queen', 'worker', 'drone', 'soldier'

    Args:
        ants (list): List of Ant objects

    Returns:
        None
    """

    valid_types = {"queen", "worker", "drone", "soldier"}

    for ant in ants:
        if ant.ant_type not in valid_types:
            raise ValueError(
                f"Invalid ant type: {ant.ant_type}. Valid types \
                are: 'queen', 'worker', 'drone', 'soldier'."
            )

        if ant.ant_type == "queen":
            speed = np.random.uniform(0.01, 0.05)
        elif ant.ant_type == "worker":
            speed = np.random.uniform(0.05, 0.1)
        elif ant.ant_type == "soldier":
            speed = np.random.uniform(0.05, 0.1)
        elif ant.ant_type == "drone":
            speed = np.random.uniform(0.1, 0.2)
        movement_direction = np.random.rand(2) - 0.5
        movement_direction /= np.linalg.norm(movement_direction)  # Normalize

        ant.start_pos = ant.get_pos() + speed * movement_direction


def identify_outliers(soldier_ants, param_contamination):
    """
    Identifies outliers based on their head size and mandible size

    Args:
        soldier_ants
        param_contamination: contamination parameter for the Isolation Forest

    Returns:
        Outlier information
    """
    data = np.array(
        [[ant.head_size, ant.mandible_size] for ant in soldier_ants]
    )
    iso_forest = IsolationForest(contamination=param_contamination)
    outliers = iso_forest.fit_predict(data)
    outlier_info = {
        ant.unique_id: deepcopy(ant.__dict__)
        for ant, outlier in zip(soldier_ants, outliers)
        if outlier == -1
    }
    return outlier_info
