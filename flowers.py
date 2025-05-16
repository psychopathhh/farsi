import kagglehub

# Download latest version
path = kagglehub.dataset_download("aksha05/flower-image-dataset")

print("Path to dataset files:", path)