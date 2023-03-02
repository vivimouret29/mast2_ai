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
