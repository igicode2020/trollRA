import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
# from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load the dataset
file_path = 'justin.csv'
df = pd.read_csv(file_path, parse_dates=[['Date', 'Time']], keep_date_col=True)

# Convert 'Date' and 'Time' to datetime format
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

# Extract features from datetime
df['Hour'] = df['DateTime'].dt.hour
df['DayOfWeek'] = df['DateTime'].dt.dayofweek

# Encode categorical 'Location' labels
label_encoder = LabelEncoder()
df['Location_Code'] = label_encoder.fit_transform(df['Location'])

# Prepare features and target
X = df[['Hour', 'DayOfWeek']].values
y = df['Location_Code'].values

# One-hot encode categorical features (DayOfWeek)
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [1])],
    remainder='passthrough'
)
X = ct.fit_transform(X)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the model architecture
model = Sequential([
    Dense(128, activation='relu', input_dim=X_train.shape[1]),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(len(label_encoder.classes_), activation='softmax')  # Output layer with softmax for multiclass classification
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {accuracy * 100:.2f}%')

# Predictions on the test set
predictions = model.predict(X_test)

# Example prediction for the first test sample
sample_index = 0
predicted_location_code = predictions[sample_index].argmax()
predicted_location = label_encoder.inverse_transform([predicted_location_code])[0]

actual_location_code = y_test[sample_index]
actual_location = label_encoder.inverse_transform([actual_location_code])[0]

print(f'Example Prediction:\n'
      f'Predicted Location: {predicted_location}\n'
      f'Actual Location: {actual_location}')

