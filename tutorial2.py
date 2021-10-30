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
plt.figure(figsize=(10,10))

for i in range(25):

  plt.subplot(5,5, i+1)

  plt.xticks([])
  plt.yticks([])

  # 画像の描画
  # NNCに変換
  plt.imshow(train_images[i]/255, cmap="gray")

  # グリッド線の有無
  plt.grid(False)

  plt.xlabel(class_name[train_labels[i]])

# 描画
plt.show()
