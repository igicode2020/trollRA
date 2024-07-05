import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Example data
time_data = np.array([8, 12, 13, 20, 5, 6, 18, 14, 22, 7, 11, 15, 19, 9, 21])
location_data = np.array([1, 3, 1, 4, 2, 2, 4, 1, 3, 5, 1, 4, 2, 5, 3])
likelihood_data = np.array([0.1, 0.2, 0.1, 0.9, 0.5, 0.2, 0.6, 0.4, 0.7, 0.3, 0.5, 0.9, 0.2, 0.8, 0.6])

# Define the model
model = Sequential([
    Dense(10, activation='relu', input_shape=(1,)),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Fit the model
model.fit(time_data, location_data, epochs=1000, verbose=0)

# Evaluate the model (optional)
loss = model.evaluate(time_data, location_data)
print(f"Mean Squared Error: {loss}")

# Predict locations for new time_data
'''new_time_data = np.array([13, 17, 23])
predictions = model.predict(new_time_data)
print("Predictions:")
for i in range(len(new_time_data)):
    print(f"Time: {new_time_data[i]}, Predicted Location: {predictions[i][0]}")'''
