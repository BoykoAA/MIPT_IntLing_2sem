
# coding: utf-8

# In[1]:


get_ipython().system('pip install wikipedia')


# In[1]:


import wikipedia as wiki
from tqdm import tqdm_notebook
from collections import Counter
import nltk
from nltk.corpus import stopwords


# In[2]:


wiki.set_lang("ru")


# ### Battle

# In[3]:



with open('battle.txt', 'a') as fout:
    for i in tqdm_notebook(article_list_every):
        for attempt in range(3):
            try:
                x = wiki.page(i).content
                fout.write(x)
                fout.write(' ')  
            except:
                continue
            break
        


# In[6]:


get_ipython().run_cell_magic('time', '', "with open('battle.txt') as fin:\n    battle = fin.readlines()")


# In[7]:


battle_text = []
for i in tqdm_notebook(battle):
    if i != '\n':
        battle_text.append(i)
    


# In[8]:


battle_text_rep = []
for i in tqdm_notebook(battle_text):
    x = i.replace('\n', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '').split(' ')
    battle_text_rep.append(x)


# In[9]:


battle_text = []
for i in battle_text_rep:
    for j in i:
        battle_text.append(j)


# In[10]:


battle_text = [x.lower() for x in battle_text if x not in ['—', '==', '===', '', '====']]


# In[11]:


battle_stopwords = []
stopword = stopwords.words("russian")
for i in tqdm_notebook(battle_text):
    if i not in stopword:
        battle_stopwords.append(i)


# In[12]:


dict_freq = sorted(Counter(battle_stopwords).items(), key=lambda x: x[1], reverse=True)


# In[13]:


final_battle = []
for i in dict_freq:
    a = round((int(i[1]) / len(battle_text))*100, 2)
    final_battle.append((i[0], str(a) + '%'))


# In[16]:


with open('dict_freq_battle.txt', 'w') as fout:
    for i in final_battle:
        fout.write(str(i))
        fout.write('\n')


# ### Game



with open('game.txt') as fin:
    game = fin.readlines()

game_text = []
for i in tqdm_notebook(game):
    if i != '\n':
        game_text.append(i)

game_text_rep = []
for i in tqdm_notebook(game_text):
    x = i.replace('\n', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '').split(' ')
    game_text_rep.append(x)
    
game_text = []
for i in game_text_rep:
    for j in i:
        game_text.append(j)

game_text = [x.lower() for x in game_text if x not in ['—', '==', '===', '', '====']]

game_stopwords = []
stopword = stopwords.words("russian")
for i in tqdm_notebook(game_text):
    if i not in stopword:
        game_stopwords.append(i)
        
dict_freq = sorted(Counter(game_stopwords).items(), key=lambda x: x[1], reverse=True)

with open('dict_freq_game.txt', 'w') as fout:
    for i in dict_freq:
        fout.write(str(i))
        fout.write('\n')


# In[112]:


final_game = []
for i in dict_freq:
    a = round((int(i[1]) / len(battle_text))*100, 2)
    final_game.append((i[0], str(a) + '%'))


# In[114]:


with open('dict_freq_game.txt', 'w') as fout:
    for i in final_game:
        fout.write(str(i))
        fout.write('\n')

