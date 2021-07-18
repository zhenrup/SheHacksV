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

    return 'parsedFile.txt'


def findIngredients(fileName):

    ingredientArray = []

    with open(fileName) as recipeFile:
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
                if line[0] == '½':
                    line = line.replace('½', '0.5')
                elif line[0] == '⅓':
                    line = line.replace('⅓', '0.333')
                elif line[0] == '¼':
                    line = line.replace('¼', '0.25')
                ingredientArray.append(line)
    return ingredientArray
    

def makeDict():
    foodDict = {'data':[]}
    with open('food.csv', 'r', encoding='utf-8') as inputData:
        reader = csv.reader(inputData)
        for line in reader:
            foodDict['data'].append({'name':line[0], 'proteins_per 100g': line[1], 'carbon_footprint': line[2]})
    return foodDict


def subsitution(array, dict, input):
    ogProtein = 0
    resultDict = {'original':[], 'subsitution':[]}
    for i in range(1, len(array)):
        for j in range(len(dict['data'])):
            if dict['data'][j].get('name') in array[i]:
                ogProtein = dict['data'][j].get('proteins_per_100g')
            if dict['data'][j].get('name') in input:
                subProtein = dict['data'][j].get('proteins_per_100g')
                

parsedFile = getWeb("https://www.allrecipes.com/recipe/268091/easy-korean-ground-beef-bowl/")
array = findIngredients(parsedFile)
# for i in range(1, len(array)):
#     print(array[i])
proteinList = makeDict()
subsitution(array, proteinList, 'tofu')