import os
from PIL import Image


# for root, dirs, files in os.walk("LEVIR-CD"):
#     for file in files:
#         if file.endswith(".png"):
#             img = Image.open(os.path.join(root, file))
#             for i in range(4):
#                 for j in range(4):
#                     crop = img.crop((i*256, j*256, (i+1)*256, (j+1)*256))
#                     crop.save(os.path.join(root, file[:-4] + "_" + str(i*4+j) + ".png"))
#             os.remove(os.path.join(root, file))

print("Now rejoining the images from 256x256 to 1024x1024...")
for root, dirs, files in os.walk("samples/predict"):
    for file in files:
        if file.endswith("_0.png"):
            img = Image.open(os.path.join(root, file))
            for i in range(1, 16):
                img.paste(Image.open(os.path.join(root, file[:-5] + str(i) + ".png")), (i%4*256, i//4*256))
            img.save(os.path.join(root, file[:-5] + ".png"))
            for i in range(16):
                os.remove(os.path.join(root, file[:-5] + str(i) + ".png"))