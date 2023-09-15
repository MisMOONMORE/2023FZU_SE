import tkinter as tk

def select_library():
    selected_library = library_var.get()
    print("Selected Library:", selected_library)

def apply_filter():
    selected_difficulty = difficulty_var.get()
    filter_text = filter_entry.get()
    print("Selected Difficulty:", selected_difficulty)
    print("Filter Text:", filter_text)

root = tk.Tk()
root.geometry('560x280+100+100')

root.title('洛谷题库查询')

# 创建标签
label = tk.Label(root, text="所属题库")
label.grid(row=8, column=2)

# 创建题库选项按钮
libraries = ["洛谷", "主题库", "入门与面试", "CodeForces", "SPOJ"]
library_var = tk.StringVar()

button_frame = tk.Frame(root)  # 创建一个框架用于容纳按钮

for i, library in enumerate(libraries):
    radio_button = tk.Radiobutton(button_frame, text=library, variable=library_var, value=library)
    radio_button.grid(row=0, column=i+5)  # 纵向排列按钮

button_frame.grid(row=8, column=6)

# 题目难度下拉选择菜单
difficulty_label = tk.Label(root, text="题目难度")
difficulty_label.grid(row=12, column=2)

difficulties = ["暂无评定", "入门", "普及-", "普及/提高-", "普及+/提高", "提高+/省选-", "省选/NOI-", "NOI/NOI+/CTSC"]
difficulty_var = tk.StringVar()
difficulty_dropdown = tk.OptionMenu(root, difficulty_var, *difficulties)
difficulty_dropdown.grid(row=12, column=6)

# 输入框
filter_label = tk.Label(root, text="筛选条件")
filter_label.grid(row=18, column=2)

filter_entry = tk.Entry(root, width=20)
filter_entry.insert(tk.END, "算法/来源/时间/状态")
filter_entry.grid(row=18, column=6)

# 创建确认按钮
button = tk.Button(root, text="确认", command=select_library)
button.grid(row=8, column=8)

# 创建应用筛选按钮
apply_button = tk.Button(root, text="应用", command=apply_filter)
apply_button.grid(row=18, column=8)

#输入框2
filter_label = tk.Label(root, text="关键字")
filter_label.grid(row=22, column=2)

filter_entry = tk.Entry(root, width=20)
filter_entry.insert(tk.END, "算法、标题或题目编号")
filter_entry.grid(row=22, column=6)

apply_button = tk.Button(root, text="搜索", command=apply_filter)
apply_button.grid(row=22, column=8)



root.mainloop()