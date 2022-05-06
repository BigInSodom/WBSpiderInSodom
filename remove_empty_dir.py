import os


def into_dir(path_now):
    print("path:"+path_now)
    list=os.listdir(path_now)
    for file_now in list:
        if os.path.isdir(path_now+"\\"+file_now):
            into_dir(path_now+'\\'+file_now)
        # if file_now.endswith(".json"):
        #     print("json")
    list=os.listdir(path_now)
    if list:
        print(" ")
    else:
        os.rmdir(path_now)


if __name__ == '__main__':
    now=os.getcwd()
    into_dir(now)


    


