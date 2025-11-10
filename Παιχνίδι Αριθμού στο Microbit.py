# Πρόγραμμα: Παιχνίδι Αριθμού στο Microbit
# Δημιουργοί: Ονόματα Μαθητών
# Ημεροηνία: 9/11/2025

# Imports Βιβλιοθηκών μπαίνουν στην αρχή
from microbit import *
import random
import music

# Η μαντεψιά του παίκτη
guess = 5
# Παραγωγή μυστικού αριθμού (τυχαίος ακέραιος) από την πλακέτα
secret = random.randint(1, 10)
display.scroll("GUESS NUMBER")    
music.play(['c'])
display.show(guess)

# Κώδικας μέσα σε βρόγχο επανάληψης 'while True:' επαναλαμβάνεται για πάντα
while True:
    if button_a.was_pressed():
        guess -= 1
        display.show(guess)
        
    if button_b.was_pressed():
        guess += 1
        display.show(guess)

    if accelerometer.was_gesture('shake'):
        if guess == secret:
            display.show(Image.HAPPY)
            sleep(2000)
            music.play(music.DADADADUM)
            display.clear()
        elif guess < secret:
            # Πάνω Βελάκι για αύξηση μαντεψιάς
            display.show(Image('00900:'
                               '09990:'
                               '99999:'
                               '00900:'
                               '00900'))
            sleep(2000)
            display.clear()
        else:
            # Κάτω Βελάκι για μείωση μαντεψιάς
            display.show(Image('00900:'
                               '00900:'
                               '99999:'
                               '09990:'
                               '00900'))
            sleep(2000)
            display.clear()