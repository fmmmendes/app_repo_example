import sys


def square(x):
    """_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    return x*x


def read_txt_file(pathfile='readme.txt'):
    """_summary_

    Args:
        pathfile (str, optional): _description_. Defaults to 'readme.txt'.
    """
    f = open(pathfile,"r")
    lines = f.readlines()
    print(lines)
    
    return lines