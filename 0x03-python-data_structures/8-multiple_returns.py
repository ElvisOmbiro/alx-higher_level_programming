#!/usr/bin/python3
def multiple_returns(sentence):
    p = len(sentence)

    if sentence == "":
        return p, None
    else:
        return p, sentence[0]
