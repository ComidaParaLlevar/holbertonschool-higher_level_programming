#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        f_char = sentence[0]
    else:
        f_char = "None"
    tuple_ = (lenght, f_char)
    return(tuple_)
