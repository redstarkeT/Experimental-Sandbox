"""
Name: Timothy Stephens
Date: 07/02/2020
"""
import random
import time

tarot = { 1:"The Magician", 2:	"The High Priestess", 3:"The Empress", 4:"The Emperor", 5:"The Hierophant", 6:"The Lovers", 7:"The Chariot", 8:"Strength", 9:"The Hermit",
          10:"Wheel of Fortune", 11:"Justice", 12:"The Hanged Man", 13:"Death", 14:"Temperance", 15:"The Devil", 16:"The Tower", 17:"The Star", 18:"The Moon", 19:"The Sun",
          20:"Judgement", 21:"The World", 22:"The Fool"}

spread = {}

position = ["reversed", "upright"]

name = input("Oh one seeking wisdom and knowledge, what is your name? 0.0 \n")

print("Well " + name + ",", "Let us look into the three windows of time...")
time.sleep(3)
print("The Sea becomes the Cloud,")
time.sleep(2)
print("The Cloud becomes the Rain,")
time.sleep(2)
print("The Rain becomes the Mist,")
time.sleep(2)
print("All things that have shape, Vanish...,")
time.sleep(2)
print("Ninja Art: HIDDEN MIST JUTSU!")
time.sleep(3)
            
spread["past"] = tarot.pop(random.choice(list(tarot.keys())))

spread["present"] = tarot.pop(random.choice(list(tarot.keys())))

spread["future"] = tarot.pop(random.choice(list(tarot.keys())))

for key,value in spread.items():
  sentence = "Your {key} is the {value} card, {position}."
  full_sentence = sentence.format(key = key, value = value,position = random.choice(position))
  print(full_sentence)
  time.sleep(1)
