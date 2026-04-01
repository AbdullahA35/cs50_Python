score=int(input("Score : "))

#AND conditional
if score<=100 and score >90:
    print("Grade : A")
elif score<=90 and score>80:
    print("Grade : B")
elif score<=80 and score>70:
    print("Grade : C")
elif score<=70 and score>60:
    print("Grade : D")
else:
    print("Grade : F")

#Another Conditional Notation
if 90<score<=100:
    print("Grade : A")
elif 80<score<=90:
    print("Grade : B")
elif 70<score<=80:
    print("Grade : C")
elif 60<score<=70:
    print("Grade : D")
else:
    print("Grade : F")