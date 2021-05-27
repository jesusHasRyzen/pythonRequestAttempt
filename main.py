
#
# url = 'https://weirdifier.herokuapp.com/'
# testArticle = open("C:/Users/Jesus/PycharmProjects/encryptionMS/demofile.txt",encoding="utf8")
# testData = testArticle.read().encode('utf-8')
# r = requests.get(url, data = testData)
# sys.stdout.buffer.write(r.content)
import requests
from flask import Flask, render_template, request


def get_text():
    pass
    # return requests.get(_url('/'))
def add_text():
    pass

def encrypt(file):
    Lines = extractTextFromFile(file)
    Lines = encodeFileTextToBinary(Lines)
    writeTextOnToFile(Lines, file)
# decrypts function that extracts the binary text from file
# and decodes into string format
# finally writes the string back to the file
def decrypt(file):
    Lines = extractTextFromFile(file)
    Lines = decodeFileBinaryToText(Lines)
    writeTextOnToFile(Lines, file)

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

# writes to the file by first clearing it and then writing new conversion
def writeTextOnToFile(text , tempfile):
    demofile = open(tempfile, "w",)
    demofile.write(text)
    demofile.close()

# url = {"url": "https://en.wikipedia.org/wiki/Stephen_Curry"}
# response = requests.post("https://wikiscraperproject.herokuapp.com/", data = url)
webSite = Flask(__name__)
# resp = requests.get('')


@webSite.route('/')
def instructions():
    return render_template('index.html')

@webSite.route('/submit', methods=['post'])
def submit():
    if request.method == 'post':
        text = request.form['text']
        print(text)
    return render_template('index.html')
@webSite.route('/encrypted')
def encrypted():
    if not isinstance(response.text, str):
        return 'No encryption has been completed'
    tempfile = "demofile2.txt"
    demofile = open(tempfile, "w")
    demofile.write(response.text)
    demofile.close()
    encrypt(tempfile)
    encryptedTextList = extractTextFromFile(tempfile)
    encryptedText = ''.join(encryptedTextList)
    return encryptedText
    # decrypt(tempfile)
    # return response.text
# if __name__ == '__main__':
    # webSite.debug = True
    # webSite.run(port=5000)




#
#
# print(response.text)





# # encryption function that extracts the string text from file
# # and encodes into binary format
# # finally writes the binary string back to the original file
# def encrypt(file):
#     Lines = extractTextFromFile(file)
#     Lines = encodeFileTextToBinary(Lines)
#     writeTextOnToFile(Lines)
# # decrypts function that extracts the binary text from file
# # and decodes into string format
# # finally writes the string back to the file
# def decrypt(file):
#     Lines = extractTextFromFile(file)
#     Lines = decodeFileBinaryToText(Lines)
#     writeTextOnToFile(Lines, file)
#
# # converts text to binary
# def encodeFileTextToBinary(text):
#     Lines = [ord(character) for everyString in text for character in everyString]
#     Lines = [character + 3 for character in Lines]
#     Lines.reverse()
#     Lines = ''.join(map(chr, Lines))
#     Lines = ' '.join(format(ord(x), 'b') for x in Lines)
#     return Lines
#
# # converts binary to string
# def decodeFileBinaryToText(binaryText):
#     if not(isinstance(binaryText, str)):
#         binaryText = ''.join(map(str, binaryText))
#     binaryValues = binaryText.split(' ')
#     Lines = [int(binaryValue, 2) for binaryValue in binaryValues]
#     Lines = [character - 3 for character in Lines]
#     Lines.reverse()
#     Lines = ''.join(map(chr, Lines))
#     return Lines
# # reads the file and extracts the text
# def extractTextFromFile(file):
#     demofile = open(file, "r")
#     Lines = demofile.readlines()
#     demofile.close()
#     return Lines
# # for docx files
# # def extractTextFromFile(file):
# #     demofile = open(file, "r")
# #     Lines = demofile.readlines()
# #     demofile.close()
# #     return Lines
#
# # writes to the file by first clearing it and then writing new conversion
# def writeTextOnToFile(text , tempfile):
#     demofile = open(tempfile, "w",)
#     demofile.write(text)
#     demofile.close()


#

# tempfile = "demofile2.txt"
# demofile = open(tempfile, "w")
# demofile.write(response.text)
# demofile.close()
# encrypt(tempfile)
# decrypt(tempfile)
print("reading the file from other Microservice!!")





