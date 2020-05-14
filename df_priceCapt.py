import pandas as pd
from price_captTerlaris import terlaris_array
from price_captTerbaru import terbaru_array
from price_captRelevansi import relevansi_array
import tkinter as tk
from tkinter import filedialog




price_capt_df = pd.DataFrame({
    'terlaris' : terlaris_array,
    'terbaru' : terbaru_array,
    'relevansi': relevansi_array
})

count1= price_capt_df['terlaris'].value_counts()
count2= price_capt_df['terbaru'].value_counts()
count3= price_capt_df['relevansi'].value_counts()

count_df =pd.DataFrame({
    'terlaris' : count1,
    'terbaru': count2,
    'relevansi':count3
}).fillna(0)
count_df['sumary'] = count_df.sum(axis=1)

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()


def exportCSV():
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    count_df.to_csv(export_file_path, index=True, header=True)


saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()