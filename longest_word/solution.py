import re


def LongestWord(sen):
    clean_sen = re.sub('[^a-zA-Z ]+', '', sen)
    words = clean_sen.split(" ")
    biggest_word = ""

    print clean_sen

    for word in words:
        if len(word) > len(biggest_word):
            biggest_word = word

    return biggest_word


print LongestWord("abc123 fjHB!D dj7483t4i4")

# Another (better?) option
# def LongestWord(sen):
#     ns = ""
#     for i in sen:
#         if i.isalpha() == True or i==" ":
#             ns+=i
#         else:
#             ns+=""
#     word = sorted(ns.split(" "),key=lambda x:len(x),reverse=True)[0]
#     return word