# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import sys
#
# import requests
#
#
#
# url = 'https://weirdifier.herokuapp.com/'
# testArticle = open("C:/Users/Jesus/PycharmProjects/encryptionMS/demofile.txt",encoding="utf8")
# testData = testArticle.read().encode('utf-8')
# r = requests.get(url, data = testData)
# sys.stdout.buffer.write(r.content)
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse
#app = Flask(__name__)
# api = Api(app)

url = {"url": "https://en.wikipedia.org/wiki/Stephen_Curry"}
response = requests.post("https://wikiscraperproject.herokuapp.com/", data = url)
webSite = Flask(__name__)
# class encrypt(Resource):
#     def get(self):
#         return response.text
#     # def post(self):
#         # parser.add_argument("")
#     api.add_resource(encrypt, '/encrypted/')

@webSite.route('/')
def instructions():
    return 'Please enter the string you would like to encrypt.'

@webSite.route('/encrypted')
def encrypted():
    if not isinstance(response.text, str):
        return 'No encryption has been completed'
    return response.text

if __name__ == '__main__':
    webSite.run(port=5000)


print(response.text)





# encryption function that extracts the string text from file
# and encodes into binary format
# finally writes the binary string back to the original file
def encrypt(file):
    Lines = extractTextFromFile(file)
    Lines = encodeFileTextToBinary(Lines)
    writeTextOnToFile(Lines)
# decrypts function that extracts the binary text from file
# and decodes into string format
# finally writes the string back to the file
def decrypt(file):
    Lines = extractTextFromFile(file)
    Lines = decodeFileBinaryToText(Lines)
    writeTextOnToFile(Lines)

# converts text to binary
def encodeFileTextToBinary(text):
    Lines = [ord(character) for everyString in text for character in everyString]
    Lines = [character + 3 for character in Lines]
    Lines.reverse()
    Lines = ''.join(map(chr, Lines))
    Lines = ' '.join(format(ord(x), 'b') for x in Lines)
    return Lines

# converts binary to string
def decodeFileBinaryToText(binaryText):
    if not(isinstance(binaryText, str)):
        binaryText = ''.join(map(str, binaryText))
    binaryValues = binaryText.split(' ')
    Lines = [int(binaryValue, 2) for binaryValue in binaryValues]
    Lines = [character - 3 for character in Lines]
    Lines.reverse()
    Lines = ''.join(map(chr, Lines))
    return Lines
# reads the file and extracts the text
def extractTextFromFile(file):
    demofile = open(file, "r")
    Lines = demofile.readlines()
    demofile.close()
    return Lines
# for docx files
# def extractTextFromFile(file):
#     demofile = open(file, "r")
#     Lines = demofile.readlines()
#     demofile.close()
#     return Lines



# writes to the file by first clearing it and then writing new conversion
def writeTextOnToFile(text):
    demofile = open(tempfile, "w",)
    demofile.write(text)
    demofile.close()


#

tempfile = "demofile2.txt"
demofile = open(tempfile, "w")
demofile.write(response.text)
demofile.close()
encrypt(tempfile)
decrypt(tempfile)
print("reading the file from other Microservice!!")





