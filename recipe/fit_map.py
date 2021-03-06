# -*- coding: utf-8 -*-

"""
Copyright 2016 Walter José and Alex de Sá

This file is part of the RECIPE Algorithm.

The RECIPE is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

RECIPE is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. See http://www.gnu.org/licenses/.

"""

import os
from collections import OrderedDict

def get_fitness_map(filename):

    fitness_map = {}

    if not os.path.exists('fit_map'):
		os.makedirs('fit_map')

    if os.path.exists(os.path.join('fit_map','fit_'+filename)):
        with open(os.path.join('fit_map','fit_'+filename),'r') as fin:
            content = fin.readlines()
            if(len(content)<2):
                return fitness_map
            for lines in content:
                line = lines.split("|")
                fitness_map[line[0]]=float(line[1])
    else:
        with open(os.path.join('fit_map','fit_'+filename),'w') as fin:
            fin.write(" ")

    return fitness_map


def save_fitness_map(fitness_map,filename):

    sorted_fitness = OrderedDict(sorted(fitness_map.items(),key=lambda x: x[1],reverse=True))

    with open(os.path.join('fit_map','fit_'+filename),'w') as fout:
        for key,value in sorted_fitness.items():
            fout.write('{}|{}\n'.format(key,value))
