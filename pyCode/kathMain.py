import urllib.request
import sys
from html.parser import HTMLParser
import re
import csv

def main():
    test = False 
    ingredients=[100]
    ingredients_new=[] 
    food = []
    count = 0
    numIng = 0

    link = input("Enter a recipe link or space to quit: ")
    while link != " ":
        with urllib.request.urlopen(link) as url:
            myfile = url.read()
        with open('file.txt', 'w') as f:
            print(myfile, file=f)
            f.close

        with open('file.txt', 'r') as htmlFile:
            with open('parsedFile.txt', 'w') as f1:
                for line in htmlFile:
                    
                    replacedLine = replaceSpecialChar(line)
   
                    for word in replacedLine.split():
         
                        if test == True:
                            count = count + 1
                            ingredients.append(word)
                        print(word, file = f1)
                        if word == '"recipeIngredient":':
                            test = True
                        if word == '"recipeInstructions":':
                            break
        total=''

        for i in ingredients:
               
            j = str(i).replace('\\xc2\\xbc','1/4')
            j = str(i).replace('\\xc2\\xbd','1/2')
            j = str(i).replace('\xc2\\xbe','3/4')
            # print(j)
            ingredients_new.append(j)
            
        for k in ingredients_new:
            total = total+" "+str(k)
            
        ing = re.findall("\"[0-9].*?\"",total)
        numImg = len(ing)
        print ("here is", ing)

        
        for i in range(0, len(ing)):
            num = ''
            lastWord = ''
            inList = ''
            foodItem = []
            for word in ing[i].split():
                if word[0] == '"':
                    for x in range(1, len(word)):
                        num = num + str(word[x])
                    foodItem.append(num)
                else:
                    if word[len(word)-1] == '"':
                        for x in range(0, len(word) - 1):
                            lastWord = lastWord + word[x]
                        inList = inList + ' ' + lastWord
                        foodItem.append(inList)
                    else:
                        inList = inList + ' ' + word
            food.append(foodItem)

        # for i in food:
        #     print(i)
        print(data)
        protein = 0
        carbon = 0
        tofuProtein = [8, 1.6]
        for i in range(len(data)-1): 
            current = data[i][0]
            index = 0
            for item in food: #ingredients
                index = index + 1
                if(current in item[1]):
                    print(food[index - 1][0])
                    protein = (int(food[index - 1][0])*454)/100 * float(data[i][1])
                    print(round(protein,2))
                    serveTofu = (protein/tofuProtein[0] * 100)/454
                    print(round(serveTofu, 2)," lb")
                    carbon = ((int(food[index-1][0])*454)/100 * float(data[i][2])) - ((protein/tofuProtein[0])*tofuProtein[1])
                    print(round(carbon,2), ' kg')
                    break
                    

        link = input("Enter a recipe link or space to quit: ")


def replaceSpecialChar(line):
    line = line.replace('\\xc2\\xbd','1/2')
    line = line.replace('\\xc2\\xbc','1/4')
    line = line.replace('\\xc2\\xbe','3/4')
    line = line.replace('\\xe2\\x85\\x93', '1/3')
    line = line.replace('\\xe2\\x85\\x94', '2/3')
    return line

def load_data(filename='food.csv'):
    reader = csv.reader(open(filename, 'r', encoding='utf-8'))
    data = []
    for line in reader:
        data.append(line)
    return data

data = load_data()

main()
           