from PIL import Image

# 打开图像文件
img = Image.open("D:\\大四上\\课内学习\\科研相关\\graphic-design-generation.github.io-main\\design-edit\\static_lr\\img_new\\teaser\\a.jpg")

# 获取图像的宽度和高度
width, height = img.size

# 计算宽高比例
aspect_ratio = width / height

# 打印宽高比例
print("图像宽高比例：", aspect_ratio)
