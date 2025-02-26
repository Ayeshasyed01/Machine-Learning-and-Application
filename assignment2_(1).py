# -*- coding: utf-8 -*-
"""Assignment2 (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ADHXrMlh-Jk-4T07hUH-0O_RxCvWAZyZ
"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam

from sklearn.metrics import classification_report, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tensorflow.keras import models, layers

data = np.load('/content/yale-face-database (1) (3).npz')
arr_0 = data['arr_0']
arr_1 = data['arr_1']
arr_2 = data['arr_2']
arr_3 = data['arr_3']

num_classes=16
y_train = to_categorical(arr_1)
y_test = to_categorical(arr_3)
X_train = arr_0.astype('float32')/255.0
X_test = arr_2.astype('float32')/255.0

"""Model 1 activation = relu,layers = 3,kernal size =(3,3)"""

from tensorflow.keras import models, layers

model = models.Sequential([
    # First convolutional layer
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(160, 160, 3)),
    layers.AveragePooling2D((2, 2)),

    # Second convolutional layer
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.AveragePooling2D((2, 2)),

    # Third convolutional layer
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.AveragePooling2D((2, 2)),

    # Dense classifier
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(16, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model to view the architecture
model.summary()

history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

print(classification_report(y_true, y_pred))

"""Model 2 activation = relu,layers = 3,Kernal size = (5,5),Average pooling"""

from tensorflow.keras import models, layers

model = models.Sequential([
    # First convolutional layer
    layers.Conv2D(32, (5, 5), activation='relu', input_shape=(160, 160, 3)),
    layers.AveragePooling2D((2, 2)),

    # Second convolutional layer
    layers.Conv2D(64, (5, 5), activation='relu'),
    layers.AveragePooling2D((2, 2)),

    # Third convolutional layer
    layers.Conv2D(128, (5, 5), activation='relu'),
    layers.AveragePooling2D((2, 2)),

    # Dense classifier
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(16, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model to view the architecture
model.summary()

history = model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

print(classification_report(y_true, y_pred))

"""Model 3 activation = relu,layers = 3,Kernal size = (5,5),Padding =(1,1),Pooling = average pooling


"""

from tensorflow.keras import models, layers

model = models.Sequential([
    # Input layer
    layers.Input(shape=(160, 160, 3)),

    # First convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(1, 1)),  # Add 1 pixel of padding on each side
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.AveragePooling2D((2, 2)),

    # Second convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(1, 1)),  # Maintain dimensionality
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.AveragePooling2D((2, 2)),

    # Third convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(1, 1)),  # Keep size before applying convolution
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.AveragePooling2D((2, 2)),

    # Dense classifier
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(16, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model to view the architecture
model.summary()

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test accuracy:", test_acc)

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

print(classification_report(y_true, y_pred))

"""Model 4 layers = 3,Padding=(2,2),Kernal size(3,3),Maxpooling,Activation = Relu"""

from tensorflow.keras import models, layers

model = models.Sequential([
    # Input layer
    layers.Input(shape=(160, 160, 3)),

    # First convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Add 1 pixel of padding on each side
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Second convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Maintain dimensionality
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Keep size before applying convolution
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Dense classifier
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(16, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model to view the architecture
model.summary()

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test accuracy:", test_acc)

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

print(classification_report(y_true, y_pred))

"""Model 4 layers = 3,Padding=(2,2),Kernal size(5,5),Maxpooling,Activation = Relu


"""

from tensorflow.keras import models, layers

model = models.Sequential([
    # Input layer
    layers.Input(shape=(160, 160, 3)),

    # First convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Add 1 pixel of padding on each side
    layers.Conv2D(32, (5, 5), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Second convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Maintain dimensionality
    layers.Conv2D(64, (5, 5), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Keep size before applying convolution
    layers.Conv2D(128, (5, 5), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Dense classifier
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(16, activation='softmax')  # Assuming 10 classes for output
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model to view the architecture
model.summary()

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test accuracy:", test_acc)

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

print(classification_report(y_true, y_pred))

"""Model 4 layers = 3,Padding=(2,2),Kernal size(5,5),Maxpooling,Activation = tanh"""

from tensorflow.keras import models, layers

model = models.Sequential([
    # Input layer
    layers.Input(shape=(160, 160, 3)),

    # First convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Add 1 pixel of padding on each side
    layers.Conv2D(32, (5, 5), activation='tanh'),
    layers.MaxPooling2D((2, 2)),

    # Second convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Maintain dimensionality
    layers.Conv2D(64, (5, 5), activation='tanh'),
    layers.MaxPooling2D((2, 2)),

    # Third convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Keep size before applying convolution
    layers.Conv2D(128, (5, 5), activation='tanh'),
    layers.MaxPooling2D((2, 2)),

    # Dense classifier
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(16, activation='softmax')  # Assuming 10 classes for output
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model to view the architecture
model.summary()

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test accuracy:", test_acc)

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

print(classification_report(y_true, y_pred))

"""From outoff this All 5 models Model 4 is good according to the performance curves and confusion matrix and Accuracy so now iam increasing the epochs to 100 and learning rate to 0.001"""

from tensorflow.keras import models, layers

model = models.Sequential([
    # Input layer
    layers.Input(shape=(160, 160, 3)),

    # First convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Add 1 pixel of padding on each side
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Second convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Maintain dimensionality
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third convolutional block with explicit padding
    layers.ZeroPadding2D(padding=(2, 2)),  # Keep size before applying convolution
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Dense classifier
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(16, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model to view the architecture
model.summary()

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test accuracy:", test_acc)

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

print(classification_report(y_true, y_pred))

cnn = models.Sequential([
    layers.Input(shape=(160,160, 3)),
    layers.Conv2D(32, (3, 3)),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Conv2D(12, (3, 3)),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Conv2D(64, (3, 3)),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(16, activation='softmax')
])
cnn.summary()

optim = Adam(learning_rate=0.001)
cnn.compile(optimizer=optim, loss='categorical_crossentropy', metrics=['accuracy'])

history = cnn.fit(X_train, y_train, epochs=20, batch_size=128, validation_data=(X_test, y_test))

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test accuracy:", test_acc)

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

import cv2
def visualize_neuron_weights(model, layer_name, neuron_index, input_shape):
    # Ensure input_shape is a tuple of (height, width)
    assert isinstance(input_shape, tuple) and len(input_shape) == 2, "input_shape must be a tuple of (height, width)"

    # Extract weights for the specified layer
    weights, biases = model.get_layer(layer_name).get_weights()

    # Extract weights for the specified neuron
    neuron_weights = weights[:, neuron_index]
    # print(neuron_weights.shape)

    # Initial attempt to reshape weights to a square shape
    side_length = int(np.sqrt(len(neuron_weights)))
    if side_length * side_length != len(neuron_weights):
        # If weights cannot be reshaped into a perfect square, they need to be resized
        # First, resha pe into the closest square for initial visualization

        closest_square_side_length = int(np.sqrt(len(neuron_weights)))
        reshaped_weights = np.resize (neuron_weights, (closest_square_side_length**2))
        reshaped_weights = reshaped_weights.reshape((closest_square_side_length,closest_square_side_length))

        # Use OpenCV to resize (upsample or downsample) to match input_shape
        resized_weights = cv2.resize(reshaped_weights, input_shape, interpolation=cv2.INTER_LINEAR)
    else:
        # If weights can be perfectly squared, check if they match input_shape already
        reshaped_weights = np.reshape(neuron_weights, (side_length, side_length))
        if reshaped_weights.shape == input_shape:
            resized_weights = reshaped_weights
        else:
            # Resize to match input_shape if they don't match
            resized_weights = cv2.resize(reshaped_weights, input_shape, interpolation=cv2.INTER_LINEAR)

    # Visualization as heatmap
    plt.imshow(resized_weights, cmap='viridis')
    plt.title(f"Weights of Neuron {neuron_index} in {layer_name} (resized to input shape)")
    plt.colorbar()
    plt.show()

model.summary()

visualize_neuron_weights(model, 'dense_2', 9, input_shape=(28,28))

print(classification_report(y_true, y_pred))

cnn = models.Sequential([
    layers.Input(shape=(160,160, 3)),
    layers.Conv2D(32, (3, 3)),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Conv2D(12, (3, 3)),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Conv2D(64, (3, 3)),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.15),
    layers.Dense(16, activation='softmax')
])
cnn.summary()

"""Model 4.2"""

optim = Adam(learning_rate=0.001)
cnn.compile(optimizer=optim, loss='categorical_crossentropy', metrics=['accuracy'])

history = cnn.fit(X_train, y_train, epochs=20, batch_size=128, validation_data=(X_test, y_test))

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(history.history['loss'], label='training')
plt.plot(history.history['val_loss'], label='validation')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()

plt.subplot(122)
plt.plot(history.history['accuracy'], label='training')
plt.plot(history.history['val_accuracy'], label='validation')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()

plt.show()

y_true = np.argmax(y_test, axis=1)
y_pred = np.argmax(model.predict(X_test), axis=1)

plt.figure(figsize=(8, 8))

sns.heatmap(confusion_matrix(y_true, y_pred), cmap='Blues', annot=True, fmt='d')
plt.show()

import cv2
def visualize_neuron_weights(model, layer_name, neuron_index, input_shape):
    # Ensure input_shape is a tuple of (height, width)
    assert isinstance(input_shape, tuple) and len(input_shape) == 2, "input_shape must be a tuple of (height, width)"

    # Extract weights for the specified layer
    weights, biases = model.get_layer(layer_name).get_weights()

    # Extract weights for the specified neuron
    neuron_weights = weights[:, neuron_index]
    # print(neuron_weights.shape)

    # Initial attempt to reshape weights to a square shape
    side_length = int(np.sqrt(len(neuron_weights)))
    if side_length * side_length != len(neuron_weights):
        # If weights cannot be reshaped into a perfect square, they need to be resized
        # First, resha pe into the closest square for initial visualization

        closest_square_side_length = int(np.sqrt(len(neuron_weights)))
        reshaped_weights = np.resize (neuron_weights, (closest_square_side_length**2))
        reshaped_weights = reshaped_weights.reshape((closest_square_side_length,closest_square_side_length))

        # Use OpenCV to resize (upsample or downsample) to match input_shape
        resized_weights = cv2.resize(reshaped_weights, input_shape, interpolation=cv2.INTER_LINEAR)
    else:
        # If weights can be perfectly squared, check if they match input_shape already
        reshaped_weights = np.reshape(neuron_weights, (side_length, side_length))
        if reshaped_weights.shape == input_shape:
            resized_weights = reshaped_weights
        else:
            # Resize to match input_shape if they don't match
            resized_weights = cv2.resize(reshaped_weights, input_shape, interpolation=cv2.INTER_LINEAR)

    # Visualization as heatmap
    plt.imshow(resized_weights, cmap='viridis')
    plt.title(f"Weights of Neuron {neuron_index} in {layer_name} (resized to input shape)")
    plt.colorbar()
    plt.show()

model.summary()

visualize_neuron_weights(model, 'dense_3', 9, input_shape=(28,28))

