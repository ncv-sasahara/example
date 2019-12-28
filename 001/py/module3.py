import random

def start():
    random_number = random.randint(0, 1000)

    print('''ランダムな数値を出力します。
    ランダムな数値: {0}
'''.format(random_number))
