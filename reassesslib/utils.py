import numpy as np


def __softmax__(array):
    exp_array = np.exp(np.array(array))
    return exp_array/exp_array.sum()


def random_draw(x=None):
    """
        Samples from the numbers from 1 to 5, with a biased distribution based
        on the input.

        The input should be:
            - a python integer
            - an even number
            - greater than 0

        Args:
            x (python integer meeting conditions above): distribution parameter

        Returns:
            A single random draw from the resultant distribution.

    """
    if x is None:
        raise ValueError('x should not be none')
    elif type(x) is not int:
        raise ValueError('x be an integer')
    elif x <= 0:
        raise ValueError('x should be positive')
    elif x % 2 == 1:
        raise ValueError('x cannot be odd')
    probs = __softmax__(0.001 + x * np.sin((x/2) * np.pi)*np.array(range(5)))
    return np.random.choice(range(5), p=probs)
