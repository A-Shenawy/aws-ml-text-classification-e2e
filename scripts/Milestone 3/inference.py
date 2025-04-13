import joblib
import os
import json

# Load the model and vectorizer from the model directory
def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "logistic_model.pkl"))
    vectorizer = joblib.load(os.path.join(model_dir, "tfidf_vectorizer.pkl"))
    return model, vectorizer

# Parse the input data
def input_fn(request_body, content_type='application/json'):
    if content_type == 'application/json':
        input_data = json.loads(request_body)
        return input_data['text']
    else:
        raise ValueError(f"Unsupported content type: {content_type}")

# Perform prediction
def predict_fn(input_data, model_objects):
    model, vectorizer = model_objects
    vectorized_input = vectorizer.transform([input_data])  # Vectorize the input text
    prediction = model.predict(vectorized_input)
    return prediction[0]  # Return the predicted label (0 or 1)

# Format the output
def output_fn(prediction, content_type='application/json'):
    if content_type == 'application/json':
        response_body = {
            'predicted_label': int(prediction)  # make sure to cast to int for JSON serialization
        }
        return json.dumps(response_body)
    else:
        raise ValueError(f"Unsupported content type: {content_type}")