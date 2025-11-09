Qna = {
    "Hi" : "Hey",
    "How are you" : "I am fine",
    "How old are you" : "I am 20 years old", 
}

while True :
    Qs = input()

    if(Qs == "quit"):
        break
    else:
        print(Qna[Qs])