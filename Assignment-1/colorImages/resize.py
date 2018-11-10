import Image

img = Image.open('./image5.jpg') # image extension *.png,*.jpg
new_width  = 240
new_height = 160
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('image_5.png')
 
 
 
 
 
 
 
 
 
 
 
