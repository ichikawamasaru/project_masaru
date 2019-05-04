#! python3
# pw.py - パスワード脆弱性あり
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3dt' ,
             'luggage': '12345'}

import sys
import pyperclip
if len(sys.argv)<2:
    print('使い方:python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします。')
    sys.exit()

account = sys.argv[1] #最初のコマンド引数がアカウント名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account+ 'のパスワードをクリップボードにコピーしました。')
else:
    print(account+'というアカウント名はありません')
