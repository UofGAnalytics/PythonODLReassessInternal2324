""" Plotting methods for the ant library

This module consists of methods which will be useful to plot data.

The functions in this module are:
    * plot_histogram
    * plot_quiver
    * plot_scatter

"""
import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(speeds, ant_types):
    """
    Plot histogram of ant speeds by type.

    Args:
        speeds (list): List of speeds
        ant_types (list): List of ant types

    Returns:
        None
    """
    for ant_type in set(ant_types):
        mask = [at == ant_type for at in ant_types]
        plt.hist(speeds[mask], alpha=0.5, label=ant_type)
    plt.legend()
    plt.title("Speeds of Ants by Type")
    plt.xlabel("Speed")
    plt.ylabel("Frequency")
    plt.show()


def plot_quiver(X, Y, U, V):
    """
    Plot quiver plot of ant movements.

    Args:
        initial_positions: Initial positions of ants
        movements: Movements of ants

    Returns:
        None
    """
    plt.quiver(X, Y, U, V)
    plt.title("Quiver Plot of Ant Movements")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()


def plot_scatter(x_values, y_values, labels, title="", x_label="", y_label=""):
    """
    Create a scatter plot with different colors for different labels.

    Args:
        x_values (list or numpy.ndarray): The X-axis values.
        y_values (list or numpy.ndarray): The Y-axis values.
        labels (list): The labels for each point to color the points.
        title (str): The plot title (optional).
        x_label (str): The X-axis label (optional).
        y_label (str): The Y-axis label (optional).

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))  # Optional: Set the figure size

    # Create a scatter plot with different colors for each label
    unique_labels = list(set(labels))
    colors = sns.color_palette("husl", len(unique_labels))

    for i, label in enumerate(unique_labels):
        mask = [lbl == label for lbl in labels]
        plt.scatter(x_values[mask], y_values[mask], color=colors[i], label=label, alpha=0.7)

    plt.title(title)  # Optional: Set the plot title
    plt.xlabel(x_label)  # Optional: Set the X-axis label
    plt.ylabel(y_label)  # Optional: Set the Y-axis label
    plt.legend(title="Ant Type")  # Show legend with a title

    plt.grid(True)  # Optional: Add a grid to the plot

    plt.show()  # Show the plot
