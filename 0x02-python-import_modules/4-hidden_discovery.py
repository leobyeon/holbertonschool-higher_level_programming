#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in range(0, len(names)):
        if names[i][0] != '_' and names[i][1] != '_':
            print("{:s}".format(names[i]))
