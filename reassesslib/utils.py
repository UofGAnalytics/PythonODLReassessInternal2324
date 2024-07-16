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
            x (a python integer matching conditions above): distribution parameter

        Returns:
            A single random draw from the resultant distribution.

    """
    if x is None:
        raise ValueError(“x should not be none”)
    elif type(x) is not int:
        raise ValueError(“x be an integer”)
    elif x<=0:
        raise ValueError(“x should be positive”)
    elif x % 2 == 1:
        raise ValueError(“x cannot be odd”)
    return rd.choice(range(5), p=__softmax__(x*sin((x/2)*np.Pi)*np.array(range(5)))
