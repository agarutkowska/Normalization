# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:21:16 2020

@author: arutk
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def norm_method1(array, size, name, criteria_type, bins):
    maximum = max(array)
    minimum = min(array)
    normalized_array = []
    
    if(criteria_type == "P"):
        for x in array:
            x_normalized = (x - minimum)/(maximum - minimum)
            normalized_array.append(x_normalized)
    elif(criteria_type == "C"):
        for x in array:
            x_normalized = (maximum - x)/(maximum - minimum)
            normalized_array.append(x_normalized)
    else:
        print("Wrong criteria type")
        return 1
    
    normalized_mean = np.mean(normalized_array)
    normalized_std = np.std(normalized_array)
    
    plt.hist(normalized_array, bins)
    plt.title("Histogram. Metoda - minimum-maximum. \nRozklad %s. Liczba danych: %d. Typ: %s. \nSrednia: %6.2f. \
        Odchylenie standardowe: %6.2f:" % (name, size, criteria_type, normalized_mean, normalized_std))
    name_fig = "./histograms/" + name + "_" + str(size) + "_" + "method1" + "_" + criteria_type + ".png"
    plt.savefig(name_fig)
    plt.show()
    
def norm_max(array, size, name, criteria_type, bins):
    maximum = max(array)
    normalized_array = []
    
    if(criteria_type == "P"):
        for x in array:
            x_normalized = x/maximum
            normalized_array.append(x_normalized)
    elif(criteria_type == "C"):
        for x in array:
            x_normalized = 1 - (x/maximum)
            normalized_array.append(x_normalized)
    else:
        print("Wrong criteria type")
        return 1
    
    normalized_mean = np.mean(normalized_array)
    normalized_std = np.std(normalized_array)
    
    plt.hist(normalized_array, bins)
    plt.title("Histogram. Metoda - Maksimum. \nRozklad %s. Liczba danych: %d. Typ: %s. \nSrednia: %6.2f. \
        Odchylenie standardowe: %6.2f:" % (name, size, criteria_type, normalized_mean, normalized_std))
    name_fig = "./histograms/" + name + "_" + str(size) + "_" + "max" + "_" + criteria_type + ".png"
    plt.savefig(name_fig)
    plt.show()
    
def norm_sum(array, size, name, criteria_type, bins):
    normalized_array = []
    
    if(criteria_type == "P"):
        summ = sum(array)
        for x in array:
            x_normalized = x/summ
            normalized_array.append(x_normalized)           
    elif(criteria_type == "C"):
        summ = 0
        for x in array:
            x_reciprocal = 1/x
            summ += x_reciprocal
            
        for x in array:
            x_normalized = (1/x)/summ
            normalized_array.append(x_normalized)
    else:
        print("Wrong criteria type")
        return 1
    
    normalized_mean = np.mean(normalized_array)
    normalized_std = np.std(normalized_array)
    
    plt.hist(normalized_array, bins)
    plt.title("Histogram. Metoda - Suma. \nRozklad %s. Liczba danych: %d. Typ: %s. \nSrednia: %6.2f. \
        Odchylenie standardowe: %6.2f:" % (name, size, criteria_type, normalized_mean, normalized_std))
    name_fig = "./histograms/" + name + "_" + str(size) + "_" + "sum" + "_" + criteria_type + ".png"
    plt.savefig(name_fig)
    plt.show()
    
def norm_root(array, size, name, criteria_type, bins):
    root_sum_of_powers = math.sqrt(sum(np.power(array, 2)))
    normalized_array = []
    
    if(criteria_type == "P"):
        for x in array:
            x_normalized = x/root_sum_of_powers
            normalized_array.append(x_normalized)
    elif(criteria_type == "C"):
        for x in array:
            x_normalized = 1 - (x/root_sum_of_powers)
            normalized_array.append(x_normalized)
    else:
        print("Wrong criteria type")
        return 1
    
    normalized_mean = np.mean(normalized_array)
    normalized_std = np.std(normalized_array)
    
    plt.hist(normalized_array, bins)
    plt.title("Histogram. Metoda - Pierwiastek sumy iloczynow. \nRozklad %s. Liczba danych: %d. Typ: %s. \nSrednia: %6.2f. \
        Odchylenie standardowe: %6.2f:" % (name, size, criteria_type, normalized_mean, normalized_std))
    name_fig = "./histograms/" + name + "_" + str(size) + "_" + "root" + "_" + criteria_type + ".png"
    plt.savefig(name_fig)
    plt.show()
    
def norm_log(array, size, name, criteria_type, bins):
    prod_array = np.prod(array)
    ln_prod = math.log1p(abs(prod_array - 1))
    
    normalized_array = []
    
    if(criteria_type == "P"):
        for x in array:
            x_normalized = math.log1p(abs(x - 1))/ln_prod
            normalized_array.append(x_normalized)
    elif(criteria_type == "C"):
        for x in array:
            x_normalized = (1 - (math.log1p(abs(x - 1))/ln_prod))/(size - 1)
            normalized_array.append(x_normalized)
    else:
        print("Wrong criteria type")
        return 1
        
    normalized_mean = np.mean(normalized_array)
    normalized_std = np.std(normalized_array)
    
    plt.hist(normalized_array, bins)
    plt.title("Histogram. Metoda - Logarytmy. \nRozklad %s. Liczba danych: %d. Typ: %s. \nSrednia: %6.2f. \
        Odchylenie standardowe: %6.2f:" % (name, size, criteria_type, normalized_mean, normalized_std))
    name_fig = "./histograms/" + name + "_" + str(size) + "_" + "log" + "_" + criteria_type + ".png"
    plt.savefig(name_fig)
    plt.show()
    

def gauss_normalized(size, name, criteria_type, bins):
    mu, sigma = 17, 0.25
    gauss_array = np.random.normal(mu,sigma,size)
    gauss_mean = np.mean(gauss_array)
    gauss_std = np.std(gauss_array) 
    plt.hist(gauss_array, bins)
    plt.title("\nHistogram nieznormalizowanych %d liczb rozkladu Gaussa. \nSrednia: %6.2f. \
        Odchylenie standardowe: %6.2f:" % (size, gauss_mean, gauss_std))
    name_fig = "./histograms/" + name + "_" + str(size) + "_" + criteria_type + ".png"
    plt.savefig(name_fig)
    plt.show()
    
    norm_method1(gauss_array, size, name, criteria_type, bins)
    norm_max(gauss_array, size, name, criteria_type, bins)
    norm_sum(gauss_array, size, name, criteria_type, bins)
    norm_root(gauss_array, size, name, criteria_type, bins)
    norm_log(gauss_array, size, name, criteria_type, bins) 
        
def uniform_normalized(size, name, criteria_type, bins):
    low, high = -10, 20
    uniform_array = np.random.uniform(low, high, size)
    uniform_mean = np.mean(uniform_array)
    uniform_std = np.std(uniform_array)
    plt.hist(uniform_array, bins)
    plt.title("\nHistogram nieznormalizowanych %d liczb rozkladu Jednostajnego. \nSrednia: %6.2f. \
        Odchylenie standardowe: %6.2f:" % (size, uniform_mean, uniform_std))
    name_fig = "./histograms/" + name + "_" + str(size) + "_" + criteria_type + ".png"
    plt.savefig(name_fig)
    plt.show()
    
    norm_method1(uniform_array, size, name, criteria_type, bins)
    norm_max(uniform_array, size, name, criteria_type, bins)
    norm_sum(uniform_array, size, name, criteria_type, bins)
    norm_root(uniform_array, size, name, criteria_type, bins)
    norm_log(uniform_array, size, name, criteria_type, bins)    
    
def poisson_normalized(size, name, criteria_type, bins):
    lam = 30
    poisson_array = np.random.poisson(lam, size)
    poisson_mean = np.mean(poisson_array)
    poisson_std = np.std(poisson_array)
    plt.hist(poisson_array, bins)
    plt.title("\nHistogram nieznormalizowanych %d liczb rozkladu Poissona. \nSrednia: %6.2f. \
        Odchylenie standardowe: %6.2f:" % (size, poisson_mean, poisson_std))
    name_fig = "./histograms/" + name + "_" + str(size) + "_" + criteria_type + ".png"
    plt.savefig(name_fig)
    plt.show()
    
    norm_method1(poisson_array, size, name, criteria_type, bins)
    norm_max(poisson_array, size, name, criteria_type, bins)
    norm_sum(poisson_array, size, name, criteria_type, bins)
    norm_root(poisson_array, size, name, criteria_type, bins)
    norm_log(poisson_array, size, name, criteria_type, bins)  

def main():
    size = (100, 150, 200)
    bins = 20

    for x in size:
        gauss_normalized(x, "Gaussa", "P", bins)

    for x in size:
        uniform_normalized(x, "Jednostajny", "P", bins)
        
    for x in size:
        poisson_normalized(x, "Poissona", "P", bins)

if __name__ == "__main__":
    main()
