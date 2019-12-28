import sys
import module1, module2, module3 

#--- データ部分

app  = {'m1': module1,
        'm2': module2,
        'm3': module3}


#--- プログラム部分

# main関数
def main():

    # keyに引数を代入する。引数がない場合は終了
    try:
        key = sys.argv[1]

    except (IndexError):
        print('引数がないです')
        return

    # app[key].startを実行 keyがない場合（m1, m2, m3以外の場合）は終了
    try:
        app[key].start()

    except (KeyError):
        print('moduleがないです')

# main関数を実行
if __name__ == '__main__':
    main()

