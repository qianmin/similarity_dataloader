# similarity_dataloader
空地协同数据读取，作为孪生网络输入


data_folder文件夹
```
第一级：大类（人，车，男人，女人）
第二级：air,ground（不同的视角）
第三级：man1，man2，man3
里面都是xxx.jpg,xxx.png
```

多级文件夹.py
```
不要管什么文件夹有几层，不管里面什么名字，不管里面有什么其他东西
所有的图片文件作为一个列表（保存了图片位置信息）
```
