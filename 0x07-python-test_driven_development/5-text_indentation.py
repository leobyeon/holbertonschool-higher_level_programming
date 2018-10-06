#!/usr/bin/python3
def text_indentation(text):
    """indents text string by .:?"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text is '\n':
        print()
        return
    if text is "":
        return
    textlist = text.split(' ')
    new1 = " ".join(textlist)
    new2 = ""
    flag = 1
    for i in range(len(new1)):
        if flag and new1[i] is ' ':
            continue
        if new1[i] in ".:?":
            flag = 1
            new2 += "{}\n".format(new1[i])
        else:
            flag = 0
            new2 += new1[i]
    print(new2)
