import urllib.request
import sys
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from io import StringIO
import re
import csv

def getWeb(link):
    inFile = open('ogFile.txt', 'w')

    with urllib.request.urlopen(link) as url:
                recipeWeb = url.read()
    soup = BeautifulSoup(recipeWeb, 'html.parser')

    with open('parsedFile.txt', 'w') as inFile:
        for string in soup.stripped_strings:
            print(repr(string), file = inFile)        
        inFile.close
    return
    
# Ingredients checklist

getWeb("https://www.allrecipes.com/recipe/268091/easy-korean-ground-beef-bowl/")


