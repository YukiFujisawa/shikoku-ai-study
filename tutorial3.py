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

# Deep
# https://qiita.com/Kuma_T/items/4449f008cad18fbb7f1a
#


model = tf.keras.Sequential(
  [
    # 28×28サイズの2次元データを784の1次元データに平滑化する
    tf.keras.layers.Flatten(input_shape=(28,28)),
    # 二層目のHidden Layerを定義
    # 活性化関数
    tf.keras.layers.Dense(128,activation=tf.nn.relu),
    #
    tf.keras.layers.Dense(10,activation=tf.nn.softmax),
  ]
)
# model.summary()

model.compile(optimizer='adam', #どうやって学習を最適化するかを決定
              loss='sparse_categorical_crossentropy', #どうやって損失を定義するかを決定
              metrics=['accuracy']) #メトリックはとりあえずaccuracyを選んでおけば良い
model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"\nTest accuracy:{test_loss}")
