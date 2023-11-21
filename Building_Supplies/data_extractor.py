import tensorflow as tf
import os

#Avoid OOM errors by setting aside GPU Memory Constraints
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus: 
    tf.config.experimental.set_memory_growth(gpu, True)
    print(gpu)


#Data extraction
import cv2
from PIL import Image

data_dir = 'data' 
image_exts = ['jpeg','jpg', 'bmp', 'png']

print(os.listdir(data_dir))

"""for image_class in os.listdir(data_dir): 
    print(image_class)
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        try: 
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in image_exts: 
                print('Image not in ext list {}'.format(image_path))
                os.remove(image_path)
        except Exception as e: 
            print('Issue with image {}'.format(image_path))
            # os.remove(image_path)"""