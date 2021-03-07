import os
import cv2
import random
import time

#遍历文件夹
img_list=[]

#init_function
def get_all_img_path(rootDir):
    #遍历根目录
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root,file)
            ####process
            file_type=file_name[-3:]
            img_type=['jpg','png','jpeg']
            if(file_type in img_type):
                img_list.append(file_name.replace("\\", "/"))
                # tmp_img=cv2.imread(file_name)
                # cv2.imshow('cnm',tmp_img)
                # cv2.waitKey(0)
            ####process
def same_pair():
    ##先随便选一张图片
    n=random.randint(0,len(img_list)-1)
    str1=img_list[n]
    print('str1:',str1)
    ##换个视角
    #先得到另一个视角的所有图片
    if('ground' in str1):
        str2=str1.replace('ground','air')
    if ('air' in str1):
        str2 = str1.replace('air', 'ground')
    #最后一个/分割
    str2_path=str2.rsplit("/", 1)[0]
    # print('str2_path:',str2_path)

    #获取str2文件夹内所有图片位置列表
    new_list=[]
    for i in range(len(img_list)):
        tmp_path=img_list[i].rsplit("/", 1)[0]
        if(tmp_path==str2_path):
            new_list.append(img_list[i])
    #str2文件夹内随便选一个
    n2=random.randint(0,len(new_list)-1)
    str2=new_list[n2]
    print('str2',str2)
    #return str1,str2
def diff_pair():
    ##先随便选一张图片
    n1=random.randint(0,len(img_list)-1)
    str1=img_list[n1]
    print('str1:',str1)
    class1 = str1.rsplit("/", 3)[0]
    vision1 = str1.rsplit("/", 3)[1]
    id1 = str1.rsplit("/", 3)[2]

    ##再随便选一张图片
    str2=0
    while 1:
        tmp_n = random.randint(0, len(img_list) - 1)
        str2 = img_list[tmp_n]
        ###
        class2=str2.rsplit("/", 3)[0]
        vision2 = str2.rsplit("/", 3)[1]
        id2 = str2.rsplit("/", 3)[2]
        if (class1!=class2):
            break
        if (class1 == class2):
            if(id1!=id2):
                break
        ###
    print('str2',str2)
    # return str1,str2
t_init1=time.time()
get_all_img_path('..\\data_folder')
t_init2=time.time()

print('img_list',img_list)


t1=time.time()
print(' ')
print('same_pair')
same_pair()
print(' ')
print('diff_pair')
diff_pair()
t2=time.time()



print('init used:',t_init2-t_init1)
print('time used:',t2-t1)



