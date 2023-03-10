import os
from gtts import gTTS
from playsound import playsound
import time


def chose_file():
    print("请选择听写文件：")
    dir = "./docs"
    dir = os.fsdecode(dir)

    idx_to_filename = {}
    files = []
    for idx, file in enumerate(os.listdir(dir)):
        filename = os.fsdecode(file)
        files.append(filename)

    files.sort()
    for idx, file in enumerate(files):
        idx_to_filename[idx + 1] = file
        print(f"{idx + 1}): {file}")
    ans = int(input())
    return idx_to_filename[ans]


if __name__ == '__main__':
    file_name: str = chose_file()
    file_loc = f'./docs/{file_name}'

    with open(file_loc) as file:
        lines = [line.rstrip() for line in file]

    print("现在开始听写...")
    time.sleep(5)
    language = 'en'
    for line in lines:
        while True:
            try:
                tts = gTTS(text=line, lang=language, tld='co.uk')
                tts.save('speech.mp3')
                playsound('speech.mp3')
                break
            except:
                print("error, try again...")
                time.sleep(1)

        time.sleep(3)

    print("现在开始记录错误单词, 正确 y，错误 n。")
    error_line = []
    for line in lines:
        ans = input(f"{line} 是否拼写正确[y]: ") or "y"
        if ans != "y":
            error_line.append(line + '\n')

    print(f"总单词数: {len(lines)}, 错误数: {len(error_line)}, 正确率: {1.0 - 1.0 * len(error_line) / len(lines)}")
    if len(error_line) == 0:
        print("耶，没有错误！")
    else:
        flag = input("是否生成错误本？[y]: ") or "y"
        if flag != "y":
            exit(0)
        print("生成错误本中...")
        tmp = file_name.split('_')
        if len(tmp) == 1:
            tmp.append("1")
        else:
            num = int(tmp[-1])
            num += 1
            tmp.pop()
            tmp.append(str(num))

        new_file_name = '_'.join(tmp)
        with open(f"./docs/{new_file_name}", "w") as new_file:
            new_file.writelines(error_line)
