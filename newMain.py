import urllib.request
import sys
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from io import StringIO
import re
import csv

def getWeb(link):

    with urllib.request.urlopen(link) as url:
                recipeWeb = url.read()
    soup = BeautifulSoup(recipeWeb, 'html.parser')

    with open('parsedFile.txt', 'w') as inFile:
        for string in soup.stripped_strings:
            print(repr(string), file = inFile)        
        inFile.close

    return

def findIngredients(fileName):

    ingredientArray = []

    recipeFile = open(fileName, 'r')
    found = False
    count = 0
    for line in recipeFile:
        line = (line.replace("'", "")).replace("\n", "")
        count = count + 1       
        if line.__eq__('Ingredient Checklist'):
            found = True

        if line.__eq__('Add all ingredients to shopping list'):
            found = False
        
        if found == True:
            ingredientArray.append(line)
    
    return ingredientArray

# getWeb('https://www.allrecipes.com/recipe/260851/pepper-beef-rice-skillet/')
# getWeb("https://www.allrecipes.com/recipe/268091/easy-korean-ground-beef-bowl/")
array = findIngredients('parsedFile.txt')

