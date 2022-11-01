import os
import glob

# path = "static\\img\\model"

# obj = os.scandir(path=path)
 
# # List all files and directories in the specified path
# print("Files and Directories in '% s':" %path)
# for entry in obj:
#     if entry.is_dir():
#         print(entry.name)
#         new = path + '\\'+entry.name #get path for the model folder
#         obj = os.scandir(path=new) #use the path for the model folder 
#         for entry in obj: #this entry is for the specific model folder
#             if entry.is_dir() or entry.is_file():
#                 print(entry.path)#image name 

# for file in glob.glob(path + '/*[0-9].*'):
#     print(file)

# path = "static\\img\\"
# new=path + 'model'
# models_name=[]
# path_list=[]
# obj = os.scandir(path=new)

# # List all files and directories in the specified path
# for entry in obj:
#         if entry.is_dir():
#             models_name.append(entry.name)#gets model name from the folder and adds its to the list of models
#             image_path= os.listdir(path=entry.path)
#             path_list.append(image_path[0])
        # new=entry.path
        # first_image_path= os.scandir(path=new)
        # for entry in first_image_path:
        #         if entry.is_dir():
        #                 print(entry.name)


# print(path)
word='Greg'
path= "static\\img\\model\\"
new = path + word #get path for the specific model folder
obj = os.scandir(path=new) #use the path for the model folder 
image_path=[]
for entry in obj: #this entry is for the specific model folder
        if entry.is_dir() or entry.is_file():
                # print(entry.name)#image name
                image_path.append(entry.name) 
print(image_path)