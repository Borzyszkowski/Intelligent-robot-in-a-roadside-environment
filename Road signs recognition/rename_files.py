import glob
from PIL import Image

folder = 'work'
images = []
for f in glob.iglob("./images/{}/*.JPG".format(folder)):
    images.append(Image.open(f))

for i in range(len(images)):
    images[i].save('./images/{}_{}.jpg'.format(folder, i+1))
