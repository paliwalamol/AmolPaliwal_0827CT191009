text = input("Enter the text : ")

spam = False

if("buy now" in text) :
    spam = True

elif("make a lot of money" in text) :
    spam = True

elif("subscribe this" in text) :
    spam = True

elif("click this" in text) :
    spam = True

if(spam) :
    print("This text is spam")

else :
    print("This text is not spam")