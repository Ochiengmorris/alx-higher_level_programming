#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    def main():
        l = dir(hidden_4)
        for i in range(len(l)):
            if(l[i][0] != '_'):
                print("{}".format(l[i]))
