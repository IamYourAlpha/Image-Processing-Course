import Image

img = Image.open('./colorImages/image1.jpg') # image extension *.png,*.jpg
new_width  = 32
new_height = 32
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('test.png')
 
 
 
 
 
 
 
 
 
 
 
