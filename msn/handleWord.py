import os
import re
import win32com.client as win32

from kevin.handlePic import OCR

# 定义识别敏感词的正则表达式
ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
port1_regex = r"端口:\d+"
port2_regex = r"[A-Z]{3,} [0-9]{3,6}端口"
username_regex = r"用户名：\w+"
password_regex = r"密码：\w+"
defaultPassword_regex = r"默认密码：(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*_+{}\[\]:;<>,.?~\\/-]).{8,16}"
picture1_regex = r"服务器\d :"
picture2_regex = r"端口\d:"



# 合并所有正则
all_regex = re.compile(
    f"({ip_regex}|{port1_regex}|{port2_regex}|{username_regex}|{password_regex}|{defaultPassword_regex}|{picture1_regex}|{picture2_regex})")

# 路径
current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_directory, "outputWord.txt")


def handleWord(filePath):
    word = win32.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(filePath)
    text = doc.Content.Text
    print(text)
    #识别word中的图片
    # for i, shape in doc.InlineShapes:
    #     if shape.Type == 3:  # Check if the shape contains a picture
    #         image_path = os.path.join(current_directory, f'image_{i}.png')
    #         shape.Range.Copy()  # Copy the image
    #         word.Selection.PasteAndFormat(2)  # Paste the image
    #         if word.Selection.InlineShapes.Count > 0:
    #             word.Selection.InlineShapes[0].SaveAsPicture(image_path)  # Save the image
    #         add_txt(OCR(image_path), text)  # 添加图片信息到text
    for shape in doc.InlineShapes:
        # Check if shape has image data
        if shape.Type == 3:  # Type 3 indicates the shape has an image.
            image_path = os.path.join(current_directory, f'image_{shape.Range.Start}.png')
            shape.Range.Copy()  # Copy image data

            # Use clipboard to get the image data and save to file
            from PIL import ImageGrab
            img = ImageGrab.grabclipboard()  # Gets image from clipboard
            if img:
                img.save(image_path, 'PNG')
                text += str(OCR(image_path))

    doc.Close()
    word.Quit()
    print(text)
    sensitive_data = re.findall(all_regex, text)
    return sensitive_data


def save_to_txt(data, output_path):
    with open(output_path, 'w') as file:
        for item in data:
            file.write(item + '\n')


def add_txt(data, text):
    with open(text, 'a') as file:
        file.write(data + '\n')


if __name__ == "__main__":
    # 示例
    word_path = "D:\huaweicup\huaweicup2-RichTextDetc\赛题材料\office\麒麟SSL+VPN+Windows客户端使用手册.doc"


    # print(handleWord(word_path))
    tex = handleWord(word_path)
    save_to_txt(tex, output_path)
