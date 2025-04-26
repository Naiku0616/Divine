import tkinter as tk
from tkinter import font
import random

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("灵签占卜")
        self.root.geometry("500x600")
        self.root.configure(bg="#0F1B2D")
        self.root.attributes('-alpha', 1)  # 初始化窗口透明度

        # 动态效果状态变量
        self.shaking = False
        self.current_alpha = 0
        self.particles = []

        # 字体配置（带异常处理）
        try:
            self.title_font = font.Font(family="Microsoft YaHei", size=24, weight="bold")
            self.button_font = font.Font(family="Microsoft YaHei", size=16)
            self.result_font = font.Font(family="LiSu", size=20, weight="bold")
        except:
            self.title_font = font.Font(size=24, weight="bold")
            self.button_font = font.Font(size=16)
            self.result_font = font.Font(size=20, weight="bold")

        # 主容器
        self.main_frame = tk.Frame(root, bg="#FFF5E4")
        self.main_frame.pack(expand=True, fill="both", padx=25, pady=25)

        # 星空背景
        self.star_canvas = tk.Canvas(self.main_frame, bg="#0F1B2D", highlightthickness=0)
        self.star_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self._create_starry_sky()

        # 界面元素初始化
        self._create_widgets()
        self._animate_stars()

    def _create_widgets(self):
        """创建界面组件"""
        # 标题
        self.title_label = tk.Label(self.main_frame,
                                  text="✨ 灵 签 占 卜 ✨",
                                  font=self.title_font,
                                  bg="#FFF5E4",
                                  fg="#C53D43")
        self.title_label.pack(pady=(30, 20))

        # 签筒绘制
        self.canvas = tk.Canvas(self.main_frame,
                               width=200,
                               height=200,
                               bg="#FFF5E4",
                               highlightthickness=0)
        self.canvas.pack(pady=20)
        self._draw_bamboo()

        # 光效初始化
        self.glow = self.canvas.create_oval(50,50,150,150,
                                          fill="yellow",
                                          state="hidden",
                                          stipple="gray50")

        # 抽签按钮
        self.draw_button = tk.Button(self.main_frame,
                                    text="点此求签",
                                    font=self.button_font,
                                    command=self.draw_lot,
                                    bg="#FFA07A",
                                    fg="white",
                                    activebackground="#FF7F50",
                                    relief="flat",
                                    borderwidth=0)
        self.draw_button.pack(pady=20)

        # 结果展示框
        self.result_frame = tk.Frame(self.main_frame,
                                    bg="#FFFFFF",
                                    relief="groove",
                                    borderwidth=3)
        self.result_frame.pack(pady=10, ipadx=20, ipady=15)

        self.result_label = tk.Label(self.result_frame,
                                    text="",
                                    font=self.result_font,
                                    bg="#FFFFFF",
                                    fg="#4B0082",
                                    wraplength=300)
        self.result_label.pack()

        # 动画标签
        self.anim_label = tk.Label(self.main_frame,
                                 text="",
                                 font=self.title_font,
                                 bg="#FFF5E4")
        self.anim_label.place(relx=0.5, rely=0.5, anchor="center")

    def _draw_bamboo(self):
        """绘制签筒图形"""
        # 筒身
        self.canvas.create_rectangle(95, 50, 105, 150, fill="#8B4513", tags="bamboo")
        # 筒口
        self.canvas.create_polygon(80,50, 120,50, 130,70, 70,70, fill="#DEB887", tags="bamboo")
        # 底座
        self.canvas.create_oval(80, 150, 120, 190, fill="#6B8E23", tags="bamboo")

    def _create_starry_sky(self):
        """创建星空粒子"""
        for _ in range(50):
            x = random.randint(0, 450)
            y = random.randint(0, 550)
            size = random.randint(1, 3)
            star = self.star_canvas.create_oval(x,y,x+size,y+size,
                                               fill="white",
                                               tags="star")
            self.star_canvas.itemconfig(star, state="hidden")

    def _animate_stars(self):
        """星空闪烁动画"""
        stars = self.star_canvas.find_withtag("star")
        for star in stars:
            if random.random() < 0.1:
                self.star_canvas.itemconfig(star, state="normal")
                self.star_canvas.after(100,
                    lambda s=star: self.star_canvas.itemconfig(s, state="hidden"))
        self.root.after(500, self._animate_stars)

    def _bamboo_shake(self, count=0):
        """签筒摇晃动画"""
        if count < 8:
            offset = 5 if count%2 == 0 else -5
            self.canvas.move("bamboo", offset, 0)
            self.root.after(50, lambda: self._bamboo_shake(count+1))
        else:
            self.shaking = False
            self.canvas.update_idletasks()  # 强制更新布局

    def _particle_effect(self):
        """修正粒子效果坐标"""
        # 动态获取签筒中心坐标
        bamboo_coords = self.canvas.bbox("bamboo")
        x_center = (bamboo_coords[0] + bamboo_coords[2]) // 2
        y_center = (bamboo_coords[1] + bamboo_coords[3]) // 2
        
        # 转换为全局坐标
        canvas_x = self.canvas.winfo_x()
        canvas_y = self.canvas.winfo_y()
        x = canvas_x + x_center
        y = canvas_y + y_center

        colors = ["#FFD700", "#FF4500", "#FF1493"]
        for _ in range(15):
            dx = random.randint(-5,5)
            dy = random.randint(-10,0)
            size = random.randint(5,10)
            particle = self.star_canvas.create_oval(x,y,x+size,y+size,
                                                  fill=random.choice(colors),
                                                  tags="particle")
            self.particles.append((particle, dx, dy))
        self._update_particles()

    def _update_particles(self):
        """粒子运动更新"""
        for i, (particle, dx, dy) in enumerate(self.particles):
            self.star_canvas.move(particle, dx, dy)
            dy += 0.5  # 重力效果
            if self.star_canvas.coords(particle)[1] > 550:
                self.star_canvas.delete(particle)
                del self.particles[i]
            else:
                self.particles[i] = (particle, dx, dy)
        if self.particles:
            self.root.after(30, self._update_particles)

    def _text_animation(self, text, color):
        """修正文字渐现动画"""
        if self.current_alpha < 1:
            self.current_alpha += 0.1
            self.anim_label.config(text=text, fg=color)
            self.anim_label.place(relx=0.5, rely=0.5, anchor="center")
            # 使用标签自身透明度（需要tkinter 8.6+）
            try:
                self.anim_label.config(fg=color + f"{int(self.current_alpha*255):02x}")
            except:
                self.root.attributes('-alpha', self.current_alpha)
            self.root.after(30, lambda: self._text_animation(text, color))
        else:
            self.current_alpha = 0
            self.root.attributes('-alpha', 1)
            self.anim_label.config(text="")

    def draw_lot(self):
        """抽签核心逻辑"""
        if self.shaking:
            return

        self.shaking = True
        self.root.update_idletasks()  # 强制界面更新
        
        lots = [
            ("大吉", "#FF0000", "好运连连，诸事顺遂！"),
            ("中吉", "#FF8C00", "稳步前行，心想事成！"),
            ("小吉", "#FFD700", "小有收获，更上层楼！"),
            ("末吉", "#32CD32", "脚踏实地，终有所获！"),
            ("凶", "#4169E1", "韬光养晦，静待时机！"),
            ("大凶", "#800080", "破而后立，否极泰来！")
        ]
        level, color, text = random.choice(lots)

        # 执行动画序列
        self._bamboo_shake()
        self.canvas.itemconfig(self.glow, state="normal")
        self._particle_effect()
        self._text_animation(level, color)

        # 更新结果
        self.result_frame.config(highlightbackground=color, highlightthickness=2)
        self.result_label.config(text=f"{level}\n{text}", fg=color)
        self.draw_button.config(text="再抽一签")

        # 重置状态
        self.canvas.after(1000, lambda: self.canvas.itemconfig(self.glow, state="hidden"))
        self.shaking = False

if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()