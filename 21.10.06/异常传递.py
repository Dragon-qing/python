import time
try:
    f = open("test.txt")
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            print(con)
            time.sleep(2)
    except:
        print("程序异常终止")
    finally:
        f.close()
except:
    print("file is not fond")