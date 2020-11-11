def file_handler(fl):
    '''
    :param fl: path and name of file
    :return:
    '''
    import os
    # create/open a file for writing
    f = open(fl, 'w')
    for i in range(10):
        f.write(str(i + 1) + ' : Hukam \n')
    f.close()
    # read from file
    f = open(fl, 'r')
    for i in f:
        print(i)
    f.close()
    os.remove(fl)
