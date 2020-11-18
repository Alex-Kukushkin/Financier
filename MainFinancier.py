import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox as mb
import datetime as dt
from datetime import timedelta
import os.path as ospath
import calendar


# Буферный динамический массив
bufferList = dict()


# Отображение основных окон
class MainWindow(tk.Frame):
    def __init__(self, root):
        """ Инициализация полей класса, картинок и иконок. Переход на страницу ввода пароля"""
        self.__CurrentWindow = 0
        self.__PreviousWindow = 0
        self.__SettingFilter = {'currentPage': 1, 'countPage': 1, 'period': 'AllPeriod', 'beginDate': db.beginDate,
                                'endDate': dt.date(2200, 12, 31)}
        super().__init__(root)

        # Список всех картинок и иконок в проекте
        # Картинки основных окон
        self.zamok_img = tk.PhotoImage(file='ImageGeneral/zamok.gif')
        self.time_img = tk.PhotoImage(file='ImageGeneral/Time.gif')
        self.main_img = tk.PhotoImage(file='ImageGeneral/Main_Paint.gif')
        self.coin_img = tk.PhotoImage(file='ImageGeneral/bitcoins.gif')
        self.shreder_img = tk.PhotoImage(file='ImageGeneral/shreder.gif')
        self.report_img = tk.PhotoImage(file='ImageGeneral/report.gif')

        # Иконки кнопок и значков
        self.arrowDown_img = tk.PhotoImage(file='Icons/arrowDown.gif')
        self.arrowUp_img = tk.PhotoImage(file='Icons/arrowUp.gif')
        self.arrowLeft_img = tk.PhotoImage(file='Icons/arrowLeft.gif')
        self.arrowRight_img = tk.PhotoImage(file='Icons/arrowRight.gif')
        self.arrowGreenLeft_img = tk.PhotoImage(file='Icons/arrowGreenLeft.gif')
        self.arrowRedLeft_img = tk.PhotoImage(file='Icons/arrowRedLeft.gif')
        self.arrowGreenRight_img = tk.PhotoImage(file='Icons/arrowGreenRight.gif')
        self.arrowRedRight_img = tk.PhotoImage(file='Icons/arrowRedRight.gif')
        self.arrowDoubleGreen_img = tk.PhotoImage(file='Icons/arrowGreenDouble.gif')
        self.arrowDoubleRed_img = tk.PhotoImage(file='Icons/arrowRedDouble.gif')
        self.menu_img = tk.PhotoImage(file='Icons/menu_img.gif')
        self.setting_img = tk.PhotoImage(file='Icons/if_Settings3.gif')
        self.baks_img = tk.PhotoImage(file='Icons/baks.gif')
        self.info_img = tk.PhotoImage(file='Icons/info.gif')
        self.exit_img = tk.PhotoImage(file='Icons/CloseExit2.gif')
        self.up_img = tk.PhotoImage(file='Icons/UP.gif')
        self.down_img = tk.PhotoImage(file='Icons/DOWN.gif')
        self.right_img = tk.PhotoImage(file='Icons/Right.gif')
        self.left_img = tk.PhotoImage(file='Icons/Left.gif')
        self.back_img = tk.PhotoImage(file='Icons/back.gif')
        self.forward_img = tk.PhotoImage(file='Icons/Forward.gif')
        self.plus_img = tk.PhotoImage(file='Icons/plus_icon.gif')
        self.green_up_img = tk.PhotoImage(file='Icons/green_up.gif')
        self.red_down_img = tk.PhotoImage(file='Icons/red_down.gif')
        self.payment_img = tk.PhotoImage(file='Icons/payment.gif')
        self.delete_img = tk.PhotoImage(file='Icons/delete_icon.gif')
        self.correction_img = tk.PhotoImage(file='Icons/Correction1.gif')
        self.delete25_img = tk.PhotoImage(file='Icons/delete_icon_25.gif')
        self.correction25_img = tk.PhotoImage(file='Icons/Correction1_25.gif')
        self.forward25_img = tk.PhotoImage(file='Icons/Forward25.gif')
        self.copy_img = tk.PhotoImage(file='Icons/copy.gif')
        self.reportButton_img = tk.PhotoImage(file='Icons/reportButton.gif')
        self.deployed25_img = tk.PhotoImage(file='Icons/Deployed25.gif')
        self.Wrap_img = tk.PhotoImage(file='Icons/Wrap.gif')

        # Картинки статей и разделов
        self.air_img = tk.PhotoImage(file='ImageItem/air.gif')
        self.alcogol_img = tk.PhotoImage(file='ImageItem/alcogol.gif')
        self.flat_img = tk.PhotoImage(file='ImageItem/appartament.gif')
        self.avto_img = tk.PhotoImage(file='ImageItem/avto.gif')
        self.benzin_img = tk.PhotoImage(file='ImageItem/benzin.gif')
        self.card_img = tk.PhotoImage(file='ImageItem/card.gif')
        self.dollar_img = tk.PhotoImage(file='ImageItem/dollar.gif')
        self.euro_img = tk.PhotoImage(file='ImageItem/evro.gif')
        self.fitnes1_img = tk.PhotoImage(file='ImageItem/fitnes1.gif')
        self.fitnes2_img = tk.PhotoImage(file='ImageItem/fitnes2.gif')
        self.fitnes3_img = tk.PhotoImage(file='ImageItem/fitnes3.gif')
        self.food1_img = tk.PhotoImage(file='ImageItem/food1.gif')
        self.food2_img = tk.PhotoImage(file='ImageItem/food2.gif')
        self.gift_img = tk.PhotoImage(file='ImageItem/gift.gif')
        self.giveloan_img = tk.PhotoImage(file='ImageItem/giveloan.gif')
        self.income_img = tk.PhotoImage(file='ImageItem/income.gif')
        self.investments_img = tk.PhotoImage(file='ImageItem/investments.gif')
        self.ipoteka_img = tk.PhotoImage(file='ImageItem/ipoteka.gif')
        self.kredit_img = tk.PhotoImage(file='ImageItem/kredit.gif')
        self.kredit2_img = tk.PhotoImage(file='ImageItem/kredit2.gif')
        self.magazin_img = tk.PhotoImage(file='ImageItem/magazin.gif')
        self.mebel1_img = tk.PhotoImage(file='ImageItem/mebel1.gif')
        self.mebel2_img = tk.PhotoImage(file='ImageItem/mebel2.gif')
        self.medicina1_img = tk.PhotoImage(file='ImageItem/medicina1.gif')
        self.medicina2_img = tk.PhotoImage(file='ImageItem/medicina2.gif')
        self.money_img = tk.PhotoImage(file='ImageItem/money1.gif')
        self.moneyPlus_img = tk.PhotoImage(file='ImageItem/MoneyPlus.gif')
        self.nalog_img = tk.PhotoImage(file='ImageItem/nalog.gif')
        self.otdih_img = tk.PhotoImage(file='ImageItem/otdih.gif')
        self.paricm_img = tk.PhotoImage(file='ImageItem/paricm.gif')
        self.percent_img = tk.PhotoImage(file='ImageItem/percent1.gif')
        self.pets_img = tk.PhotoImage(file='ImageItem/pets.gif')
        self.property_img = tk.PhotoImage(file='ImageItem/property.gif')
        self.cost_img = tk.PhotoImage(file='ImageItem/cost.gif')
        self.remont_img = tk.PhotoImage(file='ImageItem/remont.gif')
        self.rubl_img = tk.PhotoImage(file='ImageItem/rubl.gif')
        self.takeloan_img = tk.PhotoImage(file='ImageItem/takeloan.gif')
        self.taxi_img = tk.PhotoImage(file='ImageItem/taxi.png')
        self.tekhnica_img = tk.PhotoImage(file='ImageItem/tekhnica.gif')
        self.upgrade_img = tk.PhotoImage(file='ImageItem/upgrade.gif')
        self.clothes_img = tk.PhotoImage(file='ImageItem/clothes.gif')
        self.kill_img= tk.PhotoImage(file='ImageItem/kill.gif')
        self.work1_img = tk.PhotoImage(file='ImageItem/work1.gif')
        self.work2_img = tk.PhotoImage(file='ImageItem/work2.gif')
        self.work3_img = tk.PhotoImage(file='ImageItem/work3.gif')

        # Массив картинок для разделов и статей
        self.ImageList = [self.air_img, self.alcogol_img, self.flat_img,  self.avto_img, self.benzin_img,
                          self.card_img, self.dollar_img, self.euro_img, self.fitnes1_img, self.fitnes2_img,
                          self.fitnes3_img, self.food1_img, self.food2_img, self.gift_img, self.giveloan_img,
                          self.income_img, self.investments_img, self.ipoteka_img, self.kredit_img, self.kredit2_img,
                          self.magazin_img, self.mebel1_img, self.mebel2_img, self.medicina1_img, self.medicina2_img,
                          self.money_img, self.moneyPlus_img, self.nalog_img, self.otdih_img, self.paricm_img,
                          self.percent_img, self.pets_img, self.property_img, self.cost_img, self.remont_img,
                          self.rubl_img, self.takeloan_img, self.taxi_img, self.tekhnica_img, self.upgrade_img,
                          self.clothes_img, self.kill_img, self.work1_img, self.work2_img, self.work3_img]

        # Инициилизация основных окон программы
        # Верхний туулбар
        self.toolbarMenu = tk.Frame(bg='#131313', bd=2)
        # self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)

        # Кнопка меню
        buttonMenu = tk.Button(self.toolbarMenu, text="Меню", background="#222", foreground="#ccc",
                               highlightcolor="#C0C0C0", padx="10", pady="2", font="16", compound=tk.RIGHT,
                               image=self.menu_img, command=self.MenuWindow)
        buttonMenu.pack(side=tk.LEFT)

        # Фрейм для основных страниц
        self.frameMain = tk.Frame(bg='black')
        self.frameMain.place(x=0, y=0, height=720, width=1280)

        # Вызов окна входа в систему
        self.PasswordWindow()

    @property
    def CurrentWindow(self):
        return self.__CurrentWindow

    @CurrentWindow.setter
    def CurrentWindow(self, currentWindow):
        self.__CurrentWindow = currentWindow

    @property
    def PreviousWindow(self):
        return self.__PreviousWindow

    @PreviousWindow.setter
    def PreviousWindow(self, previousWindow):
        self.__PreviousWindow = previousWindow

    @property
    def SettingFilter(self):
        return self.__SettingFilter

    @SettingFilter.setter
    def SettingFilter(self, currentPage=1, countPage=1, period='AllPeriod', begDate='', endDate=dt.date(2200, 12, 31)):
        Date = begDate
        if begDate == '':
            Date = db.beginDate

        self.__SettingFilter['currentPage'] = currentPage
        self.__SettingFilter['countPage'] = countPage
        self.__SettingFilter['period'] = period
        self.__SettingFilter['beginDate'] = Date
        self.__SettingFilter['endDate'] = endDate

    # Окно входа в систему
    def PasswordWindow(self):
        """ Окно ввода пароля и вход в систему """
        # Картинка сейфового замка
        zamok_paint = tk.Label(self.frameMain, bg='black', image=self.zamok_img)
        zamok_paint.place(x=0, y=0)

        # Поле ввода пароля
        entry_password = ttk.Entry(self.frameMain, width=20, show="*", font="Arial 25")
        entry_password.place(x=467, y=300, width=300)
        # Кнопка входа
        button_entrance = tk.Button(self.frameMain, image=self.forward_img, bg='#2f4f4f')
        button_entrance.place(x=769, y=300, height=45, width=45)
        button_entrance.bind('<Button-1>', lambda event: self.EntranceAction(entry_password.get()))

    # Вход в систему
    def EntranceAction(self, password):
        """ Переход после ввода верного пароля на страницу стартовых настроек если программа не активирована
         или на основную страницу, если активирована """
        data = db.RequestSelectDB('parol', 'setting')
        passworddb = data[0][0]

        if passworddb == password:
            print('OK! Пароль верен, осуществлен вход в программу')
            if db.use == 0:
                # Работа не начата, переходим в окно настройки системы для начала работы
                self.SettingWindow()
            else:
                # Работа начата, переходим в основное окно программы
                self.MainWindow()
        else:
            mb.showerror("Ошибка", "Введен неверный пароль")

    # Окно меню
    def MenuWindow(self):
        """ Окно меню программы с опциями: Продолжить, Настройки, О программе, Выйти """
        if self.CurrentWindow != 2:
            self.PreviousWindow = self.CurrentWindow
        self.CurrentWindow = 1

        # Отключаем отображаемые фреймы
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.Clear()

        # Фрейм меню
        label_menu = tk.Label(self.frameMain, text='МЕНЮ:', bg="black", foreground="#ccc", font="Arial 25")
        label_menu.place(x=500, y=149)
        label_menu_icon = tk.Label(self.frameMain, image=app.menu_img)
        label_menu_icon.place(x=620, y=150)

        buttonResume = tk.Button(self.frameMain, text="Продолжить  ", background="#222", foreground="#ccc",
                                 highlightcolor="#C0C0C0", padx="10", pady="1", font="16", compound=tk.RIGHT,
                                 image=self.baks_img, command=self.BackWard)
        buttonResume.place(x=500, y=199)

        # buttonResume.bind('<Button-1>', self.BackWard(CurrentWindow))

        buttonSetting2 = tk.Button(self.frameMain, text='Настроить     ', background="#222", foreground="#ccc",
                                   highlightcolor="#C0C0C0", padx="10", command=self.SettingWindow,
                                   pady="1", font="16", compound=tk.RIGHT, image=app.setting_img)
        buttonSetting2.place(x=500, y=259)

        buttonInfo = tk.Button(self.frameMain, text='О программе', background="#222", foreground="#ccc",
                               highlightcolor="#C0C0C0",
                               padx="10", pady="1", font="16", compound=tk.RIGHT, image=self.info_img)
        buttonInfo.place(x=500, y=320)

        buttonExit = tk.Button(self.frameMain, text='Выйти             ', background="#222", foreground="#ccc",
                               highlightcolor="#C0C0C0", padx="10", pady="1", font="16", compound=tk.RIGHT,
                               image=self.exit_img, command=self.ExitTheProgram)
        buttonExit.place(x=500, y=379)

        # Картинка с битками
        coin_paint = tk.Label(self.frameMain, bg='black', image=self.coin_img)
        coin_paint.place(x=775, y=50)

    # Главное окно программы
    def MainWindow(self):
        """ Основное окно программы, содержащее информацию о текущих финансовых показателях в разрезе разделов.
         Служит для перехода на страницы разделов для создания, просмотра и редактирования записей и для
         перехода на страницу просмотра детального отчета """
        self.CurrentWindow = 5
        self.Clear()
        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)

        # Картинка с девками
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.main_img)
        Main_paint.place(x=820, y=45)

        # Запрос к БД на данные по разделам
        data = db.RequestSelectDB('*', 'typeitems')

        # Блок ввода данных по статьям доходов и расходов
        l2 = tk.Label(self.frameMain, text="ДОХОДЫ И РАСХОДЫ:", bg="black", foreground="#ccc",
                      font="Arial 25")
        l2.place(x=50, y=50)

        button_IncomeSetting = tk.Button(self.frameMain, text=data[0][2], bg='#F08080', font="Arial 16",
                                         foreground="#F5F5F5")
        button_IncomeSetting.place(x=50, y=100, width=200, height=40)
        button_IncomeSetting.bind('<Button-1>', lambda event: self.ListItemForEnterDataWindow(1))
        s11 = tk.Label(self.frameMain, text=self.NumberIsString(data[0][5]), bg="#A9A9A9", foreground="#F5F5F5",
                       font="Arial 12")
        s11.place(x=255, y=100, width=150, height=40)

        button_CostsSetting = tk.Button(self.frameMain, text=data[1][2], bg='#BA55D3', font="Arial 16",
                                        foreground="#F5F5F5")
        button_CostsSetting.place(x=450, y=100, width=200, height=40)
        button_CostsSetting.bind('<Button-1>', lambda event: self.ListItemForEnterDataWindow(2))
        s22 = tk.Label(self.frameMain, text=self.NumberIsString(data[1][5]), bg="#A9A9A9", foreground="#F5F5F5",
                       font="Arial 12")
        s22.place(x=655, y=100, width=150, height=40)

        # Блок  статей актива
        l3 = tk.Label(self.frameMain, text="АКТИВ:", bg="black", foreground="#C71585", font="Arial 25")
        l3.place(x=50, y=150)

        button_MoneySetting = tk.Button(self.frameMain, text=data[2][2], bg='#DB7093', font="Arial 14",
                                        foreground="#F5F5F5")
        button_MoneySetting.place(x=50, y=200, width=200, height=40)
        button_MoneySetting.bind('<Button-1>', lambda event: self.ListItemForEnterDataWindow(3))
        s1 = tk.Label(self.frameMain, text=self.NumberIsString(data[2][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s1.place(x=255, y=200, width=150, height=40)

        button_PropertySetting = tk.Button(self.frameMain, text=data[3][2], bg='#DB7093', font="Arial 14",
                                           foreground="#F5F5F5")
        button_PropertySetting.place(x=50, y=250, width=200, height=40)
        button_PropertySetting.bind('<Button-1>', lambda event: self.ListItemForEnterDataWindow(4))
        s2 = tk.Label(self.frameMain, text=self.NumberIsString(data[3][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s2.place(x=255, y=250, width=150, height=40)

        button_InvestmentsSetting = tk.Button(self.frameMain, text=data[4][2], bg='#DB7093', font="Arial 14",
                                              foreground="#F5F5F5")
        button_InvestmentsSetting.place(x=50, y=300, width=200, height=40)
        button_InvestmentsSetting.bind('<Button-1>', lambda event: self.ListItemForEnterDataWindow(5))
        s3 = tk.Label(self.frameMain, text=self.NumberIsString(data[4][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s3.place(x=255, y=300, width=150, height=40)

        button_LoansIssuedSetting = tk.Button(self.frameMain, text=data[5][2], bg='#DB7093', font="Arial 14",
                                              foreground="#F5F5F5")
        button_LoansIssuedSetting.place(x=50, y=350, width=200, height=40)
        button_LoansIssuedSetting.bind('<Button-1>', lambda event: self.ListItemForEnterDataWindow(6))
        s4 = tk.Label(self.frameMain, text=self.NumberIsString(data[5][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s4.place(x=255, y=350, width=150, height=40)

        # Блок  статей пассива
        l4 = tk.Label(self.frameMain, text="ПАССИВ:", bg="black", foreground="#800080",
                      font="Arial 25")
        l4.place(x=450, y=150)

        button_CreditSetting = tk.Button(self.frameMain, text=data[6][2], bg='#DA70D6', font="Arial 14",
                                         foreground="#F5F5F5")
        button_CreditSetting.place(x=450, y=200, width=200, height=40)
        button_CreditSetting.bind('<Button-1>', lambda event: self.ListItemForEnterDataWindow(7))
        s5 = tk.Label(self.frameMain, text=self.NumberIsString(data[6][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s5.place(x=655, y=200, width=150, height=40)

        button_LoansSetting = tk.Button(self.frameMain, text=data[7][2], bg='#DA70D6', font="Arial 14",
                                        foreground="#F5F5F5")
        button_LoansSetting.place(x=450, y=250, width=200, height=40)
        button_LoansSetting.bind('<Button-1>', lambda event: self.ListItemForEnterDataWindow(8))
        s6 = tk.Label(self.frameMain, text=self.NumberIsString(data[7][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s6.place(x=655, y=250, width=150, height=40)

        l5 = tk.Label(self.frameMain, text=data[8][2], bg='#DA70D6', foreground="#F5F5F5",
                      font="Arial 14")
        l5.place(x=450, y=350, width=200, height=40)
        s7 = tk.Label(self.frameMain, text=self.NumberIsString(data[8][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s7.place(x=655, y=350, width=150, height=40)

        # Кнопка открытия отчета
        buttonReport = tk.Button(self.frameMain, text='ПОСМОТРЕТЬ ОТЧЕТ ', background="#222", foreground="#ccc",
                                 highlightcolor="#C0C0C0", padx="10", command=self.ReportWindow,
                                 pady="1", font="16", compound=tk.RIGHT, image=self.reportButton_img)
        buttonReport.place(x=50, y=550)

    # Список статей для ввода данных
    def ListItemForEnterDataWindow(self, idtypeitem):
        """ Окно отображение списка статей раздела для создания, просмотра и редактирования записей """
        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)
        self.CurrentWindow = 6
        self.Clear()

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.DefineTextAndColor(idtypeitem)

        # Наименование раздела
        l1 = tk.Label(self.frameMain, text=nameandcolor[0] + ":", bg="black", foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=0)

        # Кнопка назад
        button_back = tk.Button(self.toolbarMenu, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=130, y=0)
        button_back.bind('<Button-1>', lambda event: self.BackWard(0))

        # Запрос к БД на перечень рабочих статей в разделе
        data = db.RequestSelectDB('*', 'items', 'typeitem_id={} AND workingitem==1'.format(str(idtypeitem)))

        # Построение списка статей
        j = 0
        if len(data) != 0:
            for i in range(1, len(data) + 1):
                if i % 2 != 0:
                    X = 50
                    Y = 50 * (i - j)
                else:
                    j = j + 1
                    X = 450
                    Y = 50 * (i - j)

                # Кнопки создания и просмотра записей по статье
                self.ButtonCreateAndViewNotes(X, Y, data[i - 1], nameandcolor[1])

        else:
            # Надпись о том, что статьи в разделе отсутствуют
            l2 = tk.Label(self.frameMain, text="В разделе отсутствуют статьи для ввода данных."
                                               "\nСоздайте их и окне настроек.",
                          bg="black", foreground="#ccc", justify='left', font="Arial 16")
            l2.place(x=50, y=50)

        # Картинка раздела
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.ImageItem(idtypeitem))
        Main_paint.place(x=820, y=45)

    # Отображение картинки в зависимости от типа раздела
    def ImageItem(self, TYPEITEM):
        """ Извлекает картинку для визуальной идентификации раздела в зависимости от типа раздела"""
        img = self.ImageList[15]
        if TYPEITEM == 1:
            img = self.ImageList[15]
        elif TYPEITEM == 2:
            img = self.ImageList[33]
        elif TYPEITEM == 3:
            img = self.ImageList[25]
        elif TYPEITEM == 4:
            img = self.ImageList[32]
        elif TYPEITEM == 5:
            img = self.ImageList[16]
        elif TYPEITEM == 6:
            img = self.ImageList[14]
        elif TYPEITEM == 7:
            img = self.ImageList[30]
        elif TYPEITEM == 8:
            img = self.ImageList[36]

        return img

    # Отображение картинки в зависимости от типа раздела
    def ImageItemInt(self, TYPEITEM):
        """ Извлекает индекс картинки в списке ImageList в зависимости от типа раздела"""
        img = 15
        if TYPEITEM == 1:
            img = 15
        elif TYPEITEM == 2:
            img = 33
        elif TYPEITEM == 3:
            img = 25
        elif TYPEITEM == 4:
            img = 32
        elif TYPEITEM == 5:
            img = 16
        elif TYPEITEM == 6:
            img = 14
        elif TYPEITEM == 7:
            img = 30
        elif TYPEITEM == 8:
            img = 36

        return img

    # Кнопки создания и просмотра записей по статье
    def ButtonCreateAndViewNotes(self, X, Y, DATAITEM, COLOR):
        """ Отображение кнопок создания и просмотра записей по статье для метода ListItemForEnterDataWindow """
        # Кнопка добавления новых данных
        button_Plus = tk.Button(self.frameMain, image=self.plus_img, bg='black', font="Arial 12",
                                foreground="#F5F5F5")
        button_Plus.place(x=(X - 40), y=Y, width=40, height=40)
        button_Plus.bind('<Button-1>', lambda eventbutton: self.DataCreateNewWindow(DATAITEM))

        # Кнопка просмотра записей в статье
        button_Item = tk.Button(self.frameMain, text=DATAITEM[2],
                                bg=COLOR, font="Arial 12", foreground="#F5F5F5")
        button_Item.place(x=X, y=Y, width=200, height=40)
        button_Item.bind('<Button-1>', lambda eventbutton: self.ListDataInItemWindow(DATAITEM))

        tex = self.NumberIsString(DATAITEM[7])
        sumItem = tk.Label(self.frameMain, text=tex, bg="#A9A9A9", foreground="#F5F5F5", font="Arial 12")
        sumItem.place(x=X + 205, y=Y, width=145, height=40)

    def DefineTextAndColor(self, idtypeitem):
        """ Извлекает наименование раздела для заголовков и цвет для кнопок статей раздела """
        # Запрос на наименование раздела и цвет кнопок
        datatype = db.RequestSelectDB('*', 'typeitems', 'id={}'.format(str(idtypeitem)))
        nametype = datatype[0][2]

        if datatype[0][1] == 0:
            colorbutton = '#F08080'
        elif datatype[0][1] == 1:
            colorbutton = '#BA55D3'
        elif datatype[0][1] == 2:
            colorbutton = '#DB7093'
        else:
            colorbutton = '#DA70D6'
        return [nametype, colorbutton]

    # Окно данных по статье
    def ListDataInItemWindow(self, DATA):
        """ Окно для отображения данных, заведенных по статье, содержит постраничный пэйджинг, фильтр по дате и
        кнопки дополнительных опций для редактирования, копирования и удаления записей при входе из вышестоящего окна
        статей для ввода и просмотра данных ListItemForEnterDataWindow """
        # Список обновляемых элементов
        ElementsToDraw = list()

        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)

        # Устанавливаем идентификатор текущей страницы
        self.CurrentWindow = 7
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.toolbarMenu, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=130, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.BackWard(DATA[1]))

        # Картинка статьи
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.ImageList[DATA[8]])
        Main_paint.place(x=820, y=45)

        # Наименование раздела
        nameandcolor = self.DefineTextAndColor(DATA[1])
        textheaders = nameandcolor[0] + '/' + DATA[2] + '/Просмотр данных:'
        l1 = tk.Label(self.frameMain, text=textheaders, bg='black', foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=0)

        # Отрисовка списка строк с данными, постраничного пэйджинга и фильтра
        self.DrawListOfRow(DATA[0], ElementsToDraw)
        print('OBJECTLIST = {}'.format(ElementsToDraw))

    # Окно данных по статье
    def ListDataInItemWindow2(self, DATA):
        """ Окно для отображения данных, заведенных по статье, содержит постраничный пэйджинг, фильтр по дате и
            кнопки дополнительных опций для редактирования, копирования и удаления записей при возврате из нижестоящих
            окон коррректировки, копирования и удаления данных"""
        print('Список данных по статье')

        # Список обновляемых элементов
        ElementsToDraw = list()

        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)

        # Устанавливаем идентификатор текущей страницы
        self.CurrentWindow = 7
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.toolbarMenu, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=130, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.BackWard(DATA[1]))

        # Картинка раздела
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.ImageItem(DATA[1]))
        Main_paint.place(x=820, y=45)

        # Наименование раздела
        nameandcolor = self.DefineTextAndColor(DATA[1])
        textheaders = nameandcolor[0] + '/' + DATA[2] + '/Просмотр данных:'
        l1 = tk.Label(self.frameMain, text=textheaders, bg='black', foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=0)

        # Отрисовка списка строк с данными, постраничного пэйджинга и фильтра
        self.DrawListOfRow(DATA[0], ElementsToDraw)
        print('OBJECTLIST = {}'.format(ElementsToDraw))

    # Изменение значений фильтра, перерисовка страницы
    def ChangeFilter(self, change, ITEMID, OBJECTLIST, DATE_BEGIN=dt.date(2200, 12, 31), DATE_END=dt.date(2200, 12, 31)):
        """ Изменение значений словаря SettingFilter при нажатии на кнопки роутинга и
        фильтра по дате при помощи вызова метода FindPeriod.
        Вызов метода обновления реестра и кнопок пэйджинга и фильтра DrawListOfRow"""
        # Изменение значений фильтрации при нажатии кнопок
        print(DATE_END, DATE_BEGIN, self.__SettingFilter)
        if change == 'PageForward':
            if self.SettingFilter['currentPage'] == self.SettingFilter['countPage']:
                self.SettingFilter['currentPage'] = 1
            else:
                self.SettingFilter['currentPage'] += 1

        elif change == 'PageBack':
            if self.SettingFilter['currentPage'] == 1:
                self.SettingFilter['currentPage'] = self.SettingFilter['countPage']
            else:
                self.SettingFilter['currentPage'] -= 1
        else:
            # Устанавливаем новые значения в SettingFilter для отбора по периоду
            self.FindPeriod(change)

        # Отрисовываем новые данные, пейджинг и фильтр
        if self.CurrentWindow == 13:
            self.DrawListOfRow(ITEMID, OBJECTLIST, DATE_BEGIN, DATE_END)
        else:
            self.DrawListOfRow(ITEMID, OBJECTLIST)

    # Расчет значений фильтра по дате
    def FindPeriod(self, ChangePeriod):
        """ Вычисляем даты начала и конца периода в зависимости от смецения по периоду и изменения размеров периода.
         Изменение значений SettingFilter если период не уперся в дату начала учета """
        if ChangePeriod == 'PeriodUp' or ChangePeriod == 'PeriodDown':
            period = ''
            if ChangePeriod == 'PeriodUp':
                if self.SettingFilter['period'] == 'AllPeriod':
                    period = 'DayPeriod'
                elif self.SettingFilter['period'] == 'DayPeriod':
                    period = 'WeekPeriod'
                elif self.SettingFilter['period'] == 'WeekPeriod':
                    period = 'MonthPeriod'
                elif self.SettingFilter['period'] == 'MonthPeriod':
                    period = 'YearPeriod'
                elif self.SettingFilter['period'] == 'YearPeriod':
                    self.SettingFilter['period'] = 'AllPeriod'

            elif ChangePeriod == 'PeriodDown':
                if self.SettingFilter['period'] == 'AllPeriod':
                    period = 'YearPeriod'
                elif self.SettingFilter['period'] == 'YearPeriod':
                    period = 'MonthPeriod'
                elif self.SettingFilter['period'] == 'MonthPeriod':
                    period = 'WeekPeriod'
                elif self.SettingFilter['period'] == 'WeekPeriod':
                    period = 'DayPeriod'
                elif self.SettingFilter['period'] == 'DayPeriod':
                    period = 'AllPeriod'

            # Если период меняем на "Весь период", то устанавливаем дату начала периода и условную дальнюю дату
            if period == 'AllPeriod':
                self.__SettingFilter['period'] = 'AllPeriod'
                self.__SettingFilter['beginDate'] = db.beginDate
                self.__SettingFilter['endDate'] = dt.date(2200, 12, 31)

            # Если период меняем на Год, то устанавливаем год текущей даты, если двигаемся с "Весь период",
            # или берем год даты конца периода, если двигаемся из "Месяц"
            elif period == 'YearPeriod':
                if self.SettingFilter['period'] == 'AllPeriod':
                    self.__SettingFilter['beginDate'] = dt.date(db.todayDate.year, 1, 1)
                    self.__SettingFilter['endDate'] = dt.date(db.todayDate.year, 12, 31)
                elif self.SettingFilter['period'] == 'MonthPeriod':
                    self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['endDate'].year, 1, 1)
                    self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year, 12, 31)
                self.SettingFilter['period'] = 'YearPeriod'

            # Если период меняем на Месяц, то устанавливаем месяц текущей даты, если двигаемся с текущего года c  "Год",
            # если двигаемся с прошлых лет - то устанавливаем месяц Декабрь
            # если двигаемся с будущих лет - то устанавливаем месяц Январь
            # или берем месяц и год с даты конца периода, если двигаемся из "Неделя"
            elif period == 'MonthPeriod':
                if self.SettingFilter['period'] == 'YearPeriod':
                    if self.__SettingFilter['endDate'].year == db.todayDate.year:
                        endDay = calendar.monthrange(db.todayDate.year, db.todayDate.month)[1]
                        self.__SettingFilter['beginDate'] = dt.date(db.todayDate.year, db.todayDate.month, 1)
                        self.__SettingFilter['endDate'] = dt.date(db.todayDate.year, db.todayDate.month, endDay)
                    elif self.__SettingFilter['endDate'].year < db.todayDate.year:
                        self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['endDate'].year, 12, 1)
                        self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year, 12, 31)
                    elif self.__SettingFilter['endDate'].year < db.todayDate.year:
                        self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['endDate'].year, 1, 1)
                        self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year, 1, 31)
                elif self.SettingFilter['period'] == 'WeekPeriod':
                    endDay = calendar.monthrange(self.__SettingFilter['endDate'].year,
                                                 self.__SettingFilter['endDate'].month)[1]
                    self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['endDate'].year,
                                                                self.__SettingFilter['endDate'].month, 1)
                    self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year,
                                                              self.__SettingFilter['endDate'].month, endDay)
                self.SettingFilter['period'] = 'MonthPeriod'

            # Если период меняем на Неделю, то устанавливаем неделю текущйй даты, если двигаемся с текущего месяца
            # c "Месяц", если двигаемся с прошлых месяцев - то устанавливаем неделю конца месяца
            # если двигаемся с будущих месяцев - то устанавливаем неделю начала месяца
            # или берем неделю выбранной даты, если двигаемся из "День"
            elif period == 'WeekPeriod':
                if self.SettingFilter['period'] == 'MonthPeriod':
                    if self.__SettingFilter['endDate'].month == db.todayDate.month:
                        dayWeek = calendar.monthrange(db.todayDate.year, db.todayDate.month)[0]
                        self.__SettingFilter['beginDate'] = db.todayDate - timedelta(dayWeek)
                        self.__SettingFilter['endDate'] = db.todayDate + timedelta(6 - dayWeek)
                    elif self.__SettingFilter['endDate'].month > db.todayDate.month:
                        dayWeekOne = calendar.monthrange(self.__SettingFilter['beginDate'].year,
                                                         self.__SettingFilter['beginDate'].month)[0]
                        self.__SettingFilter['beginDate'] = self.__SettingFilter['endDate'] - timedelta(dayWeekOne)
                        self.__SettingFilter['endDate'] = self.__SettingFilter['endDate'] + timedelta(6 - dayWeekOne)
                    elif self.__SettingFilter['endDate'].month < db.todayDate.month:
                        dayWeek = calendar.monthrange(self.__SettingFilter['beginDate'].year,
                                                      self.__SettingFilter['beginDate'].month)[0]
                        dayMonthEnd = self.__SettingFilter['beginDate'] + timedelta(28)
                        self.__SettingFilter['beginDate'] = dayMonthEnd - timedelta(dayWeek)
                        self.__SettingFilter['endDate'] = dayMonthEnd + timedelta(6 - dayWeek)
                elif self.SettingFilter['period'] == 'DayPeriod':
                    weekDay = self.__SettingFilter['beginDate'].weekday()
                    self.__SettingFilter['beginDate'] = self.__SettingFilter['beginDate'] - timedelta(weekDay)
                    self.__SettingFilter['endDate'] = self.__SettingFilter['endDate'] + timedelta(6 - weekDay)
                self.SettingFilter['period'] = 'WeekPeriod'

            # Если период меняем на день, то устанавливаем текущую дату, если двигаемся с "Весь период"
            # Если двигаемся с "Недели", включающую текущий день - то устанавливаем текущий день
            # если двигаемся с будущей недели, то устанавливаем первый день недели
            # если двигаемся с прошедшей недели то устанавливаем  последний день недели
            elif period == 'DayPeriod':
                if self.SettingFilter['period'] == 'AllPeriod':
                    self.__SettingFilter['beginDate'] = db.todayDate
                    self.__SettingFilter['endDate'] = db.todayDate
                elif self.SettingFilter['period'] == 'WeekPeriod':
                    if self.__SettingFilter['beginDate'] >= db.todayDate >= self.__SettingFilter['endDate']:
                        self.__SettingFilter['beginDate'] = db.todayDate
                        self.__SettingFilter['endDate'] = db.todayDate
                    elif self.__SettingFilter['beginDate'] > db.todayDate:
                        self.__SettingFilter['endDate'] = self.__SettingFilter['beginDate']
                    elif self.__SettingFilter['endDate'] < db.todayDate:
                        self.__SettingFilter['beginDate'] = self.__SettingFilter['endDate']
                self.__SettingFilter['period'] = 'DayPeriod'

            # Если дата начала периода получилась < даты начала учета, делаем датой начала периода дату начала учета
            if self.__SettingFilter['beginDate'] < db.beginDate:
                self.__SettingFilter['beginDate'] = db.beginDate

        # Листаем отрезок времени назад
        elif ChangePeriod == 'PeriodBack':
            # Листаем годы назад, пока не дойдем до года начала учета
            if self.SettingFilter['period'] == 'YearPeriod':
                if self.__SettingFilter['endDate'].year == db.beginDate.year:
                    self.__SettingFilter['beginDate'] = db.beginDate
                elif self.__SettingFilter['endDate'].year > db.beginDate.year:
                    if (self.__SettingFilter['endDate'].year - 1) == db.beginDate.year:
                        self.__SettingFilter['beginDate'] = db.beginDate
                        self.__SettingFilter['endDate'] = dt.date(db.beginDate.year, 12, 31)
                    else:
                        self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['beginDate'].year - 1, 1, 1)
                        self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year - 1, 12, 31)

            # Листаем месяцы назад, пока не дойдем до месяца начала учета
            elif self.SettingFilter['period'] == 'MonthPeriod':
                if self.__SettingFilter['beginDate'] == db.beginDate:
                    self.__SettingFilter['beginDate'] = db.beginDate
                else:
                    if self.__SettingFilter['endDate'].month != 1:
                        dayMonth = calendar.monthrange(self.__SettingFilter['endDate'].year,
                                                       self.__SettingFilter['endDate'].month - 1)[1]
                        self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['endDate'].year,
                                                                    self.__SettingFilter['endDate'].month - 1, 1)

                        self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year,
                                                                  self.__SettingFilter['endDate'].month - 1, dayMonth)
                    else:
                        dayMonth = calendar.monthrange(self.__SettingFilter['endDate'].year - 1, 1)[1]
                        self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['endDate'].year - 1, 12, 1)

                        self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year - 1, 12,
                                                                  dayMonth)

            # Листаем недели назад, пока не дойдем до недели начала учета
            elif self.SettingFilter['period'] == 'WeekPeriod':
                if self.__SettingFilter['beginDate'] == db.beginDate:
                    self.__SettingFilter['beginDate'] = db.beginDate
                else:
                    self.__SettingFilter['beginDate'] = self.__SettingFilter['beginDate'] - timedelta(weeks=1)
                    self.__SettingFilter['endDate'] = self.__SettingFilter['endDate'] - timedelta(weeks=1)

            # Листаем дни назад, пока не дойдем до дня начала учета
            elif self.SettingFilter['period'] == 'DayPeriod':
                if self.__SettingFilter['beginDate'] == db.beginDate:
                    self.__SettingFilter['beginDate'] = db.beginDate
                else:
                    self.__SettingFilter['beginDate'] = self.__SettingFilter['beginDate'] - timedelta(1)
                    self.__SettingFilter['endDate'] = self.__SettingFilter['endDate'] - timedelta(1)

            # Если дата начала периода получилась < даты начала учета, делаем датой начала периода дату начала учета
            if self.__SettingFilter['beginDate'] < db.beginDate:
                self.__SettingFilter['beginDate'] = db.beginDate

        # Листаем отрезок времени вперед
        elif ChangePeriod == 'PeriodForward':
            # Листаем годы вперед
            if self.SettingFilter['period'] == 'YearPeriod':
                self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['beginDate'].year + 1, 1, 1)
                self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year + 1, 12, 31)

            # Листаем месяцы вперед
            elif self.SettingFilter['period'] == 'MonthPeriod':
                if self.__SettingFilter['endDate'].month != 12:
                    dayMonth = calendar.monthrange(self.__SettingFilter['endDate'].year,
                                                   self.__SettingFilter['endDate'].month + 1)[1]
                    self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['endDate'].year,
                                                                self.__SettingFilter['endDate'].month + 1, 1)

                    self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year,
                                                              self.__SettingFilter['endDate'].month + 1, dayMonth)
                else:
                    dayMonth = calendar.monthrange(self.__SettingFilter['endDate'].year + 1, 1)[1]
                    self.__SettingFilter['beginDate'] = dt.date(self.__SettingFilter['endDate'].year + 1, 1, 1)

                    self.__SettingFilter['endDate'] = dt.date(self.__SettingFilter['endDate'].year + 1, 1, dayMonth)

            # Листаем недели вперед
            elif self.SettingFilter['period'] == 'WeekPeriod':
                self.__SettingFilter['beginDate'] = self.__SettingFilter['endDate'] + timedelta(weeks=1)
                self.__SettingFilter['endDate'] = self.__SettingFilter['endDate'] + timedelta(6)

            # Листаем дни вперед
            elif self.SettingFilter['period'] == 'DayPeriod':
                self.__SettingFilter['beginDate'] = self.__SettingFilter['beginDate'] + timedelta(1)
                self.__SettingFilter['endDate'] = self.__SettingFilter['endDate'] + timedelta(1)

            # Если дата начала периода получилась < даты начала учета, делаем датой начала периода дату начала учета
            if self.__SettingFilter['beginDate'] < db.beginDate:
                self.__SettingFilter['beginDate'] = db.beginDate

    # Установка дефолтных настроек фильтра
    def SetDefaultFilter(self):
        """ Установка дефолтных настроек фильтра и роутинга в словаре SettingFilter """
        self.__SettingFilter['currentPage'] = 1
        self.__SettingFilter['countPage'] = 1
        self.__SettingFilter['period'] = 'AllPeriod'
        self.__SettingFilter['beginDate'] = db.beginDate
        self.__SettingFilter['endDate'] = dt.date(2200, 12, 31)

    # Отрисовка списка строк с данными, постраничного пэйджинга и фильтра
    def DrawListOfRow(self, ITEMID, OBJECTLIST, DATE_BEGIN=dt.date(2200, 12, 31), DATE_END=dt.date(2200, 12, 31)):
        """ Запрос в БД на список записей для отображение в реестре в зависимости от заначений роутинга и фильтра в
        словаре SettingFilter.
        Отрисовка реестра строк с данными, постраничного пэйджинга и фильтра для метода ListDataInItemWindow. """
        # Запрашиваем список данных в статье без учета страниц
        requestAll = 'item_id={} or source={}'.format(ITEMID, ITEMID)
        listnotesAll = db.RequestSelectDB('*', 'notes', requestAll)
        listnotes = list()

        # Очищаем строки и удаляем блок фильтра и блок постраничного пэйджинга
        if len(OBJECTLIST) != 0:
            for obj in OBJECTLIST:
                obj.destroy()

        # Данных по статье нет
        if len(listnotesAll) == 0:
            # Надпись о том, что данные в статье отсутствуют
            l2 = tk.Label(self.frameMain, text="В статье отсутствуют данные.\nСоздайте их по кнопке +.", bg="black",
                          foreground="#ccc", justify='left', font="Arial 16")
            l2.place(x=50, y=50)
            self.SettingFilter['currentPage'] = 1
            self.SettingFilter['countPage'] = 1
        elif len(listnotesAll) != 0:
            # Запрашиваем список данных в статье c фильтром по дате без учета страниц, если данные по статье есть
            DATE1 = DATE_BEGIN if self.CurrentWindow == 13 else self.SettingFilter['beginDate']
            DATE2 = DATE_END if self.CurrentWindow == 13 else self.SettingFilter['endDate']

            requestDate = '(item_id={} or source={}) and dateoperation Between \'{}\' and \'{}\' ORDER BY ' \
                          'dateoperation DESC'.format(ITEMID, ITEMID, DATE1, DATE2)

            listnotes = db.RequestSelectDB('*', 'notes', requestDate)

            # Данные по статье есть, но они не попали под сортировку по периоду
            if len(listnotes) == 0:
                # Надпись о том, что данные в статье отсутствуют при заданной фильтрации по периоду
                tf = "Отсутствуют данные при данной фильтрации.\nИзмените фильтрацию по периоду"
                l2 = tk.Label(self.frameMain, text=tf, bg="black", foreground="#ccc", justify='left', font="Arial 16")
                l2.place(x=50, y=50)
                self.SettingFilter['currentPage'] = 1
                self.SettingFilter['countPage'] = 1
                OBJECTLIST.append(l2)

            # Данные влезают на одну страницу - пэйджинг не отобразится
            elif 0 < len(listnotes) <= 15:
                self.SettingFilter['currentPage'] = 1
                self.SettingFilter['countPage'] = 1

            # Данные НЕ влезают на одну страницу - расчет количества страниц и отбор данных для текущей страницы
            else:
                print(self.__SettingFilter)
                count = len(listnotes) // 15
                if len(listnotes) % 15 != 0:
                    count += 1
                if self.SettingFilter['countPage'] != count:
                    self.SettingFilter['countPage'] = count

                if self.SettingFilter['currentPage'] > count:
                    self.SettingFilter['currentPage'] = count

                # Отбираем записи в зависимости от текущей страницы
                sortedPageList = list()
                countnotes = len(listnotes)

                if self.SettingFilter['currentPage'] == 1:
                    iBegin = 0
                else:
                    iBegin = self.SettingFilter['currentPage'] * 15 - 15
                iEnd = self.SettingFilter['currentPage'] * 15
                if iEnd > countnotes:
                    iEnd = countnotes
                print('iB={}, iE={}'.format(iBegin, iEnd))
                for i in range(iBegin, iEnd):
                    sortedPageList.append(listnotes[i])
                listnotes = sortedPageList

        # Отрисовываем строки с данными
        if len(listnotesAll) != 0:
            # Сортируем данные по убыванию даты не более 15 записей
            if len(listnotes) != 0:
                # Строка с остатками и оборотами
                DATE1 = DATE_BEGIN if self.CurrentWindow == 13 else self.SettingFilter['beginDate']
                DATE2 = DATE_END if self.CurrentWindow == 13 else self.SettingFilter['endDate']
                self.TotalLine(ITEMID, OBJECTLIST, DATE1, DATE2)

                # Фон/область для отображения строк
                Fon_report = tk.Label(self.frameMain, bg='#2F4F4F')
                Fon_report.place(x=20, y=95, width=780, height=460)
                OBJECTLIST.append(Fon_report)

                HY = 100
                for note in listnotes:
                    # Отрисовываем строки
                    self.DrawRowWithData(ITEMID, note, HY, OBJECTLIST)
                    HY += 30

            # Блок фильтра по периоду, если это не расшифровка из Отчета
            if self.CurrentWindow != 13:
                if self.SettingFilter['period'] != 'AllPeriod':
                    # Кнопка фильтрации на период назад
                    buttonPeriodLeft = tk.Button(self.frameMain, name='period_Left', background="black",
                                                 image=self.arrowLeft_img)
                    buttonPeriodLeft.place(x=250, y=580, width=40, height=40)
                    buttonPeriodLeft.bind('<Button-1>', lambda eventbutton: self.ChangeFilter('PeriodBack', ITEMID,
                                                                                              OBJECTLIST))
                    OBJECTLIST.append(buttonPeriodLeft)

                    # Кнопка фильтрации на период вперёд
                    buttonPeriodRight = tk.Button(self.frameMain, name='period_Right', background="black",
                                                  image=self.arrowRight_img)
                    buttonPeriodRight.place(x=330, y=580, width=40, height=40)
                    buttonPeriodRight.bind('<Button-1>', lambda eventbutton: self.ChangeFilter('PeriodForward', ITEMID,
                                                                                               OBJECTLIST))
                    OBJECTLIST.append(buttonPeriodRight)

                # Кнопка изменения размера периода фильтрации вверх
                buttonPeriodUp = tk.Button(self.frameMain, name='period_Up', background="black", image=self.arrowUp_img)
                buttonPeriodUp.place(x=290, y=560, width=40, height=40)
                buttonPeriodUp.bind('<Button-1>', lambda eventbutton: self.ChangeFilter('PeriodUp', ITEMID, OBJECTLIST))
                OBJECTLIST.append(buttonPeriodUp)

                # Кнопка изменения размера периода фильтрации вниз
                buttonPeriodDown = tk.Button(self.frameMain, name='period_Down', background="black",
                                             image=self.arrowDown_img)
                buttonPeriodDown.place(x=290, y=600, width=40, height=40)
                buttonPeriodDown.bind('<Button-1>', lambda eventbutton: self.ChangeFilter('PeriodDown', ITEMID,
                                                                                          OBJECTLIST))
                OBJECTLIST.append(buttonPeriodDown)

                # Выставленное значение фильтра
                lFilterValue = tk.Label(self.frameMain, name='filter_Text', text=self.SetFilterText(), bg="#808080",
                                        foreground="#ccc", font="Arial 12")
                lFilterValue.place(x=375, y=580, width=200, height=40)
                OBJECTLIST.append(lFilterValue)
            else:
                # Выставленное значение фильтра
                if self.SettingFilter['period'] == 'AllPeriod':
                    textFilter = '{}-...'.format(db.beginDate.strftime('%d.%m.%Y'))
                else:
                    textFilter = '{}-{}'.format(DATE_BEGIN.strftime('%d.%m.%Y'), DATE_END.strftime('%d.%m.%Y'))

                lFilterValue = tk.Label(self.frameMain, name='filter_Text', text=textFilter, bg="#808080",
                                        foreground="#ccc", font="Arial 12")
                lFilterValue.place(x=250, y=580, width=200, height=40)
                OBJECTLIST.append(lFilterValue)

        # Блок постраничного пейджинга
        if self.SettingFilter['countPage'] > 1:
            pagetext = '{} из {}'.format(self.SettingFilter['currentPage'], self.SettingFilter['countPage'])
            # Кнопка перелистывания страниц влево
            buttonPageLeft = tk.Button(self.frameMain, name='page_Left', background="black", image=self.arrowLeft_img)
            buttonPageLeft.place(x=50, y=580, width=40, height=40)
            buttonPageLeft.bind('<Button-1>', lambda eventbutton: self.ChangeFilter('PageBack', ITEMID, OBJECTLIST,
                                                                                    DATE_BEGIN, DATE_END))
            OBJECTLIST.append(buttonPageLeft)

            # Счетчик страниц
            lPageCounter = tk.Label(self.frameMain, name='page_Counter', text=pagetext, bg="#808080", foreground="#ccc",
                                    font="Arial 12")
            lPageCounter.place(x=95, y=580, width=100, height=40)
            OBJECTLIST.append(lPageCounter)

            # Кнопка перелистывания страниц вправо
            buttonPageRight = tk.Button(self.frameMain, name='page_Right', background="black",
                                        image=self.arrowRight_img)
            buttonPageRight.place(x=200, y=580, width=40, height=40)
            buttonPageRight.bind('<Button-1>', lambda eventbutton: self.ChangeFilter('PageForward', ITEMID, OBJECTLIST,
                                                                                     DATE_BEGIN, DATE_END))
            OBJECTLIST.append(buttonPageRight)

    # Итоговая строка в реестре данных по статье
    def TotalLine(self, ITEMID, OBJECTLIST, DATE_BEGIN, DATE_END):
        """ Итоговая строка в реестре данных по статье """
        section = db.RequestSelectDB('typeitem_id', 'items', 'id={}'.format(ITEMID))[0][0]

        initial_balance_item, sumitem_plus, sumitem_minus, final_balance_item = 0, 0, 0, 0

        if section == 1 or section == 2:
            where1 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(
                ITEMID, db.beginDate, DATE_BEGIN - timedelta(1))
            initial_balance_item = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', where1))
            where2 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(ITEMID, DATE_BEGIN, DATE_END)
            sumitem_plus = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', where2))

            final_balance_item = initial_balance_item + sumitem_plus

        else:
            # Считаем сумму положительных оборотов по статье на начало периода отбора
            tex2 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                                         increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(
                ITEMID, ITEMID, db.beginDate, DATE_BEGIN - timedelta(1))

            data2 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex2))

            # Считаем сумму положительных оборотов по статье
            tex3 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                                               increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(
                ITEMID, ITEMID, DATE_BEGIN, DATE_END)
            sumitem_plus = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex3))

            # Считаем сумму отицательных обортов по статье
            tex4 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                                        increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(
                ITEMID, ITEMID, DATE_BEGIN, DATE_END)
            sumitem_minus = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex4))

            # Считаем сумму отицательных обортов по статье на начало периода отбора
            tex5 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                                               increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(
                ITEMID, ITEMID, db.beginDate, DATE_BEGIN - timedelta(1))
            data5 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex5))

            initial = db.CheckResultForNone(db.RequestSelectDB('initialbalanceitem', 'items', 'id={}'.format(
                ITEMID)))

            initial_balance_item = initial + data2 - data5
            final_balance_item = initial_balance_item + sumitem_plus - sumitem_minus

        # Отображение виджетов с остатками и оборотами
        l_ini = tk.Label(self.frameMain, text='Начальный остаток', bg="black", foreground="#ccc", font="Arial 9")
        l_ini.place(x=100, y=47, width=150, height=13)
        OBJECTLIST.append(l_ini)

        lSum_ini = tk.Label(self.frameMain, text=self.NumberIsString(initial_balance_item),
                            bg="#696969", foreground="#ccc", font="Arial 12")
        lSum_ini.place(x=100, y=60, width=150, height=30)
        OBJECTLIST.append(lSum_ini)

        l_plus = tk.Label(self.frameMain, text='Положительный оборот', bg="black", foreground="#ccc", font="Arial 9")
        l_plus.place(x=260, y=47, width=150, height=13)
        OBJECTLIST.append(l_plus)

        lSum_plus = tk.Label(self.frameMain, text=self.NumberIsString(sumitem_plus), bg="green",
                             foreground="#ccc", font="Arial 12")
        lSum_plus.place(x=260, y=60, width=150, height=30)
        OBJECTLIST.append(lSum_plus)

        if section != 1 or section != 2:
            l_minus = tk.Label(self.frameMain, text='Отрицательный оборот', bg="black", foreground="#ccc",
                               font="Arial 9")
            l_minus.place(x=420, y=47, width=150, height=13)
            OBJECTLIST.append(l_minus)

            lSum_minus = tk.Label(self.frameMain, text=self.NumberIsString(sumitem_minus), bg="red",
                                  foreground="#ccc", font="Arial 12")
            lSum_minus.place(x=420, y=60, width=150, height=30)
            OBJECTLIST.append(lSum_minus)

        l_fin = tk.Label(self.frameMain, text='Конечный остаток', bg="black", foreground="#ccc", font="Arial 9")

        lSum_fin = tk.Label(self.frameMain, text=self.NumberIsString(final_balance_item), bg="#696969",
                            foreground="#ccc", font="Arial 12")
        if section == 1 or section == 2:
            lSum_fin.place(x=420, y=60, width=150, height=30)
            l_fin.place(x=420, y=47, width=150, height=13)
        else:
            lSum_fin.place(x=580, y=60, width=150, height=30)
            l_fin.place(x=580, y=47, width=150, height=13)
        OBJECTLIST.append(lSum_fin)
        OBJECTLIST.append(l_fin)

    # Получить текст фильтра по дате
    def SetFilterText(self):
        """ Извлекает надпись для фильтра по дате в зависимости от значений в словаре SettingFilter """
        textFilter = ''
        if self.SettingFilter['period'] == 'AllPeriod':
            textFilter = 'Весь период: \n {}-...'.format(self.__SettingFilter['beginDate'].strftime('%d.%m.%Y'),
                                                         self.__SettingFilter['endDate'].strftime('%d.%m.%Y'))
        elif self.SettingFilter['period'] == 'YearPeriod':
            textFilter = 'По годам: \n {}-{}'.format(self.__SettingFilter['beginDate'].strftime('%d.%m.%Y'),
                                                     self.__SettingFilter['endDate'].strftime('%d.%m.%Y'))
        elif self.SettingFilter['period'] == 'MonthPeriod':
            textFilter = 'По месяцам: \n {}-{}'.format(self.__SettingFilter['beginDate'].strftime('%d.%m.%Y'),
                                                       self.__SettingFilter['endDate'].strftime('%d.%m.%Y'))
        elif self.SettingFilter['period'] == 'WeekPeriod':
            textFilter = 'По неделям: \n {}-{}'.format(self.__SettingFilter['beginDate'].strftime('%d.%m.%Y'),
                                                       self.__SettingFilter['endDate'].strftime('%d.%m.%Y'))
        elif self.SettingFilter['period'] == 'DayPeriod':
            textFilter = 'По дням: \n {}-{}'.format(self.__SettingFilter['beginDate'].strftime('%d.%m.%Y'),
                                                    self.__SettingFilter['endDate'].strftime('%d.%m.%Y'))
        return textFilter

    # Отрисовка строки с данными
    def DrawRowWithData(self, itemNotes, drawNotes, HightY, OBJECTLIST):
        # Определяем цвет записи в зависимости от того уменьшает или увеличивает она сумму остатка статьи
        colorbutton = 'red'
        if (itemNotes == drawNotes[1] and (drawNotes[6] == 1 or drawNotes[6] == 2)) or \
                (itemNotes == drawNotes[7] and (drawNotes[6] == 0 or drawNotes[6] == 2)):
            colorbutton = 'green'
        elif (itemNotes == drawNotes[1] and (drawNotes[6] == 0 or drawNotes[6] == 3)) or \
                (itemNotes == drawNotes[7] and (drawNotes[6] == 1 or drawNotes[6] == 3)):
            colorbutton = 'red'

        # Дата операции
        dat = dt.datetime.strptime(drawNotes[3], '%Y-%m-%d').date()
        dat = dt.date.strftime(dat, '%d.%m.%Y')
        lDate = tk.Label(self.frameMain, text=dat, bg=colorbutton, foreground="#ccc", font="Arial 12")
        lDate.place(x=30, y=HightY, width=90, height=25)
        OBJECTLIST.append(lDate)

        # Сумма операции
        lSum = tk.Label(self.frameMain, text=self.NumberIsString(drawNotes[5]), bg=colorbutton,
                        foreground="#ccc", font="Arial 12")
        lSum.place(x=125, y=HightY, width=140, height=25)
        OBJECTLIST.append(lSum)

        # Корреспондирующая статья
        namesource = ''
        if itemNotes == drawNotes[1]:
            namesource = db.RequestSelectDB('nameitem', 'items', 'id={}'.format(drawNotes[7]))
        elif itemNotes == drawNotes[7]:
            namesource = db.RequestSelectDB('nameitem', 'items', 'id={}'.format(drawNotes[1]))
        lSource = tk.Label(self.frameMain, text=namesource[0][0], bg=colorbutton, foreground="#ccc",
                           font="Arial 10")
        lSource.place(x=270, y=HightY, width=180, height=25)
        OBJECTLIST.append(lSource)

        # Кнопка отображения/скрытия дополнительных опций(удаления, корректировки, копирования)
        if self.CurrentWindow != 13:
            buttonOptions = tk.Button(self.frameMain, background="black", image=self.forward25_img)
            buttonOptions.place(x=455, y=HightY, width=25, height=25)
            buttonOptions.bind('<Button-1>', lambda eventbutton: self.DisplayOptionsButtons(drawNotes, itemNotes,
                                                                                            HightY, OBJECTLIST))
            OBJECTLIST.append(buttonOptions)

        # Описание операции
        if drawNotes[4]:
            lDescription = tk.Label(self.frameMain, text=drawNotes[4], bg="#808080", foreground="#ccc",
                                    font="Arial 10")
            lDescription.place(x=485, y=HightY, width=300, height=25)
            OBJECTLIST.append(lDescription)

    # Отображение кнопок с опциями (удалить, редактировать, копировать) в реестре операций
    def DisplayOptionsButtons(self, NOTE, ITEMID, HightY, OBJECTLIST):
        # Удаление кнопок допопций, если они уже есть
        for obj in OBJECTLIST:
            if obj.winfo_name == 'delete_button' or obj.winfo_name == 'correction_button' or\
                    obj.winfo_name == 'copy_button':
                obj.destroy()

        # Кнопка удаления
        buttonDelete = tk.Button(self.frameMain, background="black", name='delete_button', image=self.delete25_img)
        buttonDelete.place(x=505, y=HightY, width=25, height=25)
        buttonDelete.bind('<Button-1>', lambda eventbutton: self.AskAQuestion(NOTE, ITEMID, OBJECTLIST))
        OBJECTLIST.append(buttonDelete)

        DATA = db.RequestSelectDB('*', 'items', 'id={}'.format(ITEMID))[0]
        print('DisplayOptionsButtons = {}'.format(DATA))

        # Кнопка корректировки записи
        buttonCorrection = tk.Button(self.frameMain, background="black", name='correction_button',
                                     image=self.correction25_img)
        buttonCorrection.place(x=535, y=HightY, width=25, height=25)
        buttonCorrection.bind('<Button-1>', lambda eventbutton: self.DataCorrectWindow(DATA, NOTE))
        OBJECTLIST.append(buttonCorrection)

        # Кнопка копирования
        buttonCopy = tk.Button(self.frameMain, background="black", name='copy_button', image=self.copy_img)
        buttonCopy.place(x=565, y=HightY, width=25, height=25)
        buttonCopy.bind('<Button-1>', lambda eventbutton: self.DataCreateNewWindowCopy(DATA, NOTE))
        OBJECTLIST.append(buttonCopy)

    # Удаление записи с данными из реестра
    def DeleteNoteFromTheRegistry(self, NOTE, ITEMID, OBJECTLIST):
        print('Удалена запись из реестра')
        # Удаляем запись из БД
        db.DeleteNoteDB(NOTE)
        # Перерисовываем строки с данными
        self.DrawListOfRow(ITEMID, OBJECTLIST)
        # Пересчет и установка остатков при удалении операции
        db.RecalculatingBalances(NOTE[1], NOTE[7], NOTE[6], -(NOTE[5]))

    # Вопрос об удалении
    def AskAQuestion(self, NOTE, ITEMID, OBJECTLIST):
        # Очищаем строки и удаляем блок фильтра и блок постраничного пэйджинга
        if len(OBJECTLIST) != 0:
            for obj in OBJECTLIST:
                obj.destroy()

        # Надпись с вопросом
        nameitem = db.RequestSelectDB('nameitem', 'items', 'id={}'.format(ITEMID))[0][0]
        textQuestion = 'Удалить запись по статье:\n {} на сумму {} руб.\nВосстановление записи невозможно'.format(
            nameitem, NOTE[5])
        lQuestion = tk.Label(self.frameMain, text=textQuestion, bg='black', foreground="#ccc", font="Arial 16",
                             justify='center')
        lQuestion.place(x=100, y=150, width=600, height=70)
        OBJECTLIST.append(lQuestion)

        # Кнопка подтверждения
        buttonYes = tk.Button(self.frameMain, text='ДА', font="Arial 16", bg="#708090", foreground="#F5F5F5")
        buttonYes.place(x=320, y=250, width=80, height=40)
        buttonYes.bind('<Button-1>', lambda eventbutton: self.DeleteNoteFromTheRegistry(NOTE, ITEMID, OBJECTLIST))
        OBJECTLIST.append(buttonYes)

        # Кнопка отмены
        buttonNo = tk.Button(self.frameMain, text='НЕТ', font="Arial 12", bg="#708090", foreground="#F5F5F5")
        buttonNo.place(x=420, y=250, width=80, height=40)
        buttonNo.bind('<Button-1>', lambda eventbutton: self.DrawListOfRow(ITEMID, OBJECTLIST))
        OBJECTLIST.append(buttonNo)

        # Картинка с шредером
        shreder_paint = tk.Label(self.frameMain, bg='black', image=self.shreder_img)
        shreder_paint.place(x=200, y=320)
        OBJECTLIST.append(shreder_paint)

    # Окно создания новой записи в БД
    def DataCreateNewWindow(self, DATA):
        print('Создание новой записи данных')
        self.CurrentWindow = 8
        global bufferList

        # Отключаем отображаемые фреймы
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.BackWard(DATA[1]))

        # Картинка статьи
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.ImageList[DATA[8]])
        Main_paint.place(x=820, y=45)

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.DefineTextAndColor(DATA[1])

        # Наименование раздела
        l1 = tk.Label(self.frameMain, text=nameandcolor[0] + "/Ввод данных:", bg="black", foreground="#ccc",
                      font="Arial 25")
        l1.place(x=50, y=50)

        # Отображение полей для ввода и изменения данных
        self.ShowOperationInputFields('NEW', DATA)

        # Кнопка сохранения новой  статьи
        button_SaveNote = tk.Button(self.frameMain, text='Сохранить', name='button_Save',
                                    font="Arial 14", bg="#708090", foreground="#F5F5F5")
        button_SaveNote.place(x=50, y=600, width=200, height=40)
        button_SaveNote.bind('<Button-1>', lambda eventbutton: self.SaveNewOperation())

    # Окно создания новой записи в БД через копирование
    def DataCreateNewWindowCopy(self, DATA, NOTE):
        print('Создание новой записи данных через копирование')
        self.CurrentWindow = 10
        global bufferList

        # Отключаем отображаемые фреймы
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.BackWard(DATA))

        # Картинка статьи
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.ImageList[DATA[8]])
        Main_paint.place(x=820, y=45)

        # Запрос на наименование раздела и цвет кнопок
        print('DataCreateNewWindowCopy DATA = {}'.format(DATA))
        typeitem = DATA[1]
        nameandcolor = self.DefineTextAndColor(typeitem)

        # Наименование раздела
        l1 = tk.Label(self.frameMain, text=nameandcolor[0] + "/Копирование записи:", bg="black", foreground="#ccc",
                      font="Arial 25")
        l1.place(x=50, y=50)

        # Отображение полей для ввода и изменения данных
        self.ShowOperationInputFields('COPY', DATA, NOTE)

        # Кнопка сохранения новой  статьи
        button_SaveNote = tk.Button(self.frameMain, text='Сохранить', name='button_Save',
                                    font="Arial 14", bg="#708090", foreground="#F5F5F5")
        button_SaveNote.place(x=50, y=600, width=200, height=40)
        button_SaveNote.bind('<Button-1>', lambda eventbutton: self.SaveNewOperation(DATA))

    # Расчет кошелька и значений отображаемых полей
    def VariablesShowOperationInputFields(self, TYPEOPERATIONS, DATAITEM, NOTE=()):
        # TYPEOPERATIONS: "NEW", 'COPY', 'CORRECTION'
        # Установка заначений в буферном словаре
        global bufferList
        # [0"iditemkey"] - id статьи; [1"idtypeitemkey"] - id статьи; [2'dateoperationkey'] - дата операции;
        # [3'descriptionkey'] - Описание операции; # [4'sumoperationkey'] - сумма операции;
        # [5'increasekey'] - Направление (Уменьшение/Увеличение);
        # [6'sourcekey'] - Источник пополнения/ Изъятия(id статьи);
        # [7'typeinvestmentidkey'] - тип вложений (id типа вложений);
        # [8'countnotekey'] - количество вложений; [9'priseunit'] - цена единицы вложений

        textitem = ''
        textwallet = ''
        icon = self.arrowGreenRight_img

        if TYPEOPERATIONS == "NEW" and not bufferList:
            # Запрос к БД на id кошелька
            wallet = self.SearchWallet(DATAITEM)
            idtypewallet = 0

            if not wallet:
                idwallet = 0
                textwallet = ''
            else:
                idtypewallet = wallet[1]
                idwallet = wallet[0]

            increase = 0
            if DATAITEM[1] == 1:
                textitem = 'Статья дохода:'
                textwallet = 'Статья пополнения:'
                increase = 2
                icon = self.arrowDoubleGreen_img
            elif DATAITEM[1] == 2:
                textitem = 'Статья расхода:'
                if idtypewallet == 3:
                    textwallet = 'Статья списания:'
                    increase = 1
                    icon = self.arrowGreenLeft_img
                elif idtypewallet == 7:
                    textwallet = 'Статья пополнения:'
                    increase = 2
                    icon = self.arrowDoubleGreen_img
            elif DATAITEM[1] == 7 or DATAITEM[1] == 8:
                textitem = 'Статья пополнения:'
                textwallet = 'Статья пополнения:'
                increase = 2
                icon = self.arrowDoubleGreen_img
            else:
                textitem = 'Статья пополнения:'
                textwallet = 'Статья списания:'
                increase = 1
                icon = self.arrowGreenLeft_img

            # Если bufferList пустой, устанавливаем значения
            if not bufferList:
                bufferList = {'iditemkey': DATAITEM[0], 'idtypeitemkey': DATAITEM[1], 'dateoperationkey': db.todayDate,
                              'descriptionkey': '', 'sumoperationkey': 0, 'increasekey': increase,
                              'sourcekey': idwallet, 'typeinvestmentidkey': None, 'countnotekey': 0, 'priseunit': 0}

        elif TYPEOPERATIONS == 'COPY' or TYPEOPERATIONS == 'CORRECTION' or (TYPEOPERATIONS == "NEW" and bufferList):
            # Если bufferList пустой, устанавливаем значения
            if not bufferList:
                bufferList = {'iditemkey': NOTE[1], 'idtypeitemkey': NOTE[2], 'dateoperationkey': NOTE[3],
                              'descriptionkey': NOTE[4], 'sumoperationkey': NOTE[5], 'increasekey': NOTE[6],
                              'sourcekey': NOTE[7], 'typeinvestmentidkey': None, 'countnotekey': 0, 'priseunit': 0}
                if TYPEOPERATIONS == 'COPY':
                    bufferList['dateoperationkey'] = db.todayDate

            # Определяем раздел кошелька
            idtypeitemsourse = db.RequestSelectDB('typeitem_id', 'items', 'id={}'.format(bufferList['sourcekey']))
            if not idtypeitemsourse:
                idtypeitemsourse = 0
            else:
                idtypeitemsourse = idtypeitemsourse[0][0]

            if DATAITEM[1] == 1:
                textitem = 'Статья дохода:'
                if idtypeitemsourse in (3, 4, 5, 6):
                    textwallet = 'Статья пополнения:'
                    icon = self.arrowDoubleGreen_img
                elif idtypeitemsourse == 7 or idtypeitemsourse == 8:
                    textwallet = 'Статья списания:'
                    icon = self.arrowGreenLeft_img
                else:
                    textwallet = ''

            elif DATAITEM[1] == 2:
                textitem = 'Статья расхода:'
                if idtypeitemsourse in (3, 4, 5, 6):
                    textwallet = 'Статья списания:'
                    icon = self.arrowGreenLeft_img
                elif idtypeitemsourse == 7 or idtypeitemsourse == 8:
                    textwallet = 'Статья пополнения:'
                    icon = self.arrowDoubleGreen_img
                else:
                    textwallet = ''

            elif DATAITEM[1] == 7 or DATAITEM[1] == 8:
                if idtypeitemsourse in (3, 4, 5, 6):
                    if bufferList['increasekey'] == 2:
                        textitem = 'Статья пополнения:'
                        textwallet = 'Статья пополнения:'
                        icon = self.arrowDoubleGreen_img
                    elif bufferList['increasekey'] == 3:
                        textitem = 'Статья списания:'
                        textwallet = 'Статья списания:'
                        icon = self.arrowDoubleRed_img
                    else:
                        bufferList['increasekey'] = 2
                        textitem = 'Статья пополнения:'
                        textwallet = 'Статья пополнения:'
                        icon = self.arrowDoubleGreen_img

                elif idtypeitemsourse == 7 or idtypeitemsourse == 8:
                    if bufferList['increasekey'] == 1:
                        textitem = 'Статья пополнения:'
                        textwallet = 'Статья списания:'
                        icon = self.arrowGreenLeft_img
                    elif bufferList['increasekey'] == 0:
                        textitem = 'Статья списания:'
                        textwallet = 'Статья пополнения:'
                        icon = self.arrowRedRight_img
                    else:
                        bufferList['increasekey'] = 1
                        textitem = 'Статья пополнения:'
                        textwallet = 'Статья списания:'
                        icon = self.arrowGreenLeft_img
                else:
                    textitem = 'Статья пополнения:'
                    textwallet = ''
            else:
                if idtypeitemsourse in (3, 4, 5, 6):
                    if bufferList['increasekey'] == 1:
                        textitem = 'Статья пополнения:'
                        textwallet = 'Статья списания:'
                        icon = self.arrowGreenLeft_img
                    elif bufferList['increasekey'] == 0:
                        textitem = 'Статья списания:'
                        textwallet = 'Статья пополнения:'
                        icon = self.arrowRedRight_img
                    else:
                        bufferList['increasekey'] = 1
                        textitem = 'Статья пополнения:'
                        textwallet = 'Статья списания:'
                        icon = self.arrowGreenLeft_img

                elif idtypeitemsourse == 7 or idtypeitemsourse == 8:
                    if bufferList['increasekey'] == 2:
                        textitem = 'Статья пополнения:'
                        textwallet = 'Статья пополнения:'
                        icon = self.arrowDoubleGreen_img
                    elif bufferList['increasekey'] == 3:
                        textitem = 'Статья списания:'
                        textwallet = 'Статья списания:'
                        icon = self.arrowDoubleRed_img
                    else:
                        bufferList['increasekey'] = 2
                        textitem = 'Статья пополнения:'
                        textwallet = 'Статья пополнения:'
                        icon = self.arrowDoubleGreen_img
                else:
                    textitem = 'Статья пополнения:'
                    textwallet = ''

        AreaItemsAndWallets = {'textitem': textitem, 'textwallet': textwallet, 'icon': icon}

        return AreaItemsAndWallets

    # Отображение полей для ввода и изменения данных
    def ShowOperationInputFields(self, TYPEOPERATIONS, DATAITEM, NOTE=()):
        # Установка заначений в буферном словаре
        global bufferList
        AreaIW = self.VariablesShowOperationInputFields(TYPEOPERATIONS, DATAITEM, NOTE)
        # [0"iditemkey"] - id статьи; [1"idtypeitemkey"] - id статьи; [2'dateoperationkey'] - дата операции;
        # [3'descriptionkey'] - Описание операции; # [4'sumoperationkey'] - сумма операции;
        # [5'increasekey'] - Направление (Уменьшение/Увеличение);
        # [6'sourcekey'] - Источник пополнения/ Изъятия(id статьи);
        # [7'typeinvestmentidkey'] - тип вложений (id типа вложений);
        # [8'countnotekey'] - количество вложений; [9'priseunit'] - цена единицы вложений

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.DefineTextAndColor(bufferList['idtypeitemkey'])

        # Наименование статьи операции
        l2 = tk.Label(self.frameMain, name='label_signature_item', text=AreaIW['textitem'], bg="black",
                      foreground="#ccc", font="Arial 16")
        l2.place(x=50, y=100)

        labelItemOperation = tk.Label(self.frameMain, text=DATAITEM[2], name='label_ItemOperation',
                                      background=nameandcolor[1], foreground="#ccc", font="14", justify='center')
        labelItemOperation.place(x=50, y=130, width=300, height=45)

        # Кнопка переключения уменьшения/увеличения
        if bufferList['sourcekey'] != 0:
            if bufferList['idtypeitemkey'] == 1 or bufferList['idtypeitemkey'] == 2:
                paintIncrease = tk.Label(self.frameMain, name='label_Increase', bg='black', image=AreaIW['icon'])
                paintIncrease.place(x=379, y=130)
            else:
                buttonIncrease = tk.Button(self.frameMain, background='black', foreground="#ccc",
                                           highlightcolor="#C0C0C0", justify='center', image=AreaIW['icon'],
                                           name='button_Increase', command=self.IncreaseDecreaseModeSwitch)
                buttonIncrease.place(x=379, y=130)

        # Запрос к БД на наименование кошелька
        colorwallet = 'red'
        if bufferList['sourcekey'] == 0:
            namewallet = 'Кошельков нет'
        else:
            data2 = db.RequestSelectDB('*', 'items', 'id={}'.format(str(bufferList['sourcekey'])))
            namewallet = data2[0][2]
            colorwallet = self.DefineTextAndColor(data2[0][1])[1]

        # Наименование кошелька
        l3 = tk.Label(self.frameMain, name='label_signature_wallet', text=AreaIW['textwallet'], bg="black",
                      foreground="#ccc", font="Arial 16")
        l3.place(x=450, y=100)

        labelPayment = tk.Label(self.frameMain, text=namewallet, name='label_Payment', background=colorwallet,
                                foreground="#ccc", font="14", justify='center')
        labelPayment.place(x=450, y=130, width=300, height=45)

        # Кнопки выбора кошелька
        buttonLeft = tk.Button(self.frameMain, background="black", image=self.arrowLeft_img)
        buttonLeft.place(x=525, y=170, width=45, height=45)
        buttonLeft.bind('<Button-1>', lambda eventbutton: self.WalletSwitch(0, DATAITEM))

        buttonPayment = tk.Button(self.frameMain, background="black", image=self.payment_img)
        buttonPayment.place(x=575, y=170, width=45, height=45)
        buttonPayment.bind('<Button-1>', lambda eventbutton: self.ChoiceItemWriteDownsWindow(TYPEOPERATIONS, DATAITEM,
                                                                                             NOTE))

        buttonRight = tk.Button(self.frameMain, background="black", image=self.arrowRight_img)
        buttonRight.place(x=625, y=170, width=45, height=45)
        buttonRight.bind('<Button-1>', lambda eventbutton: self.WalletSwitch(1, DATAITEM))

        # Поле ввода даты
        l4 = tk.Label(self.frameMain, text="Дата операции:", bg="black", foreground="#ccc", font="Arial 16")
        l4.place(x=50, y=220)

        date = bufferList['dateoperationkey']
        if type(bufferList['dateoperationkey']) == str:
            date = dt.datetime.strptime(bufferList['dateoperationkey'], '%Y-%m-%d').date()
        tex2 = dt.date.strftime(date, '%d.%m.%Y')
        button_Date = tk.Button(self.frameMain, name='button_Date', text=tex2,
                                bg='#708090', font="Arial 25", foreground="#F5F5F5")
        button_Date.place(x=50, y=250, width=300, height=40)
        Data2 = (1, 50, 250, 300, 40, tex2, 'button_Date', 'Arial 25', '#708090', '#F5F5F5', tex2, 0)
        button_Date.bind('<Button-1>', lambda eventbutton: self.ChangeTheData(Data2))

        # Кнопка ввода суммы
        l5 = tk.Label(self.frameMain, text="Сумма операции:", bg="black", foreground="#ccc", font="Arial 16")
        l5.place(x=450, y=220)
        tex3 = self.NumberIsString(bufferList['sumoperationkey'])
        tex3_2 = bufferList['sumoperationkey']
        button_SumItem = tk.Button(self.frameMain, text=tex3, name='button_Sum',
                                   font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_SumItem.place(x=450, y=250, width=300, height=40)
        Data3 = (2, 450, 250, 300, 40, tex3, 'button_Sum', 'Arial 14', '#A9A9A9', '#F5F5F5', tex3_2, 0)
        button_SumItem.bind('<Button-1>', lambda eventbutton: self.ChangeTheData(Data3))

        # Поле ввода описания статьи
        l6 = tk.Label(self.frameMain, text="Описание операции:", bg="black", foreground="#ccc", font="Arial 16")
        l6.place(x=50, y=320)
        button_DescriptionItem = tk.Button(self.frameMain, text=bufferList['descriptionkey'], name='button_Description',
                                           wraplength=680, font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_DescriptionItem.place(x=50, y=350, width=700, height=50)
        Data4 = (3, 50, 350, 700, 50, bufferList['descriptionkey'], 'button_Description', 'Arial 14', '#A9A9A9',
                 '#F5F5F5', '', 0)
        button_DescriptionItem.bind('<Button-1>', lambda eventbutton: self.ChangeTheData(Data4))

    # Переключение режима уменьшения/увеличения статьи
    def IncreaseDecreaseModeSwitch(self):
        print('Переключение режима уменьшения/увеличения статьи')
        global bufferList
        icon = self.arrowGreenRight_img
        signature_item = 'Статья пополнения:'
        signature_wallet = 'Статья списания:'
        listobject = self.frameMain.place_slaves()

        # Запрос ID раздела кошелька
        idtypeitemsourse = db.RequestSelectDB('typeitem_id', 'items', 'id={}'.format(bufferList['sourcekey']))
        idtypeitemsourse = idtypeitemsourse[0][0]

        if bufferList['idtypeitemkey'] == 1:
            if idtypeitemsourse in (3, 4, 5, 6):
                bufferList['increasekey'] = 2
            elif idtypeitemsourse == 7 or idtypeitemsourse == 8:
                bufferList['increasekey'] = 1

        elif bufferList['idtypeitemkey'] == 2:
            if idtypeitemsourse in (3, 4, 5, 6):
                bufferList['increasekey'] = 1
            elif idtypeitemsourse == 7 or idtypeitemsourse == 8:
                bufferList['increasekey'] = 2

        else:
            if bufferList['increasekey'] == 0:
                bufferList['increasekey'] = 1
                icon = self.arrowGreenLeft_img
                signature_item = 'Статья пополнения:'
                signature_wallet = 'Статья списания:'
            elif bufferList['increasekey'] == 1:
                bufferList['increasekey'] = 0
                icon = self.arrowRedRight_img
                signature_item = 'Статья списания:'
                signature_wallet = 'Статья пополнения:'
            elif bufferList['increasekey'] == 2:
                bufferList['increasekey'] = 3
                icon = self.arrowDoubleRed_img
                signature_item = 'Статья списания:'
                signature_wallet = 'Статья списания:'
            elif bufferList['increasekey'] == 3:
                bufferList['increasekey'] = 2
                icon = self.arrowDoubleGreen_img
                signature_item = 'Статья пополнения:'
                signature_wallet = 'Статья пополнения:'

            print('increasekey {}'.format(bufferList['increasekey']))

        # Перебираем элементы страницы и устанавливливаем новые свойства
        for obj in listobject:
            if obj.winfo_name() == 'button_Increase':
                obj.config(image=icon)
            if obj.winfo_name() == 'label_signature_item':
                obj.config(text=signature_item)
            if obj.winfo_name() == 'label_signature_wallet':
                obj.config(text=signature_wallet)

    # Переключатель кошельков
    def WalletSwitch(self, side, DATAITEM):
        print('Wallet switch')
        global bufferList
        # Берем из буферного массива ID текущего кошелька
        currentwallet = bufferList['sourcekey']

        # Запрос к БД на массив кошельков
        if DATAITEM[1] == 2:
            wallets = db.RequestSelectDB('*', 'items', 'typeitem_id=3 or (typeitem_id=7 AND creditcard=1) AND id!={}'
                                                       ' AND workingitem=1'.format(DATAITEM[0]))
        else:
            wallets = db.RequestSelectDB('*', 'items', 'typeitem_id=3 AND id!={} AND workingitem=1'.format(DATAITEM[0]))

        if not wallets:
            return
        else:
            # Создаем и заполняем массив индексов кошельков
            listindex = list()
            ind = 0

            for i in range(0, len(wallets)):
                listindex.append(wallets[i][0])

            # Ищем индекс текущего кошелька и длину массива
            newwallet = currentwallet
            if currentwallet in listindex:
                ind = listindex.index(currentwallet)
                col = len(listindex)

                # Вычисляем индекс нового кошелька в зависимости от стороны прокрутки
                if side == 1:
                    if ind < (col - 1):
                        ind = ind + 1
                        newwallet = listindex[ind]
                    else:
                        ind = 0
                        newwallet = listindex[ind]
                elif side == 0:
                    if ind == 0:
                        ind = col - 1
                        newwallet = listindex[ind]
                    else:
                        ind = ind - 1
                        newwallet = listindex[ind]
            else:
                newwallet = listindex[0]

            # Устанавливаем индекс нового кошелька в буферный массив
            bufferList['sourcekey'] = newwallet

            # Изменяем наименование текущего кошелька, кнопки направления операции и описание кошелька на фрейме
            listobject = self.frameMain.place_slaves()

            for obj in listobject:
                if obj.winfo_name() == 'label_Payment':
                    obj.config(text=wallets[ind][2])

                if DATAITEM[1] == 2:

                    if obj.winfo_name() == 'label_Increase':
                        if wallets[ind][1] == 7:
                            obj.config(image=self.arrowDoubleGreen_img)
                            bufferList['increasekey'] = 2
                        else:
                            obj.config(image=self.arrowGreenLeft_img)
                            bufferList['increasekey'] = 1

                    if obj.winfo_name() == 'label_signature_wallet':
                        if wallets[ind][1] == 7:
                            obj.config(text='Статья пополнения:')
                        else:
                            obj.config(text='Статья списания:')

                elif DATAITEM[1] == 1:

                    if obj.winfo_name() == 'label_Increase':
                        obj.config(image=self.arrowDoubleGreen_img)
                        bufferList['increasekey'] = 2

                    if obj.winfo_name() == 'label_signature_wallet':
                        obj.config(text='Статья пополнения:')

    # Вычисление кошелька
    def SearchWallet(self, DATAITEM):
        # Запрос к БД на id кошелька
        data = db.RequestSelectDB('*', 'setting')
        idwallet = data[0][4]
        wallet = db.RequestSelectDB('*', 'items', 'id={}'.format(idwallet))

        # Не нашли такой кошелёк в БД
        if not wallet:
            wallet = self.SearchNewWallet(DATAITEM)
        # Нашли кошелёк
        else:
            wallet = wallet[0]
            # Найденный кошелёк не рабочий
            if wallet[3] == 0:
                wallet = self.SearchNewWallet(DATAITEM)
            # Найденный кошелёк рабочий
            else:
                if wallet[1] == 7:
                    if DATAITEM[1] == 2:
                        if wallet[0] == DATAITEM[0]:
                            wallet = self.SearchNewWallet(DATAITEM)
                        else:
                            return wallet
                    else:
                        wallet = self.SearchNewWallet(DATAITEM)
                else:
                    if wallet[0] == DATAITEM[0]:
                        wallet = self.SearchNewWallet(DATAITEM)
                    else:
                        return wallet

        print(wallet)
        return wallet

    # Поиск нового кошелька
    def SearchNewWallet(self, DATAITEM):
        print('SearchNewWallet')
        wallet = ()

        if DATAITEM[1] == 2:
            wallets = db.RequestSelectDB('*', 'items', 'typeitem_id=3 or (typeitem_id=7 AND creditcard=1) AND id!={}'
                                                       ' AND workingitem=1'.format(DATAITEM[0]))
            print(wallets)
        else:
            wallets = db.RequestSelectDB('*', 'items', 'typeitem_id=3 AND id!={} AND workingitem=1'.format(DATAITEM[0]))
            print(wallets)

        if not wallets:
            return wallet
        else:
            print('SearchNewWallet = {}'.format(wallets))
            wallet = wallets[0]

        return wallet

    # Сохранение операции
    def SaveNewOperation(self, DATA=()):
        global bufferList

        if bufferList['sumoperationkey'] != 0 and bufferList['sourcekey'] != 0:
            print('Сохранение операции')
            # Сохранение индекса нового текущего кошелька в БД
            wallets = db.RequestSelectDB('*', 'items', '(typeitem_id=3 or (typeitem_id=7 AND creditcard=1)) '
                                                       ' AND workingitem=1')
            wall = list()
            for wa in wallets:
                wall.append(wa[0])
            if bufferList['sourcekey'] in wall:
                db.UpdateNoteDB('setting', 'wallet', 'id', bufferList['sourcekey'], 1)
                print('В БД настроек изменен кошелек')

            # Сохранение операции
            db.AddNewOperation(bufferList)

            # Очищаем фрейм и отрисовываем список статей
            self.Clear()
            if self.CurrentWindow == 8:
                self.BackWard(bufferList['idtypeitemkey'])
            elif self.CurrentWindow == 10:
                self.BackWard(DATA)

            # чистим буферный словарь
            bufferList = {}
        else:
            if bufferList['sumoperationkey'] == 0:
                mb.showerror("Ошибка", "Сумма операции должна быть заполнена и не равняться нулю!!!")
            if bufferList['sourcekey'] == 0:
                mb.showerror("Ошибка", "Не выбрана коррелирующая статья для  сохранения операции!!!")

    # Выбор статьи списания / пополнения
    def ChoiceItemWriteDownsWindow(self, TYPEOPERATIONS, DATAITEM, NOTE=()):
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=0, y=0)
        if TYPEOPERATIONS == 'NEW':
            button_back.bind('<Button-1>', lambda event: self.DataCreateNewWindow(DATAITEM))
        elif TYPEOPERATIONS == 'COPY':
            button_back.bind('<Button-1>', lambda event: self.DataCreateNewWindowCopy(DATAITEM, NOTE))
        elif TYPEOPERATIONS == 'CORRECTION':
            button_back.bind('<Button-1>', lambda event: self.DataCorrectWindow(DATAITEM, NOTE))

        print('Окно выбора статьи списания/пополнения')
        wallets = db.RequestSelectDB('*', 'items', 'typeitem_id!=1 AND typeitem_id!=2 AND id!={}'
                                                   ' AND workingitem=1'.format(DATAITEM[0]))

        # Картинка статьи
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.ImageList[DATAITEM[8]])
        Main_paint.place(x=820, y=45)

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.DefineTextAndColor(DATAITEM[1])

        # Наименование раздела
        l1 = tk.Label(self.frameMain, text=nameandcolor[0] + "/Выбор связанной статьи :", bg="black",
                      foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=50)

        # Построение списка статей
        j = 0

        if 0 < len(wallets) <= 20:
            i = 1
            for DATA in wallets:
                if i % 2 != 0:
                    X = 50
                    Y = 50 * (i - j) + 50
                else:
                    j = j + 1
                    X = 450
                    Y = 50 * (i - j) + 50
                # Кнопка выбора статьи
                self.ButtonChangeSource(TYPEOPERATIONS, DATA, DATAITEM, NOTE, X, Y)
                i += 1

        elif len(wallets) > 20:
            # Определяем количество страниц и список для отрисовки
            count = len(wallets) // 20
            if len(wallets) % 20 != 0:
                count += 1

            if self.SettingFilter['currentPage'] > count:
                self.SettingFilter['currentPage'] = 1
            self.SettingFilter['countPage'] = count

            # Отбираем записи в зависимости от текущей страницы
            sortedPageList = list()
            countnotes = len(wallets)

            if self.SettingFilter['currentPage'] == 1:
                iBegin = 0
            else:
                iBegin = self.SettingFilter['currentPage'] * 20 - 20
            iEnd = self.SettingFilter['currentPage'] * 20
            if iEnd > countnotes:
                iEnd = countnotes

            for i in range(iBegin, iEnd):
                sortedPageList.append(wallets[i])
            data = sortedPageList

            # Отрисовываем отобранные записи
            i = 1
            for DATA in data:
                if i % 2 != 0:
                    X = 50
                    Y = 50 * (i - j) + 50
                else:
                    j = j + 1
                    X = 450
                    Y = 50 * (i - j) + 50

                # Кнопка выбора статьи
                self.ButtonChangeSource(TYPEOPERATIONS, DATA, DATAITEM, NOTE, X, Y)
                i += 1

            # Блок постраничного пейджинга
            pagetext = '{} из {}'.format(self.SettingFilter['currentPage'], self.SettingFilter['countPage'])
            # Кнопка перелистывания страниц влево
            buttonPageLeft = tk.Button(self.frameMain, name='page_Left', background="black", image=self.arrowLeft_img)
            buttonPageLeft.place(x=255, y=650, width=40, height=40)
            buttonPageLeft.bind('<Button-1>', lambda eventbutton: self.ChangePageSourceItem('PageForward',
                                                                                            TYPEOPERATIONS, DATAITEM,
                                                                                            NOTE))

            # Счетчик страниц
            lPageCounter = tk.Label(self.frameMain, name='page_Counter', text=pagetext, bg="#808080", foreground="#ccc",
                                    font="Arial 12")
            lPageCounter.place(x=300, y=650, width=100, height=40)

            # Кнопка перелистывания страниц вправо
            buttonPageRight = tk.Button(self.frameMain, name='page_Right', background="black",
                                        image=self.arrowRight_img)
            buttonPageRight.place(x=405, y=650, width=40, height=40)
            buttonPageRight.bind('<Button-1>', lambda eventbutton: self.ChangePageSourceItem('PageBack',
                                                                                             TYPEOPERATIONS, DATAITEM,
                                                                                             NOTE))

        elif len(wallets) == 0:
            # Надпись о том, что статьи в разделе отсутствуют
            l2 = tk.Label(self.frameMain, text="Отсутствуют доступные статьи для ввода выбора статьи."
                                               "\nСоздайте их и окне настроек.",
                          bg="black", foreground="#ccc", justify='left', font="Arial 16")
            l2.place(x=50, y=100)

    # Отображение кнопки выбора статьи
    def ButtonChangeSource(self, TYPEOPERATIONS, DATA, DATAITEM, NOTE, X, Y):
        COLOR = self.DefineTextAndColor(DATA[1])[1]

        # Кнопка выбора статьи
        button_Item = tk.Button(self.frameMain, text=DATA[2], bg=COLOR, font="Arial 12", foreground="#F5F5F5")
        button_Item.place(x=X, y=Y, width=200, height=40)
        button_Item.bind('<Button-1>', lambda event: self.ChangeSourceNote(TYPEOPERATIONS, DATA, DATAITEM, NOTE))

    # Изменяем статью2 и возвращаемся обратно
    def ChangeSourceNote(self, TYPEOPERATIONS, DATA, DATAITEM, NOTE):
        self.Clear()
        bufferList['sourcekey'] = DATA[0]

        if TYPEOPERATIONS == 'NEW':
            self.DataCreateNewWindow(DATAITEM)
        elif TYPEOPERATIONS == 'COPY':
            self.DataCreateNewWindowCopy(DATAITEM, NOTE)
        elif TYPEOPERATIONS == 'CORRECTION':
            self.DataCorrectWindow(DATAITEM, NOTE)

    # Изменение страницы в настройках статей
    def ChangePageSourceItem(self, change, TYPEOPERATIONS, DATAITEM, NOTE):
        # Изменение значений фильтрации при нажатии кнопок
        if change == 'PageForward':
            if self.SettingFilter['currentPage'] == self.SettingFilter['countPage']:
                self.SettingFilter['currentPage'] = 1
            else:
                self.SettingFilter['currentPage'] += 1

        elif change == 'PageBack':
            if self.SettingFilter['currentPage'] == 1:
                self.SettingFilter['currentPage'] = self.SettingFilter['countPage']
            else:
                self.SettingFilter['currentPage'] -= 1

        # Отрисовываем новые данные, пейджинг и фильтр
        self.ChoiceItemWriteDownsWindow(TYPEOPERATIONS, DATAITEM, NOTE)

    # Окно корректировки записи в БД
    def DataCorrectWindow(self, DATA, NOTE):
        print('Корректировка данных')
        self.CurrentWindow = 9
        # Отключаем отображаемые фреймы
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda event: self.BackWard(DATA))

        # Картинка статьи
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.ImageList[DATA[8]])
        Main_paint.place(x=820, y=45)

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.DefineTextAndColor(DATA[1])

        # Наименование раздела
        l1 = tk.Label(self.frameMain, text=nameandcolor[0] + "/Ввод данных:", bg="black", foreground="#ccc",
                      font="Arial 25")
        l1.place(x=50, y=50)

        # Отображение полей для ввода и изменения данных
        self.ShowOperationInputFields('CORRECTION', DATA, NOTE)

        # Кнопка сохранения изменений
        button_SaveNote = tk.Button(self.frameMain, text='Сохранить изменения', name='button_Save',
                                    font="Arial 14", bg="#708090", foreground="#F5F5F5")
        button_SaveNote.place(x=50, y=600, width=200, height=40)
        button_SaveNote.bind('<Button-1>', lambda eventbutton: self.SaveChangesOperation(DATA, NOTE))

    # Сохранение изменений после корректировки
    def SaveChangesOperation(self, DATA, NOTE):
        global bufferList

        if bufferList['sumoperationkey'] != 0:
            print('Сохранение изменений в операции')

            # Сохранение операции
            db.UpdateOperation(bufferList, NOTE)

            # Очищаем фрейм и отрисовываем список статей
            self.Clear()
            if self.CurrentWindow == 9:
                self.BackWard(DATA)

            # чистим буферный словарь
            bufferList = {}
        else:
            mb.showerror("Ошибка", "Сумма операции должна быть заполнена и не равняться нулю!!!")

    # Окно настройки системы
    def SettingWindow(self):
        self.CurrentWindow = 2
        self.Clear()
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)

        # Кнопка назад
        if db.use == 1:
            button_back = tk.Button(self.frameMain, image=self.back_img, bg='black', command=self.MenuWindow)
            button_back.place(x=0, y=0)

        # Наименование страницы
        l0 = tk.Label(self.frameMain, text="Настройка:", bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        # Картинка часового механизма
        time_paint = tk.Label(self.frameMain, bg='black', image=self.time_img)
        time_paint.place(x=820, y=75)

        # Поле ввода даты
        l1 = tk.Label(self.frameMain, text="Дата начала учета:", bg="black", foreground="#ccc", font="Arial 20")
        l1.place(x=50, y=60)
        date = dt.date.strftime(db.beginDate, '%d.%m.%Y')
        button_Date = tk.Button(self.frameMain, name='button_Date', text=date,
                                bg='#708090', font="Arial 25", foreground="#F5F5F5")
        button_Date.place(x=50, y=100, width=300, height=40)
        Data = (1, 50, 100, 300, 40, date, 'button_Date', 'Arial 25', '#708090', '#F5F5F5', date, 0)
        button_Date.bind('<Button-1>', lambda event: self.ChangeTheData(Data))

        # Предупреждение о смысле даты начала учета
        if db.use == 0:
            info_paint2 = tk.Label(self.frameMain, bg='black', image=self.info_img)
            info_paint2.place(x=450, y=100)
            l1_2 = tk.Label(self.frameMain, text="Данные можно вводить\n не ранее даты начала учета!!!:",
                            bg="black", foreground="#ccc", font="Arial 14")
            l1_2.place(x=500, y=100)

        # Блок настройки статей доходов и расходов
        l2 = tk.Label(self.frameMain, text="Настройка статей учета:", bg="black", foreground="#ccc", font="Arial 20")
        l2.place(x=50, y=160)

        button_IncomeSetting = tk.Button(self.frameMain, text='Настройка статей доходов', bg='#F08080', font="Arial 16",
                                         foreground="#F5F5F5")
        button_IncomeSetting.place(x=50, y=200, width=360, height=40)
        button_IncomeSetting.bind('<Button-1>', lambda event: self.ListItemSettingWindow(1))

        button_CostsSetting = tk.Button(self.frameMain, text='Настройка статей расходов', bg='#BA55D3', font="Arial 16",
                                        foreground="#F5F5F5")
        button_CostsSetting.place(x=450, y=200, width=360, height=40)
        button_CostsSetting.bind('<Button-1>', lambda event: self.ListItemSettingWindow(2))

        # Запрос к БД на данные по разделам
        data = db.RequestSelectDB('*', 'typeitems')

        # Блок настройки статей актива
        l3 = tk.Label(self.frameMain, text="АКТИВ:", bg="black", foreground="#C71585", font="Arial 25")
        l3.place(x=50, y=250)

        button_MoneySetting = tk.Button(self.frameMain, text=data[2][2], bg='#DB7093', font="Arial 14",
                                        foreground="#F5F5F5")
        button_MoneySetting.place(x=50, y=300, width=200, height=40)
        button_MoneySetting.bind('<Button-1>', lambda event: self.ListItemSettingWindow(3))
        s1 = tk.Label(self.frameMain, text=self.NumberIsString(data[2][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s1.place(x=255, y=300, width=150, height=40)

        button_PropertySetting = tk.Button(self.frameMain, text=data[3][2], bg='#DB7093', font="Arial 14",
                                           foreground="#F5F5F5")
        button_PropertySetting.place(x=50, y=350, width=200, height=40)
        button_PropertySetting.bind('<Button-1>', lambda event: self.ListItemSettingWindow(4))
        s2 = tk.Label(self.frameMain, text=self.NumberIsString(data[3][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s2.place(x=255, y=350, width=150, height=40)

        button_InvestmentsSetting = tk.Button(self.frameMain, text=data[4][2], bg='#DB7093', font="Arial 14",
                                              foreground="#F5F5F5")
        button_InvestmentsSetting.place(x=50, y=400, width=200, height=40)
        button_InvestmentsSetting.bind('<Button-1>', lambda event: self.ListItemSettingWindow(5))
        s3 = tk.Label(self.frameMain, text=self.NumberIsString(data[4][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s3.place(x=255, y=400, width=150, height=40)

        button_LoansIssuedSetting = tk.Button(self.frameMain, text=data[5][2], bg='#DB7093', font="Arial 14",
                                              foreground="#F5F5F5")
        button_LoansIssuedSetting.place(x=50, y=450, width=200, height=40)
        button_LoansIssuedSetting.bind('<Button-1>', lambda event: self.ListItemSettingWindow(6))
        s4 = tk.Label(self.frameMain, text=self.NumberIsString(data[5][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s4.place(x=255, y=450, width=150, height=40)

        # Блок настройки статей пассива
        l4 = tk.Label(self.frameMain, text="ПАССИВ:", bg="black", foreground="#800080", font="Arial 25")
        l4.place(x=450, y=250)

        button_CreditSetting = tk.Button(self.frameMain, text=data[6][2], bg='#DA70D6', font="Arial 14",
                                         foreground="#F5F5F5")
        button_CreditSetting.place(x=450, y=300, width=200, height=40)
        button_CreditSetting.bind('<Button-1>', lambda event: self.ListItemSettingWindow(7))
        s5 = tk.Label(self.frameMain, text=self.NumberIsString(data[6][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s5.place(x=655, y=300, width=150, height=40)

        button_LoansSetting = tk.Button(self.frameMain, text=data[7][2], bg='#DA70D6', font="Arial 14",
                                        foreground="#F5F5F5")
        button_LoansSetting.place(x=450, y=350, width=200, height=40)
        button_LoansSetting.bind('<Button-1>', lambda event: self.ListItemSettingWindow(8))
        s6 = tk.Label(self.frameMain, text=self.NumberIsString(data[7][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s6.place(x=655, y=350, width=150, height=40)

        # Информация об собственном капитале
        l5 = tk.Label(self.frameMain, text=data[8][2], bg='#DA70D6', foreground="#F5F5F5", font="Arial 14")
        l5.place(x=450, y=450, width=200, height=40)
        s7 = tk.Label(self.frameMain, text=self.NumberIsString(data[8][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s7.place(x=655, y=450, width=150, height=40)

        # Блок дополнительных настроек
        l6 = tk.Label(self.frameMain, text="Дополнительные настройки:", bg="black", foreground="#ccc",
                      font="Arial 20")
        l6.place(x=50, y=510)

        # costkm_Setting = tk.Button(self.frameMain, text='НЕ учитывать пробег', bg='#708090', font="Arial 16",
        #                           foreground="#F5F5F5")
        # costkm_Setting.place(x=50, y=550, width=350, height=40)
        # costkm_Setting.bind('<Button-1>', lambda event: self.ChangeTheDate())

        parol_Setting = tk.Button(self.frameMain, text='Смена пароля', bg='#708090', font="Arial 16",
                                  foreground="#F5F5F5")
        parol_Setting.place(x=50, y=550, width=350, height=40)
        # parol_Setting.bind('<Button-1>', lambda event: self.ChangeTheDate())

        image_Setting = tk.Button(self.frameMain, text='Настройка изображений', bg='#708090', font="Arial 16",
                                  foreground="#F5F5F5")
        image_Setting.place(x=50, y=600, width=350, height=40)
        # image_Setting.bind('<Button-1>', lambda event: self.ChangeTheDate())

        # Блок начала работы
        if db.use == 0:
            info_paint1 = tk.Label(self.frameMain, bg='black', image=self.info_img)
            info_paint1.place(x=580, y=5)
            l7 = tk.Label(self.frameMain,
                          text="После настройки необходимых параметров \nнажмите кнопку начать для начала работы:",
                          bg="black", foreground="#ccc", font="Arial 14")
            l7.place(x=630, y=1)
            info_paint3 = tk.Label(self.frameMain, bg='black', image=self.right_img)
            info_paint3.place(x=1030, y=3)
            button_Begin = tk.Button(self.frameMain, text='Начать', bg='#708090', font="Arial 20", foreground="#F5F5F5")
            button_Begin.place(x=1077, y=5, width=200, height=40)
            button_Begin.bind('<Button-1>', lambda event: self.StartOfWork())

        print('Окно настроек')

    # Переход на основную страницу и создание БД
    def StartOfWork(self):
        self.Clear()
        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)
        if ospath.exists('setting.db'):
            # Запрос к БД на id кошелька и изменение даты стартовых статей на дату начала учета
            data = db.RequestSelectDB('*', 'items', 'typeitem_id=3')
            tex = data[0][0]

            # Запрос к БД на запись параметра рабочей программы и кошелька по умолчанию
            db.UpdateNoteDB('setting', 'use', 'id', 1, 1)
            db.UpdateNoteDB('setting', 'wallet', 'id', tex, 1)
            db.use = 1
        else:
            print('WARNING!!! No setting.db')

        # Создаем БД для внесения записей и запускаем основное окно программы
        db.CreateBDforNotes()
        self.MainWindow()

    # Выход из программы
    def ExitTheProgram(self):
        root.quit()

    # Окно настройки статей
    def ListItemSettingWindow(self, idtypeitem):
        print('Окно настройки статей')
        self.CurrentWindow = 3
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda event: self.BackWard(0))

        # Наименование страницы
        TextAndColor = self.DefineTextAndColor(idtypeitem)
        texthead = 'Настройка/{}:'.format(TextAndColor[0])
        l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        # Запрос к БД на перечень статей в разделе
        data = db.RequestSelectDB('*', 'items', 'typeitem_id={}'.format(idtypeitem))

        # Построение списка статей
        j = 0
        X = 50
        Y = 100

        if 0 < len(data) < 20:
            i = 1
            for DATA in data:
                if i % 2 != 0:
                    X = 50
                    Y = 50 * (i - j) + 50
                else:
                    j = j + 1
                    X = 450
                    Y = 50 * (i - j) + 50
                # Кнопка настройки статьи
                if DATA[3] == 0:
                    COLOR = '#2F4F4F'
                else:
                    COLOR = TextAndColor[1]

                self.ButtonItem(DATA, COLOR, X, Y)
                i += 1

            if X == 50:
                X = 450
            else:
                X = 50
                Y = Y + 50

            # Кнопка создания новой статьи
            button_AddItem = tk.Button(self.frameMain, text=' Добавить статью ', compound=tk.RIGHT, image=self.plus_img,
                                       bg=TextAndColor[1], font="Arial 14", foreground="#F5F5F5")
            button_AddItem.place(x=X, y=Y, width=200, height=40)
            button_AddItem.bind('<Button-1>', lambda event: self.ItemCreateNewWindow(idtypeitem))

        elif len(data) == 20:
            i = 1
            for DATA in data:
                if i % 2 != 0:
                    X = 50
                    Y = 50 * (i - j) + 50
                else:
                    j = j + 1
                    X = 450
                    Y = 50 * (i - j) + 50
                # Кнопка настройки статьи
                if DATA[3] == 0:
                    COLOR = '#2F4F4F'
                else:
                    COLOR = TextAndColor[1]

                self.ButtonItem(DATA, COLOR, X, Y)
                i += 1

            # Кнопка создания новой статьи
            button_AddItem = tk.Button(self.frameMain, text=' Добавить статью ', compound=tk.RIGHT, image=self.plus_img,
                                       bg=TextAndColor[1], font="Arial 14", foreground="#F5F5F5")
            button_AddItem.place(x=50, y=650, width=200, height=40)
            button_AddItem.bind('<Button-1>', lambda event: self.ItemCreateNewWindow(idtypeitem))

        elif len(data) > 20:
            # Определяем количество страниц и список для отрисовки
            count = len(data) // 20
            if len(data) % 20 != 0:
                count += 1

            if self.SettingFilter['currentPage'] > count:
                self.SettingFilter['currentPage'] = 1
            self.SettingFilter['countPage'] = count

            # Отбираем записи в зависимости от текущей страницы
            sortedPageList = list()
            countnotes = len(data)

            if self.SettingFilter['currentPage'] == 1:
                iBegin = 0
            else:
                iBegin = self.SettingFilter['currentPage'] * 20 - 20
            iEnd = self.SettingFilter['currentPage'] * 20
            if iEnd > countnotes:
                iEnd = countnotes

            for i in range(iBegin, iEnd):
                sortedPageList.append(data[i])
            data = sortedPageList

            # Отрисовываем отобранные записи
            i = 1
            for DATA in data:
                if i % 2 != 0:
                    X = 50
                    Y = 50 * (i - j) + 50
                else:
                    j = j + 1
                    X = 450
                    Y = 50 * (i - j) + 50
                # Кнопка настройки статьи
                if DATA[3] == 0:
                    COLOR = '#696969'
                else:
                    COLOR = TextAndColor[1]

                self.ButtonItem(DATA, COLOR, X, Y)
                i += 1

            # Кнопка создания новой статьи
            button_AddItem = tk.Button(self.frameMain, text=' Добавить статью ', compound=tk.RIGHT, image=self.plus_img,
                                       bg=TextAndColor[1], font="Arial 14", foreground="#F5F5F5")
            button_AddItem.place(x=50, y=650, width=200, height=40)
            button_AddItem.bind('<Button-1>', lambda event: self.ItemCreateNewWindow(idtypeitem))

            # Блок постраничного пейджинга
            pagetext = '{} из {}'.format(self.SettingFilter['currentPage'], self.SettingFilter['countPage'])
            # Кнопка перелистывания страниц влево
            buttonPageLeft = tk.Button(self.frameMain, name='page_Left', background="black", image=self.arrowLeft_img)
            buttonPageLeft.place(x=255, y=650, width=40, height=40)
            buttonPageLeft.bind('<Button-1>', lambda eventbutton: self.ChangePageSettingItem('PageForward', idtypeitem))

            # Счетчик страниц
            lPageCounter = tk.Label(self.frameMain, name='page_Counter', text=pagetext, bg="#808080", foreground="#ccc",
                                    font="Arial 12")
            lPageCounter.place(x=300, y=650, width=100, height=40)

            # Кнопка перелистывания страниц вправо
            buttonPageRight = tk.Button(self.frameMain, name='page_Right', background="black",
                                        image=self.arrowRight_img)
            buttonPageRight.place(x=405, y=650, width=40, height=40)
            buttonPageRight.bind('<Button-1>', lambda eventbutton: self.ChangePageSettingItem('PageBack', idtypeitem))

        elif len(data) == 0:
            # Кнопка создания новой статьи
            button_AddItem = tk.Button(self.frameMain, text=' Добавить статью ', compound=tk.RIGHT, image=self.plus_img,
                                       bg=TextAndColor[1], font="Arial 14", foreground="#F5F5F5")
            button_AddItem.place(x=50, y=100, width=200, height=40)
            button_AddItem.bind('<Button-1>', lambda event: self.ItemCreateNewWindow(idtypeitem))

        # Картинка  типа статьи
        time_paint = tk.Label(self.frameMain, bg='black', image=self.ImageItem(idtypeitem))
        time_paint.place(x=820, y=75)

    # Изменение страницы в настройках статей
    def ChangePageSettingItem(self, change, ITEMID):
        # Изменение значений фильтрации при нажатии кнопок
        if change == 'PageForward':
            if self.SettingFilter['currentPage'] == self.SettingFilter['countPage']:
                self.SettingFilter['currentPage'] = 1
            else:
                self.SettingFilter['currentPage'] += 1

        elif change == 'PageBack':
            if self.SettingFilter['currentPage'] == 1:
                self.SettingFilter['currentPage'] = self.SettingFilter['countPage']
            else:
                self.SettingFilter['currentPage'] -= 1

        # Отрисовываем новые данные, пейджинг и фильтр
        self.ListItemSettingWindow(ITEMID)

    # Кнопка настройки статьи
    def ButtonItem(self, DATA, COLOR, X, Y):
        # Кнопка настройки статьи
        button_Item = tk.Button(self.frameMain, text=DATA[2], bg=COLOR, font="Arial 12", foreground="#F5F5F5")
        button_Item.place(x=X, y=Y, width=200, height=40)
        button_Item.bind('<Button-1>', lambda eventbutton: self.ItemCorrectWindow(DATA))

        if DATA[1] == 3 or DATA[1] == 4 or DATA[1] == 5 or DATA[1] == 6 or DATA[1] == 7 or DATA[1] == 8:
            tex = self.NumberIsString(DATA[6])
            sumItem = tk.Label(self.frameMain, text=tex, bg="#A9A9A9", foreground="#F5F5F5", font="Arial 12")
            sumItem.place(x=X + 205, y=Y, width=150, height=40)

    # Окно корректировки статьи
    def ItemCorrectWindow(self, DATA):
        print('correct item')
        self.CurrentWindow = 4
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.BackWard(DATA[1]))

        # Наименование страницы
        TextAndColor = self.DefineTextAndColor(DATA[1])
        texthead = 'Настройка/{}/Корректировка статьи:'.format(TextAndColor[0])
        l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        # Картинка статьи
        time_paint = tk.Label(self.frameMain, bg='black', image=self.ImageList[DATA[8]])
        time_paint.place(x=820, y=75)

        # Поле ввода наименования статьи
        tex1 = DATA[2]
        l1 = tk.Label(self.frameMain, text="Наименование статьи:", bg="black", foreground="#ccc",
                      font="Arial 20")
        l1.place(x=50, y=60)
        button_NameItem = tk.Button(self.frameMain, text=tex1, name='button_Name', font="Arial 14", bg="#A9A9A9",
                                    foreground="#F5F5F5")
        button_NameItem.place(x=50, y=100, width=700, height=40)
        Data1 = (0, 50, 100, 700, 40, tex1, 'button_Name', 'Arial 14', '#A9A9A9', '#F5F5F5', tex1, DATA[0])
        button_NameItem.bind('<Button-1>', lambda eventbutton: self.ChangeTheData(Data1))

        # Кнопка редактирования суммы
        if DATA[1] != 1 and DATA[1] != 2:
            l3 = tk.Label(self.frameMain, text="Начальный остаток:", bg="black", foreground="#ccc", font="Arial 20")
            l3.place(x=50, y=160)
            tex3 = self.NumberIsString(DATA[6])
            tex33 = '{0:.2f}'.format(DATA[6])
            button_SumItem = tk.Button(self.frameMain, text=tex3, name='button_Sum', font="Arial 14", bg="#A9A9A9",
                                       foreground="#F5F5F5")
            button_SumItem.place(x=50, y=200, width=300, height=40)
            Data3 = (2, 50, 200, 300, 40, tex3, 'button_Sum', 'Arial 14', '#A9A9A9', '#F5F5F5', tex33, DATA[0])
            button_SumItem.bind('<Button-1>', lambda eventbutton: self.ChangeTheData(Data3))

        # Кнопка изменения картинки для статьи
        button_Image = tk.Button(self.frameMain, name='button_Date', text='Картинка', bg='#708090', font="Arial 25",
                                 foreground="#F5F5F5")
        button_Image.place(x=450, y=200, width=300, height=40)
        button_Image.bind('<Button-1>', lambda event: self.SelectImageWindow('CORRECTION', DATA, DATA[8]))

        # Поле ввода описания статьи
        l4 = tk.Label(self.frameMain, text="Описание статьи:", bg="black", foreground="#ccc", font="Arial 20")
        l4.place(x=50, y=260)
        tex4 = DATA[4]
        button_DescriptionItem = tk.Button(self.frameMain, text=tex4, name='button_Description', wraplength=680,
                                           font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_DescriptionItem.place(x=50, y=300, width=700, height=50)
        Data4 = (3, 50, 300, 700, 50, tex4, 'button_Description', 'Arial 14', '#A9A9A9', '#F5F5F5', tex4, DATA[0])
        button_DescriptionItem.bind('<Button-1>', lambda eventbutton: self.ChangeTheData(Data4))

        # Кнопка назначения кредитной картой
        if DATA[1] == 7:
            texcredit = ''
            COLOR = '#696969'
            if DATA[5] == 0:
                texcredit = 'Не  кредитная карта'
                COLOR = '#696969'
            elif DATA[5] == 1:
                texcredit = 'Кредитная карта'
                COLOR = "#DA70D6"

            button_Credit = tk.Button(self.frameMain, text=texcredit, name='button_Credit', font="Arial 14",
                                      bg=COLOR, foreground="#F5F5F5")
            button_Credit.place(x=50, y=370, width=200, height=40)
            button_Credit.bind('<Button-1>', lambda event: self.CreditItemSwitch(DATA[0]))

            # Информация о смысле назначить статью кредитной картой
            info_paint2 = tk.Label(self.frameMain, bg='black', image=self.info_img)
            info_paint2.place(x=270, y=367)
            texinfo = "Кредитная карта будет добавлена в список кошельков\nдля быстого выбора при оплате расходов"
            l5 = tk.Label(self.frameMain, text=texinfo, bg="black", foreground="#ccc", font="Arial 14", justify='left')
            l5.place(x=320, y=365)

        if db.use != 0:
            COLORCLOSE = ''
            TEXTCLOSE = ''
            if DATA[3] == 0:
                COLORCLOSE = '#696969'
                TEXTCLOSE = 'Закрытая статья'
            elif DATA[3] == 1:
                COLORCLOSE = TextAndColor[1]
                TEXTCLOSE = 'Рабочая статья'

            l6 = tk.Label(self.frameMain, text="Закрытие статьи:", bg="black", foreground="#ccc", font="Arial 20")
            l6.place(x=50, y=440)
            button_Close = tk.Button(self.frameMain, text=TEXTCLOSE, name='button_Close', font="Arial 14",
                                     bg=COLORCLOSE, foreground="#F5F5F5")
            button_Close.place(x=50, y=480, width=200, height=40)
            button_Close.bind('<Button-1>', lambda event: self.CloseItemSwitch(DATA[0]))

            # Информация о смысле назначить статью кредитной картой
            info_paint3 = tk.Label(self.frameMain, bg='black', image=self.info_img)
            info_paint3.place(x=270, y=477)
            texinfo = "Закрытую статью нельзя выбрать\nпри созданиии и корректировке данных"
            l7 = tk.Label(self.frameMain, text=texinfo, bg="black", foreground="#ccc", font="Arial 14", justify='left')
            l7.place(x=320, y=475)

        if DATA[9] == 1:
            # Кнопка удаления статьи
            button_DeleteItem = tk.Button(self.frameMain, text='Удалить', name='button_Delete',
                                          font="Arial 14", bg="#FF0000", foreground="#F5F5F5")
            button_DeleteItem.place(x=50, y=600, width=200, height=40)
            button_DeleteItem.bind('<Button-1>', lambda event: self.AskAQuestionItem(DATA))
        elif DATA[9] == 0:
            label_StartItem = tk.Label(self.frameMain, text='Не удалить', font="Arial 14", bg="#5F9EA0",
                                       foreground="#F5F5F5")
            label_StartItem.place(x=50, y=600, width=200, height=40)

    # Страница выбора картинки
    def SelectImageWindow(self, TYPE, DATAITEM, IND=100):
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black')
        button_back.place(x=0, y=0)
        if TYPE == 'NEW':
            button_back.bind('<Button-1>', lambda eventbutton: self.ItemCreateNewWindow(DATAITEM))
        elif TYPE == 'CORRECTION':
            button_back.bind('<Button-1>', lambda eventbutton: self.ItemCorrectWindow(DATAITEM))

        # Наименование страницы
        if TYPE == 'NEW':
            TextAndColor = self.DefineTextAndColor(DATAITEM)
        else:
            TextAndColor = self.DefineTextAndColor(DATAITEM[1])

        texthead = 'Настройка/{}/Выбор изображения:'.format(TextAndColor[0])
        l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        countImage = len(self.ImageList)

        numberImageItem = 0
        if IND == 100:
            numberImageItem = 7
        else:
            if IND < 0:
                numberImageItem = countImage - 1
            elif IND > countImage - 1:
                numberImageItem = 0
            else:
                numberImageItem = IND

        listInd = list()
        numL, numR = numberImageItem, numberImageItem
        for i in range(3):
            if numR + 1 <= countImage - 1:
                numR += 1
            else:
                numR = 0
            listInd.append(numR)

            if numL - 1 < 0:
                numL = countImage - 1
            else:
                numL -= 1
            listInd.append(numL)

        print(listInd)

        # Картинки слева
        l_paint1 = tk.Label(self.frameMain, bg='black', image=self.ImageList[listInd[5]])
        l_paint1.place(x=0, y=110)

        l_paint2 = tk.Label(self.frameMain, bg='black', image=self.ImageList[listInd[3]])
        l_paint2.place(x=140, y=105)

        l_paint3 = tk.Label(self.frameMain, bg='black', image=self.ImageList[listInd[1]])
        l_paint3.place(x=280, y=100)

        # Картинки справа
        l_paint4 = tk.Label(self.frameMain, bg='black', image=self.ImageList[listInd[4]])
        l_paint4.place(x=840, y=40)

        l_paint5 = tk.Label(self.frameMain, bg='black', image=self.ImageList[listInd[2]])
        l_paint5.place(x=700, y=45)

        l_paint6 = tk.Label(self.frameMain, bg='black', image=self.ImageList[listInd[0]])
        l_paint6.place(x=560, y=50)

        # Кнопка выбора
        button_image = tk.Button(self.frameMain, image=self.ImageList[numberImageItem], bg='black')
        button_image.place(x=420, y=75, width=440, height=600)
        button_image.bind('<Button-1>', lambda eventbutton: self.ButtonImage(TYPE, numberImageItem, DATAITEM))

        # Блок постраничного пейджинга
        pagetext = '{} из {}'.format(numberImageItem+1, countImage)
        # Кнопка перелистывания страниц влево
        buttonPageLeft = tk.Button(self.frameMain, name='page_Left', background="black", image=self.arrowLeft_img)
        buttonPageLeft.place(x=535, y=680, width=40, height=40)
        buttonPageLeft.bind('<Button-1>', lambda eventbutton: self.SelectImageWindow(TYPE, DATAITEM, numberImageItem-1))

        # Счетчик страниц
        lPageCounter = tk.Label(self.frameMain, name='page_Counter', text=pagetext, bg="#808080", foreground="#ccc",
                                font="Arial 12")
        lPageCounter.place(x=580, y=680, width=100, height=40)

        # Кнопка перелистывания страниц вправо
        buttonPageRight = tk.Button(self.frameMain, name='page_Right', background="black",
                                    image=self.arrowRight_img)
        buttonPageRight.place(x=685, y=680, width=40, height=40)
        buttonPageRight.bind('<Button-1>', lambda eventbutton: self.SelectImageWindow(TYPE, DATAITEM, numberImageItem+1))

    # Кнопка-картинка
    def ButtonImage(self, TYPE, IND, DATAITEM):
        global bufferList
        if TYPE == 'NEW':
            bufferList[6] = IND
            self.ItemCreateNewWindow(DATAITEM)
        elif TYPE == 'CORRECTION':
            db.UpdateNoteDB('items', 'paintitem', 'id', IND, DATAITEM[0])
            DATAITEM = db.RequestSelectDB('*', 'items', 'id={}'.format(DATAITEM[0]))[0]
            self.ItemCorrectWindow(DATAITEM)

    # Вопрос об удалении
    def AskAQuestionItem(self, DATA):
        notes = list()
        if db.use == 1:
            notes = db.RequestSelectDB('*', 'notes', 'item_id={} OR source={}'.format(DATA[0], DATA[0]))

        if not notes:
            # Очищаем страницу
            self.Clear()

            # Наименование страницы
            TextAndColor = self.DefineTextAndColor(DATA[1])
            texthead = 'Настройка/{}/Удаление статьи:'.format(TextAndColor[0])
            l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
            l0.place(x=50, y=0)

            # Картинка часового механизма
            time_paint = tk.Label(self.frameMain, bg='black', image=self.time_img)
            time_paint.place(x=820, y=75)

            # Надпись с вопросом
            textQuestion = 'Удалить статью: {}?\nВосстановление статьи невозможно'.format(DATA[2])
            lQuestion = tk.Label(self.frameMain, text=textQuestion, bg='black', foreground="#ccc", font="Arial 16",
                                 justify='center')
            lQuestion.place(x=100, y=150, width=600, height=70)

            # Кнопка подтверждения
            buttonYes = tk.Button(self.frameMain, text='ДА', font="Arial 16", bg="#708090", foreground="#F5F5F5")
            buttonYes.place(x=320, y=250, width=80, height=40)
            buttonYes.bind('<Button-1>', lambda eventbutton: self.DeleteItem(DATA))

            # Кнопка отмены
            buttonNo = tk.Button(self.frameMain, text='НЕТ', font="Arial 12", bg="#708090", foreground="#F5F5F5")
            buttonNo.place(x=420, y=250, width=80, height=40)
            buttonNo.bind('<Button-1>', lambda eventbutton: self.ItemCorrectWindow(DATA))

            # Картинка с шредером
            shreder_paint = tk.Label(self.frameMain, bg='black', image=self.shreder_img)
            shreder_paint.place(x=200, y=320)
        else:
            mb.showerror("Ошибка", "Нельзя удалить статью, содержащую записи об операциях, удалите все записи!!!")

    # Закрытие статьи
    def CloseItemSwitch(self, IDITEM):
        DATA = db.RequestSelectDB('*', 'items', 'id={}'.format(IDITEM))[0]
        LIST = db.RequestSelectDB('*', 'items', 'typeitem_id={} AND workingitem=1'.format(DATA[1]))

        if DATA[3] == 0 and len(LIST) >= 20:
            mb.showerror("Ошибка", "Рабочих статей на может быть больше 20\n"
                         "Удалите или закрой неиспользуемые статьи")
            return

        TextAndColor = self.DefineTextAndColor(DATA[1])
        listobject = self.frameMain.place_slaves()
        for obj in listobject:
            if obj.winfo_name() == 'button_Close':
                if DATA[3] == 0:
                    obj.config(text='Рабочая статья', bg=TextAndColor[1])
                    db.UpdateNoteDB('items', 'workingitem', 'id', 1, DATA[0])
                elif DATA[3] == 1:
                    obj.config(text='Закрытая статья', bg="#696969")
                    db.UpdateNoteDB('items', 'workingitem', 'id', 0, DATA[0])

    # Удаление статьи из БД
    def DeleteItem(self, DATA):
        print('Delete Item')
        global bufferList

        # Удаляем  статью из БД
        db.DeleteItemDB(DATA[0])

        # Отрисовываем список статей
        self.ListItemSettingWindow(DATA[1])

        # чистим буферный динамический массив
        bufferList = list()

    # Окно создания новой статьи
    def ItemCreateNewWindow(self, idtypeitem):
        print('Create NEW item')
        if len(db.RequestSelectDB('*', 'items', 'typeitem_id={} AND workingitem=1'.format(idtypeitem))) >= 20:
            mb.showerror("Ошибка", "Рабочих статей на может быть больше 20\n"
                                   "Удалите или закрой неиспользуемые статьи")
            return
        global bufferList
        self.CurrentWindow = 11
        self.Clear()

        if not bufferList:
            # Установка заначений в буферном динамическим массиве
            bufferList = [idtypeitem, '', 1, '', 0, 0, self.ImageItemInt(idtypeitem)]

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda event: self.BackWard(idtypeitem))

        # Наименование страницы
        nametypeitem = self.DefineTextAndColor(idtypeitem)[0]
        texthead = 'Настройка/{}/Создание новой статьи:'.format(nametypeitem)
        l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        # Картинка статьи
        time_paint = tk.Label(self.frameMain, bg='black', image=self.ImageList[bufferList[6]])
        time_paint.place(x=820, y=75)

        # Поле ввода наименования статьи
        l1 = tk.Label(self.frameMain, text="Наименование статьи:", bg="black", foreground="#ccc", font="Arial 20")
        l1.place(x=50, y=60)

        if bufferList[1] == '':
            tex1 = 'Новая статья'
        else:
            tex1 = bufferList[1]
        button_NameItem = tk.Button(self.frameMain, text=tex1, name='button_Name',
                                    font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_NameItem.place(x=50, y=100, width=700, height=50)

        Data1 = (0, 50, 100, 700, 40, tex1, 'button_Name', 'Arial 14', '#A9A9A9', '#F5F5F5', '', 0)
        button_NameItem.bind('<Button-1>', lambda event: self.ChangeTheData(Data1))

        # Кнопка редактирования суммы
        if idtypeitem != 1 and idtypeitem != 2:
            print(type(idtypeitem))
            print(idtypeitem)
            l3 = tk.Label(self.frameMain, text="Начальный остаток:", bg="black", foreground="#ccc", font="Arial 20")
            l3.place(x=50, y=160)

            tex3 = self.NumberIsString(bufferList[5])
            button_SumItem = tk.Button(self.frameMain, text=tex3, name='button_Sum', font="Arial 14", bg="#A9A9A9",
                                       foreground="#F5F5F5")
            button_SumItem.place(x=50, y=200, width=300, height=40)
            Data3 = (2, 50, 200, 300, 40, tex3, 'button_Sum', 'Arial 14', '#A9A9A9', '#F5F5F5', tex3, 0)
            button_SumItem.bind('<Button-1>', lambda event: self.ChangeTheData(Data3))

        # Кнопка изменения картинки для статьи
        button_Image = tk.Button(self.frameMain, name='button_Date', text='Картинка', bg='#708090', font="Arial 25",
                                 foreground="#F5F5F5")
        button_Image.place(x=450, y=200, width=300, height=40)
        button_Image.bind('<Button-1>', lambda event: self.SelectImageWindow('NEW', idtypeitem, bufferList[6]))

        # Поле ввода описания статьи
        l4 = tk.Label(self.frameMain, text="Описание статьи:", bg="black", foreground="#ccc", font="Arial 20")
        l4.place(x=50, y=260)

        if bufferList[3] == '':
            tex4 = 'Описание новой статьи'
        else:
            tex4 = bufferList[3]
        button_DescriptionItem = tk.Button(self.frameMain, text=tex4, name='button_Description', wraplength=680,
                                           font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_DescriptionItem.place(x=50, y=300, width=700, height=40)
        Data4 = (3, 50, 300, 700, 50, tex4, 'button_Description', 'Arial 14', '#A9A9A9', '#F5F5F5', '', 0)
        button_DescriptionItem.bind('<Button-1>', lambda event: self.ChangeTheData(Data4))

        # Кнопка назначения кредитной картой
        if idtypeitem == 7:
            texcredit = ''
            if bufferList[4] == 0:
                texcredit = 'Не  кредитная карта'
            elif bufferList[4] == 1:
                texcredit = 'Кредитная карта'

            button_Credit = tk.Button(self.frameMain, text=texcredit, name='button_Credit', font="Arial 14",
                                      bg="#696969", foreground="#F5F5F5")
            button_Credit.place(x=50, y=370, width=200, height=40)
            button_Credit.bind('<Button-1>', lambda event: self.CreditItemSwitch())

            # Информация о смысле назначить статью кредитной картой
            info_paint2 = tk.Label(self.frameMain, bg='black', image=self.info_img)
            info_paint2.place(x=270, y=367)
            texinfo = "Кредитная карта будет добавлена в список кошельков\nдля быстого выбора при оплате расходов"
            l5 = tk.Label(self.frameMain, text=texinfo, bg="black", foreground="#ccc", font="Arial 14", justify='left')
            l5.place(x=320, y=365)

        # Кнопка сохранения новой  статьи
        button_SaveItem = tk.Button(self.frameMain, text='Сохранить', name='button_Save', font="Arial 14", bg="#708090",
                                    foreground="#F5F5F5")
        button_SaveItem.place(x=50, y=600, width=200, height=40)
        button_SaveItem.bind('<Button-1>', lambda event: self.SaveNewItem())

    # Сохранение новой статьи в БД
    def SaveNewItem(self):
        print('Save New Item')
        global bufferList
        print(bufferList)
        # Проверяем, что наименование статьи заполнено
        if bufferList[1] == '':
            mb.showerror("Ошибка", "Наименование статьи должно быть заполнено!!!")
        else:
            # Собираем кортеж для записи в БД
            adddata = (bufferList[0], bufferList[1], bufferList[2], bufferList[3], bufferList[4], bufferList[5],
                       bufferList[5], bufferList[6], 1, 0, None, 0, 0, '2200-01-01')

            # Записываем новую статью в БД
            db.AddNewItem(adddata)

            # Очищаем фрейм и отрисовываем список статей
            self.Clear()
            self.BackWard(bufferList[0])

            # чистим буферный динамический массив
            bufferList = list()

    # Переключение значения Кредитная карта
    def CreditItemSwitch(self, IDITEM=1):
        global bufferList

        listobject = self.frameMain.place_slaves()
        for obj in listobject:
            if obj.winfo_name() == 'button_Credit':
                if self.CurrentWindow == 11:
                    if bufferList[4] == 0:
                        obj.config(text='Кредитная карта', bg="#DA70D6")
                        bufferList[4] = 1
                    elif bufferList[4] == 1:
                        obj.config(text='Не  кредитная карта', bg="#696969")
                        bufferList[4] = 0
                elif self.CurrentWindow == 4:
                    DATA = db.RequestSelectDB('*', 'items', 'id={}'.format(IDITEM))[0]
                    if DATA[5] == 0:
                        obj.config(text='Кредитная карта', bg="#DA70D6")
                        db.UpdateNoteDB('items', 'creditcard', 'id', 1, DATA[0])
                    elif DATA[5] == 1:
                        obj.config(text='Не  кредитная карта', bg="#696969")
                        db.UpdateNoteDB('items', 'creditcard', 'id', 0, DATA[0])

    # Ввод корректных данных
    def EnterData(self, DATA, NewData):
        global bufferList
        # DATA - кортеж 0 - номер (тип) поля ввода, 1 - х, 2 - у, 3 - width, 4 - height,
        # 5 - text, 6 - name, 7 - font, 8 - bg, 9 - foreground, 10 - значение для корректировки,
        # 11 - новая(0)/текущая == id статьи

        # 0 -строка - Наименование статьи, 1 - дата, 2- число, 3 - строка - описание статьи
        print('EnterData')
        print(NewData)
        dateNew = ''
        NewData1 = ''
        try:
            qq = 'Тип данных {}'.format(DATA[0])
            print(qq)
            if DATA[0] == 1:
                print(NewData)
                dateNew = dt.datetime.strptime(NewData, '%d.%m.%Y').date()
                NewData = dt.date.strftime(dateNew, '%d.%m.%Y')
                NewData1 = NewData
                print(dateNew)
            elif DATA[0] == 2:
                dateNew = round(float(NewData), 2)
                NewData1 = self.NumberIsString(dateNew)
                NewData = '{0:.2f}'.format(dateNew)
            elif DATA[0] == 0 or DATA[0 == 4]:
                dateNew = NewData
                NewData1 = NewData

            # Удаление поля ввода и кнопок
            listobject = self.frameMain.place_slaves()
            for obj in listobject:
                if obj.winfo_name() == 'entry_DATA' or obj.winfo_name() == 'button_DataOK' or \
                        obj.winfo_name() == 'button_DataNO':
                    obj.destroy()

            # Корректируем существующую запись
            if DATA[11] != 0:
                print('Обработчик корректировки значения существующей записи EnterData')
                if self.CurrentWindow == 4:
                    database = 'items'
                    idname = 'id'
                    field = ''
                    if DATA[0] == 1:
                        field = 'dateitem'
                    elif DATA[0] == 3:
                        field = 'descriptoionitem'
                    elif DATA[0] == 0:
                        field = 'nameitem'
                    elif DATA[0 == 2]:
                        field = 'initialbalanceitem'
                    db.UpdateNoteDB(database, field, idname, dateNew, DATA[11])
                if self.CurrentWindow == 9:
                    if DATA[0] == 1:
                        database = 'items'
                        field = 'dateitem'
                        idname = 'id'
                    elif DATA[0] == 2:
                        database = 'items'
                        field = 'descriptoionitem'
                        idname = 'id'
                    elif DATA[0] == 0:
                        database = 'items'
                        field = 'nameitem'
                        idname = 'id'
                    elif DATA[0 == 3]:
                        database = 'items'
                        field = 'initialbalanceitem'
                        idname = 'id'

            # Изменение значения поля при создании новой записи
            elif DATA[11] == 0:
                print('Обработчик сохранения в буфер значения из поле новой записи EnterData')
                if self.CurrentWindow == 11:
                    if DATA[0] == 1:
                        bufferList[2] = dateNew
                    elif DATA[0] == 2:
                        bufferList[5] = dateNew
                    elif DATA[0] == 0:
                        bufferList[1] = dateNew
                    elif DATA[0 == 3]:
                        bufferList[3] = dateNew
                elif self.CurrentWindow == 8 or self.CurrentWindow == 9 or self.CurrentWindow == 10:
                    if DATA[0] == 1:
                        bufferList['dateoperationkey'] = dateNew
                    elif DATA[0] == 2:
                        bufferList['sumoperationkey'] = dateNew
                    elif DATA[0 == 3]:
                        bufferList['descriptionkey'] = dateNew
                elif self.CurrentWindow == 2:
                    # Запрет на изменение даты начала учета на дату больше даты самой ранней операции
                    if ospath.exists('notes.db'):
                        # Запрос массива дат операций
                        data2 = db.RequestSelectDB('dateoperation', 'notes')

                        for i in data2:
                            dateOperations = dt.datetime.strptime(i[0], '%Y-%m-%d').date()
                            if dateOperations < dateNew:
                                mb.showerror("Ошибка", "Есть операции с более ранними датами, чем новая дата начала "
                                                       "учета. Измените их")
                                break
                                # return

                    listobject = self.frameMain.place_slaves()
                    for obj in listobject:
                        if obj.winfo_name() == 'entry_date' or obj.winfo_name() == 'button_dateOK' or \
                                obj.winfo_name() == 'button_dateNo':
                            obj.destroy()
                    if db.beginDate != dateNew:
                        db.beginDate = dateNew
                        # Внесение новой даты в файл настроек
                        db.UpdateNoteDB('setting', 'date', 'id', db.beginDate, 1)

            # Сборка нового кортежа и создание кнопки
            DATA1 = (DATA[0], DATA[1], DATA[2], DATA[3], DATA[4], NewData1, DATA[6], DATA[7], DATA[8], DATA[9], NewData,
                     DATA[11])
            button_DataItem = tk.Button(self.frameMain, text=NewData1, name=DATA[6], wraplength=680, font=DATA[7],
                                        bg=DATA[8], foreground=DATA[9])

            button_DataItem.place(x=DATA[1], y=DATA[2], width=DATA[3], height=DATA[4])
            button_DataItem.bind('<Button-1>', lambda event: self.ChangeTheData(DATA1))

        except ValueError:
            if DATA[0] == 1:
                print(NewData)
                mb.showerror("Ошибка", "Дата должна быть в формате ДД.ММ.ГГГГ")
            elif DATA[0] == 2:
                mb.showerror("Ошибка", "Должно быть введено число")

    # Изменение введенных данных
    def ChangeTheData(self, DATA):
        # DATA - кортеж 0 - номер (тип) поля ввода, 1 - х, 2 - у, 3 - width, 4 - height,
        # 5 - text, 6 - name, 7 - font, 8 - bg, 9 - foreground, 10 - значение для корректировки,
        # 11 - новая(0)/текущая == id статьи

        # Прерываем функцию, если поле ввода уже есть на фрейме
        listobject = self.frameMain.place_slaves()
        for obj in listobject:
            if obj.winfo_name() == 'entry_DATA':
                return

        # Заменяем кнопку на поле ввода со кнопками отмены и подтверждения
        for obj in listobject:
            if obj.winfo_name() == DATA[6]:
                obj.destroy()
        print(DATA)

        # Поле ввода данных
        entry_Data = ttk.Entry(self.frameMain, name='entry_DATA', width=20, font="Arial 25")
        entry_Data.insert(0, DATA[10])
        entry_Data.place(x=DATA[1], y=DATA[2], width=DATA[3])

        # Кнопка утверждения изменений
        xx = DATA[1] + DATA[3] + 2
        button_DataOK = tk.Button(self.frameMain, image=self.forward_img, bg='#2f4f4f', name='button_DataOK')
        button_DataOK.place(x=xx, y=DATA[2], height=45, width=45)
        newdata = entry_Data.get()
        print(newdata)
        button_DataOK.bind('<Button-1>', lambda event: self.EnterData(DATA, entry_Data.get()))

        # Кнопка отмены изменений
        xxx = DATA[1] + DATA[3] + 49
        button_DataNO = tk.Button(self.frameMain, image=self.exit_img, bg='#2f4f4f', name='button_DataNO')
        button_DataNO.place(x=xxx, y=DATA[2], height=45, width=45)
        button_DataNO.bind('<Button-1>', lambda event: self.cancelData(DATA))

    # Отмена изменения данных
    def cancelData(self, DATA):
        # DATA - кортеж 0 - номер (тип) поля ввода, 1 - х, 2 - у, 3 - width, 4 - height,
        # 5 - text, 6 - name, 7 - font, 8 - bg, 9 - foreground, 10 - значение для корректировки,
        # 11 - новая(0)/текущая == id статьи
        listobject = self.frameMain.place_slaves()

        for obj in listobject:
            if (obj.winfo_name() == 'entry_DATA' or obj.winfo_name() == 'button_DataOK' or
                    obj.winfo_name() == 'button_DataNO'):
                obj.destroy()

        button_DataItem = tk.Button(self.frameMain, text=DATA[5], name=DATA[6], wraplength=680,
                                    font=DATA[7], bg=DATA[8], foreground=DATA[9])
        button_DataItem.place(x=DATA[1], y=DATA[2], width=DATA[3], height=DATA[4])
        button_DataItem.bind('<Button-1>', lambda event: self.ChangeTheData(DATA))

    # Функция строкового отображения чисел
    def NumberIsString(self, number):
        string = '{0:,.2f}'.format(number)
        string = string.replace(',', ' ')
        return string

    # Функция возврата в предыдущее окно
    def BackWard(self, section=1):
        print('BackWard')
        # Перечисление окон
        # passwordWindow = 0
        # menuWindow = 1
        # settingWindow = 2
        # listItemSettingWindow = 3
        # correctItemWindow = 4
        # ItemCreateNewWindow = 11
        # mainWindow = 5
        # ListItemForEnterDataWindow = 6
        # ListDataInItemWindow = 7
        # DataCreateNewWindow = 8
        # DataCorrectWindow = 9
        # DataCreateNewWindowCopy = 10
        # ReportWindow = 12
        # ListDataInItemInReportWindow = 13

        # Чистим буферный динамический массив
        global bufferList
        bufferList = list()

        # Сбрасываем настройку фильтра
        self.SetDefaultFilter()

        if self.CurrentWindow == 3:
            self.SettingWindow()
        elif self.CurrentWindow == 4 or self.CurrentWindow == 11:
            self.ListItemSettingWindow(section)
        elif self.CurrentWindow == 2:
            self.MenuWindow()
        elif self.CurrentWindow == 1:
            if self.PreviousWindow == 5:
                self.MainWindow()
            elif self.PreviousWindow == 6:
                self.ListItemForEnterDataWindow(section)
            elif self.PreviousWindow == 7:
                self.ListItemForEnterDataWindow(section)
            elif self.PreviousWindow == 4:
                self.ListItemSettingWindow(section)
        elif self.CurrentWindow == 6:
            self.MainWindow()
        elif self.CurrentWindow == 7 or self.CurrentWindow == 8:
            self.ListItemForEnterDataWindow(section)
        elif self.CurrentWindow == 9:
            self.ListDataInItemWindow2(section)
        elif self.CurrentWindow == 10:
            self.ListDataInItemWindow2(section)
        elif self.CurrentWindow == 12:
            self.MainWindow()

    # Функция очистки основного фрейма окна программы
    def Clear(self):
        listobject = self.frameMain.place_slaves()
        for obj in listobject:
            obj.destroy()
        listobject2 = self.toolbarMenu.place_slaves()
        for obj in listobject2:
            if obj.winfo_name() == 'button_Back':
                obj.destroy()

    # Окно отчета
    def ReportWindow(self, REQUEST_LIST='', VIEW='narrow', TOPLINE=0):
        """ Окно просмотра отчета с пэйджингом и фильтром """
        self.CurrentWindow = 12
        self.SettingFilter['currentPage'] = 1
        self.SettingFilter['countPage'] = 1

        if REQUEST_LIST == '':
            REQUEST_LIST = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]

        # Отключаем отображаемые фреймы
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.BackWard(0))

        # Наименование страницы
        l1 = tk.Label(self.frameMain, text="ПРОСМОТР ОТЧЕТА:", bg="black", foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=50)

        self.StringsReport(REQUEST_LIST, VIEW, TOPLINE)

    # Отображение строк отчета и фильтра по периоду
    def StringsReport(self, REQUEST_LIST, VIEW='narrow', TOPLINE=0):
        # Список строк для отображения
        LIST_STRING = list()
        print(REQUEST_LIST)
        # Список обновляемых объектов
        OBJECTLIST = list()

        # Запрашиваем данные по разделам
        DATA_SECTION = db.RequestSelectDB('*', 'typeitems')

        # Список строк для расчета результирующих строк
        list_string = list()

        ind_aktiv, ind_passiv = 0, 0

        # Установлен фильтр за весь период (в запросе по разделу есть только флаг раскрытия узла и id раздела)
        if len(REQUEST_LIST[0]) == 2:
            for section in REQUEST_LIST:
                # Добавляем доходы и расходы в отчет
                if section[1] in (1, 2):
                    # Рассчитываем обороты по разделу
                    sum_section = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes',
                                                                           'typeitem_id={}'.format(section[1])))

                    # Записываем нулевую строку, если оборотов в разделе нет
                    # print(DATA_SECTION)
                    if DATA_SECTION[section[1]-1][4] == 0 and DATA_SECTION[section[1]-1][5] == 0 and sum_section == 0:
                        LIST_STRING.append([0, 0, 'section', DATA_SECTION[section[1]-1][2], 0, 0, 0, section[1]])
                        list_string.append([0, 0, 'section', DATA_SECTION[section[1]-1][2], 0, 0, 0])

                    else:
                        # Записываем строку, если есть обороты в разделе
                        LIST_STRING.append([1, section[0], 'section', DATA_SECTION[section[1]-1][2], 0, sum_section,
                                            DATA_SECTION[section[1]-1][5], section[1]])
                        list_string.append([1, section[0], 'section', DATA_SECTION[section[1]-1][2], 0, sum_section,
                                            DATA_SECTION[section[1]-1][5]])

                        if section[0] == 1:
                            # Запрашиваем строки со статьями, если узел раскрыт
                            DATA_ITEM = db.RequestSelectDB('*', 'items', 'typeitem_id={}'.format(section[1]))
                            for item in DATA_ITEM:
                                sumitem = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes',
                                                                'item_id={}'.format(item[0])))

                                # Записываем строки со статьями, если есть остатки или обороты
                                if item[6] != 0 or item[7] != 0 or sumitem != 0:
                                    LIST_STRING.append([0, 0, 'item', item[2], 0, sumitem, item[7], item[0]])

                    # Записываем строку с прибылью/убытком
                    if section[1] == 2:
                        LIST_STRING.insert(0, [0, 0, 'result', 'Прибыль/Убыток', 0, list_string[0][5] -
                                               list_string[1][5], list_string[0][6] - list_string[1][6], 0])

                # Добавляем статьи баланса в отчет
                elif section[1] in (3, 4, 5, 6, 7, 8):
                    # Оборот по разделу
                    Turnover, TurnoverPlus, TurnoverMinus = 0, 0, 0

                    DATA_ITEM = db.RequestSelectDB('*', 'items', 'typeitem_id={}'.format(section[1]))

                    # Индекс для вставки строки раздела
                    ind = len(LIST_STRING)

                    # Индекс строки актива
                    if section[1] == 3:
                        ind_aktiv = len(LIST_STRING)

                    # Индекс статьи пассива
                    if section[1] == 7:
                        ind_passiv = len(LIST_STRING)

                    if len(DATA_ITEM) == 0:
                        LIST_STRING.append([0, section[0], 'section', DATA_SECTION[section[1]-1][2], 0, 0, 0,
                                            section[1]])
                        list_string.append([0, section[0], 'section', DATA_SECTION[section[1]-1][2], 0, 0, 0])
                    else:

                        for item in DATA_ITEM:
                            # Считаем сумму положительных оборотов по статье
                            tex2 = '(item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or ' \
                                   'increase=2))'.format(item[0], item[0])
                            data2 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex2))

                            # Считаем сумму отицательных обортов по статье
                            tex3 = '(item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or ' \
                                   'increase=3))'.format(item[0], item[0])
                            data3 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex3))

                            # Рассчитываем оборот
                            sumitem = data2 - data3

                            # Приращиваем данные по обороту раздела
                            Turnover += sumitem
                            TurnoverPlus += data2
                            TurnoverMinus += data3

                            if section[0] == 1 and (item[6] != 0 or item[7] != 0 or data2 != 0 or data3 != 0):
                                # Записываем строку со статьёй если узел у раздела открыт, есть остатки или обороты
                                LIST_STRING.append([0, 0, 'item', item[2], item[6], sumitem, item[7], item[0]])

                        # Записываем стоку раздела по индексу
                        if section[0] == 0 and DATA_SECTION[section[1]-1][4] == 0 and DATA_SECTION[section[1]-1][5] and\
                                TurnoverPlus == 0 and TurnoverMinus == 0:
                            # Записываем нулевую строку, если оборотов в разделе нет
                            LIST_STRING.insert(ind, [0, 0, 'section', DATA_SECTION[section[1]-1][2], 0, 0, 0,
                                                     section[1]])
                            list_string.append([0, 0, 'section', DATA_SECTION[section[1]-1][2], 0, 0, 0])
                        else:
                            # Записываем строку, если есть обороты в разделе
                            LIST_STRING.insert(ind, [1, section[0], 'section', DATA_SECTION[section[1]-1][2],
                                               DATA_SECTION[section[1]-1][4], Turnover, DATA_SECTION[section[1]-1][5],
                                               section[1]])
                            list_string.append([1, section[0], 'section', DATA_SECTION[section[1]-1][2],
                                                DATA_SECTION[section[1]-1][4], Turnover, DATA_SECTION[section[1]-1][5]])

                    # Записываем строку актива
                    if section[1] == 6:
                        LIST_STRING.insert(ind_aktiv, [0, 0, 'aktiv', 'АКТИВ', list_string[2][4] + list_string[3][4] +
                                                       list_string[4][4] + list_string[5][4], list_string[2][5] +
                                                       list_string[3][5] + list_string[4][5] + list_string[5][5],
                                                       list_string[2][6] + list_string[3][6] + list_string[4][6] +
                                                       list_string[5][6], 0])

                    if section[1] == 8:
                        # Записываем строку пассива
                        LIST_STRING.insert(ind_passiv, [0, 0, 'passiv', 'ПАССИВ', list_string[6][4] +
                                                        list_string[7][4] + DATA_SECTION[8][4], list_string[0][5] -
                                                        list_string[1][5], list_string[6][6] + list_string[7][6] +
                                                        DATA_SECTION[8][5], 0])

                        # Записываем строку заёмных средств
                        LIST_STRING.append([0, 0, 'result', 'Заёмные средства', list_string[6][5] + list_string[7][5],
                                            list_string[6][5] + list_string[7][5], list_string[6][6] +
                                            list_string[7][6], 0])

                        # Записываем строку собственного капитала
                        LIST_STRING.append([0, 0, 'section', DATA_SECTION[8][2], DATA_SECTION[8][4], list_string[0][5] -
                                            list_string[1][5], DATA_SECTION[8][5], 9])
                        print(LIST_STRING)

        # Установлен фильтр за  период, узкий вид (в запросе по разделу есть флаг раскрытия узла, id раздела,
        # дата начала и дата конца периода)
        elif len(REQUEST_LIST[0]) == 4:
            for section in REQUEST_LIST:
                # Добавляем доходы и расходы в отчет
                if section[1] in (1, 2):
                    # Рассчитываем остатки обороты по разделу

                    # Остаток на начало дня
                    where1 = 'typeitem_id={} and dateoperation Between \'{}\' and \'{}\''.format(
                                                 section[1], db.beginDate, section[2]-timedelta(1))
                    initial_balance_section = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes',
                                                                                       where1))

                    # Оборот за период
                    where2 = 'typeitem_id={} and dateoperation Between \'{}\' and \'{}\''.format(section[1], section[2],
                                                                                                 section[3])
                    sum_section = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', where2))

                    # Записываем нулевую строку, если оборотов и остатков в разделе нет
                    if initial_balance_section == 0 and sum_section == 0:
                        LIST_STRING.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0, section[1]])
                        list_string.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0])

                    else:
                        # Записываем строку, если есть обороты в разделе
                        LIST_STRING.append([1, section[0], 'section', DATA_SECTION[section[1] - 1][2],
                                            initial_balance_section, sum_section, initial_balance_section + sum_section,
                                            section[1]])
                        list_string.append([1, section[0], 'section', DATA_SECTION[section[1] - 1][2],
                                            initial_balance_section, sum_section, initial_balance_section +
                                            sum_section])

                        if section[0] == 1:
                            # Запрашиваем строки со статьями, если узел раскрыт
                            DATA_ITEM = db.RequestSelectDB('*', 'items', 'typeitem_id={}'.format(section[1]))
                            for item in DATA_ITEM:
                                where3 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(item[0],
                                                                                 db.beginDate, section[3]-timedelta(1))
                                initial_balance_item = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)',
                                                                                                'notes', where3))
                                where4 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(item[0],
                                                                                                 section[2], section[3])
                                sumitem = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', where4))

                                # Записываем строки со статьями, если есть остатки или обороты
                                if initial_balance_item != 0 or sumitem != 0:
                                    LIST_STRING.append([0, 0, 'item', item[2], initial_balance_item, sumitem,
                                                        initial_balance_item + sumitem, item[0]])

                    # Записываем строку с прибылью/убытком
                    if section[1] == 2:
                        LIST_STRING.insert(0, [0, 0, 'result', 'Прибыль/Убыток', list_string[0][4] - list_string[1][4],
                                           list_string[0][5] - list_string[1][5], list_string[0][6] -
                                           list_string[1][6], 0])

                # Добавляем статьи баланса в отчет
                elif section[1] in (3, 4, 5, 6, 7, 8):
                    # Оборот по разделу
                    Turnover, TurnoverPlus, TurnoverMinus, Initial_balance_item = 0, 0, 0, 0

                    DATA_ITEM = db.RequestSelectDB('*', 'items', 'typeitem_id={}'.format(section[1]))

                    # Индекс для вставки строки раздела
                    ind = len(LIST_STRING)

                    # Индекс строки актива
                    if section[1] == 3:
                        ind_aktiv = len(LIST_STRING)

                    # Индекс статьи пассива
                    if section[1] == 7:
                        ind_passiv = len(LIST_STRING)

                    if len(DATA_ITEM) == 0:
                        LIST_STRING.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0,
                                            section[1]])
                        list_string.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0])
                    else:

                        for item in DATA_ITEM:
                            # Считаем сумму положительных оборотов по статье на начало периода отбора
                            tex2 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                             increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(item[0], item[0],
                                                                                 db.beginDate, section[2]-timedelta(1))
                            data2 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex2))
                            # Считаем сумму положительных оборотов по статье
                            tex3 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                                   increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(item[0], item[0],
                                                                                                section[2], section[3])
                            data3 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex3))

                            # Считаем сумму отицательных обортов по статье
                            tex4 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                            increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(item[0], item[0],
                                                                                               section[2], section[3])
                            data4 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex4))

                            # Считаем сумму отицательных обортов по статье на начало периода отбора
                            tex5 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                                   increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(item[0], item[0],
                                                                                 db.beginDate, section[2]-timedelta(1))
                            data5 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex5))

                            # рассчитываем начальный остаток на начало периода отбора
                            initial_item_day = item[6] + data2 - data5

                            # Рассчитываем оборот
                            sumitem = data3 - data4

                            # Приращиваем данные по обороту раздела
                            Initial_balance_item += initial_item_day
                            Turnover += sumitem
                            TurnoverPlus += data3
                            TurnoverMinus += data4

                            if section[0] == 1 and (initial_item_day != 0 or data3 != 0 or data4 != 0):
                                # Записываем строку со статьёй если узел у раздела открыт, есть остатки или обороты
                                LIST_STRING.append([0, 0, 'item', item[2], initial_item_day, sumitem, initial_item_day +
                                                    sumitem, item[0]])

                        # Записываем стpоку раздела по индексу
                        if Initial_balance_item == 0 and TurnoverPlus == 0 and TurnoverMinus == 0:
                            # Записываем нулевую строку, если оборотов и остатков в разделе нет
                            LIST_STRING.insert(ind, [0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0,
                                                     section[1]])
                            list_string.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0])
                        else:
                            # Записываем строку, если есть обороты в разделе
                            LIST_STRING.insert(ind, [1, section[0], 'section', DATA_SECTION[section[1] - 1][2],
                                                     Initial_balance_item, Turnover, Initial_balance_item + Turnover,
                                                     section[1]])
                            list_string.append([1, section[0], 'section', DATA_SECTION[section[1] - 1][2],
                                                Initial_balance_item, Turnover, Initial_balance_item + Turnover])

                    # Записываем строку актива
                    if section[1] == 6:
                        LIST_STRING.insert(ind_aktiv, [0, 0, 'aktiv', 'АКТИВ', list_string[2][4] + list_string[3][4] +
                                                       list_string[4][4] + list_string[5][4], list_string[2][5] +
                                                       list_string[3][5] + list_string[4][5] + list_string[5][5],
                                                       list_string[2][6] + list_string[3][6] + list_string[4][6] +
                                                       list_string[5][6], 0])

                    if section[1] == 8:
                        # Записываем строку пассива
                        LIST_STRING.insert(ind_passiv, [0, 0, 'passiv', 'ПАССИВ', list_string[6][4] +
                                                        list_string[7][4] + DATA_SECTION[8][4] + list_string[0][4] -
                                                        list_string[1][4],
                                                        list_string[0][5] - list_string[1][5],
                                                        list_string[6][6] + list_string[7][6] + list_string[0][6] -
                                                        list_string[1][6] + DATA_SECTION[8][4], 0])

                        # Записываем строку заёмных средств
                        LIST_STRING.append([0, 0, 'result', 'Заёмные средства', list_string[6][4] + list_string[7][4],
                                            list_string[6][5] + list_string[7][5], list_string[6][6] +
                                            list_string[7][6], 0])

                        # Записываем строку собственного капитала
                        LIST_STRING.append([0, 0, 'section', DATA_SECTION[8][2],
                                            DATA_SECTION[8][4] + list_string[0][4] - list_string[1][4],
                                            list_string[0][5] - list_string[1][5],
                                            DATA_SECTION[8][4] + list_string[0][6] - list_string[1][6], 9])
                        print(LIST_STRING)

        # Установлен фильтр за  период, широкий вид(в запросе по разделу есть флаг раскрытия узла, id раздела,
        # и четыре пары дат начала и конца периода)
        elif len(REQUEST_LIST[0]) == 10:
            for section in REQUEST_LIST:
                # Добавляем доходы и расходы в отчет
                if section[1] in (1, 2):
                    # Рассчитываем остатки обороты по разделу

                    # Остаток на начало дня
                    where1 = 'typeitem_id={} and dateoperation Between \'{}\' and \'{}\''.format(
                        section[1], db.beginDate, section[2] - timedelta(1))
                    initial_balance_section = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes',
                                                                                       where1))

                    # Обороты за периоды
                    where2_1 = 'typeitem_id={} and dateoperation Between \'{}\' and \'{}\''.format(section[1],
                                                                                                   section[2],
                                                                                                   section[3])
                    sum_section_1 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', where2_1))
                    where2_2 = 'typeitem_id={} and dateoperation Between \'{}\' and \'{}\''.format(section[1],
                                                                                                   section[4],
                                                                                                   section[5])
                    sum_section_2 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', where2_2))
                    where2_3 = 'typeitem_id={} and dateoperation Between \'{}\' and \'{}\''.format(section[1],
                                                                                                   section[6],
                                                                                                   section[7])
                    sum_section_3 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', where2_3))
                    where2_4 = 'typeitem_id={} and dateoperation Between \'{}\' and \'{}\''.format(section[1],
                                                                                                   section[8],
                                                                                                   section[9])
                    sum_section_4 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', where2_4))

                    final_balance_section = initial_balance_section + sum_section_1 + sum_section_2 + sum_section_3 +\
                                                                                                      sum_section_4

                    # Записываем нулевую строку, если оборотов и остатков в разделе нет
                    if initial_balance_section == 0 and sum_section_1 == 0 and sum_section_2 == 0 and\
                            sum_section_3 == 0 and sum_section_4 == 0:
                        LIST_STRING.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0, 0, 0, 0,
                                            section[1]])
                        list_string.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0, 0, 0, 0])

                    else:
                        # Записываем строку, если есть обороты в одном из разделов или начальный остаток != 0
                        LIST_STRING.append([1, section[0], 'section', DATA_SECTION[section[1] - 1][2],
                                            initial_balance_section, sum_section_1, sum_section_2, sum_section_3,
                                            sum_section_4, final_balance_section, section[1]])
                        list_string.append([1, section[0], 'section', DATA_SECTION[section[1] - 1][2],
                                            initial_balance_section, sum_section_1, sum_section_2, sum_section_3,
                                            sum_section_4, final_balance_section])

                        if section[0] == 1:
                            # Запрашиваем строки со статьями, если узел раскрыт
                            DATA_ITEM = db.RequestSelectDB('*', 'items', 'typeitem_id={}'.format(section[1]))
                            for item in DATA_ITEM:
                                where3 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(item[0],
                                         db.beginDate, section[2] - timedelta(1))
                                initial_balance_item = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)',
                                                                                                'notes', where3))
                                where4_1 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(item[0],
                                                                                                           section[2],
                                                                                                           section[3])
                                sumitem_1 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes',
                                                                                     where4_1))
                                where4_2 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(item[0],
                                                                                                           section[4],
                                                                                                           section[5])
                                sumitem_2 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes',
                                                                                     where4_2))
                                where4_3 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(item[0],
                                                                                                           section[6],
                                                                                                           section[7])
                                sumitem_3 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes',
                                                                                     where4_3))
                                where4_4 = 'item_id={} and dateoperation Between \'{}\' and \'{}\''.format(item[0],
                                                                                                           section[8],
                                                                                                           section[9])
                                sumitem_4 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes',
                                                                                     where4_4))
                                final_balance_item = initial_balance_item + sumitem_1 + sumitem_2 + sumitem_3 + \
                                                     sumitem_4

                                # Записываем строки со статьями, если есть остатки или обороты по одному из периодов
                                if initial_balance_item != 0 or sumitem_1 != 0 or sumitem_2 != 0 or sumitem_3 != 0\
                                        or sumitem_4 != 0:
                                    LIST_STRING.append([0, 0, 'item', item[2], initial_balance_item, sumitem_1,
                                                        sumitem_2, sumitem_3, sumitem_4, final_balance_item, item[0]])

                    # Записываем строку с прибылью/убытком
                    if section[1] == 2:
                        LIST_STRING.insert(0, [0, 0, 'result', 'Прибыль/Убыток', list_string[0][4] - list_string[1][4],
                                           list_string[0][5] - list_string[1][5], list_string[0][6] -
                                           list_string[1][6], list_string[0][7] - list_string[1][7], list_string[0][8]
                                           - list_string[1][8], list_string[0][9] - list_string[1][9], 0])

                # Добавляем статьи баланса в отчет
                elif section[1] in (3, 4, 5, 6, 7, 8):
                    # Оборот по разделу
                    Turnover_1, Turnover_2, Turnover_3, Turnover_4, TurnoverPlus_1, TurnoverPlus_2, TurnoverPlus_3,\
                    TurnoverPlus_4, TurnoverMinus_1, TurnoverMinus_2, TurnoverMinus_3, TurnoverMinus_4, \
                    Initial_balance_section, final_balance_section = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

                    DATA_ITEM = db.RequestSelectDB('*', 'items', 'typeitem_id={}'.format(section[1]))

                    # Индекс для вставки строки раздела
                    ind = len(LIST_STRING)

                    # Индекс строки актива
                    if section[1] == 3:
                        ind_aktiv = len(LIST_STRING)

                    # Индекс статьи пассива
                    if section[1] == 7:
                        ind_passiv = len(LIST_STRING)

                    if len(DATA_ITEM) == 0:
                        LIST_STRING.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0, 0, 0, 0,
                                            section[1]])
                        list_string.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0, 0, 0, 0])
                    else:
                        for item in DATA_ITEM:
                            # Считаем сумму положительных оборотов по статье на начало периода отбора
                            tex2 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                                 increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(
                                 item[0], item[0], db.beginDate, section[2] - timedelta(1))
                            data2 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex2))

                            # Считаем сумму отицательных обортов по статье на начало периода отбора
                            tex5 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                                       increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(
                                       item[0], item[0],  db.beginDate, section[2] - timedelta(1))
                            data5 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex5))

                            # Считаем сумму положительных оборотов по статье за 4 периода
                            tex3_1 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                                   increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(
                                item[0], item[0], section[2], section[3])
                            data3_1 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex3_1))
                            tex3_2 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                                   increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(
                                   item[0], item[0], section[4], section[5])
                            data3_2 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex3_2))
                            tex3_3 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                                   increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(
                                   item[0], item[0], section[6], section[7])
                            data3_3 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex3_3))
                            tex3_4 = '''((item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or
                                   increase=2)))  and dateoperation Between \'{}\' and \'{}\''''.format(
                                   item[0], item[0], section[8], section[9])
                            data3_4 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex3_4))

                            # Считаем сумму отицательных обортов по статье за 4 периода
                            tex4_1 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                                   increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(
                                   item[0], item[0], section[2], section[3])
                            data4_1 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex4_1))
                            tex4_2 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                                   increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(
                                   item[0], item[0], section[4], section[5])
                            data4_2 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex4_2))
                            tex4_3 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                                   increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(
                                   item[0], item[0], section[6], section[7])
                            data4_3 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex4_3))
                            tex4_4 = '''((item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or 
                                   increase=3))) and dateoperation Between \'{}\' and \'{}\''''.format(
                                   item[0], item[0], section[8], section[9])
                            data4_4 = db.CheckResultForNone(db.RequestSelectDB('sum(sumoperation)', 'notes', tex4_4))

                            # рассчитываем начальный остаток на начало периода отбора
                            if section[1] == 3:
                                print(data2, data5)
                            initial_item_day = item[6] + data2 - data5

                            # Рассчитываем оборот
                            sumitem_1 = data3_1 - data4_1
                            sumitem_2 = data3_2 - data4_2
                            sumitem_3 = data3_3 - data4_3
                            sumitem_4 = data3_4 - data4_4

                            # Рассчитываем конечный остаток по статье
                            final_balance_item = initial_item_day + sumitem_1 + sumitem_2 + sumitem_3 + sumitem_4

                            # Приращиваем данные по обороту раздела
                            Initial_balance_section += initial_item_day

                            Turnover_1 += data3_1 - data4_1
                            Turnover_2 += data3_2 - data4_2
                            Turnover_3 += data3_3 - data4_3
                            Turnover_4 += data3_4 - data4_4

                            TurnoverPlus_1 += data3_1
                            TurnoverPlus_2 += data3_2
                            TurnoverPlus_3 += data3_3
                            TurnoverPlus_4 += data3_4

                            TurnoverMinus_1 += data4_1
                            TurnoverMinus_2 += data4_2
                            TurnoverMinus_3 += data4_3
                            TurnoverMinus_4 += data4_4

                            final_balance_section = Initial_balance_section + Turnover_1 + \
                                                    Turnover_2 + Turnover_3 + Turnover_4

                            if section[0] == 1 and (initial_item_day != 0 or data3_1 != 0 or data3_2 != 0 or
                                                    data3_3 != 0 or data3_4 != 0 or data4_1 != 0 or data4_2 != 0 or
                                                    data4_3 != 0 or data4_4 != 0):
                                # Записываем строку со статьёй если узел у раздела открыт, есть остатки или обороты
                                LIST_STRING.append([0, 0, 'item', item[2], initial_item_day, sumitem_1, sumitem_2,
                                                    sumitem_3, sumitem_4, final_balance_item, item[0]])

                        # Записываем стpоку раздела по индексу
                        if Initial_balance_section == 0 and TurnoverPlus_1 == 0 and TurnoverPlus_2 == 0 and \
                                TurnoverPlus_3 == 0 and TurnoverPlus_4 == 0 and TurnoverMinus_1 == 0 and \
                                TurnoverMinus_2 == 0 and TurnoverMinus_3 == 0 and TurnoverMinus_4 == 0:
                            # Записываем нулевую строку, если оборотов и остатков в разделе нет
                            LIST_STRING.insert(ind, [0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0, 0, 0,
                                                     0, section[1]])
                            list_string.append([0, 0, 'section', DATA_SECTION[section[1] - 1][2], 0, 0, 0, 0, 0, 0])
                        else:
                            # Записываем строку, если есть обороты в разделе
                            LIST_STRING.insert(ind, [1, section[0], 'section', DATA_SECTION[section[1] - 1][2],
                                                     Initial_balance_section, Turnover_1, Turnover_2, Turnover_3,
                                                     Turnover_4, final_balance_section, section[1]])
                            list_string.append([1, section[0], 'section', DATA_SECTION[section[1] - 1][2],
                                                Initial_balance_section, Turnover_1, Turnover_2, Turnover_3,
                                                Turnover_4, final_balance_section])

                    # Записываем строку актива
                    if section[1] == 6:
                        LIST_STRING.insert(ind_aktiv, [0, 0, 'aktiv', 'АКТИВ',
                                                       list_string[2][4] + list_string[3][4] + list_string[4][4] +
                                                       list_string[5][4],
                                                       list_string[2][5] + list_string[3][5] + list_string[4][5] +
                                                       list_string[5][5],
                                                       list_string[2][6] + list_string[3][6] + list_string[4][6] +
                                                       list_string[5][6],
                                                       list_string[2][7] + list_string[3][7] + list_string[4][7] +
                                                       list_string[5][7],
                                                       list_string[2][8] + list_string[3][8] + list_string[4][8] +
                                                       list_string[5][8],
                                                       list_string[2][9] + list_string[3][9] + list_string[4][9] +
                                                       list_string[5][9],
                                                       0])

                    if section[1] == 8:
                        # Записываем строку пассива
                        LIST_STRING.insert(ind_passiv, [0, 0, 'passiv', 'ПАССИВ',
                                                        list_string[0][4] - list_string[1][4] + list_string[6][4] +
                                                        list_string[7][4] + DATA_SECTION[8][4],
                                                        list_string[0][5] - list_string[1][5] + list_string[6][5] +
                                                        list_string[7][5],
                                                        list_string[0][6] - list_string[1][6] + list_string[6][6] +
                                                        list_string[7][6],
                                                        list_string[0][7] - list_string[1][7] + list_string[6][7] +
                                                        list_string[7][7],
                                                        list_string[0][8] - list_string[1][8] + list_string[6][8] +
                                                        list_string[7][8],
                                                        list_string[0][9] - list_string[1][9] + list_string[6][9] +
                                                        list_string[7][9] + DATA_SECTION[8][4],
                                                        0])

                        # Записываем строку заёмных средств
                        LIST_STRING.append([0, 0, 'result', 'Заёмные средства',
                                            list_string[6][4] + list_string[7][4],
                                            list_string[6][5] + list_string[7][5],
                                            list_string[6][6] + list_string[7][6],
                                            list_string[6][7] + list_string[7][7],
                                            list_string[6][8] + list_string[7][8],
                                            list_string[6][9] + list_string[7][9],
                                            0])

                        # Записываем строку собственного капитала
                        LIST_STRING.append([0, 0, 'section', DATA_SECTION[8][2],
                                            DATA_SECTION[8][4] + list_string[0][4] - list_string[1][4],
                                            list_string[0][5] - list_string[1][5],
                                            list_string[0][6] - list_string[1][6],
                                            list_string[0][7] - list_string[1][7],
                                            list_string[0][8] - list_string[1][8],
                                            list_string[0][9] - list_string[1][9]  + DATA_SECTION[8][4],
                                            9])
                        print(LIST_STRING)

        # Отображение картинки, фона и заголовков для узкого вида
        if VIEW == 'narrow':
            # Картинка статьи
            Main_paint = tk.Label(self.frameMain, bg='black', image=self.report_img)
            Main_paint.place(x=820, y=45)
            OBJECTLIST.append(Main_paint)

            # Фон/область для отображения строк отчета
            Fon_report = tk.Label(self.frameMain, bg='#2F4F4F')
            Fon_report.place(x=25, y=100, width=775, height=500)
            OBJECTLIST.append(Fon_report)

            # Отображение заголовков таблицы отчета
            column_name_l = tk.Label(self.frameMain, text='Наименование статьи/раздела', bg='#2F4F4F',
                                     foreground="#F5F5F5", font="Arial 14")
            column_name_l.place(x=55, y=102, width=270, height=25)
            OBJECTLIST.append(column_name_l)

            column_initial_balance_l = tk.Label(self.frameMain, text='Начальный остаток', bg="#2F4F4F",
                                                foreground="#F5F5F5", font="Arial 12")
            column_initial_balance_l.place(x=329, y=102, width=150, height=25)
            OBJECTLIST.append(column_initial_balance_l)

            column_turnover_l1 = tk.Label(self.frameMain, text='Оборот', bg="#2F4F4F", foreground="#F5F5F5",
                                          font="Arial 12")
            column_turnover_l1.place(x=483, y=102, width=150, height=25)
            OBJECTLIST.append(column_turnover_l1)

            column_final_balance_l = tk.Label(self.frameMain, text='Конечный остаток', bg="#2F4F4F",
                                              foreground="#F5F5F5", font="Arial 12")
            column_final_balance_l.place(x=637, y=102, width=150, height=25)
            OBJECTLIST.append(column_final_balance_l)

        # Отображение фона и заголовков для широкого вида
        elif VIEW == 'wide':
            # Фон/область для отображения строк отчета
            Fon_report = tk.Label(self.frameMain, bg='#2F4F4F')
            Fon_report.place(x=25, y=100, width=1244, height=500)
            OBJECTLIST.append(Fon_report)

            # Отображение заголовков таблицы отчета
            column_name_l = tk.Label(self.frameMain, text='Наименование статьи/раздела', bg='#2F4F4F',
                                     foreground="#F5F5F5", font="Arial 14")
            column_name_l.place(x=55, y=102, width=270, height=25)
            OBJECTLIST.append(column_name_l)

            column_initial_balance_l = tk.Label(self.frameMain, text='Начальный остаток', bg="#2F4F4F",
                                                foreground="#F5F5F5", font="Arial 12")
            column_initial_balance_l.place(x=329, y=102, width=150, height=25)
            OBJECTLIST.append(column_initial_balance_l)

            print(REQUEST_LIST)

            tex_d1 ='{} - {}'.format(dt.date.strftime(REQUEST_LIST[0][2], '%d.%m.%Y'),
                                     dt.date.strftime(REQUEST_LIST[0][3], '%d.%m.%Y'))
            column_turnover_l1 = tk.Label(self.frameMain, text=tex_d1, bg="#2F4F4F", foreground="#F5F5F5",
                                          font="Arial 10")
            column_turnover_l1.place(x=483, y=102, width=150, height=25)
            OBJECTLIST.append(column_turnover_l1)

            tex_d2 = '{} - {}'.format(dt.date.strftime(REQUEST_LIST[0][4], '%d.%m.%Y'),
                                      dt.date.strftime(REQUEST_LIST[0][5], '%d.%m.%Y'))
            column_turnover_l2 = tk.Label(self.frameMain, text=tex_d2, bg="#2F4F4F", foreground="#F5F5F5",
                                          font="Arial 10")
            column_turnover_l2.place(x=637, y=102, width=150, height=25)
            OBJECTLIST.append(column_turnover_l2)

            tex_d3 = '{} - {}'.format(dt.date.strftime(REQUEST_LIST[0][6], '%d.%m.%Y'),
                                      dt.date.strftime(REQUEST_LIST[0][7], '%d.%m.%Y'))
            column_turnover_l3 = tk.Label(self.frameMain, text=tex_d3, bg="#2F4F4F", foreground="#F5F5F5",
                                          font="Arial 10")
            column_turnover_l3.place(x=791, y=102, width=150, height=25)
            OBJECTLIST.append(column_turnover_l3)

            tex_d4 = '{} - {}'.format(dt.date.strftime(REQUEST_LIST[0][8], '%d.%m.%Y'),
                                      dt.date.strftime(REQUEST_LIST[0][9], '%d.%m.%Y'))
            column_turnover_l4 = tk.Label(self.frameMain, text=tex_d4, bg="#2F4F4F", foreground="#F5F5F5",
                                          font="Arial 10")
            column_turnover_l4.place(x=945, y=102, width=150, height=25)
            OBJECTLIST.append(column_turnover_l4)

            column_final_balance_l = tk.Label(self.frameMain, text='Конечный остаток', bg="#2F4F4F",
                                              foreground="#F5F5F5",
                                              font="Arial 12")
            column_final_balance_l.place(x=1099, y=102, width=150, height=25)
            OBJECTLIST.append(column_final_balance_l)

        # Отображение строк отчета
        self.DrawStrings(LIST_STRING, OBJECTLIST, REQUEST_LIST, VIEW, TOPLINE)

        # Блок фильтра по периоду
        if self.SettingFilter['period'] != 'AllPeriod':
            # Кнопка фильтрации на период назад
            buttonPeriodLeft = tk.Button(self.frameMain, name='period_Left', background="black",
                                         image=self.arrowLeft_img)
            buttonPeriodLeft.place(x=250, y=640, width=40, height=40)
            buttonPeriodLeft.bind('<Button-1>', lambda eventbutton: self.ChangeFilterReport('PeriodBack', REQUEST_LIST,
                                                                                            OBJECTLIST, VIEW))
            OBJECTLIST.append(buttonPeriodLeft)

            # Кнопка фильтрации на период вперёд
            buttonPeriodRight = tk.Button(self.frameMain, name='period_Right', background="black",
                                          image=self.arrowRight_img)
            buttonPeriodRight.place(x=330, y=640, width=40, height=40)
            buttonPeriodRight.bind('<Button-1>', lambda eventbutton: self.ChangeFilterReport('PeriodForward',
                                                                                             REQUEST_LIST,
                                                                                             OBJECTLIST, VIEW))
            OBJECTLIST.append(buttonPeriodRight)

        # Кнопка изменения размера периода фильтрации вверх
        buttonPeriodUp = tk.Button(self.frameMain, name='period_Up', background="black", image=self.arrowUp_img)
        buttonPeriodUp.place(x=290, y=620, width=40, height=40)
        buttonPeriodUp.bind('<Button-1>', lambda eventbutton: self.ChangeFilterReport('PeriodUp', REQUEST_LIST,
                                                                                      OBJECTLIST, VIEW))
        OBJECTLIST.append(buttonPeriodUp)

        # Кнопка изменения размера периода фильтрации вниз
        buttonPeriodDown = tk.Button(self.frameMain, name='period_Down', background="black",
                                     image=self.arrowDown_img)
        buttonPeriodDown.place(x=290, y=660, width=40, height=40)
        buttonPeriodDown.bind('<Button-1>', lambda eventbutton: self.ChangeFilterReport('PeriodDown', REQUEST_LIST,
                                                                                        OBJECTLIST, VIEW))
        OBJECTLIST.append(buttonPeriodDown)

        # Выставленное значение фильтра
        lFilterValue = tk.Label(self.frameMain, name='filter_Text', text=self.SetFilterText(), bg="#808080",
                                foreground="#ccc", font="Arial 12")
        lFilterValue.place(x=375, y=640, width=200, height=40)
        OBJECTLIST.append(lFilterValue)

        # Кнопка переключения на широкий вид
        if self.SettingFilter['period'] != 'AllPeriod':
            paint_view = self.forward_img if VIEW == 'narrow' else self.Wrap_img

            # Кнопка переключения узкого и широкого вида
            button_view = tk.Button(self.frameMain, background="black", image=paint_view)
            button_view.place(x=580, y=640, width=40, height=40)
            button_view.bind('<Button-1>', lambda eventbutton: self.ChangeView(REQUEST_LIST, OBJECTLIST, VIEW))
            OBJECTLIST.append(button_view)

    # Отображение строк отчета
    def DrawStrings(self, LIST_STRING,  OBJECTLIST, REQUEST_LIST, VIEW, TOPLINE):
        """ Отображение строк отчета """
        # Список обновляемых объектов при скроллировании
        OBJSTRING = list()

        Y = 129
        if len(LIST_STRING) <= 16:
            for STRING in LIST_STRING:
                if STRING[2] == 'aktiv' or STRING[2] == 'passiv':
                    Y += 5
                self.StringReport(OBJECTLIST, OBJSTRING, STRING, Y, REQUEST_LIST, TOPLINE, VIEW)
                Y += 27
        else:
            length = len(LIST_STRING)
            count = length - TOPLINE
            count = TOPLINE + count if count < 16 else TOPLINE + 16
            for i in range(TOPLINE, count):
                if LIST_STRING[i][2] == 'aktiv' or LIST_STRING[i][2] == 'passiv':
                    Y += 5
                self.StringReport(OBJECTLIST, OBJSTRING, LIST_STRING[i], Y, REQUEST_LIST, TOPLINE, VIEW)
                Y += 27

        if len(LIST_STRING) > 16:
            # Кнопка прокрутки реестра вверх
            buttonUp = tk.Button(self.frameMain, background="black", image=self.arrowUp_img)
            buttonUp.place(x=10, y=300, width=40, height=40)
            buttonUp.bind('<Button-1>', lambda eventbutton: self.ScrollRegistryReport('UP', LIST_STRING, OBJECTLIST,
                                                                                      OBJSTRING, REQUEST_LIST, VIEW,
                                                                                      TOPLINE))
            OBJECTLIST.append(buttonUp)

            # Кнопка прокрутки реестра вниз
            buttonDown = tk.Button(self.frameMain, background="black", image=self.arrowDown_img)
            buttonDown.place(x=10, y=340, width=40, height=40)
            buttonDown.bind('<Button-1>', lambda eventbutton: self.ScrollRegistryReport('DOWN', LIST_STRING, OBJECTLIST,
                                                                                        OBJSTRING, REQUEST_LIST, VIEW,
                                                                                        TOPLINE))
            OBJECTLIST.append(buttonDown)

    # Скроллирование реестра отчета
    def ScrollRegistryReport(self, SIDE, LIST_STRING, OBJECTLIST, OBJSTRING, REQUEST_LIST, VIEW, TOPLINE):
        """ Скроллирование реестра отчета """
        if SIDE == 'UP':
            if TOPLINE == 0:
                return
            else:
                TOPLINE -= 3

                for obj in OBJSTRING:
                    if obj in OBJECTLIST:
                        OBJECTLIST.remove(obj)
                        obj.destroy()

                self.DrawStrings(LIST_STRING,  OBJECTLIST, REQUEST_LIST, VIEW, TOPLINE)

        elif SIDE == 'DOWN':
            if (len(LIST_STRING) - TOPLINE) <= 16:
                return
            else:
                TOPLINE += 3

                for obj in OBJSTRING:
                    if obj in OBJECTLIST:
                        OBJECTLIST.remove(obj)
                        obj.destroy()

                self.DrawStrings(LIST_STRING, OBJECTLIST, REQUEST_LIST, VIEW, TOPLINE)

    # Отображение строки отчета
    def StringReport(self, OBJECTLIST, OBJSTRING, STRING, Y, REQUEST_LIST, TOPLINE, VIEW='narrow'):
        """ Отображение одной строки отчета """
        COLOR, FONT, X, WIDTH = '', '', 0, 0

        if STRING[2] == 'item':
            typeitem = db.RequestSelectDB('typeitem_id', 'items', 'id={}'.format(STRING[len(STRING) - 1]))[0][0]
            COLOR = self.DefineTextAndColor(typeitem)[1]
            X = 125
            WIDTH = 200
        elif STRING[2] == 'section':
            if STRING[len(STRING) - 1] == 1:
                COLOR = '#F08080'
            elif STRING[len(STRING) - 1] == 2:
                COLOR = '#BA55D3'
            elif STRING[len(STRING) - 1] in (7, 8, 9):
                COLOR = '#DA70D6'
            else:
                COLOR = '#DB7093'
            X = 95
            WIDTH = 230

        elif STRING[2] == 'result':
            COLOR = '#DAA520'
            X = 55
            WIDTH = 270

        elif STRING[2] == 'aktiv':
            COLOR = '#C71585'
            X = 55
            WIDTH = 270

        elif STRING[2] == 'passiv':
            COLOR = '#800080'
            X = 55
            WIDTH = 270

        # Кнопка раскрытия узла
        if STRING[0] == 1 and STRING[2] == 'section':
            if STRING[1] == 0:
                IMAGE = self.forward25_img
            else:
                IMAGE = self.deployed25_img

            button_node = tk.Button(self.frameMain, background="black", image=IMAGE)
            button_node.place(x=67, y=Y, width=25, height=25)
            button_node.bind('<Button-1>', lambda eventbutton: self.NodeClick(OBJECTLIST, STRING, REQUEST_LIST, VIEW))
            OBJECTLIST.append(button_node)
            OBJSTRING.append(button_node)

        tex_font = "Arial 12" if STRING[2] == 'item' else "Arial 14"
        l_name = tk.Label(self.frameMain, text=STRING[3], bg=COLOR, foreground="#F5F5F5", font=tex_font)
        l_name.place(x=X, y=Y, width=WIDTH, height=25)
        OBJECTLIST.append(l_name)
        OBJSTRING.append(l_name)

        l_initial_balance = tk.Label(self.frameMain, text=self.NumberIsString(STRING[4]), bg="#A9A9A9",
                                     foreground="#F5F5F5", font="Arial 12")
        l_initial_balance.place(x=329, y=Y, width=150, height=25)
        OBJECTLIST.append(l_initial_balance)
        OBJSTRING.append(l_initial_balance)

        if VIEW == 'narrow':
            if STRING[5] != 0 and STRING[2] == 'item':
                button1_turnover = tk.Button(self.frameMain, text=self.NumberIsString(STRING[5]), bg="#808080",
                                             foreground="#F5F5F5", font="Arial 12")
                button1_turnover.place(x=483, y=Y, width=150, height=25)
                DATE1 = REQUEST_LIST[0][2] if self.SettingFilter['period'] != 'AllPeriod' else \
                    self.SettingFilter['beginDate']
                DATE2 = REQUEST_LIST[0][3] if self.SettingFilter['period'] != 'AllPeriod' else \
                    self.SettingFilter['endDate']
                button1_turnover.bind('<Button-1>', lambda eventbutton: self.ListDataInItemInReportWindow(
                    STRING, (DATE1, DATE2), REQUEST_LIST, VIEW, TOPLINE))

                OBJECTLIST.append(button1_turnover)
                OBJSTRING.append(button1_turnover)
            else:
                l1_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[5]), bg="#808080",
                                       foreground="#F5F5F5", font="Arial 12")
                l1_turnover.place(x=483, y=Y, width=150, height=25)
                OBJECTLIST.append(l1_turnover)
                OBJSTRING.append(l1_turnover)

            l_final_balance = tk.Label(self.frameMain, text=self.NumberIsString(STRING[6]), bg="#A9A9A9",
                                       foreground="#F5F5F5", font="Arial 12")
            l_final_balance.place(x=637, y=Y, width=150, height=25)
            OBJECTLIST.append(l_final_balance)
            OBJSTRING.append(l_final_balance)

        elif VIEW == 'wide':
            if STRING[5] != 0 and STRING[2] == 'item':
                button1_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[5]), bg="#808080",
                                            foreground="#F5F5F5", font="Arial 12")
                button1_turnover.place(x=483, y=Y, width=150, height=25)
                DATE3 = REQUEST_LIST[0][2]
                DATE4 = REQUEST_LIST[0][3]
                button1_turnover.bind('<Button-1>', lambda eventbutton: self.ListDataInItemInReportWindow(
                    STRING, (DATE3, DATE4), REQUEST_LIST, VIEW, TOPLINE))
                OBJECTLIST.append(button1_turnover)
                OBJSTRING.append(button1_turnover)
            else:
                l1_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[5]), bg="#808080",
                                       foreground="#F5F5F5", font="Arial 12")
                l1_turnover.place(x=483, y=Y, width=150, height=25)
                OBJECTLIST.append(l1_turnover)
                OBJSTRING.append(l1_turnover)

            if STRING[6] != 0 and STRING[2] == 'item':
                button2_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[6]), bg="#808080",
                                            foreground="#F5F5F5", font="Arial 12")
                button2_turnover.place(x=637, y=Y, width=150, height=25)
                DATE5 = REQUEST_LIST[0][4]
                DATE6 = REQUEST_LIST[0][5]
                button2_turnover.bind('<Button-1>', lambda eventbutton: self.ListDataInItemInReportWindow(
                    STRING, (DATE5, DATE6), REQUEST_LIST, VIEW, TOPLINE))
                OBJECTLIST.append(button2_turnover)
                OBJSTRING.append(button2_turnover)
            else:
                l2_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[6]), bg="#808080",
                                       foreground="#F5F5F5", font="Arial 12")
                l2_turnover.place(x=637, y=Y, width=150, height=25)
                OBJECTLIST.append(l2_turnover)
                OBJSTRING.append(l2_turnover)

            if STRING[7] != 0 and STRING[2] == 'item':
                button3_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[7]), bg="#808080",
                                            foreground="#F5F5F5", font="Arial 12")
                button3_turnover.place(x=791, y=Y, width=150, height=25)
                DATE7 = REQUEST_LIST[0][6]
                DATE8 = REQUEST_LIST[0][7]
                button3_turnover.bind('<Button-1>', lambda eventbutton: self.ListDataInItemInReportWindow(
                    STRING, (DATE7, DATE8), REQUEST_LIST, VIEW, TOPLINE))
                OBJECTLIST.append(button3_turnover)
                OBJSTRING.append(button3_turnover)
            else:
                l3_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[7]), bg="#808080",
                                       foreground="#F5F5F5", font="Arial 12")
                l3_turnover.place(x=791, y=Y, width=150, height=25)
                OBJECTLIST.append(l3_turnover)
                OBJSTRING.append(l3_turnover)

            if STRING[8] != 0 and STRING[2] == 'item':
                button4_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[8]), bg="#808080",
                                            foreground="#F5F5F5", font="Arial 12")
                button4_turnover.place(x=945, y=Y, width=150, height=25)
                DATE9 = REQUEST_LIST[0][8]
                DATE10 = REQUEST_LIST[0][9]
                button4_turnover.bind('<Button-1>', lambda eventbutton: self.ListDataInItemInReportWindow(
                    STRING, (DATE9, DATE10), REQUEST_LIST, VIEW, TOPLINE))
                OBJECTLIST.append(button4_turnover)
                OBJSTRING.append(button4_turnover)
            else:
                l4_turnover = tk.Label(self.frameMain, text=self.NumberIsString(STRING[8]), bg="#808080",
                                       foreground="#F5F5F5", font="Arial 12")
                l4_turnover.place(x=945, y=Y, width=150, height=25)
                OBJECTLIST.append(l4_turnover)
                OBJSTRING.append(l4_turnover)

            l_final_balance = tk.Label(self.frameMain, text=self.NumberIsString(STRING[9]), bg="#A9A9A9",
                                       foreground="#F5F5F5", font="Arial 12")
            l_final_balance.place(x=1099, y=Y, width=150, height=25)
            OBJECTLIST.append(l_final_balance)
            OBJSTRING.append(l_final_balance)

    #  Раскрытие/сворачивание узла раздела в отчете
    def NodeClick(self, OBJECTLIST, STRING, REQUEST_LIST, VIEW):
        """ Раскрытие/сворачивание узла раздела в отчете """
        NEW_REQUEST_LIST = list()
        for STR in REQUEST_LIST:
            if STR[1] == STRING[len(STRING) - 1]:
                if STR[0] == 0:
                    STR[0] = 1
                else:
                    STR[0] = 0
                NEW_REQUEST_LIST.append(STR)
            else:
                NEW_REQUEST_LIST.append(STR)
        print(NEW_REQUEST_LIST)

        # Очищаем область отчета
        for obj in OBJECTLIST:
            obj.destroy()

        # Строим обновленный очтет
        self.StringsReport(NEW_REQUEST_LIST, VIEW)

    # Обновление реестра отчета при изменении фильтрации
    def ChangeFilterReport(self, change, REQUEST_LIST, OBJECTLIST, VIEW='narrow'):
        """ Изменение значений словаря SettingFilter при нажатии на кнопку фильтра по дате при помощи вызова
         метода FindPeriod.
        Вызов метода обновления реестра и кнопок пэйджинга и фильтра ReportWindow"""
        # Изменение значений фильтрации при нажатии кнопок

        # Устанавливаем новые значения в SettingFilter для отбора по периоду
        self.FindPeriod(change)

        NEW_REQUEST_LIST = list()

        if self.SettingFilter['period'] == 'AllPeriod':
            VIEW = 'narrow'
            for section in REQUEST_LIST:
                section_list = [section[0], section[1]]
                NEW_REQUEST_LIST.append(section_list)

        elif self.SettingFilter['period'] != 'AllPeriod' and VIEW == 'narrow':
            for section in REQUEST_LIST:
                section_list = [section[0], section[1], self.SettingFilter['beginDate'], self.SettingFilter['endDate']]
                NEW_REQUEST_LIST.append(section_list)

        elif self.SettingFilter['period'] != 'AllPeriod' and VIEW == 'wide':
            FourPeriod = self.CalculateFourPeriods()
            for section in REQUEST_LIST:
                section_list = [section[0], section[1]]
                for li in FourPeriod:
                    section_list.append(li[0])
                    section_list.append(li[1])
                NEW_REQUEST_LIST.append(section_list)

        # Очищаем область отчета
        for obj in OBJECTLIST:
            obj.destroy()

        # Отрисовываем новые данные, пейджинг и фильтр
        self.StringsReport(NEW_REQUEST_LIST, VIEW)

    # Переключение на широкий/узкий вид
    def ChangeView(self, REQUEST_LIST, OBJECTLIST, VIEW):
        """ Переключение на широкий/узкий вид """
        NEW_REQUEST_LIST = list()
        view = 'narrow' if VIEW == 'wide' else 'wide'
        print(view)
        if view == 'narrow':
            for section in REQUEST_LIST:
                section_list = [section[0], section[1], self.SettingFilter['beginDate'], self.SettingFilter['endDate']]
                NEW_REQUEST_LIST.append(section_list)
        elif view == 'wide':
            FourPeriod = self.CalculateFourPeriods()
            print(FourPeriod)
            for section in REQUEST_LIST:
                section_list = [section[0], section[1]]
                for li in FourPeriod:
                    section_list.append(li[0])
                    section_list.append(li[1])
                NEW_REQUEST_LIST.append(section_list)

        # Очищаем область отчета
        for obj in OBJECTLIST:
            obj.destroy()

        # Отрисовываем новые данные, пейджинг и фильтр
        self.StringsReport(NEW_REQUEST_LIST, view)

    # Расчет 4 периодов для широкого вида
    def CalculateFourPeriods(self):
        print('CalculateFourPeriods(self)')
        """ Расчет 4 периодов для широкого вида """
        FourPeriods = list()
        FourPeriods.append([self.SettingFilter['beginDate'], self.SettingFilter['endDate']])

        # Подбираем 3 периода года, ищем сначала сзади, если там упираемся, то спереди
        if self.SettingFilter['period'] == 'YearPeriod':
            print('YearPeriod')
            if self.SettingFilter['beginDate'] == db.beginDate:
                for i in range(3):
                    new_date_begin = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1, 1)
                    new_date_end = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 12, 31)
                    FourPeriods.append([new_date_begin, new_date_end])
            else:
                for i in range(3):
                    new_date_begin = dt.date(FourPeriods[0][1].year - 1, 1, 1)
                    new_date_end = dt.date(FourPeriods[0][1].year - 1, 12, 31)
                    if new_date_begin.year == db.beginDate.year:
                        new_date_begin = db.beginDate
                        FourPeriods.insert(0, [new_date_begin, new_date_end])
                        break
                    else:
                        FourPeriods.insert(0, [new_date_begin, new_date_end])

            if len(FourPeriods) < 4:
                for i in range(4 - len(FourPeriods)):
                    new_date_begin = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1, 1)
                    new_date_end = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 12, 31)
                    FourPeriods.append([new_date_begin, new_date_end])

        # Подбираем 3 периода месяца, ищем сначала сзади, если там упираемся, то спереди
        elif self.SettingFilter['period'] == 'MonthPeriod':
            print('MonthPeriod')
            if self.SettingFilter['beginDate'] == db.beginDate:
                for i in range(3):
                    if FourPeriods[len(FourPeriods) - 1][1].month != 12:
                        dayMonth = calendar.monthrange(FourPeriods[len(FourPeriods) - 1][1].year,
                                                       FourPeriods[len(FourPeriods) - 1][1].month + 1)[1]
                        new_date_begin = dt.date(FourPeriods[len(FourPeriods) - 1][1].year,
                                                 FourPeriods[len(FourPeriods) - 1][1].month + 1, 1)

                        new_date_end = dt.date(FourPeriods[len(FourPeriods) - 1][1].year,
                                               FourPeriods[len(FourPeriods) - 1][1].month + 1, dayMonth)
                        FourPeriods.append([new_date_begin, new_date_end])

                    else:
                        dayMonth = calendar.monthrange(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1)[1]
                        new_date_begin = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1, 1)

                        new_date_end = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1, dayMonth)
                        FourPeriods.append([new_date_begin, new_date_end])
            else:
                for i in range(3):
                    if FourPeriods[0][1].month != 1:
                        dayMonth = calendar.monthrange(FourPeriods[0][1].year,
                                                       FourPeriods[0][1].month - 1)[1]
                        new_date_begin = dt.date(FourPeriods[0][1].year, FourPeriods[0][1].month - 1, 1)

                        new_date_end = dt.date(FourPeriods[0][1].year, FourPeriods[0][1].month - 1, dayMonth)
                    else:
                        dayMonth = calendar.monthrange(FourPeriods[0][1].year - 1, 1)[1]
                        new_date_begin = dt.date(FourPeriods[0][1].year - 1, 12, 1)

                        new_date_end = dt.date(FourPeriods[0][1].year - 1, 12, dayMonth)

                    if new_date_begin <= db.beginDate:
                        new_date_begin = db.beginDate
                        FourPeriods.insert(0, [new_date_begin, new_date_end])
                        break
                    FourPeriods.insert(0, [new_date_begin, new_date_end])

            if len(FourPeriods) < 4:
                for i in range(4 - len(FourPeriods)):
                    if FourPeriods[len(FourPeriods) - 1][1].month != 12:
                        dayMonth = calendar.monthrange(FourPeriods[len(FourPeriods) - 1][1].year,
                                                       FourPeriods[len(FourPeriods) - 1][1].month + 1)[1]
                        new_date_begin = dt.date(FourPeriods[len(FourPeriods) - 1][1].year,
                                                 FourPeriods[len(FourPeriods) - 1][1].month + 1, 1)

                        new_date_end = dt.date(FourPeriods[len(FourPeriods) - 1][1].year,
                                               FourPeriods[len(FourPeriods) - 1][1].month + 1, dayMonth)
                        FourPeriods.append([new_date_begin, new_date_end])

                    else:
                        dayMonth = calendar.monthrange(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1)[1]
                        new_date_begin = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1, 1)
                        new_date_end = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1, dayMonth)
                        FourPeriods.append([new_date_begin, new_date_end])

        # Подбираем 3 периода недели, ищем сначала сзади, если там упираемся, то спереди
        elif self.SettingFilter['period'] == 'WeekPeriod':
            print('WeekPeriod')
            if self.SettingFilter['beginDate'] == db.beginDate:
                for i in range(3):
                    new_date_begin = FourPeriods[len(FourPeriods) - 1][0] + timedelta(weeks=1)
                    new_date_end = FourPeriods[len(FourPeriods) - 1][1] + timedelta(6)
                    FourPeriods.append([new_date_begin, new_date_end])
            else:
                for i in range(3):
                    new_date_begin = FourPeriods[0][0] - timedelta(weeks=1)
                    new_date_end = FourPeriods[0][1] - timedelta(weeks=1)

                    if new_date_begin <= db.beginDate:
                        new_date_begin = db.beginDate
                        FourPeriods.insert(0, [new_date_begin, new_date_end])
                        break
                    FourPeriods.insert(0, [new_date_begin, new_date_end])
            if len(FourPeriods) < 4:
                for i in range(4 - len(FourPeriods)):
                    new_date_begin = FourPeriods[len(FourPeriods) - 1][0] + timedelta(weeks=1)
                    new_date_end = FourPeriods[len(FourPeriods) - 1][1] - timedelta(6)
                    FourPeriods.append([new_date_begin, new_date_end])

        # Подбираем 3 периода дня, ищем сначала сзади, если там упираемся, то спереди
        elif self.SettingFilter['period'] == 'DayPeriod':
            print('DayPeriod')
            if self.SettingFilter['beginDate'] == db.beginDate:
                for i in range(3):
                    new_date_begin = FourPeriods[len(FourPeriods) - 1][0] + timedelta(1)
                    new_date_end = FourPeriods[len(FourPeriods) - 1][1] + timedelta(1)
                    FourPeriods.append([new_date_begin, new_date_end])
            else:
                for i in range(3):
                    new_date_begin = FourPeriods[0][0] - timedelta(1)
                    new_date_end = FourPeriods[0][1] - timedelta(1)

                    if new_date_begin <= db.beginDate:
                        new_date_begin = db.beginDate
                        FourPeriods.insert(0, [new_date_begin, new_date_end])
                        break
                    FourPeriods.insert(0, [new_date_begin, new_date_end])

            if len(FourPeriods) < 4:
                for i in range(4 - len(FourPeriods)):
                    new_date_begin = FourPeriods[len(FourPeriods) - 1][0] + timedelta(1)
                    new_date_end = FourPeriods[len(FourPeriods) - 1][1] + timedelta(1)
                    FourPeriods.append([new_date_begin, new_date_end])

        return FourPeriods

    # Окно для отображения данных по статье за период фильтрации из Отчета, содержит постраничный пэйджинг
    def ListDataInItemInReportWindow(self, STRING, DATES, REQUEST_LIST, VIEW, TOPLINE):
        """ Окно для отображения данных по статье за период фильтрации из Отчета, содержит постраничный пэйджинг """
        # Список обновляемых элементов
        ElementsToDraw = list()

        # Устанавливаем идентификатоо текущей страницы
        self.CurrentWindow = 13

        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)

        # Очищаем страницу
        self.Clear()

        # Кнопка назад
        button_back = tk.Button(self.toolbarMenu, image=self.back_img, bg='black', name='button_Back')
        button_back.place(x=130, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.ReportWindow(REQUEST_LIST, VIEW, TOPLINE))

        # Картинка отчета
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.report_img)
        Main_paint.place(x=820, y=45)

        # Заголовок страницы
        textheaders = 'ПРОСМОТР ОТЧЕТА' + '/' + STRING[3] + '/Расшифровка :'
        l1 = tk.Label(self.frameMain, text=textheaders, bg='black', foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=0)
        item_id = (STRING[len(STRING) - 1])
        print(item_id, DATES)
        # Отрисовка списка строк с данными, постраничного пэйджинга и фильтра
        self.DrawListOfRow(item_id, ElementsToDraw, DATES[0], DATES[1])
        print('OBJECTLIST = {}'.format(ElementsToDraw))


# Создание и управление базами данных
class DB:
    def __init__(self):
        # Сегодняшняя дата и дата начала учета для быстрого доступа
        self.__today = dt.date.today()
        self.__beginDate = dt.date.today()
        # Переменная рабочей/нерабочей программы
        self.__use = 0

        # global beginDate
        # global use

        if not ospath.exists('setting.db'):
            # Создаем базу данных настроек при первом входе
            self.conn = sqlite3.connect('setting.db')
            self.c = self.conn.cursor()
            self.c.execute('''CREATE TABLE IF NOT EXISTS setting (id integer primary key, parol text, date date,
                              use integer, wallet integer references typeitems(id),  costkm integer)''')
            self.conn.commit()
            self.c.execute('''INSERT INTO setting(parol, date, use, wallet, costkm) VALUES (?, ?, ?, ?, ?)''',
                           ('777', self.todayDate, self.use, None, 0))
            self.conn.commit()
            print('OK! БД с настроек создана')
            self.conn.close()
        else:
            print('OK! БД настроек уже существует')
            data = self.RequestSelectDB('date, use', 'setting')
            self.beginDate = dt.datetime.strptime(data[0][0], '%Y-%m-%d').date()
            self.use = data[0][1]

        if not ospath.exists('typeitems.db'):  # Создаем базу данных типов статей при начале работы
            self.conn = sqlite3.connect('typeitems.db')
            self.c = self.conn.cursor()
            self.c.execute(
                '''CREATE TABLE IF NOT EXISTS typeitems (id integer primary key, typetypeitems integer,
                 nametypeitems text, descriptoiontypeitems text, suminitialtypeitems real, sumcurrenttypeitems real)''')
            # Доходы = 0, Расходы = 1, Актив = 2, Пассив = 3, Собственный капитал = 4;
            data = [(
                0, 'Доходы', 'Поступление доходов: зарплаты, процентов по депозитам, ареднных платежей и прочих', 0,
                0),
                (1, 'Расходы', 'Расход денежных средств на еду, бытовые расходы, процентные платежи и прочее', 0, 0),
                (2, 'Денежные средства', 'Рублевые денежные средства наличными и на картах ', 0, 0),
                (2, 'Имущество', 'Квартиры, автотранспорт, земельные участки и иное дорогостоящее имущество', 0, 0),
                (2, 'Вложения', 'Депозиты, валюта, акции, золото и другие ликвидные активы', 0, 0),
                (2, 'Выданные займы', 'Денежные средства выданные третьим лицам на условиях возврата', 0, 0),
                (3, 'Кредиты', 'Задолженность по основному долгу по кредитам, кредитным картам, ипотеке и прочим '
                               'продуктам перед банками', 0, 0),
                (3, 'Полученные займы', 'Задолженность перед родственниками, друзьями, и прочими лицами', 0, 0),
                (4, 'Собственный капитал', 'Разница между активом и пассивом', 0, 0)]
            self.c.executemany('''INSERT INTO typeitems(typetypeitems, nametypeitems, descriptoiontypeitems, 
                             suminitialtypeitems, sumcurrenttypeitems) VALUES( ?, ?, ?, ?, ?)''', data)
            self.conn.commit()
            print('OK! БД с типами статей создана')
            self.conn.close()
        else:
            # Скорее всего делать ничего не надо, максимум забрать суммы из статей в "Дежурный" динамический массив
            print('OK! БД с типами статей уже существует')

        if not ospath.exists('typeinvestments.db'):
            # Создаем базу данных для хранения данных по видам вложений при начале работы
            self.conn = sqlite3.connect('typeinvestments.db')
            self.c = self.conn.cursor()
            self.c.execute(
                '''CREATE TABLE IF NOT EXISTS typeinvestments (id integer primary key,nametypeinvestments text )''')
            self.conn.commit()
            print('OK! БД для хранения видов вложений создана')
            self.conn.close()
        else:
            # Скорее всего делать ничего не надо, максимум забрать суммы из статей в "Дежурный" динамический массив
            print('OK! БД для хранения видов вложений уже существует')

        if not ospath.exists('items.db'):
            # Создаем базу данных инсталляционных статей при начале работы
            self.conn = sqlite3.connect('items.db')
            self.c = self.conn.cursor()
            self.c.execute(
                '''CREATE TABLE IF NOT EXISTS items (id integer primary key, 
                       typeitem_id integer references typeitems(id), nameitem text, workingitem integer,
                       descriptoionitem text, creditcard integer, initialbalanceitem real, currentbalanceitem real,
                       paintitem integer, candelete integer, quantitativeaccounting integer, 
                       typeinvestment_id integer references typeinvestments(id), countinvestment real,
                       priceunit real, dateclose date )''')

            # Добавление исталляционных статей в таблицу
            # workingitem == 1 - статья рабочая, workingitem == 0 - статья НЕ рабочая (Закрыта)
            # creditcard == 0 - не КК, creditcard == 1 - КК - выбирается в кошельке при оплате затрат
            # candelete == 1 -можно удалить; candelete == 0 - нельзя удалить;
            # quantitativeaccounting == 0 -нет количественного учета в статье;
            # quantitativeaccounting == 1 -есть количественный учет в статье;
            # startitem == 1 - статья стартовая; startitem == 0 - статья текущая;
            data = [

                (1, 'Прочие доходы', 1, 'Поступление непостоянных, случайных доходов, продажа имущества,'
                 ' переоцека имущества и вложений в большую сторону',
                 0, 0, 0, 15, 0, 0, None, 0, 0, '2200-01-01'),
                (2, 'Еда', 1, 'Расходы на еду дома и в заведениях',
                 0, 0, 0, 11, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Жильё', 1, 'Аренда, коммунальные услуги',
                 0, 0, 0, 2, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Быт', 1, 'Расходы на мелкие бытовые расходы: ',
                 0, 0, 0, 20, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Передвижение', 1, 'Расходы на такси, автобусы, метро',
                 0, 0, 0, 0, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Здоровье', 1, 'Расходы на лекарства и медицинские процедуры',
                 0, 0, 0, 24, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Подарки', 1, 'Расходы на подарки и знаки внимания',
                 0, 0, 0, 13, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Алкоголь', 1, 'Расходы на быры, пиво и подобное',
                 0, 0, 0, 1, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Бытовая техника, мебель', 1, 'Расходы на бытовую технику и мебель: ',
                 0, 0, 0, 38, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Спорт', 1, 'Расходы на абонементы и спорттовары',
                 0, 0, 0, 8, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Образование и развитие', 1, 'Расходы на образовательные курсы и книги',
                 0, 0, 0, 39, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Одежда', 1, 'Расходы на одежду и аксессуары',
                 0, 0, 0, 40, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Питомцы и растения', 1, 'Раходы на домашних животных и комнатные растения: ',
                 0, 0, 0, 31, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Автотранспорт', 1, 'Расходы на авто-мото технику',
                 0, 0, 0, 3, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Бензин', 1, 'Расходы на бензин и дизельное топливо',
                 0, 0, 0, 4, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Проценты и комиссии', 1, 'Расходы на проценты по кредитам и комиссии банкам',
                 0, 0, 0, 19, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Прочее', 1, 'Расходы не укладывающиеся в другие статьи',
                 0, 0, 0, 33, 1, 0, None, 0, 0, '2200-01-01'),
                (2, 'Прочие расходы', 1,
                 'Внезапные расходы или потеря имущества, переоцека имущества и вложений в меньшую сторону',
                 0, 0, 0, 33, 0, 0, None, 0, 0, '2200-01-01'),
                (3, 'Наличные', 1, 'Наличные денежные средства в рублях',
                 0, 0, 0, 25, 0, 0, None, 0, 0, '2200-01-01')]

            self.c.executemany('''INSERT INTO items(typeitem_id, nameitem, workingitem, descriptoionitem, creditcard, 
                       initialbalanceitem, currentbalanceitem, paintitem, candelete, quantitativeaccounting, 
                       typeinvestment_id, countinvestment, priceunit, dateclose) 
                       VALUES(  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
            self.conn.commit()
            print('OK! БД с перечнем инсталляционных статей создана')
            self.conn.close()
        else:
            # Скорее всего делать ничего не надо, максимум забрать суммы из статей в "Дежурный" динамический массив
            print('OK! БД с перечнем инсталляционных статей уже существует')

        if self.use == 1 and ospath.exists('notes.db'):
            print('OK! Программа рабочая, БД notes.db существует')
        elif self.use == 0 and not ospath.exists('notes.db'):
            print('OK! Программа НЕ рабочая, БД notes.db НЕ существует')
        elif self.use == 0 and ospath.exists('notes.db'):
            print('ERROR Программа НЕ рабочая, БД notes.db существует')
        elif self.use == 1 and not ospath.exists('notes.db'):
            print('ERROR Программа рабочая, БД notes.db НЕ существует')

        # Перепроверяем остатки расчетные с сохраненными в базе в статьях и разделах
        if ospath.exists('items.db') and ospath.exists('typeitems.db') and ospath.exists('notes.db'):
            self.HardRecalculatingBalances()
            # self.autocomplete()

    @property
    def todayDate(self):
        return self.__today

    @todayDate.setter
    def todayDate(self, todayDate):
        self.__today = todayDate

    @property
    def beginDate(self):
        return self.__beginDate

    @beginDate.setter
    def beginDate(self, beginDat):
        self.__beginDate = beginDat

    @property
    def use(self):
        return self.__use

    @use.setter
    def use(self, useProgram):
        self.__use = useProgram

    # Создаем таблицу для записи данных
    def CreateBDforNotes(self):
        # increase == 1 - запись увеличивает сумму статьи; increase == 0 - запись уменьшает сумму статьи;
        if not ospath.exists('notes.db'):
            # Создаем базу данных для хранения данных по операциям при начале работы
            self.conn = sqlite3.connect('notes.db')
            self.c = self.conn.cursor()
            self.c.execute(
                '''CREATE TABLE IF NOT EXISTS notes (id integer primary key, item_id integer references items(id),
                       typeitem_id integer references typeitems(id), dateoperation date, descriptoionoperation text,
                       sumoperation real, increase integer, source integer references items(id),
                       typeinvestment_id integer references typeinvestment(id), countnote real, priseunit real )''')
            self.conn.commit()
            print('БД для внесения записей создана')
            self.conn.close()
        else:
            # Скорее всего делать ничего не надо, максимум забрать суммы из статей в "Дежурный" динамический массив
            print('WARNING!!! БД для внесения записей уже существует')

    # Метод добавления новой статьи
    def AddNewItem(self, data):
        self.conn = sqlite3.connect('items.db')
        self.c = self.conn.cursor()
        self.c.execute(''' INSERT INTO items (typeitem_id, nameitem, workingitem, descriptoionitem, creditcard,
                       initialbalanceitem, currentbalanceitem, paintitem, candelete, quantitativeaccounting, 
                       typeinvestment_id, countinvestment, priceunit, dateclose)
                       VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
        self.conn.commit()
        print('В БД внесена запись по статье')
        self.conn.close()

        # Пересчитываем остатки при создании новой статьи
        self.RecalculatingBalancesItem('NEW', data[0], data[5])

    # Метод удаления статьи
    def DeleteItemDB(self, iditem):
        # Пересчитываем остатки при удалении статьи
        self.RecalculatingBalancesItem('DELETE', iditem)

        print('Type iditemDB {}'.format(type(iditem)))
        self.conn = sqlite3.connect('items.db')
        self.c = self.conn.cursor()
        self.c.execute('''DELETE FROM items WHERE id=?''', (iditem,))
        self.conn.commit()
        print('Из БД удалена запись по статье')
        self.conn.close()

    # Метод изменения данных операции
    def UpdateOperation(self, DATA, NOTE):
        print(DATA)
        self.conn = sqlite3.connect('notes.db')
        self.c = self.conn.cursor()
        self.c.execute(''' UPDATE notes SET item_id=?, typeitem_id=?, dateoperation=?, descriptoionoperation=?,
                           sumoperation=?, increase=?, source=?, typeinvestment_id=?, countnote=?, priseunit=? 
                            WHERE id=? ''', (DATA['iditemkey'], DATA['idtypeitemkey'], DATA['dateoperationkey'],
                                             DATA['descriptionkey'], DATA['sumoperationkey'], DATA['increasekey'],
                                             DATA['sourcekey'], DATA['typeinvestmentidkey'], DATA['countnotekey'],
                                             DATA['priseunit'], NOTE[0]))
        self.conn.commit()
        print('В БД изменена запись по статье')
        self.conn.close()

        # Пересчитываем остатки
        # Сторнируем операцию до изменения
        self.RecalculatingBalances(NOTE[1], NOTE[7], NOTE[6], -NOTE[5])
        # Пересчитываем остатки с учетом измененной операции
        self.RecalculatingBalances(DATA['iditemkey'], DATA['sourcekey'], DATA['increasekey'], DATA['sumoperationkey'])

    # Метод изменения данных одного поля
    def UpdateNoteDB(self, database, field, idname, data, iditem):
        # Пересчитываем остатки при изменении начального остатка статьи
        if field == 'initialbalanceitem':
            self.RecalculatingBalancesItem('CORRECTION', iditem, data)

        namedb = '{}.db'.format(database)
        self.conn = sqlite3.connect(namedb)
        self.c = self.conn.cursor()
        request = 'UPDATE {} SET {}=? WHERE {}=?'.format(database, field, idname)
        # print(request)
        self.c.execute(request, (data, iditem))
        self.conn.commit()
        print('В БД изменена запись по статье в одном поле {}-{}'.format(data, iditem))
        self.conn.close()

    # Метод запроса данных
    def RequestSelectDB(self, selectionfields, database, conditionfields=''):
        namedb = '{}.db'.format(database)
        self.conn = sqlite3.connect(namedb)
        self.c = self.conn.cursor()

        if conditionfields == '':
            request = 'SELECT {} FROM {} '.format(selectionfields, database)
        else:
            request = 'SELECT {} FROM {} WHERE {}'.format(selectionfields, database, conditionfields)

        # print(request)
        self.c.execute(request)
        data = self.c.fetchall()
        self.conn.close()
        return data

    # Метод добавления новой операции
    def AddNewOperation(self, data):
        print(data)
        datalist = list()
        for value in data.values():
            datalist.append(value)

        self.conn = sqlite3.connect('notes.db')
        self.c = self.conn.cursor()
        self.c.execute('''INSERT INTO notes (item_id, typeitem_id, dateoperation, descriptoionoperation, sumoperation,
          increase, source, typeinvestment_id, countnote, priseunit) VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', datalist)

        self.conn.commit()
        print('В БД внесена запись по операции')
        self.conn.close()

        # Пересчитываем остатки
        self.RecalculatingBalances(data['iditemkey'], data['sourcekey'], data['increasekey'], data['sumoperationkey'])

    # Метод удаления записи с данными по операции
    def DeleteNoteDB(self, DATA):
        self.conn = sqlite3.connect('notes.db')
        self.c = self.conn.cursor()
        self.c.execute('''DELETE FROM notes WHERE id=?''', (DATA[0],))
        self.conn.commit()
        print('Из БД удалена запись по c данными по операции')
        self.conn.close()

    # Пересчет и установка остатков при загрузке программы
    def HardRecalculatingBalances(self):
        print('Тяжелый пересчет остатков запущен')
        # Получаем кортеж разделов
        typeitemdata = self.RequestSelectDB('*', 'typeitems')
        # Перебираем все разделы
        for TYPEITEM in typeitemdata:
            # Прерываем, если добрались до собственного капитала
            if TYPEITEM[0] == 9:
                break
            # Получаем кортеж всех статей в разделе
            itemdata = self.RequestSelectDB('*', 'items', 'typeitem_id={}'.format(TYPEITEM[0]))

            # Перебираем все статьи
            for ITEM in itemdata:
                # Упрощенный расчет для доходов и расходов
                remainsITEM = 0
                if TYPEITEM[0] == 1 or TYPEITEM[0] == 2:
                    sumitem = self.RequestSelectDB('sum(sumoperation)', 'notes', 'item_id={}'.format(ITEM[0]))
                    sumitem = self.CheckResultForNone(sumitem)
                    remainsITEM = sumitem

                # Расчет остатка для остальных статей
                elif TYPEITEM[0] != 1 or TYPEITEM[0] != 2 or TYPEITEM[0] != 9:
                    # Считаем сумму положительных оборотов по статье
                    tex2 = '(item_id={} AND (increase=1 or increase=2)) or (source={} AND (increase=0 or increase=2))'.\
                        format(ITEM[0], ITEM[0])
                    data2 = self.RequestSelectDB('sum(sumoperation)', 'notes', tex2)
                    data2 = self.CheckResultForNone(data2)

                    # Считаем сумму отицательных обортов по статье
                    tex3 = '(item_id={} AND (increase=0 or increase=3)) or (source={} AND (increase=1 or increase=3))'.\
                        format(ITEM[0], ITEM[0])
                    data3 = self.RequestSelectDB('sum(sumoperation)', 'notes', tex3)
                    data3 = self.CheckResultForNone(data3)

                    # Считаем сумму текущего остатка по статье
                    remainsITEM = ITEM[6] + data2 - data3

                # Сравниваем полученный остаток по статье с остатком в базе, выкидываем сообщение и перезаписываем
                # остаток в базе, если они различаются
                if ITEM[7] != remainsITEM:
                    print('WARNING: Остаток статьи {} рассчитан {} не равен остатку в базе {}, перезаписан на'
                          ' расчетный'.format(ITEM[2], remainsITEM, ITEM[7]))
                    self.UpdateNoteDB('items', 'currentbalanceitem', 'id', remainsITEM, ITEM[0])

            # Рассчитывем начальный остаток разделов и сравниваем с сохраненным в базе
            if TYPEITEM[0] != 1 and TYPEITEM[0] != 2 and TYPEITEM[0] != 9:
                data4_1 = self.RequestSelectDB('sum(initialbalanceitem)', 'items', 'typeitem_id={}'.format(TYPEITEM[0]))
                data4_1 = self.CheckResultForNone(data4_1)
                if data4_1 != TYPEITEM[4]:
                    print('WARNING: Начальный остаток раздела {} рассчитан {} не равен остатку в базе {}, перезаписан '
                          'на расчетный'.format(TYPEITEM[2], data4_1, TYPEITEM[4]))
                    self.UpdateNoteDB('typeitems', 'suminitialtypeitems', 'id', data4_1, TYPEITEM[0])

                # Рассчитывем текущий остаток и сравниваем с сохраненным в базе
                data4_2 = self.RequestSelectDB('sum(currentbalanceitem)', 'items', 'typeitem_id={}'.format(TYPEITEM[0]))
                data4_2 = self.CheckResultForNone(data4_2)
                if data4_2 != TYPEITEM[5]:
                    print('WARNING: Текущий остаток раздела {} рассчитан {} не равен остатку в базе {}, перезаписан на'
                          ' расчетный'.format(TYPEITEM[2], data4_2, TYPEITEM[5]))
                    self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', data4_2, TYPEITEM[0])

        # Рассчитываем собственный капитал
        # Получаем кортеж разделов снова, на случай перезаписи данных
        TYPEITEMNEW = self.RequestSelectDB('*', 'typeitems')
        # Рассчитываем начальный собственный капитал
        suminitial = TYPEITEMNEW[2][4] + TYPEITEMNEW[3][4] + TYPEITEMNEW[4][4] + TYPEITEMNEW[5][4] - TYPEITEMNEW[6][4] \
                     - TYPEITEMNEW[7][4]
        if suminitial != typeitemdata[8][4]:
            print('WARNING: Начальный остаток раздела {} рассчитан {} не равен остатку в базе {}, перезаписан на'
                  ' расчетный'.format(typeitemdata[8][2], suminitial, typeitemdata[8][4]))
            self.UpdateNoteDB('typeitems', 'suminitialtypeitems', 'id', suminitial, 9)

        # Рассчитываем текущий собственный капитал
        sumcurrent = TYPEITEMNEW[2][5] + TYPEITEMNEW[3][5] + TYPEITEMNEW[4][5] + TYPEITEMNEW[5][5] - TYPEITEMNEW[6][5] \
                   - TYPEITEMNEW[7][5]
        if sumcurrent != typeitemdata[8][5]:
            print('WARNING: Текущий остаток раздела {} рассчитан {} не равен остатку в базе {}, перезаписан на'
                  ' расчетный'.format(typeitemdata[8][2], sumcurrent, typeitemdata[8][5]))
            self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', sumcurrent, 9)

        print('Тяжелый пересчет остатков завершен')

    # Пересчет и установка остатков при создании/изменении операции
    def RecalculatingBalances(self, ITEM1, ITEM2, INCREASE, SUMOPERATIONS):
        print('Пересчет остатков')

        # Расчет и установка нового текущего остатка по статьям
        balance_item = self.RequestSelectDB('currentbalanceitem', 'items', 'id={}'.format(ITEM1))
        balance_source = self.RequestSelectDB('currentbalanceitem', 'items', 'id={}'.format(ITEM2))

        if INCREASE == 0:
            balanceitem = balance_item[0][0] - SUMOPERATIONS
            balancesource = balance_source[0][0] + SUMOPERATIONS
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', balanceitem, ITEM1)
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', balancesource, ITEM2)
        elif INCREASE == 1:
            balanceitem = balance_item[0][0] + SUMOPERATIONS
            balancesource = balance_source[0][0] - SUMOPERATIONS
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', balanceitem, ITEM1)
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', balancesource, ITEM2)
        elif INCREASE == 2:
            balanceitem = balance_item[0][0] + SUMOPERATIONS
            balancesource = balance_source[0][0] + SUMOPERATIONS
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', balanceitem, ITEM1)
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', balancesource, ITEM2)
        elif INCREASE == 3:
            balanceitem = balance_item[0][0] - SUMOPERATIONS
            balancesource = balance_source[0][0] - SUMOPERATIONS
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', balanceitem, ITEM1)
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', balancesource, ITEM2)

        # Расчет и установка нового текущего остатка по разделам
        sectionItem1 = self.RequestSelectDB('typeitem_id', 'items', 'id={}'.format(ITEM1))[0][0]
        sectionItem2 = self.RequestSelectDB('typeitem_id', 'items', 'id={}'.format(ITEM2))[0][0]
        if sectionItem1 != sectionItem2:
            balans_sectionItem1 = self.RequestSelectDB('sumcurrenttypeitems', 'typeitems', 'id={}'.format(
                sectionItem1))[0][0]
            balans_sectionItem2 = self.RequestSelectDB('sumcurrenttypeitems', 'typeitems', 'id={}'.format(
                sectionItem2))[0][0]

            if INCREASE == 0:
                balanssectionItem1 = balans_sectionItem1 - SUMOPERATIONS
                balanssectionItem2 = balans_sectionItem2 + SUMOPERATIONS
                self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem1, sectionItem1)
                self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem2, sectionItem2)
            elif INCREASE == 1:
                balanssectionItem1 = balans_sectionItem1 + SUMOPERATIONS
                balanssectionItem2 = balans_sectionItem2 - SUMOPERATIONS
                self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem1, sectionItem1)
                self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem2, sectionItem2)
            elif INCREASE == 2:
                balanssectionItem1 = balans_sectionItem1 + SUMOPERATIONS
                balanssectionItem2 = balans_sectionItem2 + SUMOPERATIONS
                self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem1, sectionItem1)
                self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem2, sectionItem2)
            elif INCREASE == 3:
                balanssectionItem1 = balans_sectionItem1 - SUMOPERATIONS
                balanssectionItem2 = balans_sectionItem2 - SUMOPERATIONS
                self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem1, sectionItem1)
                self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem2, sectionItem2)

            # Рассчитываем и устанавливаем текущий собственный капитал
            data5 = self.RequestSelectDB('*', 'typeitems')
            sumcurrent = data5[2][5] + data5[3][5] + data5[4][5] + data5[5][5] - data5[6][5] - data5[7][5]
            self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', sumcurrent, 9)

    # Пересчет остатков при внесении изменений в начальные остатки статей
    def RecalculatingBalancesItem(self, TYPE, ITEMID, SUM=0):
        """ Пересчет остатков при внесении изменений в начальные остатки статей """
        if TYPE == 'DELETE':
            SUM = -self.RequestSelectDB('initialbalanceitem', 'items', 'id={}'.format(ITEMID))[0][0]

        elif TYPE == 'CORRECTION':
            SUM = SUM - self.RequestSelectDB('initialbalanceitem', 'items', 'id={}'.format(ITEMID))[0][0]
            SUM2 = self.RequestSelectDB('currentbalanceitem', 'items', 'id={}'.format(ITEMID))[0][0]
            self.UpdateNoteDB('items', 'currentbalanceitem', 'id', SUM2 + SUM, ITEMID)

        # Изменяем остатки в разделе статьи
        type_id = ITEMID if TYPE == 'NEW' else self.RequestSelectDB('typeitem_id', 'items', 'id={}'.format(
            ITEMID))[0][0]
        sums = self.RequestSelectDB('suminitialtypeitems, sumcurrenttypeitems', 'typeitems', 'id={}'.format(
                type_id))[0]
        print(sums)
        self.UpdateNoteDB('typeitems', 'suminitialtypeitems', 'id', sums[0] + SUM, type_id)
        self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', sums[1] + SUM, type_id)
        print('Cумма изменений = {}'.format(SUM))
        # Изменяем остаток собственного капитала
        SUM = SUM if type_id in (3, 4, 5, 6) else -SUM
        print('Cумма изменений = {}'.format(SUM))

        sums2 = self.RequestSelectDB('suminitialtypeitems, sumcurrenttypeitems', 'typeitems', 'id=9')[0]
        print(sums2)
        self.UpdateNoteDB('typeitems', 'suminitialtypeitems', 'id', sums2[0] + SUM, 9)
        self.UpdateNoteDB('typeitems', 'sumcurrenttypeitems', 'id', sums2[1] + SUM, 9)

    # Проверяем результат запроса суммы на None
    def CheckResultForNone(self, DATA):
        if DATA[0][0] is None:
            data = 0
        else:
            data = DATA[0][0]
        return data

    # Преобразование строковых данных старой версии программы в записи БД
    def autocomplete(self, item_id=20, typeitem_id=3):
        global bufferList
        myfile = 'D://FinancierDirectoryD1/17000002.txt'
        if ospath.exists(myfile):
            with open(myfile, 'r', encoding="utf8") as text:
                line = text.readlines()
                for str_file in line:
                    sub_str = str_file.split('*')

                    source = 19 if sub_str[1] == '17000001' else 20
                    Date = dt.date(int(sub_str[3][4] + sub_str[3][5] + sub_str[3][6] + sub_str[3][7]),
                                   int(sub_str[3][2] + sub_str[3][3]), int(sub_str[3][0] + sub_str[3][1]))
                    sumoperation = float(sub_str[5])

                    if typeitem_id == 1:
                        increase = 2
                    elif typeitem_id == 2:
                        increase = 1
                    elif typeitem_id in (7, 8):
                        increase = 2 if sub_str[2] == '1' else 3
                    else:
                        increase = int(sub_str[2])

                    bufferList = {'iditemkey': item_id, 'idtypeitemkey': typeitem_id, 'dateoperationkey': Date,
                                  'descriptionkey': sub_str[4], 'sumoperationkey': sumoperation,
                                  'increasekey': increase, 'sourcekey': source, 'typeinvestmentidkey': None,
                                  'countnotekey': 0, 'priseunit': 0}
                    self.AddNewOperation(bufferList)


if __name__ == "__main__":
    root = tk.Tk()
    # Создаём экземпляр класса базы данных
    db = DB()
    # Создаём экземпляр класса отображения основных окон
    app = MainWindow(root)

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
