import os
suffix={".jpg",".jpeg",".png",".gif",".bmp"}
path=input("请输入文件路径:")
if os.path.isdir(path):
    print("这是文件夹，开始遍历里边内容")
    document=os.listdir(path)
    count=1
    for i in document:
        full_path=os.path.join(path,i)
        if os.path.isfile(full_path):
            d_suffix = os.path.splitext(i)[1]
            if d_suffix in suffix:
                print(f"文件：{i}是图片")
                new_name = f"img_{count:03d}{d_suffix}"
                new_fullpath = os.path.join(path, new_name)
                os.rename(full_path, new_fullpath)
                print(f"重命名：{i} → {new_name}")
                count += 1
            else:
                print(f"文件：{i}不是图片")
else:
    print("这不是文件夹")