 for i in range(rounds):
        print('1. グー  2. チョキ  3. パー')
        hand = int(input('あなたの手を入力してください: '))

        if hand == 1:
            print('あなたの手: グー')
        elif hand == 2:
            print('あなたの手: チョキ')
        elif hand == 3:
            print('あなたの手: パー')
        else:
            print('1, 2, 3 のどれかで入力してください')
            continue  