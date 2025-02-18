
import re
import random


"""with open("harry_potter.txt", "r", encoding="utf-8") as file:
    text = file.read()"""

text = "The sun was setting behind the mountains, casting a golden glow over the valley. Birds chirped as the cool evening breeze rustled through the trees. A small stream meandered through the landscape, its waters reflecting the fading light. In the distance, a traveler walked along a winding path, his footsteps echoing softly. He had been on the road for days, searching for a place to rest. The village was not far now, and the warm lights of the cottages flickered like stars in the twilight. He quickened his pace, eager to find shelter before nightfall."



p_text = re.sub(r'[^\w\s]', "" , text).lower().split()

print(p_text)

#breaking the sentence into tokens

bigrams_dict = {}

for i in range(len(p_text) -1) :
    key = p_text[i]
    next_word = p_text[i+1]

    if key not in bigrams_dict:
        bigrams_dict[key] = []


    bigrams_dict[key].append(next_word)

print(bigrams_dict)

#now get the list based on the key and choose the word from the list

start_key = "the"

if start_key not in bigrams_dict.keys():
    print("Start key doesnt exist")
length = 10
current_word =  start_key
generated_list = [start_key]
for i in range(length -1):
    print("The Number of Iterations " ,i)

    possible_vales = bigrams_dict.get(generated_list[i], [])
    print("reached here")
    generated_word =  random.choice(list(possible_vales))
    print(generated_word)
    generated_list.append(generated_word)

print("The new list")
print(generated_list)
