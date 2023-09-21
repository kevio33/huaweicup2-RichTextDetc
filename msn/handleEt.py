import xlrd

wb = xlrd.open_workbook('E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\wps\资产梳理.et')

# 读取文件内容pip
sheet = wb.sheet_by_index(0)
data = sheet.get_rows()


# 打印文件内容
for row in data:
    print(row)


def handlEt(fileName,filePath):
    wb = xlrd.open_workbook('E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\wps\资产梳理.et')

    # 读取文件内容
    sheet = wb.sheet_by_index(0)
    data = sheet.get_rows()


    # 打印文件内容
    for row in data:
        print(row)

    

if __name__ == '__main__':
    handlEt('','E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\wps\资产梳理.et')