import glob
from PIL import Image
import numpy as np

folder = 'speed'
images = []
for f in glob.iglob("./images/{}/*.JPG".format(folder)):
    images.append(np.asarray(Image.open(f)))

images = np.array(images)

for i in range(len(images)):
    images[i].save('{}_{}.jpg'.format(folder, i+1))
