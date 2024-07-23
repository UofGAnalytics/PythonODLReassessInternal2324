""" Data methods for the ant library

This module consists of methods which will be useful to load the ant
data for your assignment. It also contains the implementation of the class
structure which will represent the Ant.

The classes in this module are:
    * Ant

The functions in this module are:
    * load_data

"""
import random as rd
import numpy as np


class IncorrectArgument(Exception):
    """ Custom exception to capture incorrect arguments
    """
    pass


class Ant:
    """
        This is a simple class representing a Ant

        This class does not have any public attributes
        and thus you should use the methods to get and update
        each of the Ant's attributes.
    """

    def __init__(self, ant_type, start_pos, weight, age, mandible_size):
        """Setting up the Ant class

        Args:
            ant_type: Queen, worker or drone 
            start_pos (array_like): Array of the start position of the Ant
            weight: Array of ant weights
            age (int or float): Array of the end position of the Ant
            mandible_size: Array of mandible sizes of the ants

        Returns:
            None
        """
        self.ant_type = ant_type
        self.start_pos = start_pos
        self.weight = weight
        self.age = age
        self.mandible_size = mandible_size

    def get_pos(self):
        """Get position of the Ant at the initial time

        Returns:
            array_like: Returns the requested position
        """
        return self.start_pos

        raise IncorrectArgument("Unknown time requested")

    def get_stats(self):
        """Getting statistics on this Ant

        Args:
            None

        Returns:
            dict: A dictionary mapping each of the properties of the Ant to
            the respective value.
        """
        return {
            "ant_type": self.ant_type,
            "weight": self.weight,
            "age": self.age,
            "mandible_size": self.mandible_size,
        }


def load_data(data_set_id):
    """
    Loads a specific Ant dataset from all of the datasets
    we collect every year.

    Args:
        data_set_id (int): The ID of the dataset you wish to load

    Returns:
        list of Ant in this dataset, each Ant is represented by the
        Ant class
    """
    np.random.seed(data_set_id)

    # Number of individuals in each cluster
    num_individuals = 100

    # Generate ant types
    ant_types = ['queen'] + ['worker'] * 60 + ['drone'] * 39

    # Generate random positions
    positions = np.random.rand(num_individuals, 2) * 100

    # Generate weights, ages, and mandible sizes based on ant type
    weights = np.zeros(num_individuals)
    ages = np.random.randint(1, 5, num_individuals)
    mandible_sizes = np.zeros(num_individuals)

    worker_indices = [i for i, ant_type in enumerate(ant_types) if ant_type == 'worker']
    num_worker_large = len(worker_indices) // 2
    

    for i, ant_type in enumerate(ant_types):
        if ant_type == 'queen':
            weights[i] = np.random.uniform(10, 15)
            mandible_sizes[i] = np.random.uniform(0.5, 1.5)
        elif ant_type == 'worker':
            if i in worker_indices[:num_worker_large]:
                weights[i] = np.random.uniform(5, 10)
                mandible_sizes[i] = np.random.uniform(2.5, 3.5)  # Larger mandibles
            else:
                weights[i] = np.random.uniform(5, 10)
                mandible_sizes[i] = np.random.uniform(1.5, 2.5)  # Smaller mandibles
        elif ant_type == 'drone':
            weights[i] = np.random.uniform(1, 5)
            mandible_sizes[i] = np.random.uniform(0.5, 1.0)

    # Add an outlier to the worker ants
    outlier_index = worker_indices[0]  # Choose the first worker with larger mandibles
    weights[outlier_index] = np.random.uniform(15, 20)  # Significantly higher weight
    mandible_sizes[outlier_index] = np.random.uniform(4.5, 5.5)  # Significantly larger mandible size

    data = []
    for i in range(num_individuals):
        ant_type = ant_types[i]
        position = positions[i]
        weight = weights[i]
        age = ages[i]
        mandible_size = mandible_sizes[i]
        data.append(Ant(ant_type, position, weight, age, mandible_size))

    rd.shuffle(data)

    return data
