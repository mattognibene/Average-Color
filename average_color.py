from PIL import Image
#tree method?
file = input("Enter file name: ")
im = Image.open(file)
pix=im.load()
r = 0
g = 0
b = 0

for x in range(im.size[0]):
    for y in range(im.size[1]):
        r += pix[x,y][0]
        g += pix[x, y][1]
        b += pix[x, y][2]



def find_average(a):
    return int(a/(im.size[0]*im.size[1]))


rgb = (find_average(r), find_average(g), find_average(b))
print(rgb)

