#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:24:18 2017

@author: Rwik
"""

class OddEvenTree():
    def getTree(self, x):
        flag = True
        ctr1=0
        ctr2=0
        for i in x:
            print "Index of i is "+str(ctr1)
            print list(i)
            y = list(i)
            ctr1+=1
            for j in y:
                n = int(ctr2-ctr1)
                print n
                if j == "E":
                    if n%2 == 0:
                        flag == True
                    else:
                        flag == False
                else:
                    if n%2 == 1:
                        flag == True
                    else:
                        flag == False
                if flag == True:
                    print ctr1,ctr2
                ctr2+=1
            