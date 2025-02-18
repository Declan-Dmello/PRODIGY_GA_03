
import re
import random


"""with open("harry_potter.txt", "r", encoding="utf-8") as file:
    text = file.read()"""


text = "The sun was setting behind the mountains, casting a golden glow over the valley. Birds chirped as the cool evening breeze rustled through the trees. A small stream meandered through the landscape, its waters reflecting the fading light. In the distance, a traveler walked along a winding path, his footsteps echoing softly. He had been on the road for days, searching for a place to rest. The village was not far now, and the warm lights of the cottages flickered like stars in the twilight. He quickened his pace, eager to find shelter before nightfall."



p_text = re.sub(r'[^\w\s]', "" , text).lower().split()

print(p_text)

#breaking the sentence into tokens

trigrams_dict = {}

for i in range(len(p_text) -2) :
    key = (p_text[i],p_text[i+1])
    next_word = p_text[i+2]

    if key not in trigrams_dict:
        trigrams_dict[key] = {}


    trigrams_dict[key][next_word] = trigrams_dict[key].get(next_word, 0) + 1

print(trigrams_dict)

#now get the list based on the key and choose the word from the list

start_key = random.choice(list(trigrams_dict.keys()))
generated_list = list(start_key)

length = 10
current_pair = start_key

for _ in range(length - 2):
    possible_values = trigrams_dict.get(current_pair, {})

    if not possible_values:
        current_pair = random.choice(list(trigrams_dict.keys()))  # Restart with new pair
        continue


    generated_word = random.choices(list(possible_values.keys()), weights=possible_values.values())[0]

    generated_list.append(generated_word)
    current_pair = (current_pair[1], generated_word)

print("Generated Sentence:")
print(" ".join(generated_list))
