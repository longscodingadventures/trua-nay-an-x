import random

# txt to py list
tnag_file = open("tnag.txt", "r")
trua_nay_an_gi = tnag_file.read()
tnag_list = trua_nay_an_gi.split("\n")

# debug
print("danh sách có số item : ", + len(tnag_list))

# random
random_item = random.choice(tnag_list)
print("Hôm nay ăn", random_item)

tnag_file.close()
