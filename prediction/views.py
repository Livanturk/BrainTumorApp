import os
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageUploadForm
from keras.api.models import load_model
import numpy as np
from PIL import Image

MODEL_PATH = os.path.join("prediction", "model", "brain_tumor_model.keras")
model = load_model(MODEL_PATH)

CLASS_LABELS = {
    0: "Glioma Tumor",
    1: "Meningioma Tumor",
    2: "Pituitary Tumor",
    3: "No Tumor"
}

def preprocess_image(image, target_size = (224, 224)):
    image = image.resize(target_size).convert("RGB")
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis = 0)
    return image_array

def upload_and_predict(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES["image"]
            image = Image.open(uploaded_image)

            processed_image = preprocess_image(image)

            predictions = model.predict(processed_image)
            predicted_class = np.argmax(predictions)
            confidence = predictions[0][predicted_class]

            return JsonResponse({
                "predicted_class": CLASS_LABELS[predicted_class],
                "confidence": float(confidence)
            })
        
    else:
        form = ImageUploadForm()

    return render(
        request,
        "upload_and_predict.html",
        {"form": form}
    )

def home(request):
    return render(request, "home.html")