#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:32:02 2022

@author: lucasdonaire
"""

import scipy.linalg as sl

import numpy as np
def householder(v):
    dim = len(v)
    v = np.array(v)
    v.shape = (dim,1)
    num = np.transpose(v).dot(v)[0,0]
    mat = v.dot(np.transpose(v))
    print(mat)
    i = np.eye(dim)
    Hv = i - (2/num)*(mat)
    return Hv
if False:
        
    def mmq(A,b):
        A = np.array(A)
        b = np.array(b).reshape((len(b),1))
        At = np.transpose(A)
        nA = At.dot(A)
        nb = At.dot(b)
        res = sl.solve(nA,nb)
        return res
        
    
    def pi(v,w = None):
        if w == None: w = v
        dim = len(v)
        v = np.array(v)
        v.shape = (dim,1)
        w = np.array(w)
        w.shape = (dim,1)
        num = np.transpose(v).dot(w)[0,0]
        return num
        
    
    def matvw(v,w = None):
        if w == None: w = v
        dim = len(v)
        v = np.array(v)
        v.shape = (dim,1)
        w = np.array(w)
        w.shape = (dim,1)
        mat = v.dot(np.transpose(w))
        return mat
    
    def matvwnorm(v,w = None):
        if w == None: w = v
        dim = len(v)
        v = np.array(v)
        v.shape = (dim,1)
        w = np.array(w)
        w.shape = (dim,1)
        w = w/np.sqrt(pi(w))
        v = v/np.sqrt(pi(v))
        mat = v.dot(np.transpose(w))
        return mat
    
    
    def projmat(A):
        A = np.array(A)
        At = np.transpose(A)
        AtA = At.dot(A)
        AtAI = np.linalg.inv(AtA)
        AAtAI = A.dot(AtAI)
        #return AAtAI.dot(At)
        return A, At, AtA, AtAI, AAtAI, AAtAI.dot(At)
        
    
    
    
    
    
    def ambas(v,w):
        A = np.transpose(np.array([v,w]))
        res1 = projmat(A)
        res2 = matvwnorm(v) + matvwnorm(w)
        return res1, res2