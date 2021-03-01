#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 07:54:54 2021

@author: Saadia Bayou
"""

""" Dans ce programme ,on considère une barre cylindrique déformable en acier 
    encastré à l’une de ses extrémités et soumisà un effort de taction F à l’extrémité opposée."""

# imports 
import numpy as np
import matplotlib.pyplot as plt


# Donnée constantes
    
# Module de Young
E=2e+10 # Pascal -Pa
nu=0.3

# Surface
S=15e-04 # mètre carré - m²
# LOngueur de la barre
L=1.01 # m
F=3.75e+05 # Newton - N
 
dx=[]
du=[]
eps=[]

# Fonctions

def sigma ():
    sigma=(F/S)
    
    return sigma
print("\nsigma = ",sigma(), "Pa")
   
# Définition du domaine Omega_x - Longeur de la barre
x=np.arange(0,L,0.1)
print("\nx=",x)

# Le déplacement u(x)
def depl_u (x):
    u=(F/E*S)*x
    return u

u=depl_u(x)

print("\nu=",u)


print("\n")
# dx=xi+1 -xi
for i in range(len(x)-1):
        dxi=x[i+1]-x[i]
        print("dx","[",i,"] = ", dxi)
        dx.append(dxi)
print("\ndx = ", dx)

print("\n")

# du=ui+1 -ui
for i in range(len(u)-1):
    dui=u[i+1]-u[i]
    print("du","[",i,"] = ", dui)
    du.append(dui)
print("\ndu = ", du)

# La déformation : eps=du(x)/dx 
for xi in dx:
    for ui in du:
        eps_i=(dui/dxi)
    eps.append(eps_i)
print("\nLa déformation: \nepsilon = ", eps)
        
# Tracé du dépalcement selon x 

plt.plot(x,u)

plt.title(" \nDéplacement u ")
plt.xlabel(" postion x")
plt.ylabel(" Déplacement u")

plt.savefig("Fig-1-Déplacement")
plt.show()


plt.plot(x[0:10],eps)
plt.title(" \nDéformation epsilon")
plt.xlabel(" postion x")
plt.ylabel(" Déformation epsilon")

plt.savefig("Fig-2-déformation")
plt.show()


plt.plot(x,u,eps)
plt.title(" \n Déplacement et déformation")
plt.xlabel(" postion x")
plt.ylabel(" u(x), epsilon")

plt.savefig("Fig-3-déplacement_et_déformation")
plt.show()
