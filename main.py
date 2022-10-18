import random
import time

# vanity
print('=======================================')
print('           Trua nay an gi (tm)         ')
print('             (c) 2022 Long             ')
print('=======================================')

# txt to py list
tnag_file = open("tnag.txt", "r")
trua_nay_an_gi = tnag_file.read()
tnag_list = trua_nay_an_gi.split("\n")
tnag_list.pop(0)

# debug
print('Danh sách có {} items'.format(len(tnag_list)))

# "artificial" "intelligence"
print('please wait while the AI leverages choices')
time.sleep(2)
print('almost done...')
time.sleep(3)
print("Hôm nay ăng {}".format(random.choice(tnag_list)))

input('press any key to close')

tnag_file.close()
