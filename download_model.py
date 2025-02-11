import gdown  

url = "https://drive.google.com/drive/folders/1VzubGg1UjkcT8_ky2_W9hQS_scAAUFLb"  
output = "model/gender_model.onnx"  

gdown.download(url, output, quiet=False)
