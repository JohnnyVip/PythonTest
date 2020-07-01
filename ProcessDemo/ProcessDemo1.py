# 根据进程池和进程间通信实现文件拷贝

from multiprocessing import Pool, Manager
import os


# 完成拷贝文件
def copyFile(fileName, oldFilesName, newFilesName, queue):
    "拷贝文件函数"
    #	print('拷贝文件名字：%s'%fileName)
    queue.put(fileName)
    fr = open(oldFilesName + '/' + fileName)
    fw = open(newFilesName + '/' + fileName, 'w')

    content = fr.read()
    fw.write(content)
    #	print('----------over!-------------')
    fr.close()
    fw.close()


#	queue.put(fileName)  #这条语句放在这总会导致最后完成的那个子进程的文件无法存入队列，最终导致 程序实际上已经完成，但是不能终止！why?

# 由于我在linux中运行，加之以前的一些文件因为某些操作的不当，产生了.swap和.idea文件，利用一个循环实现过滤,如果有其他的干扰文件也可以用同样的方法过滤
def solute(temp_data):
    temps = []
    for temp in temp_data:
        if (temp.split('.')[-1] == "swap" or
                temp.split('.')[-1] == "idea"):
            continue
        else:
            temps.append(temp)
    return temps


def main():
    # 1、提示用户输入要拷贝的文件
    oldFilesName = input('请输入要拷贝的文件夹的名字：')

    # 2、创建文件夹，存放被拷贝的文件
    newFilesName = oldFilesName + '_cp'
    # print('新文件夹的名字：%s'%newFilesName)
    os.mkdir(newFilesName)

    # 2、获取元文件中的所有文件名字
    fileNames = os.listdir(oldFilesName)
    #	print(fileNames)
    # 过滤文件
    fileName = solute(fileNames)
    #	print(fileNames)
    # 4、使用多进程的方式copy原文件夹中的数据到新文件夹中
    pool = Pool(5)
    queue = Manager().Queue()
    for fileName in fileNames:
        pool.apply_async(copyFile, args=(fileName, oldFilesName, newFilesName, queue))

    pool.close()
    pool.join()

    count = 0
    allCounts = len(fileNames)
    #	print(allCounts)
    while True:  # 用主进程来显示拷贝进度
        name_t = queue.get()
        #		print(name_t)
        count += 1
        #		print('count:%s'%count)
        #		print('-----------------------------------')
        print('\r拷贝进度：%.2f%%' % ((count / allCounts) * 100), end='')
        if count == allCounts:
            print('\n--------over---------')
            break


if __name__ == '__main__':
    main()