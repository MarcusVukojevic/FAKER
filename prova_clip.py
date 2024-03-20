import clip
from PIL import Image
import torch


device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)



image_path = "vecchia.png"
image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)


with torch.no_grad():
    image_features = model.encode_image(image)

print(len(image_features[0]))
# Assuming image_features1 and image_features2 are the feature vectors for two images
#cosine_similarity = torch.nn.functional.cosine_similarity(image_features1, image_features2)
#print("Cosine Similarity:", cosine_similarity.item())
