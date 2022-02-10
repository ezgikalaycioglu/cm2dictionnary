import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
from django.conf.urls.static import static
import os
from django.conf import settings
import pandas as pd



def translate(word):
    data = pd.read_excel (os.path.join(settings.BASE_DIR, 'static/data.xlsx'))
    df = pd.DataFrame(data, columns= ['TR','EN', 'TNM', 'DEF', 'KST', 'ABR'])
    print(df)
    print(word)
    print(get_close_matches(word, df.TR.astype(str)))
    if get_close_matches(word, df.astype(str))[1] == word.capitalize():
        word=word.capitalize()
    elif get_close_matches(word, df.astype(str))[1] == word.upper():
        word=word.upper()
    print(word)

    if len(df[df.eq(word).any(1)])>0 and word==df.TR[df[df.eq(word).any(1)].index[0]]: #if word exists in excel and it is in TR
        return df.EN[df[df.eq(word).any(1)].index[0]] #return english
    elif len(df[df.eq(word).any(1)])>0 and word==df.EN[df[df.eq(word).any(1)].index[0]]:#if word exists in excel and it is in EN
        return df.EN[df[df.eq(word).any(1)].index[0]] #return turkish
    else:
        return "girmedim"






    #print(get_close_matches(word, df.TR.astype(str)))
    #if word in df.TR:

    #word=word.lower()

    #if get_close_matches(word,data.keys())[0] == word.capitalize():
    #    word=word.capitalize()
    #elif get_close_matches(word,data.keys())[0] == word.upper():
    #    word=word.upper()


    #for i in range(len(df)):
        #if df['TR'][i]==word:
        #    output=df['EN'][i];
        #    break;
        #elif df['EN'][i]==word:
        #    output=df['TR'][i];
        #    break;
        #else:
        #    output="yanlış yazdın"



#else:
#    return "The word doesn't exist. Please double check it"



    #elif len(get_close_matches(word,data.keys())) >0:
    #    yn = input("Did you mean %s instead? Enter Y if yes, or N if no: \n" % get_close_matches(word,data.keys())[0])
    #    if yn == "Y":
    #        return data[get_close_matches(word,data.keys())[0]]
    #    elif yn == "N":
    #        return "The word doesn't exist. Please double check it"
    #    else:
    #        return "Sorry. We didn't understand your entry."


import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
from django.conf.urls.static import static
import os
from django.conf import settings
import pandas as pd



def translate(word):
    data = pd.read_excel (os.path.join(settings.BASE_DIR, 'static/data.xlsx'))
    df = pd.DataFrame(data, columns= ['TR','EN', 'TNM', 'DEF', 'KST', 'ABR'])
    state=1
    while True:

        while state==1: # word exist in dictionnary
            print("I'm at state 1")
            if len(df[df.eq(word).any(1)])>0 and word==df.TR[df[df.eq(word).any(1)].index[0]]: #if word exists in excel and it is in TR
                return [df.EN[df[df.eq(word).any(1)].index[0]],"","",df.TNM[df[df.eq(word).any(1)].index[0]],df.DEF[df[df.eq(word).any(1)].index[0]]] #return english
                break
            elif len(df[df.eq(word).any(1)])>0 and word==df.EN[df[df.eq(word).any(1)].index[0]]:#if word exists in excel and it is in EN
                return [df.TR[df[df.eq(word).any(1)].index[0]],"","",df.TNM[df[df.eq(word).any(1)].index[0]],df.DEF[df[df.eq(word).any(1)].index[0]]] #return turkish
                break
            else:
                state=2
                break

        while state==2: #similar words exists in dictionnary
            print("I'm at state 2")
            word=word.title()
            if len(get_close_matches(word, df.TR.astype(str)))>0: #similar words exist in TR
                state=3
                break
            elif len(get_close_matches(word, df.EN.astype(str)))>0: #similar words exist in EN
                state=4
                break
            else:
                state=7
                break

        while state==3: #only case sensitive issue
            print("I'm at state 3")
            if word.capitalize() == get_close_matches(word, df.TR.astype(str))[0] or word.capitalize() == get_close_matches(word, df.EN.astype(str))[0] :
                print ("I'm here 3.1")
                word=word.capitalize()
                state=1
                break
            elif get_close_matches(word, df.TR.astype(str))[0] == word.upper() or get_close_matches(word, df.EN.astype(str))[0] == word.upper():
                print ("I'm here 3.2")
                word=word.upper()
                state=1
                break
            elif get_close_matches(word, df.TR.astype(str))[0] == word.lower() or get_close_matches(word, df.EN.astype(str))[0] == word.lower():
                print ("I'm here 3.3")
                word=word.lower()
                state=1
                break
            elif get_close_matches(word, df.TR.astype(str))[0] == word.title() or get_close_matches(word, df.EN.astype(str))[0] == word.title():
                print ("I'm here 3.4")
                word=word.title()
                state=1
                break
            else:
                state=4
                print ("I'm here 3.5")
                break

        while state==4: #similar words
            print("I'm at state 4")
            close_words=[get_close_matches(word, df.TR.astype(str))[0], get_close_matches(word, df.EN.astype(str))[0]]
            print(close_words)
            if get_close_matches(word, close_words)[0]==get_close_matches(word, df.TR.astype(str))[0]:
                return ["", "Bu kelimeyi bulamadık. %s demek mi istediniz? " % get_close_matches(word, df.TR.astype(str))[0],get_close_matches(word, df.TR.astype(str))[0],"",""]
                break
            elif get_close_matches(word, close_words)[0]==get_close_matches(word, df.EN.astype(str))[0]:
                return ["","We could not find that word. Did you mean %s instead? " % get_close_matches(word, df.EN.astype(str))[0], get_close_matches(word, df.EN.astype(str))[0],"",""]
                break

        while state==7: #No similar words in dictionnary
            print("I'm at state 7")
            return ["","Yanlış yazdınız","","","",""]
