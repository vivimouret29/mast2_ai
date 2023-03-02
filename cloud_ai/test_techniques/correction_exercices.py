

# Exercice 1 :
def average_words_length(sentence):
    for punctuation in "!?',;.":
        sentence = sentence.replace(punctuation, ' ')  # remplacer dans notre texte, les caractères de ponctuation par un espace
    words = sentence.split()  # splitter notre texte en mots

    return round(sum(len(word) for word in words) / len(words), 2)  # retourner la longueur moyenne des mots avec deux décimales maximum


sentence1 = "Même les phrases avec des caractères de la langue française peuvent être utilisées."
sentence2 = "Le blog 'ledatascientist' est le blog français de référence en Data Science."

print(average_words_length(sentence1))
print(average_words_length(sentence2))

# Exercice 2 :
def count_string(string1, string2):
    count = 0
    for i in range(len(string2)-len(string1)+1):
        if string2[i:i+len(string1)] == string1:
            count += 1
    return count

string1 = 'abbe'
string2 = 'beaabbebeabeabbebeaebeabbeabebaebb'
string3 = 'beaabbebeabeabbabeaebeabbeabebaebb'

print(count_string(string1, string2))
print(count_string(string1, string3))