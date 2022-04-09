from my_funtions import read_txt_file


def test_read_txt_file():
    assert read_txt_file(pathfile = 'readme.txt') == ['This is app 1, relase 3']
    