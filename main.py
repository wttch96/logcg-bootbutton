file = open('wttch.plist', 'w')

keys = {
    # P Y F G C R L
    'p': ['#隐私模式', ''],
    'y': ['#中英切换', ''],
    'f': ['#粘贴', ''],
    'g': ['#行首', ''],
    'c': ['#行尾', ''],
    'r': ['#大团结', ''],
    'l': ['#软回车', ''],
    # A O E U I D H T N S
    # ! @ # $ % ^ & * ( ) - 上划
    # 1 2 3 4 5 6 7 8 9 0 - 下划
    'a': ['!', '1'],
    'o': ['@', '2'],
    'e': ['#', '3'],
    'u': ['$', '4'],
    'i': ['%', '5'],
    'd': ['^', '6'],
    'h': ['&', '7'],
    't': ['*', '8'],
    'n': ['(', '9'],
    's': [')', '0'],
    # Q J K X B M W V Z
    # - + / ' : ; . , ?
    # _ = \ " ： ；。，？
    'q': ['-', '_'],
    'j': ['+', '='],
    'k': ['/', '\\'],
    'x': ['\'', '"'],
    'b': [':', '：'],
    'm': [';', '；'],
    'w': ['.', '。'],
    'v': [',', '，'],
    'z': ['?', '？']
}

file.write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
""")
for key in sorted(keys):
    file.write('  <key>{}</key>\n  <string>{}</string>\n  <key>{}⇣</key>\n  <string>{}</string>\n'.format(
        key, keys[key][0], key, keys[key][1]
    ))
file.write("""</dict>
</plist>""")
