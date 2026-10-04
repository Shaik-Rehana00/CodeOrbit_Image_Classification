import torch
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights
from PIL import Image

# Load the pretrained MobileNetV2 model
weights = MobileNet_V2_Weights.DEFAULT
model = mobilenet_v2(weights=weights)
model.eval()

# Get image preprocessing
preprocess = weights.transforms()

# Load the sample image
image = Image.open("sample.jpg").convert("RGB")

# Prepare the image
input_image = preprocess(image).unsqueeze(0)

# Make prediction
with torch.no_grad():
    output = model(input_image)

# Convert output into probabilities
probabilities = torch.nn.functional.softmax(output[0], dim=0)

# Get the predicted class
prediction = probabilities.argmax().item()
label = weights.meta["categories"][prediction]
confidence = probabilities[prediction].item() * 100

print("Predicted class:", label)
print("Confidence:", f"{confidence:.2f}%")