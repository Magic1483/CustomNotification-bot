import os 

for file in os.listdir("files/tmp_inst"):
    print(os.path.join(file))