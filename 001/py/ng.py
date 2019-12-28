import sys
import module1, module2, module3 

#--- プログラム部分

# main関数
def main():

    # keyに引数を代入する。引数がない場合は終了
    try:
        key = sys.argv[1]

    except (IndexError):
        print('引数がないです', file=sys.stderr)
        sys.exit(1)

    # ifで確認して実行
    if key == 'm1':
        module1.start()

    elif key == 'm2':
        module2.start()

    elif key == 'm3':
        module3.start()

    else:
        print('moduleがないです', file=sys.stderr)
        sys.exit()

# main関数を実行
if __name__ == '__main__':
    main()
