import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
from django.conf.urls.static import static
import os
from django.conf import settings
import pandas as pd



def translate(word,data):
    df = pd.DataFrame(data, columns= ['id', 'tr','eng', 'tnm', 'dfn'])
    state=0
    while True:

        while state==0:
            if word=="" or word==" " or word=="  ":
                return["","","","","",""]
                break
            else:
                state=1
                break

        while state==1: # word exist in dictionnary
            message=["Bu kelimeye farklı bir çeviri önerin."]
            if len(df[df.eq(word).any(1)])>0 and word==df.tr[df[df.eq(word).any(1)].index[0]]: #if word exists in excel and it is in tr
                return [df.eng[df[df.eq(word).any(1)].index[0]],message,"",df.tnm[df[df.eq(word).any(1)].index[0]],df.dfn[df[df.eq(word).any(1)].index[0]]] #return engglish
                break
            elif len(df[df.eq(word).any(1)])>0 and word==df.eng[df[df.eq(word).any(1)].index[0]]:#if word exists in excel and it is in EN
                return [df.tr[df[df.eq(word).any(1)].index[0]],message,"",df.tnm[df[df.eq(word).any(1)].index[0]],df.dfn[df[df.eq(word).any(1)].index[0]]] #return turkish
                break
            else:
                state=2
                break

        while state==2: #similar words exists in dictionnary
            word=word.title()

            if get_close_matches(word, df.tr.astype(str), 2, 0.3) and get_close_matches(word, df.eng.astype(str), 2, 0.3):
                best_match_tr=get_close_matches(word, df.tr.astype(str), 2, 0.3)[0]
                best_match_eng=get_close_matches(word, df.eng.astype(str), 2, 0.3)[0]
                score_tr = difflib.SequenceMatcher(None, word, best_match_tr).ratio()
                score_eng = difflib.SequenceMatcher(None, word, best_match_eng).ratio()
                if score_tr>score_eng:
                    state=3
                    break
                elif score_eng>score_tr:
                    state=4
                    break
            elif len(get_close_matches(word, df.tr.astype(str), 2, 0.3))>0: #similar words exist in tr
                state=3
                print(get_close_matches(word, df.tr.astype(str), 2, 0.3))
                break
            elif len(get_close_matches(word, df.eng.astype(str), 2, 0.3))>0: #similar words exist in EN
                state=4
                print(get_close_matches(word, df.eng.astype(str), 2, 0.3))
                break
            else:
                state=7
                break

        while state==3: #only case sensitive issue TR
            if word.capitalize() == get_close_matches(word, df.tr.astype(str), 5, 0.3)[0] :
                word=word.capitalize()
                state=1
                break
            elif get_close_matches(word, df.tr.astype(str), 2, 0.3)[0] == word.upper():
                word=word.upper()
                state=1
                break
            elif get_close_matches(word, df.tr.astype(str), 2, 0.3)[0] == word.lower():
                word=word.lower()
                state=1
                break
            elif get_close_matches(word, df.tr.astype(str), 2, 0.3)[0] == word.title():
                word=word.title()
                state=1
                break
            else:
                state=5
                break

        while state==4: #only case sensitive issue ENG
            if word.capitalize() == get_close_matches(word, df.eng.astype(str), 2, 0.3)[0] :
                word=word.capitalize()
                state=1
                break
            elif get_close_matches(word, df.eng.astype(str), 2, 0.3)[0] == word.upper():
                word=word.upper()
                state=1
                break
            elif get_close_matches(word, df.eng.astype(str), 2, 0.3)[0] == word.lower():
                word=word.lower()
                state=1
                break
            elif get_close_matches(word, df.eng.astype(str), 2, 0.3)[0] == word.title():
                word=word.title()
                state=1
                break
            else:
                state=6
                break

        while state==5: #similar words in TR
            message=["Bu kelimeyi bulamadık. Aşağıdakilerden birini mi demek istediniz?", "Aradığınızı bulamadınız mı? Bu kelimeye bir çeviri önerin."]
            return ["", message ,get_close_matches(word, df.tr.astype(str), 2, 0.3),"",""]
            break

        while state==6: #similar words in ENG
            message=["Bu kelimeyi bulamadık. Aşağıdakilerden birini mi demek istediniz?", "Aradığınızı bulamadınız mı? Bu kelimeye bir çeviri önerin."]
            return ["", message ,get_close_matches(word, df.eng.astype(str), 2, 0.3),"",""]
            break


        while state==7: #No similar words in dictionnary
            print("I'm at state 7")
            message=["Buna benzer bir kelime bulamadık. Bu kelimeye çeviri önermek için tıklayın."]
            return ["",message,"","","",""]
            break
