#!/usr/bin/env python

servers = {}
servers['1'] = {'1':'10', '2':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['3'] = {'5':'10', '2':'10', '3':'10', '4':'10', '6':'10', '29':'10'} # Diccionario
servers['7'] = {'1':'10', '2':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['32'] = {} # Diccionario
servers['9'] = {'1':'10', '2':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['10'] = {'1':'10', '2':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['11'] = {'15':'10', '26':'10', '35':'10', '47':'10', '67':'10', '30':'10'} # Diccionario
servers['12'] = {'1':'10', '29':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['13'] = {'1':'10', '22':'10', '39':'10', '48':'10', '6':'10', '309':'10'} # Diccionario
servers['19'] = {'1':'10', '2':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['20'] = {'1':'10', '2':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['21'] = {'15':'10', '26':'10', '35':'10', '47':'10', '67':'10', '30':'10'} # Diccionario
servers['22'] = {'1':'10', '29':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['23'] = {'1':'10', '22':'10', '39':'10', '48':'10', '6':'10', '309':'10'} # Diccionario
servers['24'] = {'1':'10', '2':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['25'] = {'1':'10', '2':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['26'] = {'15':'10', '26':'10', '35':'10', '47':'10', '67':'10', '30':'10'} # Diccionario
servers['27'] = {'1':'10', '29':'10', '3':'10', '4':'10', '6':'10', '30':'10'} # Diccionario
servers['28'] = {'1':'10', '22':'10', '39':'10', '48':'10', '6':'10', '309':'10'} # Diccionario


f = open('salidalarga', 'w')

numServers = 0

# Print the long imdb canonical title and movieID of the results.
for key, value in servers.items():
    if(value):      # Comprueba si hay videos asignados
        numServers=numServers+1

f.write(str(numServers) + '\n')

# Print the long imdb canonical title and movieID of the results.
for key, value in servers.items():
    if(value):      # Comprueba si hay videos asignados
        f.write(str(key))
        for idVideo, val in value.items():
            f.write(' ' + str(idVideo))
        f.write('\n')

f.close()