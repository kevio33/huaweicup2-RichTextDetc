from pptx import Presentation
import aspose.slides as slides
import aspose.pydrawing as drawing


'''
    读取ppt内容
    只能读取pptx内容，而无法读取ppt
    因此要先转换格式
'''
def handlePpt(fileName,filePath,isPPT=False):
    pptx = None
    if isPPT == True:
        # 转换为pptx格式
        with slides.Presentation(filePath) as presentation:
            filePath = filePath[:-(len(fileName)+3)]
            filePath = "{0}{1}.pptx".format(filePath,fileName)
            presentation.save(filePath, slides.export.SaveFormat.PPTX)

    pptx = Presentation(filePath)# 文件对象
    for slide in pptx.slides: # 每个幻灯片
        for shape in slide.shapes: #幻灯片的所有形状
            # if shape.has_text_frame: #如果有文本框
            #     text_frame = shape.text_frame
            # if shape.
            print(shape)
    




if __name__ == '__main__':
    handlePpt('学生信息管理系统使用介绍',r'E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\office\220180327081403010127.pptx')
