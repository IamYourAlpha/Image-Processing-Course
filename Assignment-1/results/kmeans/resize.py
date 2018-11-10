import Image

img = Image.open('./kmean5.png') # image extension *.png,*.jpg
new_width  = 240
new_height = 160
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('kmean_5.png')
 
 
 
 
 
 
 
 
 
 
 
