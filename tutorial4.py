import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

# class_names = ['Top', 'Trouser', 'Pullover', 'Dress',
#             'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Boot']

class_names = ['0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9']

def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

fashion_mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# print(type(train_images)) => <class 'numpy.ndarray'>
# print(type(train_labels)) => <class 'numpy.ndarray'>

# Deep
# https://qiita.com/Kuma_T/items/4449f008cad18fbb7f1a
#


# model = tf.keras.Sequential(
#   [
#     # 28×28サイズの2次元データを784の1次元データに平滑化する
#     tf.keras.layers.Flatten(input_shape=(28,28)),
#     tf.keras.layers.Dense(1000,activation=tf.nn.relu),
#     tf.keras.layers.Dense(1000,activation=tf.nn.relu),
#     #
#     tf.keras.layers.Dense(10,activation=tf.nn.softmax),
#   ]
# )

model = tf.keras.Sequential(
  [
    # 28×28サイズの2次元データを784の1次元データに平滑化する
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(1000,activation=tf.nn.relu),
    tf.keras.layers.Dense(1000,activation=tf.nn.relu),
    #
    tf.keras.layers.Dense(10,activation=tf.nn.softmax),
  ]
)

model.summary()

# model.compile(optimizer='adam', #どうやって学習を最適化するかを決定
#               loss='sparse_categorical_crossentropy', #どうやって損失を定義するかを決定
#               metrics=['accuracy']) #メトリックはとりあえずaccuracyを選んでおけば良い
# model.fit(train_images, train_labels, epochs=5)

# test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
# print(f"\nTest accuracy:{test_acc}")
