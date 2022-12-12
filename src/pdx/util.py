def get_if_file(s):
    try:
        s = open(s).read()
    except:
        pass

    return s
