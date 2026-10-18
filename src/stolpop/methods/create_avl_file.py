import numpy as np


def create_avl_file(ac):
    """
    Creates an .avl file given the aircraft geometry

    INPUTS:
    -------
    - self: class -> airplane class of all parameters

    RETURNS:
    --------
    - path: string -> path to .avl file
    """

    # Unpack aircraft
    wing = ac.wing
    hstab = ac.hstab