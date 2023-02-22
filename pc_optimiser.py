import tkinter as tk
import os

def optimize_pc():
    # Disable visual effects
    os.system("SystemPropertiesPerformance.exe /NOAPPEARANCE")

    # Disable startup programs
    os.system("taskkill /IM explorer.exe /F")
    os.system("start explorer.exe")

    # Clear temporary files
    os.system("runDll32.exe inetcpl.cpl,ClearMyTracksByProcess 8")

    # Defragment hard drive
    os.system("defrag %SystemDrive% /U")

def run_optimization():
    optimize_pc()
    result_text.config(text="PC Optimization completed successfully")

root = tk.Tk()
root.title("PC Optimizer")
root.geometry("300x100")

optimize_button = tk.Button(root, text="Optimize PC", command=run_optimization)
optimize_button.pack()

result_text = tk.Label(root, text="")
result_text.pack()

root.mainloop()