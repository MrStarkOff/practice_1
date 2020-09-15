# Вывести последнюю букву в слове
word = 'Архангельск'
print (word[-1])
# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
print("2")
# ???


# Вывести количество гласных букв в слове

for test in ['Архангельск']:
    print(len(list(filter(lambda x: x in 'АЕИОУЭЮЫЯауоыиэяюе', test))))



# Вывести количество слов в предложении

a = 'Мы приехали в гости'
print(len(a.split(' ')))
# ???


# Вывести первую букву каждого слова на отдельной строке





# Вывести усреднённую длину слова.
def main():

       sentence = "Мы приехали в гости"
       SumAccum = 0
       for ch in sentence.split():
           character = len(ch)
           SumAccum = SumAccum + character

       average = (SumAccum) / (len(sentence.split()))
       return average
print(main())