import random
from tkinter import * # import all in tkinter
import time
# pseudo-code  --> code

# Create app window
window = Tk()
window.title("ທາຍສິຈະເກມ")
window.geometry('700x840')

# ຕົວແປທີ່ລະບຸສະຖານະຂອງເກມ
game_finished = False
score = 0 
lives = 3
words = ['Phasouk','Louangchalern','Kimberry']

# ສະແດງ score and lives ບົນ Window
status_str =  StringVar() # ມາຈາກ tkinter

status_str.set('Score: ' + str(score) + ' | ' + 'Lives: ' + '❤️'*lives)
show_status =  Label(window, textvariable = status_str)
show_status.pack(pady=20)


# ສ້າງ words category hints

word_dict = {
    'Phasouk':
        {'category': 'ນັກທຸລະກິດພັນລ້ານ',
         'hints': ['ນັກສ້າງແຮງບັນດານໃຈ','ສະມາຊິກ CEIT ROBOT','ເປັນນັກທຸລະກິດເບີໜື່ງ 1 ຂອງລາວ']
        },
    'Louangchalern':
        {'category': 'ບໍລິສັດ Tech',
         'hints': ['ບໍລິສັດ Finance', 'ບໍລິສັດ Laolife', 'ບໍລິສັດ BotX']
        },



}




def update_clue(guess, secret_word, clue):
    #guess ໄລ່ໄປທີ່ລະຕົວອັກສອນໃນ Secret_word ເບິ່ງວ່າມີຕົວໃດແນ່ທີ່ຕົງກັບຕົວທີ່ທາຍ
    # ຖ້າທາຍຖືກຕົວກໍໃຫ້ອັບເດດເບາະເເສ ຕົງຕຳແໜ່ງນັ້ນ 
    for i in range (len(secret_word)):
        if guess == secret_word[i]:
            clue[i] = guess
    win =''.join(clue) == secret_word
    return win # ທາຍຈົນບໍ່ເຫຼືອ '?' ແລ້ວ -> True,  ຍັງເຫຼືອ -> False    


# ຕາບໃດທີ່ຍັງມີຄຳໃຫ້ທາຍຢູ່ ແລະ ຊີວິດຍັງເຫຼືອ ---> ຫຼີ້ນຕໍ່ໄປໄດ້

while ( len(words) > 0 ) and ( lives > 0):
    random.shuffle(words)
    # ສຸ່ມຄຳຈາກ words ແລ້ວດືງຄຳນັ້ນອອກຈາກ List
    secret_word = words.pop()
    clue = list('?'*len(secret_word)) # ['?','?','?'....] ຈຳນວນເທົ່າກັບຕົວອັກສອນ Secret_word

    # ຕາບໃດທີ່ຍັງທາຍຄຳນີ້ບໍ່ແລ້ວ ຫຼື ຊີວິດຍັງບໍ່ໝົດ 
    while True : #ຍັງທາຍຄຳບໍ່ແລ້ວ
        print(clue)
        print("ຊີວິດທີ່ເຫຼືອ :" + str(lives))
        guess = input('ທາຍຕົວອັກສອນມາດຸ : ')

        # Check ວ່າຕົວອັກສອນທີ່ທາຍຢູ່ໃນ secret_word ບໍ ?

        if guess in secret_word:
            win = update_clue(guess, secret_word, clue)
            if  win:
                print('ເຢ້ ! ຄຳນັ້ນກໍຄື : ' + secret_word)
                score = score + 1 
                print ('Score : ' + str(score))
                break # ທາຍຄຳນີ້ສຳເລັດແລ້ວ 
             
        else: # ທີ່ guess ມາບໍ່ຢູ່ໃນ secret_word
            print('ທາຍຜິດແລ້ວ ! ເລືອດລົດ')
            lives = lives - 1
            if lives == 0:
                print('ເຈົ້າແພ້ແລ້ວ ຄຳນັ້ນກໍຄື : ' + secret_word)
                break # ມົ່ງເທັງແລ້ວ

            print('Final Score: ' + str(score))
            print('Game End !')