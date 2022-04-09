import sys


def devision(x,y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """
    return x/y


def read_txt_file(pathfile='readme.txt'):
    """_summary_

    Args:
        pathfile (str, optional): _description_. Defaults to 'readme.txt'.
    """
    f = open(pathfile,"r")
    lines = f.readlines()
    print(lines)
    
    return lines


if __name__ == "__main__":
    
    read_txt_file(sys.argv[0])