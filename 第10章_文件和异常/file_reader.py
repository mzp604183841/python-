# 读文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 逐行读取文件内容 使用for循环
with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    for line_content in file_object:
        print(line_content.rstrip())

# 将文件每一行内容保存到列表中

content_list = []
with open('pi_digits.txt') as file_object:
    lines_content = file_object.readlines()
