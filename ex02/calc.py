import tkinter as tk
import tkinter.messagebox as tkm


# 練習３
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get() # 数式の文字列
        res = eval(siki) # 数式文字列の評価
        entry.delete(0, tk.END) # 表示文字列の削除
        entry.insert(tk.END, res) # 結果の挿入
    else: # 「=」以外のボタン字
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        # 練習６
        entry.insert(tk.END, num)

    
# 練習１
root = tk.Tk()
root.geometry("1070x600")

# 練習４
entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)

# 練習２
r, c = 1, 0
i = -2
x = 0
operators = ["%","^","c","/"]
operators2 = ["*","-","+"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
c = 0
r = 2
for num in range(9, -1, -1):
    #普通の電卓の並び変える
    # if num == 10:
    #     operators = ["%","^","c","/","*", "-","+"]
    #     for ope in operators[0:4]:
    #         button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    #         button.grid(row=r, column=c)
    #         button.bind("<1>", button_click)
    #         c += 1
    #         if c%4 == 0:
    #             r += 1
    #             c = 0
    # else:
    #     if c == 3:
    #         button = tk.Button(root, text=f"{operators2[x]}", width=4, height=2, font=("", 30))
    #         button.grid(row=r, column=c)
    #         button.bind("<1>", button_click)
    #         x += 1
    #         r += 1
    #         c = 0
    #     else:
    if num == 8 or num ==5 or num ==2:
        i = 0
    elif num ==  9 or num == 6 or num == 3:
        i = -2
    elif num ==  7 or num == 4 or num == 1:
        i = 2
    elif num == 0:
        i = 0
    button = tk.Button(root, text=f"{num + i}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
    

#練習５
operators3 = ["="]
for ope3 in operators3:
    button = tk.Button(root, text=f"{ope3}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
c = 3
r = 2
for ope2 in operators2:
    button = tk.Button(root, text=f"{ope2}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    r += 1

root.mainloop()