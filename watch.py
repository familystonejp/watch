import tkinter as tk
import datetime
import time  # ← これを追加
import threading

# メインウィンドウの作成
root = tk.Tk()
root.title('countdown')
root.geometry('1922x1082')
root.attributes('-fullscreen', True)

# キャンバス作成
canvas = tk.Canvas(root, width=1922, height=1082, background='black')
canvas.pack()

# 初期テキストを一度だけ作成し、そのIDを保持
text_id = canvas.create_text(960, 520, text="", font=('Arial Black', 300), fill='white')

# 時刻更新関数
def update_time():
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        canvas.itemconfig(text_id, text=now)  # テキストだけ更新
        time.sleep(1)

# スレッドで時刻更新
thread = threading.Thread(target=update_time, daemon=True)
thread.start()

# Esc キーで終了する関数
def on_esc(event):
    root.destroy()

# イベントバインド
root.bind("<Escape>", on_esc)

# メインループ
root.mainloop()
