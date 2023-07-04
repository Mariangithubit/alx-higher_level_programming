#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
     prints a text with 2 new lines
     after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]
    for i in ".?:":
        list_text = s.split(i)
        s = ""
        for j in list_text:
            j = j.strip(" ")
            s = i + j if s == "" else s + "\n\n" + i + j

    print(s[:-3], end="")
