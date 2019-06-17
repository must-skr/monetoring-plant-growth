import glob
import os, os.path
import cv2
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pickle
import numpy as np
import matplotlib.pyplot as plt




TestFolder ='E:/Train/test'
FP = 'E:/Train/Demo'
def SaveMetaData(DataList):
    TypeName = str.split(DataList[0],'_')
    TypeName = TypeName[0]
    FileName = 'MetaData/'+TypeName+'.txt'
    f = open(FileName, "w+")
    for i in range(0,len(DataList)):
        f.write(DataList[i]+'\n')
    f.close()
def ReadImages(FolderPath):
    ImagesList = []
    FolderName =[]
    for root, dirs, files in os.walk(FolderPath):
        for name in dirs:
            path = FolderPath + '/' + name + '/*.jpg'
            FolderOfImage = []
            FolderName.append(name)
            for f in glob.glob(path):
                img = cv2.imread(f)
                FolderOfImage.append(img)

            ImagesList.append(FolderOfImage)
    return ImagesList,FolderName
def TrainDataSet(ListOfImages):
    ImagesFeatures = []
    Label=[]
    print('Extract Features')
    for i in range (0,len(ListOfImages)):
        FolderObject = ListOfImages[i]
       #print(len(FolderObject))
        for j in range(0,len(FolderObject)):
            img_rz = cv2.resize(FolderObject[j], (64, 128))
            hog = cv2.HOGDescriptor()
            h = hog.compute(img_rz)
            ImagesFeatures.append(h)
            Label.append(i)
    print('Features Extracted succesfully')
    return ImagesFeatures , Label
def CreateModel(ImagesFeatures ,Label):
    ft_x = np.array(ImagesFeatures, np.float32)
    ft_y = np.array(Label, np.int32)
    svm = cv2.ml.SVM_create()
    svm.setType(cv2.ml.SVM_C_SVC)
    svm.setKernel(cv2.ml.SVM_RBF)
    svm.setGamma(0.1)
    print(Label)
    svm.train(ft_x, cv2.ml.ROW_SAMPLE, ft_y)
    svm.save('SVM_Gender_Model_Apple.dat')
    print('Model created using SVM')
def TestModel(TestFolderPath,ModelName):
    Image = ReadImages(TestFolderPath)
    Data = TrainDataSet(Image[0])
    Label = Data[1]
    Images = Data[0]
    count =0
    for i in range(0 ,len(Data[0])):

        ft_x = np.array([Images[i]], np.float32)
        svm = cv2.ml.SVM_load(ModelName)
        response = svm.predict(ft_x)
        num = response[1][0]
        if(num == Label[i]):
            count+=1
    print(Label)
    print('accuracy = ',count/len(Data[0]))

def test_single_image(image_path,plant_type):
    img=cv2.imread(image_path)
    if(len(img)!= 0):
        im=cv2.resize(img,(64, 128))
        hog = cv2.HOGDescriptor()
        h = hog.compute(im)
        model_name=get_model(plant_type)
        ft_x = np.array([im], np.float32)
        svm = cv2.ml.SVM_load(model_name)
        response = svm.predict(ft_x)
        num = response[1][0]
        return get_metadata(plant_type,num)
    else:
        return 'Error:No Image found in this path :'+image_path


def get_metadata(P_type,predict):
    file_path='MetaData/'+P_type+'.txt'
    file = open(file_path, 'r')
    content = file.read()
    # print(content)
    filelines = content.split()
    list_Names=[]
    for i in  range(0,len(filelines)):
        list_Names.append(filelines[i])

    index=predict[0]
    return list_Names[int(index)]




def get_model(P_type):
    model_name='SVM_Gender_Model_'+P_type+'.dat'
    return model_name

IL = ReadImages(FP)
print('len of Folders = ',len(IL[0]))
SaveMetaData(IL[1])

Data =TrainDataSet(IL[0])

CreateModel(Data[0],Data[1])

TestModel(TestFolder,'SVM_Gender_Model_Apple.dat')

