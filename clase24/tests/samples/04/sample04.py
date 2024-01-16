def mid(frase):

    largo = len(frase)

    if largo % 2 == 0:
        return ""
    else:
        return frase[int((largo-1)/2)]
    


