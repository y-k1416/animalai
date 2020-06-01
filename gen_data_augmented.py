import numpy as np
import os, glob
from PIL import Image
from sklearn.model_selection import train_test_split

classes = ['monkey', 'boar', 'crow']
num_classes = len(classes)
image_size = 50
num_testdata = 100

#image load
X_train = []
X_test = []
y_train = []
y_test = []

for index, class_label in enumerate(classes):
    photo_dir = './' + class_label
    files = glob.glob(photo_dir + '/*.jpg')
    for i , file_ in enumerate(files):
        if i  >= 200: break
        image = Image.open(file_)
        image = image.convert('RGB')
        image = image.resize((image_size, image_size))
        data = np.asarray(image)

        if i < num_testdata:
            X_test.append(data)
            y_test.append(index)
        else:


            for angle in range(-20, 20, 5):
                img_r = image.rotate(angle)
                data = np.asarray(img_r)
                X_train.append(data)
                y_train.append(index)


                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                data = np.asarray(img_trans)
                X_train.append(data)
                y_train.append(index)



# X = np.array(X)
# Y = np.array(Y)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

xy = (X_train, X_test, y_train, y_test)

np.save('./animal_aug.npy', xy)
