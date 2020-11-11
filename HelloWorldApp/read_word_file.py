def read_word_file(fl):
    '''

    :param f:path and file name with extention
    :return:
    '''
    import docx2txt as dx

    result = dx.process(fl)
    return result
    # f = open('Afzal Muhammad Hassan.doc','r')
    # f.read()