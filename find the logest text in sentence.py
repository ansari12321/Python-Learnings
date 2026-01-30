#longest word in sentence
sentence="Python makes problem solving fun"
words=sentence.split()
longest=""
for i in words:
    if len(i)>len(longest):
        longest=i
print(longest)
