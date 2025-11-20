import numpy as np
from PIL import Image

image = "BMW.jpg"
output = "BMW_gray.jpg"

original = Image.open(image)
data = np.asarray(original)
# print(data.shape) #(183 ,275 ,3)

red_channel = data[:, :, 0]
print(f"red_channel: {red_channel}, Mean: {red_channel.mean()} , Min:{red_channel.min()}")

# Y=0.2126R + 0.7152G + 0.0722B
result = [0.2126 , 0.7152 ,0.0722]
gray = data @ result
gray = gray.astype('uint8')

grayscale_image = Image.fromarray(gray)
grayscale_image.save(output)