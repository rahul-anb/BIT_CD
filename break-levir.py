import os
from PIL import Image
from demo import test
from multiprocessing import freeze_support
import cv2


if __name__=="__main__":
    freeze_support()
    images_read = []
    images_readB=[]
    dir_path = "breakimages/A"

    for itr in range(len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])):
        open('samples\list\demo.txt', 'w').close()
        f = open('samples\list\demo.txt','a')
        # blank = Image.open("D:/Github/BIT_CD/samples/blank.png")
        # blank = cv2.imread("D:/Github/BIT_CD/samples/blank.png")


        # Clear both folders
        # import glob
        # files = glob.glob('D:/Github/BIT_CD/samples/A')
        # for f in files:
        #     os.remove(f)

        
        for root, dirs, files in os.walk("breakimages/A"):
            for file in files:
                if file.endswith(".png") and file in images_read:
                    continue
                if file.endswith(".png"):
                    img = Image.open(os.path.join(root, file))
                    img = img.resize((512,512))
                    for i in range(2):
                        for j in range(2):
                            blank = Image.open("D:/Github/BIT_CD/samples/blank.png")
                            crop = img.crop((i*256, j*256, (i+1)*256, (j+1)*256))
                            crop.save("D:/Github/BIT_CD/samples/A/"+ file[:-4] + "_" + str(i*4+j) + ".png")
                            f.write(file[:-4] + "_" + str(i*4+j) + ".png\n")
                            blank.save("D:/Github/BIT_CD/samples/label/"+file[:-4] + "_" + str(i*4+j) + ".png")
                            # cv2.imwrite("D:\Github\BIT_CD\samples\label",file[:-4] + "_" + str(i*4+j) + ".png",blank)
                    #os.remove(os.path.join(root, file))
                    
                    images_read.append(file)
                    break
            break
        f.close()
        lastfile = ''
        for root, dirs, files in os.walk("breakimages/B"):
            for file in files:
                if file.endswith(".png") and file in images_readB:
                    continue
                if file.endswith(".png"):
                    img = Image.open(os.path.join(root, file))
                    img = img.resize((512,512))
                    for i in range(2):
                        for j in range(512):
                            crop = img.crop((i*256, j*256, (i+1)*256, (j+1)*256))
                            crop.save("D:/Github/BIT_CD/samples/B/"+file[:-4] + "_" + str(i*4+j) + ".png")
                            lastfile = file
                    #os.remove(os.path.join(root, file))
                    images_readB.append(file)

                    break
            break
                    

        test()
        print("\n\n\nTesting start:")
        imgList=[]
        readfile = open('samples\list\demo.txt','r')
        lines = readfile.readlines()
        readfile.close()
        for line in lines:
            print(line)
            img=cv2.imread("samples/predict/"+line.strip())
            imgList.append(img)

        # for root, dirs, files in os.walk("samples/predict"):
        #     for file in files:
        #         if file.endswith(".png"):
        #             print(file)
        #             img = cv2.imread(os.path.join(root, file))
        #             imgList.append(img)


        # img1 = cv2.vconcat(imgList[:4])
        # img2 = cv2.vconcat(imgList[4:8])
        # img3 = cv2.vconcat(imgList[8:12])
        # img4 = cv2.vconcat(imgList[12:16])
        # img = cv2.hconcat([img1,img2,img3,img4])
        img1 = cv2.vconcat(imgList[:2])
        img2 = cv2.vconcat(imgList[2:4])
        img = cv2.hconcat([img1,img2])
        print(str(itr)+'.png')
        cv2.imwrite(str(itr)+'.png',img) 
        del img
        # del img1,img2,img3,img4
        del img1,img2

# file = open('samples\list\demo.txt','r')
# for each in file:
#     print(each)