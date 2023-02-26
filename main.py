import os
import pyttsx3


def chose_file():
    print("请选择听写文件：")
    dir = "./docs"
    dir = os.fsdecode(dir)

    idx_to_filename = {}
    for idx, file in enumerate(os.listdir(dir)):
        filename = os.fsdecode(file)
        idx_to_filename[idx + 1] = filename
        print(f"{idx + 1}): {filename}")
    ans = int(input())
    return idx_to_filename[ans]


if __name__ == '__main__':
    file_name: str = chose_file()
    file_loc = f'./docs/{file_name}'

    with open(file_loc) as file:
        lines = [line.rstrip() for line in file]

    print("现在开始听写...")
    engine = pyttsx3.init()
    for line in lines:
        engine.say(line)
        engine.runAndWait()

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
