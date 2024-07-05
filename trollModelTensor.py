import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, concatenate, LSTM
from tensorflow.keras.models import Model
import numpy as np

# ONLY EXAMPLE DATA SETUP CSV DATA once accurate
time_data = np.array([8, 12, 16, 20, 3, 6, 18, 14, 22, 7, 11, 15, 19, 9, 21])  # Example times (in hours)
location_data = np.array([1, 3, 2, 4, 4, 2, 4, 1, 3, 5, 1, 4, 2, 5, 3])  # Example locations (could be indices or IDs)
likelihood_data = np.array([0.1, 0.8, 0.1, 0.9, 0.5, 0.2, 0.6, 0.4, 0.7, 0.3, 0.5, 0.9, 0.2, 0.8, 0.6])  # Example likelihoods (percentages)

# Reshape data
time_data = time_data.reshape(-1, 1)
location_data = location_data.reshape(-1, 1)
likelihood_data = likelihood_data.reshape(-1, 1)

# Define inputs
time_input = Input(shape=(1,), name='time')
location_input = Input(shape=(1,), name='location')
likelihood_data = Input(shape=(1,), name='likelihood1')

#Categorial encoding
time_embedded = tf.keras.layers.Embedding(input_dim=24, output_dim=10)(time_input)
time_flattened = tf.keras.layers.Flatten()(time_embedded)

# Concatenate the flattened time embedding with location input
concatenated = concatenate([time_flattened, location_input])

# LSTM layer
lstm_layer = tf.keras.layers.LSTM(10)(tf.expand_dims(concatenated, axis=1))

# Dense layers for processing
dense1 = Dense(10, activation='relu')(lstm_layer)
dense2 = Dense(5, activation='relu')(dense1)

# Output layer
output = Dense(1, activation='sigmoidlstm_layer = tf.keras.layers.LSTM(10)(tf.expand_dims(concatenated, axis=1))

# Dense layers for processing
dense1 = Dense(10, activation='relu')(lstm_layer)
dense2 = Dense(5, activation='relu')(dense1)

# Output layer
output = Dense(1, activation='sigmoid', name='likelihood')(dense2)

# Define + Compile model, maybe change optimizer?
model = Model(inputs=[time_input, location_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

# Fit the model with', name='likelihood')(dense2)

# Define + Compile model, maybe change optimizer?
model = Model(inputs=[time_input, location_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

# Fit the model with epochs setting and validation split
modelFinal = model.fit([time_input, location_input], epochs=10)