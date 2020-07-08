import tkinter
from tkinter import *
import tkinter.messagebox as messagebox
import cv2 as cv
from PIL import Image, ImageTk
import base64
from aip import AipFace
import os


# 全局变量
img_gif = None


class FaceContrast(object):
    """clock_in_class"""

    # APPID AK SK
    APP_ID = '20687731'
    API_KEY = 'pXuzuyEU0tnjwpKmNBpFaNQc'
    SECRET_KEY = 'VRfVVGtlSpl1Z0UhuRgQSzvCvNSSmW7A'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    # 摄像机设置: 0是代表摄像头编号，只有一个的话默认为0
    capture = cv.VideoCapture(0)

    # 退出标志
    break_flag = False

    # 主窗口
    root = tkinter.Tk()

    # 当前人脸
    current_face = None

    def __init__(self):

        # 获取人脸注册库,文件读取
        self.face_database = self.get_face_database(face_dir='face_database')

        self.main_frame_init()

        self.page_arrange()
        pass

    def main_frame_init(self):
        """
        主窗口初始化
        :return:
        """
        # 给主窗口设置标题内容
        self.root.title("打卡签到系统")

        self.root.iconbitmap("hz.ico")

        # 设置窗口的大小宽x高+偏移量
        self.root.geometry('630x350+500+200')

        # 防止用户调整尺寸
        self.root.resizable(0, 0)

        # 按esc键退出程序
        self.root.bind('<Escape>', lambda e: self.on_closing())

        # 关闭按钮
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        pass

    def get_face_database(self,face_dir):
        face_list = []
        for root, dirs, files in os.walk(face_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.gif':
                    face_list.append(file[:-4])
        return face_list

    def page_arrange(self):
        """
        页面布局
        :return:
        """
        # 声明全局变量
        global img_gif

        # 创建人脸显示区
        img_gif = tkinter.PhotoImage(file='person.gif')
        self.label_img = tkinter.Label(self.root, image=img_gif, width=300, height=300)
        self.label_img.place(x=10, y=5)

        # 创建一个输入框,并设置尺寸
        self.name_id_input = tkinter.Entry(self.root, width=20)
        self.name_id_input.insert(index=0, string="请输入姓名_工号")
        self.name_id_input.place(x=20, y=315, width=150, height=30)

        # 创建一个确认结果的按钮
        confirm_button = tkinter.Button(self.root, command=self.find_face_image, text="确认")
        confirm_button.place(x=250, y=315, width=50, height=30)

        # 创建一个打卡的按钮
        click_button = tkinter.Button(self.root, command=self.get_compare_result, text="打卡")
        click_button.place(x=450, y=315, width=50, height=30)
        pass

    def find_face_image(self):
        """
        根据name_id查找人脸图像
        :return:
        """
        # 声明全局变量
        global img_gif

        # 为了避免非法值,导致程序崩溃,有兴趣可以用正则写一下具体的规则,我为了便于新手理解,减少代码量,就直接粗放的过滤了
        self.name_id = self.name_id_input.get()

        # 刷新人脸
        if self.name_id in self.face_database:
            self.current_face = self.name_id
            self.label_img.destroy()
            img_gif = tkinter.PhotoImage(file=f'face_database\\{self.name_id}.gif')
            self.label_img = tkinter.Label(self.root, image=img_gif,width=300,height=300)
            # 进行布局
            self.label_img.place(x=10,y=5)

        else:
            self.label_img.destroy()
            img_gif = tkinter.PhotoImage(file='no_person.gif')
            self.label_img = tkinter.Label(self.root, image=img_gif,width=300,height=300)
            # 进行布局
            self.label_img.place(x=10,y=5)

        self.name_id_input.delete(0,30)
        self.name_id_input.insert(index=0,string="请输入姓名_学号")

    def tk_image(self):
        ref, frame = self.capture.read()
        cvimage = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        pilImage = Image.fromarray(cvimage)
        pilImage = pilImage.resize((300, 300), Image.ANTIALIAS)
        tkImage = ImageTk.PhotoImage(image=pilImage)
        return tkImage

    def save_picture(self):
        ref, frame = self.capture.read()
        cv.imwrite(r"./save.jpg", frame)
        im = Image.open('yaoqiang_18516730037.jpg')
        im.save('yaoqiang_18516730037.gif')

    def get_face_picture(self):
        """
        调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
        :return:
        """
        # 控件定义
        self.canvas = Canvas(self.root, bg='white', width=300, height=300)  # 绘制画布

        # 控件位置设置
        self.canvas.place(x=320, y=5)

        pass

    def get_frame(self):
        ref, frame = self.capture.read()
        cv.imwrite(r"./save.jpg", frame)

    def close_camera(self):
        self.capture.release()

    def get_compare_result(self):

        # 保存照片
        self.save_picture()

        # 人脸对比结果
        result = self.client.match([
            {
                'image': bytes.decode(base64.b64encode(open("save.jpg", 'rb').read())),
                'image_type': 'BASE64',
                "face_type": "LIVE",
                "quality_control": None,
                "liveness_control": "LOW"
            },
            {
                'image': bytes.decode(base64.b64encode(open(f'face_database\\{self.current_face}.jpg', 'rb').read())),
                'image_type': 'BASE64',
                "face_type": "LIVE",
                "quality_control": None,
                "liveness_control": "LOW"
            }
        ])

        # 对比结果分值推荐为高于80分
        if result["result"]["score"] >= 80:
            messagebox.askokcancel('消息框', f'考勤打卡成功\n相似度:{round(result["result"]["score"],2)}%')
        else:
            messagebox.askokcancel('消息框', "非本人打卡，请确认信息再来一次！")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.break_flag = True
            self.root.destroy()

    # def get_liveness_result(self):
    #     """活体校验"""
    #
    #     result = self.client.faceverify([
    #         {
    #             'image': bytes.decode(base64.b64encode(open('save.jpg', 'rb').read())),
    #             'image_type': 'BASE64',
    #         }
    #     ])
    #
    #     return result["result"]["face_liveness"] >= 0.995
    #     pass


def main():

    # 初始化对象
    fc = FaceContrast()

    # 开启摄像机
    fc.get_face_picture()

    while True:
        if fc.break_flag:
            break
        picture = fc.tk_image()
        fc.canvas.create_image(0, 0, anchor='nw', image=picture)
        fc.root.update()
        fc.root.after(100)
    pass


if __name__ == "__main__":
    main()
