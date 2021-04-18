#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:06:09 2020

@author: juanfe
"""

def mult2(a,b):
    """
    :param a: (float) Primer variable a sumar
    :param b: (float) Segunda varaible a sumar
    :return c: (float) c=a*b
    """
    c = a * b 
    return c

def mult(a,b,c):
    """
    :param a: (float) Varaible a sumar.
    :param b: (float) Varaible b a sumar.
    :param c: (float) Variable c a sumar.
    
    :return d: (float) a*c.
    :return e: (float) a*b*c
    """
    d = a * c
    e = a * b * c
    return d, e
    