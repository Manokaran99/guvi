char=input()
if('a'<=char<='z' or 'A'<=char<='Z'):
    if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
