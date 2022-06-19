#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                                  PyJokes                                      # * #
# * #                         project by: Anthony Akiniz                            # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Python script that connects to pyjokes module to display various programming jokes.   #
#                                                                                       #
# Requirements:                                                                         #
# pip3 install pyjokes                                                                  #
# documentation: https://pypi.org/project/pyjokes/ & https://pyjok.es/                  #
#                                                                                       #
# Guide:                                                                                #
# language options: 'en', 'de', 'es', 'gl' , 'eus' (default: 'en')                      #
# joke categories: 'neutral', 'chuck', 'all' (default: 'neutral')                       #
# Launch by clicking run button in top right in VSCode or: py -3 jokes.py               #
#########################################################################################


import pyjokes

# Neutral/default programming jokes in English
joke = pyjokes.get_joke('en', 'neutral')
print(joke)

# Chuck Norris jokes in English
# joke = pyjokes.get_joke('en', 'chuck')
# print(joke)

# All jokes in English
# joke = pyjokes.get_joke('en', 'all')
# print(joke)
