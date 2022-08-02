import random
import time

# vanity
print('=======================================')
print('             trua nay an gi            ')
print('             (c) 2022 long             ')
print('=======================================')

# txt to py list
tnag_file = open("tnag.txt", "r")
trua_nay_an_gi = tnag_file.read()
tnag_list = trua_nay_an_gi.split("\n")

# debug
print("danh sách có số item :", + len(tnag_list))

# "artificial" "intelligence"
print('please wait while the AI leverages choices')
time.sleep(5)

# random
random_item = random.choice(tnag_list)
print("Hôm nay ăn", random_item)

tnag_file.close()
