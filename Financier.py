import tkinter as tk
import Assets.PythonScripts.FinancierControls as FC

if __name__ == "__main__":
    root = tk.Tk()
    # Создаём экземпляр класса Контроллера
    fc = FC.FinancierControls(root)

    # Основное окно
    root.title("Financier ")
    root.config(bg="black")
    root.resizable(False, False)
    w = root.winfo_screenwidth()  # ширина экрана
    h = root.winfo_screenheight()  # высота экрана
    w = str(int((w - 1280) / 2))
    h = str(int((h - 720) / 2))
    geo = "1280x720+" + w + "+" + h
    root.geometry(geo)
    root.mainloop()
