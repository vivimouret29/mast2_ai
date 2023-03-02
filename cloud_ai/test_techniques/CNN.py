# importing necessary libs
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from sklearn.model_selection import train_test_split


# loading datas, splitting datas to train, test and evaluation datasets.
(data_to_use), (data_on_side) = tf.keras.datasets.mnist.load_data()
x_train, x_test, y_train, y_test = train_test_split(data_to_use[0], data_to_use[1], test_size=0.20, random_state=42)
x_val = data_on_side[0]
y_val = data_on_side[1]

# normalisation
x_train_normalized = x_train.astype(float) / 255
x_test_normalized = x_test.astype(float) / 255
x_val_normalized = x_val.astype(float) / 255

# making categories encoded out of labels
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)
y_val = tf.keras.utils.to_categorical(y_val, 10)


# building simple model architecture
model = Sequential([
  Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
  Conv2D(64, kernel_size=(3, 3), activation='relu'),
  MaxPooling2D(pool_size=(2, 2)),
  Dropout(0.25),
  Flatten(),
  Dense(128, activation='relu'),
  Dropout(0.5),
  Dense(10, activation='softmax'),
])

# compiling model
model.compile(
  'adam',
  loss='categorical_crossentropy',
  metrics=['accuracy']
)

# training and evaluate the model
model.fit(
  x_train_normalized,
  y_train,
  epochs=5,
  batch_size=128,
  validation_data=(x_test_normalized, y_test)
)

eval_score = model.evaluate(x_val_normalized, y_val)
print(eval_score)