#!/usr/bin/python3
def no_c(my):
    new = ''
    for i in range(len(my)):
        if my[i] not in 'cC':
            new += my[i]
    return (new)
