import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_name = ['Top', 'Trouser', 'Pullover', 'Dress',
            'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Boot']

# print(type(train_images)) => <class 'numpy.ndarray'>
# print(type(train_labels)) => <class 'numpy.ndarray'>

# 描画領域全体
plt.figure()

# 画像の描画
# NNCに変換
plt.imshow(train_images[0]/255, cmap="gray")

# カラースケール
plt.colorbar()

# グリッド線の有無
plt.grid(True)

# 描画
plt.show()
