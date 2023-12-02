import PhoneticMap
import random
import tkinter as tk
import pyttsx3 as ttx

#Initializing
P=PhoneticMap.phonometer()
phones=P.phonemes_in_words()
root=tk.Tk()
fones=P.phones
eng=ttx.init()

#sets the font size. 
fs=24

# Split the keys into chunks of 10
keys = list(fones.keys())
chunks = [keys[i:i + 10] for i in range(0, len(keys), 10)]

def randomWords(keys,debug=False):
    """Generate random words at initialization """
    words_dict = {}
    for key in keys:
        if debug:
            print(key)
        val= P.find_words_with_query(phones, key)
        words_dict[key] = val
    return words_dict

random_words = randomWords(keys)

for chunk in chunks:
    frame = tk.Frame(root)
    frame.pack()

    for key in chunk:
        button = tk.Button(frame,padx=10,pady=20, font=("Comic Sans",fs), text=key,  command=lambda key=key: show_words(key))
        button.pack(side='left')

def show_words(key):
    """Gets a maximum of 5 words, containing a given phonetic expression, and says them"""
    words = random_words.get(key, [])
    if len(words) > 5:
        words = random.sample(words, 5)
    else:
        words = random.sample(words, len(words))
    label = tk.Label(root, text=' '.join(words),font=("Comic Sans",fs+10))
    label.pack()
    for word in words:
        eng.say(word)
    eng.runAndWait()
        

root.mainloop()
