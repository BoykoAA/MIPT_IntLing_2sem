
# coding: utf-8

# In[1]:


get_ipython().system('pip install wikipedia')


# In[65]:


import wikipedia as wiki
from tqdm import tqdm_notebook
from collections import Counter
import nltk
from nltk.corpus import stopwords


# In[2]:


wiki.set_lang("ru")


# ### Battle

# In[4]:


battle_worlds = ['Бой у', 'Осада', 
                 'Сражение на', 'Битва за', 
                 'Сражение при', 'Рейд на', 'Наступление на', 'Бои в', 'Битва под', 
                 'Штурм', 'Сражение за', 'Бой в проливе', 'Восстание в лагере', 'Битва на реке', 
                 'Битва за мыс', 'Атака', 'Оборона', 'Бои за', 'Бой у кишлака', 'Бой между', 'Осада форта', 
                 'Бой в заливе', 'Взятие аула', 'Битва у реки', 'Десант у', 'Первое сражение', 'Второе сражение', 
                 'Бой у острова', 'десантная операция', 'Восстание в', 'Атака', 'Вторжение', 'Вторая битва', 'Бойня', 
                 'Морское сражение', 'сражения', 'сражениях', 'битвах', 'битве', 'захват']

battle = ['Сражение', 'Бой']
article_list = []
for worlds in tqdm_notebook(battle):
    article = wiki.search(worlds, results=500)
    article_list.append(article)
        


# In[5]:


article_list_every = []
for i in tqdm_notebook(article_list):
    for j in i:
        article_list_every.append(j)       


# In[6]:


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
        


# In[18]:


get_ipython().run_cell_magic('time', '', "with open('battle.txt') as fin:\n    battle = fin.readlines()")


# In[24]:


battle_text = []
for i in tqdm_notebook(battle):
    if i != '\n':
        battle_text.append(i)
    


# In[38]:


battle_text_rep = []
for i in tqdm_notebook(battle_text):
    x = i.replace('\n', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '').split(' ')
    battle_text_rep.append(x)


# In[40]:


battle_text = []
for i in battle_text_rep:
    for j in i:
        battle_text.append(j)


# In[76]:


battle_text = [x.lower() for x in battle_text if x not in ['—', '==', '===', '', '====']]


# In[78]:


battle_stopwords = []
stopword = stopwords.words("russian")
for i in tqdm_notebook(battle_text):
    if i not in stopword:
        battle_stopwords.append(i)


# In[81]:


dict_freq = sorted(Counter(battle_stopwords).items(), key=lambda x: x[1], reverse=True)


# In[93]:


with open('dict_freq.txt', 'w') as fout:
    for i in dict_freq:
        fout.write(str(i))
        fout.write('\n')


# ### Game

# In[99]:


battle = ['Компьютерная игра', 'компьютерные игры']
article_list = []
for worlds in tqdm_notebook(battle):
    article = wiki.search(worlds, results=500)
    article_list.append(article)
    
article_list_every = []
for i in tqdm_notebook(article_list):
    for j in i:
        article_list_every.append(j)       

with open('game.txt', 'a') as fout:
    for i in tqdm_notebook(article_list_every):
        for attempt in range(3):
            try:
                x = wiki.page(i).content
                fout.write(x)
                fout.write(' ')  
            except:
                continue
            break
        


# In[100]:



with open('game.txt') as fin:
    battle = fin.readlines()

battle_text = []
for i in tqdm_notebook(battle):
    if i != '\n':
        battle_text.append(i)

battle_text_rep = []
for i in tqdm_notebook(battle_text):
    x = i.replace('\n', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '').split(' ')
    battle_text_rep.append(x)
    
battle_text = []
for i in battle_text_rep:
    for j in i:
        battle_text.append(j)

battle_text = [x.lower() for x in battle_text if x not in ['—', '==', '===', '', '====']]

battle_stopwords = []
stopword = stopwords.words("russian")
for i in tqdm_notebook(battle_text):
    if i not in stopword:
        battle_stopwords.append(i)
        
dict_freq = sorted(Counter(battle_stopwords).items(), key=lambda x: x[1], reverse=True)

print(dict_freq)

with open('dict_freq_game.txt', 'w') as fout:
    for i in dict_freq:
        fout.write(str(i))
        fout.write('\n')

