from PIL import Image, ImageTk, ImageFilter
import tkinter as tk

def create_acrylic_image(width, height, base_color, alpha=0.7, blur_radius=15):
    # 创建基础颜色图像
    base = Image.new('RGBA', (width, height), base_color)
    
    # 创建噪声图像
    noise = Image.effect_noise((width, height), 10)
    noise = noise.convert('RGBA')
    
    # 将噪声图像与基础颜色图像混合
    blended = Image.blend(base, noise, 0.1)
    
    # 应用模糊效果
    blurred = blended.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # 调整透明度
    blurred.putalpha(int(255 * alpha))
    
    return ImageTk.PhotoImage(blurred)

class AcrylicFrame(tk.Frame):
    def __init__(self, master, bg_color, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bg_color = bg_color
        self.bind('<Configure>', self.on_resize)
        self.acrylic_image = None
        self.acrylic_label = None

    def on_resize(self, event):
        if self.acrylic_label:
            self.acrylic_label.destroy()
        
        self.acrylic_image = create_acrylic_image(event.width, event.height, self.bg_color)
        self.acrylic_label = tk.Label(self, image=self.acrylic_image)
        self.acrylic_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # 将所有子组件提升到亚克力背景之上
        for child in self.winfo_children():
            if child != self.acrylic_label:
                child.lift()