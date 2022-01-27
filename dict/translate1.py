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
