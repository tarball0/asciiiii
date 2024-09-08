from PIL import Image #PIL is python imaging library
def converter(image,type,saveas,scale):
scale= int(scale)
img=Image.open(image)
w,h=img.size
