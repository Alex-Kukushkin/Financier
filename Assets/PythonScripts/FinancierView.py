import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter import messagebox as mb
import os.path as op
from enum import Enum


class TypesWindows(Enum):
    """ Список страниц в приложении """
    passwordWindow = 0
    menuWindow = 1
    settingWindow = 2
    listItemSettingWindow = 3
    correctItemWindow = 4
    itemCreateNewWindow = 11
    mainWindow = 5
    listItemForEnterDataWindow = 6
    listDataInItemWindow = 7
    dataCreateNewWindow = 8
    dataCorrectWindow = 9
    dataCreateNewWindowCopy = 10
    reportWindow = 12
    listDataInItemInReportWindow = 13
    selectImageWindow = 14


def open_image(path_image):
    """ Открытие картинок по пути к файлу """
    return tk.PhotoImage(file=path_image)


def get_string_from_number(number):
    """ Получить форматированную строку из числа """
    string = '{0:,.2f}'.format(number)
    string = string.replace(',', ' ')
    return string


class ViewWindows(tk.Frame):
    def __init__(self, root, financier_controls):
        """ Инициализация полей класса, картинок и иконок. Переход на страницу ввода пароля"""
        super().__init__(root)
        # Ссылка на экземпляр контролов
        self.fc = financier_controls

        # Словарь со списком путей ко всем картинкам и иконокам в проекте
        self.paths_to_images = {
            # Картинки основных окон
            'zamok_img': 'Assets/Images/General/zamok.gif', 'time_img': 'Assets/Images/General/Time.gif',
            'main_img': 'Assets/Images/General/Main_Paint.gif', 'coin_img': 'Assets/Images/General/bitcoins.gif',
            'shreder_img': 'Assets/Images/General/shreder.gif', 'report_img': 'Assets/Images/General/report.gif',

            # Иконки кнопок и значков
            'arrowDown_img': 'Assets/Images/Icons/arrowDown.gif', 'arrowUp_img': 'Assets/Images/Icons/arrowUp.gif',
            'arrowLeft_img': 'Assets/Images/Icons/arrowLeft.gif',
            'arrowRight_img': 'Assets/Images/Icons/arrowRight.gif',
            'arrowGreenLeft_img': 'Assets/Images/Icons/arrowGreenLeft.gif',
            'arrowRedLeft_img': 'Assets/Images/Icons/arrowRedLeft.gif',
            'arrowGreenRight_img': 'Assets/Images/Icons/arrowGreenRight.gif',
            'arrowRedRight_img': 'Assets/Images/Icons/arrowRedRight.gif',
            'arrowDoubleGreen_img': 'Assets/Images/Icons/arrowGreenDouble.gif',
            'arrowDoubleRed_img': 'Assets/Images/Icons/arrowRedDouble.gif',
            'menu_img': 'Assets/Images/Icons/menu_img.gif', 'setting_img': 'Assets/Images/Icons/if_Settings3.gif',
            'baks_img': 'Assets/Images/Icons/baks.gif', 'info_img': 'Assets/Images/Icons/info.gif',
            'exit_img': 'Assets/Images/Icons/CloseExit2.gif', 'up_img': 'Assets/Images/Icons/UP.gif',
            'down_img': 'Assets/Images/Icons/DOWN.gif', 'right_img': 'Assets/Images/Icons/Right.gif',
            'left_img': 'Assets/Images/Icons/arrowDown.gif', 'back_img': 'Assets/Images/Icons/back.gif',
            'forward_img': 'Assets/Images/Icons/Forward.gif', 'plus_img': 'Assets/Images/Icons/plus_icon.gif',
            'green_up_img': 'Assets/Images/Icons/green_up.gif', 'red_down_img': 'Assets/Images/Icons/red_down.gif',
            'payment_img': 'Assets/Images/Icons/payment.gif', 'delete_img': 'Assets/Images/Icons/delete_icon.gif',
            'correction_img': 'Assets/Images/Icons/Correction1.gif',
            'correction25_img': 'Assets/Images/Icons/Correction1_25.gif',
            'delete25_img': 'Assets/Images/Icons/delete_icon_25.gif',
            'forward25_img': 'Assets/Images/Icons/Forward25.gif',
            'copy_img': 'Assets/Images/Icons/copy.gif', 'report_button_img': 'Assets/Images/Icons/reportButton.gif',
            'deployed25_img': 'Assets/Images/Icons/Deployed25.gif', 'Wrap_img': 'Assets/Images/Icons/Wrap.gif',

            # Иконки кнопок и значков
            'air_img': 'Assets/Images/Item/air.gif', 'alcogol_img': 'Assets/Images/Item/alcogol.gif',
            'flat_img': 'Assets/Images/Item/appartament.gif', 'avto_img': 'Assets/Images/Item/avto.gif',
            'benzin_img': 'Assets/Images/Item/benzin.gif', 'card_img': 'Assets/Images/Item/card.gif',
            'dollar_img': 'Assets/Images/Item/dollar.gif', 'euro_img': 'Assets/Images/Item/evro.gif',
            'fitnes1_img': 'Assets/Images/Item/fitnes1.gif', 'fitnes2_img': 'Assets/Images/Item/fitnes2.gif',
            'fitnes3_img': 'Assets/Images/Item/fitnes3.gif', 'food1_img': 'Assets/Images/Item/food1.gif',
            'food2_img': 'Assets/Images/Item/food2.gif', 'gift_img': 'Assets/Images/Item/gift.gif',
            'giveloan_img': 'Assets/Images/Item/giveloan.gif', 'income_img': 'Assets/Images/Item/income.gif',
            'investments_img': 'Assets/Images/Item/investments.gif', 'ipoteka_img': 'Assets/Images/Item/ipoteka.gif',
            'kredit_img': 'Assets/Images/Item/kredit.gif', 'kredit2_img': 'Assets/Images/Item/kredit2.gif',
            'magazin_img': 'Assets/Images/Item/magazin.gif', 'mebel1_img': 'Assets/Images/Item/mebel1.gif',
            'mebel2_img': 'Assets/Images/Item/mebel2.gif', 'medicina1_img': 'Assets/Images/Item/medicina1.gif',
            'medicina2_img': 'Assets/Images/Item/medicina2.gif', 'money_img': 'Assets/Images/Item/money1.gif',
            'moneyPlus_img': 'Assets/Images/Item/MoneyPlus.gif', 'nalog_img': 'Assets/Images/Item/nalog.gif',
            'otdih_img': 'Assets/Images/Item/otdih.gif', 'paricm_img': 'Assets/Images/Item/paricm.gif',
            'percent_img': 'Assets/Images/Item/percent1.gif', 'pets_img': 'Assets/Images/Item/pets.gif',
            'property_img': 'Assets/Images/Item/property.gif', 'cost_img': 'Assets/Images/Item/cost.gif',
            'remont_img': 'Assets/Images/Item/remont.gif', 'rubl_img': 'Assets/Images/Item/rubl.gif',
            'takeloan_img': 'Assets/Images/Item/takeloan.gif', 'taxi_img': 'Assets/Images/Item/taxi.png',
            'tekhnica_img': 'Assets/Images/Item/tekhnica.gif', 'upgrade_img': 'Assets/Images/Item/upgrade.gif',
            'clothes_img': 'Assets/Images/Item/clothes.gif', 'kill_img': 'Assets/Images/Item/kill.gif',
            'work1_img': 'Assets/Images/Item/work1.gif', 'work2_img': 'Assets/Images/Item/work2.gif',
            'work3_img': 'Assets/Images/Item/work3.gif'
        }

        self.array_item_images = [
            self.paths_to_images.get('air_img'), self.paths_to_images.get('alcogol_img'),
            self.paths_to_images.get('flat_img'), self.paths_to_images.get('avto_img'),
            self.paths_to_images.get('benzin_img'), self.paths_to_images.get('card_img'),
            self.paths_to_images.get('dollar_img'), self.paths_to_images.get('euro_img'),
            self.paths_to_images.get('fitnes1_img'), self.paths_to_images.get('fitnes2_img'),
            self.paths_to_images.get('fitnes3_img'), self.paths_to_images.get('food1_img'),
            self.paths_to_images.get('food2_img'), self.paths_to_images.get('gift_img'),
            self.paths_to_images.get('giveloan_img'), self.paths_to_images.get('income_img'),
            self.paths_to_images.get('investments_img'), self.paths_to_images.get('ipoteka_img'),
            self.paths_to_images.get('kredit_img'), self.paths_to_images.get('kredit2_img'),
            self.paths_to_images.get('magazin_img'), self.paths_to_images.get('mebel1_img'),
            self.paths_to_images.get('mebel2_img'), self.paths_to_images.get('medicina1_img'),
            self.paths_to_images.get('medicina2_img'), self.paths_to_images.get('money_img'),
            self.paths_to_images.get('moneyPlus_img'), self.paths_to_images.get('nalog_img'),
            self.paths_to_images.get('otdih_img'), self.paths_to_images.get('paricm_img'),
            self.paths_to_images.get('percent_img'), self.paths_to_images.get('pets_img'),
            self.paths_to_images.get('property_img'), self.paths_to_images.get('cost_img'),
            self.paths_to_images.get('remont_img'), self.paths_to_images.get('rubl_img'),
            self.paths_to_images.get('takeloan_img'), self.paths_to_images.get('taxi_img'),
            self.paths_to_images.get('tekhnica_img'), self.paths_to_images.get('upgrade_img'),
            self.paths_to_images.get('clothes_img'), self.paths_to_images.get('kill_img'),
            self.paths_to_images.get('work1_img'), self.paths_to_images.get('work2_img'),
            self.paths_to_images.get('work3_img')
        ]

        # Словарь картинок, используемых на странице
        self.active_images = dict()

        # Картинка меню для кнопки в тулбаре
        self.menu_image = open_image(self.paths_to_images.get('menu_img'))

        # Инициилизация основных окон программы
        # Верхний туулбар
        self.toolbarMenu = tk.Frame(bg='#131313', bd=2)
        # self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)

        # Кнопка меню
        buttonMenu = tk.Button(self.toolbarMenu, text="Меню", background="#222", foreground="#ccc",
                               highlightcolor="#C0C0C0", padx="10", pady="2", font="16", compound=tk.RIGHT,
                               image=self.menu_image, command=self.menu_window)
        buttonMenu.pack(side=tk.LEFT)

        # Фрейм для основных страниц
        self.frameMain = tk.Frame(bg='black')
        self.frameMain.place(x=0, y=0, height=720, width=1280)

        # Вызов окна входа в систему
        self.password_window()

    # ****************************** МЕТОДЫ ДЛЯ РАБОТЫ С ИЗОБРАЖЕНИЯМИ *******************************************
    def update_dict_active_images(self, id_section=1):
        """ Метод подгрузки картинок для конкретной страницы страницы """
        self.active_images.clear()
        if self.fc.current_window == TypesWindows.passwordWindow:
            self.active_images['zamok_img'] = open_image(self.paths_to_images.get('zamok_img'))
            self.active_images['forward_img'] = open_image(self.paths_to_images.get('forward_img'))
        elif self.fc.current_window == TypesWindows.mainWindow:
            self.active_images['main_img'] = open_image(self.paths_to_images.get('main_img'))
            self.active_images['report_button_img'] = open_image(self.paths_to_images.get('report_button_img'))
            self.active_images['menu_img'] = open_image(self.paths_to_images.get('menu_img'))
        elif self.fc.current_window == TypesWindows.listItemForEnterDataWindow:
            self.active_images['back_img'] = open_image(self.paths_to_images.get('back_img'))
            self.active_images['menu_img'] = open_image(self.paths_to_images.get('menu_img'))
            self.active_images['plus_img'] = open_image(self.paths_to_images.get('plus_img'))
            self.active_images['section_image'] = open_image(self.get_path_image_section(id_section))
        elif self.fc.current_window == TypesWindows.dataCreateNewWindow or \
                self.fc.current_window == TypesWindows.dataCreateNewWindowCopy or\
                self.fc.current_window == TypesWindows.dataCorrectWindow:
            self.active_images['back_img'] = open_image(self.paths_to_images.get('back_img'))
            self.active_images['item_image'] = open_image(self.get_path_image_item(id_section))
            self.active_images['arrowLeft_img'] = open_image(self.paths_to_images.get('arrowLeft_img'))
            self.active_images['payment_img'] = open_image(self.paths_to_images.get('payment_img'))
            self.active_images['arrowRight_img'] = open_image(self.paths_to_images.get('arrowRight_img'))
            self.active_images['arrowGreenLeft_img'] = open_image(self.paths_to_images.get('arrowGreenLeft_img'))
            self.active_images['arrowRedLeft_img'] = open_image(self.paths_to_images.get('arrowRedLeft_img'))
            self.active_images['arrowGreenRight_img'] = open_image(self.paths_to_images.get('arrowGreenRight_img'))
            self.active_images['arrowRedRight_img'] = open_image(self.paths_to_images.get('arrowRedRight_img'))
            self.active_images['arrowDoubleGreen_img'] = open_image(self.paths_to_images.get('arrowDoubleGreen_img'))
            self.active_images['arrowDoubleRed_img'] = open_image(self.paths_to_images.get('arrowDoubleRed_img'))
            self.active_images['forward_img'] = open_image(self.paths_to_images.get('forward_img'))
            self.active_images['exit_img'] = open_image(self.paths_to_images.get('exit_img'))
            self.active_images['shreder_img'] = open_image(self.paths_to_images.get('shreder_img'))
        elif self.fc.current_window == TypesWindows.listDataInItemWindow or \
                self.fc.current_window == TypesWindows.listDataInItemInReportWindow:
            self.active_images['back_img'] = open_image(self.paths_to_images.get('back_img'))
            self.active_images['item_image'] = open_image(self.array_item_images[id_section])
            self.active_images['arrowLeft_img'] = open_image(self.paths_to_images.get('arrowLeft_img'))
            self.active_images['arrowRight_img'] = open_image(self.paths_to_images.get('arrowRight_img'))
            self.active_images['arrowUp_img'] = open_image(self.paths_to_images.get('arrowUp_img'))
            self.active_images['arrowDown_img'] = open_image(self.paths_to_images.get('arrowDown_img'))
            self.active_images['forward25_img'] = open_image(self.paths_to_images.get('forward25_img'))
            self.active_images['delete25_img'] = open_image(self.paths_to_images.get('delete25_img'))
            self.active_images['correction25_img'] = open_image(self.paths_to_images.get('correction25_img'))
            self.active_images['copy_img'] = open_image(self.paths_to_images.get('copy_img'))
            self.active_images['shreder_img'] = open_image(self.paths_to_images.get('shreder_img'))
            self.active_images['report_img'] = open_image(self.paths_to_images.get('report_img'))
        elif self.fc.current_window == TypesWindows.reportWindow:
            self.active_images['back_img'] = open_image(self.paths_to_images.get('back_img'))
            self.active_images['report_img'] = open_image(self.paths_to_images.get('report_img'))
            self.active_images['forward25_img'] = open_image(self.paths_to_images.get('forward25_img'))
            self.active_images['deployed25_img'] = open_image(self.paths_to_images.get('deployed25_img'))
            self.active_images['arrowLeft_img'] = open_image(self.paths_to_images.get('arrowLeft_img'))
            self.active_images['arrowRight_img'] = open_image(self.paths_to_images.get('arrowRight_img'))
            self.active_images['arrowUp_img'] = open_image(self.paths_to_images.get('arrowUp_img'))
            self.active_images['arrowDown_img'] = open_image(self.paths_to_images.get('arrowDown_img'))
            self.active_images['forward_img'] = open_image(self.paths_to_images.get('forward_img'))
            self.active_images['Wrap_img'] = open_image(self.paths_to_images.get('Wrap_img'))
        elif self.fc.current_window == TypesWindows.menuWindow:
            self.active_images['baks_img'] = open_image(self.paths_to_images.get('baks_img'))
            self.active_images['setting_img'] = open_image(self.paths_to_images.get('setting_img'))
            self.active_images['info_img'] = open_image(self.paths_to_images.get('info_img'))
            self.active_images['exit_img'] = open_image(self.paths_to_images.get('exit_img'))
            self.active_images['coin_img'] = open_image(self.paths_to_images.get('coin_img'))
        elif self.fc.current_window == TypesWindows.settingWindow:
            self.active_images['back_img'] = open_image(self.paths_to_images.get('back_img'))
            self.active_images['info_img'] = open_image(self.paths_to_images.get('info_img'))
            self.active_images['time_img'] = open_image(self.paths_to_images.get('time_img'))
            self.active_images['right_img'] = open_image(self.paths_to_images.get('right_img'))
            self.active_images['menu_img'] = open_image(self.paths_to_images.get('menu_img'))
        elif self.fc.current_window == TypesWindows.listItemSettingWindow:
            self.active_images['back_img'] = open_image(self.paths_to_images.get('back_img'))
            self.active_images['plus_img'] = open_image(self.paths_to_images.get('plus_img'))
            self.active_images['arrowLeft_img'] = open_image(self.paths_to_images.get('arrowLeft_img'))
            self.active_images['arrowRight_img'] = open_image(self.paths_to_images.get('arrowRight_img'))
            self.active_images['section_image'] = open_image(self.get_path_image_section(id_section))
        elif self.fc.current_window == TypesWindows.itemCreateNewWindow or\
                self.fc.current_window == TypesWindows.correctItemWindow:
            if self.fc.current_window == TypesWindows.itemCreateNewWindow:
                self.active_images['section_image'] = open_image(self.array_item_images[id_section])
            elif self.fc.current_window == TypesWindows.correctItemWindow:
                self.active_images['section_image'] = open_image(self.array_item_images[id_section])
            self.active_images['back_img'] = open_image(self.paths_to_images.get('back_img'))
            self.active_images['info_img'] = open_image(self.paths_to_images.get('info_img'))
            self.active_images['time_img'] = open_image(self.paths_to_images.get('time_img'))
            self.active_images['forward_img'] = open_image(self.paths_to_images.get('forward_img'))
            self.active_images['exit_img'] = open_image(self.paths_to_images.get('exit_img'))
            self.active_images['shreder_img'] = open_image(self.paths_to_images.get('shreder_img'))
        elif self.fc.current_window == TypesWindows.selectImageWindow:
            self.active_images['back_img'] = open_image(self.paths_to_images.get('back_img'))
            self.active_images['arrowLeft_img'] = open_image(self.paths_to_images.get('arrowLeft_img'))
            self.active_images['arrowRight_img'] = open_image(self.paths_to_images.get('arrowRight_img'))
            image_setting_list = list()
            for image in self.array_item_images:
                image_setting_list.append(open_image(image))
            self.active_images['image_setting_list'] = image_setting_list

    def get_path_image_section(self, TYPEITEM):
        """ Извлекает картинку для визуальной идентификации раздела в зависимости от типа раздела"""
        img = self.paths_to_images.get('income_img')
        if TYPEITEM == 1:
            img = self.paths_to_images.get('income_img')
        elif TYPEITEM == 2:
            img = self.paths_to_images.get('cost_img')
        elif TYPEITEM == 3:
            img = self.paths_to_images.get('money_img')
        elif TYPEITEM == 4:
            img = self.paths_to_images.get('property_img')
        elif TYPEITEM == 5:
            img = self.paths_to_images.get('investments_img')
        elif TYPEITEM == 6:
            img = self.paths_to_images.get('giveloan_img')
        elif TYPEITEM == 7:
            img = self.paths_to_images.get('kredit2_img')
        elif TYPEITEM == 8:
            img = self.paths_to_images.get('takeloan_img')

        return img

    @staticmethod
    def get_number_image_section(TYPEITEM):
        """ Извлекает номер картинки для визуальной идентификации раздела в зависимости от типа раздела"""
        img_number = 15
        if TYPEITEM == 1:
            img_number = 15
        elif TYPEITEM == 2:
            img_number = 33
        elif TYPEITEM == 3:
            img_number = 25
        elif TYPEITEM == 4:
            img_number = 32
        elif TYPEITEM == 5:
            img_number = 16
        elif TYPEITEM == 6:
            img_number = 14
        elif TYPEITEM == 7:
            img_number = 19
        elif TYPEITEM == 8:
            img_number = 36

        return img_number

    def get_path_image_item(self, number_paint):
        """ Извлекает картинку для визуальной идентификации статьи в зависимости от типа статьи"""
        return self.array_item_images[number_paint]

    # ****************************** ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ *******************************************
    def clear_main_frame(self):
        """ Функция очистки  фреймов окна программы """
        for obj in self.frameMain.place_slaves():
            obj.destroy()
        for obj in self.toolbarMenu.place_slaves():
            if obj.winfo_name() == 'button_Back':
                obj.destroy()

    def define_text_and_color(self, idtypeitem):
        """ Извлекает наименование раздела для заголовков и цвет для кнопок статей раздела """
        # Запрос на наименование раздела и цвет кнопок
        datatype = self.fc.fm.request_select_DB('*', 'typeitems', 'id={}'.format(str(idtypeitem)))
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

    # ***************************** СТРАНИЦА ВВОДА ПАРОЛЯ ***************************************
    def password_window(self):
        """ Окно ввода пароля и вход в систему """
        self.update_dict_active_images()
        # Картинка сейфового замка
        zamok_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('zamok_img'))
        zamok_paint.place(x=0, y=0)

        # Поле ввода пароля
        entry_password = ttk.Entry(self.frameMain, width=20, show="*", font="Arial 25")
        entry_password.place(x=467, y=300, width=300)
        # Кнопка входа
        button_entrance = tk.Button(self.frameMain, image=self.active_images.get('forward_img'), bg='#2f4f4f')
        button_entrance.place(x=769, y=300, height=45, width=45)
        button_entrance.bind('<Button-1>', lambda event: self.fc.entrance_action(entry_password.get()))

    # ****************************** ГЛАВНАЯ СТРАНИЦА *******************************************
    def main_window(self):
        """ Основное окно программы, содержащее информацию о текущих финансовых показателях в разрезе разделов.
         Служит для перехода на страницы разделов для создания, просмотра и редактирования записей и для
         перехода на страницу просмотра детального отчета """
        self.fc.current_window = TypesWindows.mainWindow
        self.update_dict_active_images()
        self.clear_main_frame()

        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)

        # Картинка главной
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('main_img'))
        Main_paint.place(x=820, y=45)

        # Запрос к БД на данные по разделам
        data = self.fc.fm.request_select_DB('*', 'typeitems')

        # Блок ввода данных по статьям доходов и расходов
        l2 = tk.Label(self.frameMain, text="ДОХОДЫ И РАСХОДЫ:", bg="black", foreground="#ccc",
                      font="Arial 25")
        l2.place(x=50, y=50)

        button_IncomeSetting = tk.Button(self.frameMain, text=data[0][2], bg='#F08080', font="Arial 16",
                                         foreground="#F5F5F5")
        button_IncomeSetting.place(x=50, y=100, width=200, height=40)
        button_IncomeSetting.bind('<Button-1>', lambda event: self.draw_list_item_for_enter_data_window(1))
        s11 = tk.Label(self.frameMain, text=get_string_from_number(data[0][5]), bg="#A9A9A9", foreground="#F5F5F5",
                       font="Arial 12")
        s11.place(x=255, y=100, width=150, height=40)

        button_CostsSetting = tk.Button(self.frameMain, text=data[1][2], bg='#BA55D3', font="Arial 16",
                                        foreground="#F5F5F5")
        button_CostsSetting.place(x=450, y=100, width=200, height=40)
        button_CostsSetting.bind('<Button-1>', lambda event: self.draw_list_item_for_enter_data_window(2))
        s22 = tk.Label(self.frameMain, text=get_string_from_number(data[1][5]), bg="#A9A9A9", foreground="#F5F5F5",
                       font="Arial 12")
        s22.place(x=655, y=100, width=150, height=40)

        # Блок  статей актива
        l3 = tk.Label(self.frameMain, text="АКТИВ:", bg="black", foreground="#C71585", font="Arial 25")
        l3.place(x=50, y=150)

        button_MoneySetting = tk.Button(self.frameMain, text=data[2][2], bg='#DB7093', font="Arial 14",
                                        foreground="#F5F5F5")
        button_MoneySetting.place(x=50, y=200, width=200, height=40)
        button_MoneySetting.bind('<Button-1>', lambda event: self.draw_list_item_for_enter_data_window(3))
        s1 = tk.Label(self.frameMain, text=get_string_from_number(data[2][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s1.place(x=255, y=200, width=150, height=40)

        button_PropertySetting = tk.Button(self.frameMain, text=data[3][2], bg='#DB7093', font="Arial 14",
                                           foreground="#F5F5F5")
        button_PropertySetting.place(x=50, y=250, width=200, height=40)
        button_PropertySetting.bind('<Button-1>', lambda event: self.draw_list_item_for_enter_data_window(4))
        s2 = tk.Label(self.frameMain, text=get_string_from_number(data[3][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s2.place(x=255, y=250, width=150, height=40)

        button_InvestmentsSetting = tk.Button(self.frameMain, text=data[4][2], bg='#DB7093', font="Arial 14",
                                              foreground="#F5F5F5")
        button_InvestmentsSetting.place(x=50, y=300, width=200, height=40)
        button_InvestmentsSetting.bind('<Button-1>', lambda event: self.draw_list_item_for_enter_data_window(5))
        s3 = tk.Label(self.frameMain, text=get_string_from_number(data[4][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s3.place(x=255, y=300, width=150, height=40)

        button_LoansIssuedSetting = tk.Button(self.frameMain, text=data[5][2], bg='#DB7093', font="Arial 14",
                                              foreground="#F5F5F5")
        button_LoansIssuedSetting.place(x=50, y=350, width=200, height=40)
        button_LoansIssuedSetting.bind('<Button-1>', lambda event: self.draw_list_item_for_enter_data_window(6))
        s4 = tk.Label(self.frameMain, text=get_string_from_number(data[5][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s4.place(x=255, y=350, width=150, height=40)

        # Блок  статей пассива
        l4 = tk.Label(self.frameMain, text="ПАССИВ:", bg="black", foreground="#800080",
                      font="Arial 25")
        l4.place(x=450, y=150)

        button_CreditSetting = tk.Button(self.frameMain, text=data[6][2], bg='#DA70D6', font="Arial 14",
                                         foreground="#F5F5F5")
        button_CreditSetting.place(x=450, y=200, width=200, height=40)
        button_CreditSetting.bind('<Button-1>', lambda event: self.draw_list_item_for_enter_data_window(7))
        s5 = tk.Label(self.frameMain, text=get_string_from_number(data[6][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s5.place(x=655, y=200, width=150, height=40)

        button_LoansSetting = tk.Button(self.frameMain, text=data[7][2], bg='#DA70D6', font="Arial 14",
                                        foreground="#F5F5F5")
        button_LoansSetting.place(x=450, y=250, width=200, height=40)
        button_LoansSetting.bind('<Button-1>', lambda event: self.draw_list_item_for_enter_data_window(8))
        s6 = tk.Label(self.frameMain, text=get_string_from_number(data[7][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s6.place(x=655, y=250, width=150, height=40)

        l5 = tk.Label(self.frameMain, text=data[8][2], bg='#DA70D6', foreground="#F5F5F5",
                      font="Arial 14")
        l5.place(x=450, y=350, width=200, height=40)
        s7 = tk.Label(self.frameMain, text=get_string_from_number(data[8][5]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s7.place(x=655, y=350, width=150, height=40)

        # Кнопка открытия отчета
        buttonReport = tk.Button(self.frameMain, text='ПОСМОТРЕТЬ ОТЧЕТ ', background="#222", foreground="#ccc",
                                 highlightcolor="#C0C0C0", padx="10", command=self.report_window, pady="1", font="16",
                                 compound=tk.RIGHT, image=self.active_images.get('report_button_img'))
        buttonReport.place(x=50, y=550)

    # ****************************** СТРАНИЦА СО СПИСКОМ СТАТЕЙ В РАЗДЕЛЕ ДЛЯ ВВОДА И ПРОСМОТРА ДАННЫХ ****************
    def draw_list_item_for_enter_data_window(self, idtypeitem):
        """ Окно отображение списка статей раздела для создания, просмотра и редактирования записей """
        self.fc.current_window = TypesWindows.listItemForEnterDataWindow
        self.update_dict_active_images(idtypeitem)
        self.clear_main_frame()
        self.fc.section = idtypeitem

        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.define_text_and_color(idtypeitem)

        # Наименование раздела
        l1 = tk.Label(self.frameMain, text=nameandcolor[0] + ":", bg="black", foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=0)

        # Кнопка назад
        button_back = tk.Button(self.toolbarMenu, image=self.active_images.get('back_img'), bg='black',
                                name='button_Back')
        button_back.place(x=130, y=0)
        button_back.bind('<Button-1>', lambda event: self.fc.do_back_ward(0))

        # Запрос к БД на перечень рабочих статей в разделе
        data = self.fc.fm.request_select_DB('*', 'items', 'typeitem_id={} AND workingitem==1'.format(str(idtypeitem)))

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
                self.create_button_and_view_notes(X, Y, data[i - 1], nameandcolor[1])

        else:
            # Надпись о том, что статьи в разделе отсутствуют
            l2 = tk.Label(self.frameMain, text="В разделе отсутствуют статьи для ввода данных."
                                               "\nСоздайте их и окне настроек.",
                          bg="black", foreground="#ccc", justify='left', font="Arial 16")
            l2.place(x=50, y=50)

        # Картинка раздела
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('section_image'))
        Main_paint.place(x=820, y=45)

    def create_button_and_view_notes(self, X, Y, DATAITEM, COLOR):
        """ Отображение кнопок создания и просмотра записей по статье для метода ListItemForEnterDataWindow """
        # Кнопка добавления новых данных
        button_Plus = tk.Button(self.frameMain, image=self.active_images.get('plus_img'), bg='black', font="Arial 12",
                                foreground="#F5F5F5")
        button_Plus.place(x=(X - 40), y=Y, width=40, height=40)
        button_Plus.bind('<Button-1>', lambda eventbutton: self.create_correct_data_window('NEW', DATAITEM))

        # Кнопка просмотра записей в статье
        button_Item = tk.Button(self.frameMain, text=DATAITEM[2],
                                bg=COLOR, font="Arial 12", foreground="#F5F5F5")
        button_Item.place(x=X, y=Y, width=200, height=40)
        button_Item.bind('<Button-1>', lambda eventbutton: self.draw_list_operations_in_item_window(DATAITEM))

        tex = get_string_from_number(DATAITEM[7])
        sumItem = tk.Label(self.frameMain, text=tex, bg="#A9A9A9", foreground="#F5F5F5", font="Arial 12")
        sumItem.place(x=X + 205, y=Y, width=145, height=40)

    def create_correct_data_window(self, TYPEOPERATIONS, DATA, NOTE=0):
        """Окно создания новой записи данных
        Если id записи (NOTE) == 0, открывается диалог записи с пустыми полями,
        если id записи (NOTE) != 0, то копируем поля из записи по id
        # TYPEOPERATIONS: 'NEW', 'COPY', 'CORRECTION'     """

        if TYPEOPERATIONS == 'NEW':
            self.fc.current_window = TypesWindows.dataCreateNewWindow
        elif TYPEOPERATIONS == 'COPY':
            self.fc.current_window = TypesWindows.dataCreateNewWindowCopy
        elif TYPEOPERATIONS == 'CORRECTION':
            self.fc.current_window = TypesWindows.dataCorrectWindow

        # Подгрузка картинок для страницы
        self.update_dict_active_images(DATA[8])

        # Отключаем отображаемые фреймы
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.clear_main_frame()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black',
                                name='button_Back')
        button_back.place(x=0, y=0)
        back_params = DATA[1] if TYPEOPERATIONS == 'NEW' else DATA
        button_back.bind('<Button-1>', lambda eventbutton: self.fc.do_back_ward(back_params))

        # Картинка статьи
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('item_image'))
        Main_paint.place(x=820, y=45)

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.define_text_and_color(DATA[1])

        # Наименование раздела
        l1 = tk.Label(self.frameMain, text=nameandcolor[0] + "/Ввод данных:", bg="black", foreground="#ccc",
                      font="Arial 25")
        l1.place(x=50, y=50)

        # Отображение полей для ввода и изменения данных
        self.show_operation_input_fields(TYPEOPERATIONS, DATA, NOTE)

        if TYPEOPERATIONS in ('NEW', 'COPY'):
            # Кнопка сохранения новой  статьи
            button_SaveNote = tk.Button(self.frameMain, text='Сохранить', name='button_Save',
                                        font="Arial 14", bg="#708090", foreground="#F5F5F5")
            button_SaveNote.place(x=50, y=600, width=200, height=40)
            button_SaveNote.bind('<Button-1>', lambda eventbutton: self.fc.save_new_operation(DATA))
        elif TYPEOPERATIONS == 'CORRECTION':
            # Кнопка сохранения изменений
            button_SaveNote = tk.Button(self.frameMain, text='Сохранить изменения', name='button_Save',
                                        font="Arial 14", bg="#708090", foreground="#F5F5F5")
            button_SaveNote.place(x=50, y=600, width=200, height=40)
            button_SaveNote.bind('<Button-1>', lambda eventbutton: self.fc.save_changes_operation(DATA, NOTE))

    # ****************************** СТРАНИЦЫ ДЛЯ СОЗДАНИЯ И КОРРЕКТИРОВКИ ДАННЫХ ****************
    def show_operation_input_fields(self, TYPEOPERATIONS, DATAITEM, NOTE=()):
        """ Отображение полей для ввода и изменения данных
        # TYPEOPERATIONS: 'NEW', 'COPY', 'CORRECTION'

        # [0"iditemkey"] - id статьи; [1"idtypeitemkey"] - id статьи; [2'dateoperationkey'] - дата операции;
        # [3'descriptionkey'] - Описание операции; # [4'sumoperationkey'] - сумма операции;
        # [5'increasekey'] - Направление (Уменьшение/Увеличение);
        # [6'sourcekey'] - Источник пополнения/ Изъятия(id статьи);
        # [7'typeinvestmentidkey'] - тип вложений (id типа вложений);
        # [8'countnotekey'] - количество вложений; [9'priseunit'] - цена единицы вложений """

        # Установка заначений в буферном словаре
        areaIW = self.fc.prepare_data_for_rendering_operation(TYPEOPERATIONS, DATAITEM, NOTE)

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.define_text_and_color(self.fc.bufferList['idtypeitemkey'])

        # Наименование статьи операции
        l2 = tk.Label(self.frameMain, name='label_signature_item', text=areaIW['textitem'], bg="black",
                      foreground="#ccc", font="Arial 16")
        l2.place(x=50, y=100)

        labelItemOperation = tk.Label(self.frameMain, text=DATAITEM[2], name='label_ItemOperation',
                                      background=nameandcolor[1], foreground="#ccc", font="14", justify='center')
        labelItemOperation.place(x=50, y=130, width=300, height=45)

        # Кнопка переключения уменьшения/увеличения
        if self.fc.bufferList['sourcekey'] != 0:
            if self.fc.bufferList['idtypeitemkey'] == 1 or self.fc.bufferList['idtypeitemkey'] == 2:
                paintIncrease = tk.Label(self.frameMain, name='label_Increase', bg='black',
                                         image=self.active_images.get(areaIW['icon']))
                paintIncrease.place(x=379, y=130)
            else:
                buttonIncrease = tk.Button(self.frameMain, background='black', foreground="#ccc",
                                           highlightcolor="#C0C0C0", justify='center',
                                           image=self.active_images.get(areaIW['icon']),
                                           name='button_Increase', command=self.fc.switch_increase_decrease_mode)
                buttonIncrease.place(x=379, y=130)

        # Запрос к БД на наименование кошелька
        colorwallet = 'red'
        if self.fc.bufferList['sourcekey'] == 0:
            namewallet = 'Кошельков нет'
        else:
            data2 = self.fc.fm.request_select_DB('*', 'items', 'id={}'.format(str(self.fc.bufferList['sourcekey'])))
            namewallet = data2[0][2]
            colorwallet = self.define_text_and_color(data2[0][1])[1]

        # Наименование кошелька
        l3 = tk.Label(self.frameMain, name='label_signature_wallet', text=areaIW['textwallet'], bg="black",
                      foreground="#ccc", font="Arial 16")
        l3.place(x=450, y=100)

        labelPayment = tk.Label(self.frameMain, text=namewallet, name='label_Payment', background=colorwallet,
                                foreground="#ccc", font="14", justify='center')
        labelPayment.place(x=450, y=130, width=300, height=45)

        # Кнопки выбора кошелька
        buttonLeft = tk.Button(self.frameMain, background="black", image=self.active_images.get('arrowLeft_img'))
        buttonLeft.place(x=525, y=170, width=45, height=45)
        buttonLeft.bind('<Button-1>', lambda eventbutton: self.fc.switch_wallet(0, DATAITEM))

        buttonPayment = tk.Button(self.frameMain, background="black", image=self.active_images.get('payment_img'))
        buttonPayment.place(x=575, y=170, width=45, height=45)
        buttonPayment.bind('<Button-1>', lambda eventbutton: self.draw_list_item_for_to_select_wallet(
            TYPEOPERATIONS, DATAITEM, NOTE))

        buttonRight = tk.Button(self.frameMain, background="black", image=self.active_images.get('arrowRight_img'))
        buttonRight.place(x=625, y=170, width=45, height=45)
        buttonRight.bind('<Button-1>', lambda eventbutton: self.fc.switch_wallet(1, DATAITEM))

        # Поле ввода даты
        l4 = tk.Label(self.frameMain, text="Дата операции:", bg="black", foreground="#ccc", font="Arial 16")
        l4.place(x=50, y=220)

        date = self.fc.bufferList['dateoperationkey']
        if type(self.fc.bufferList['dateoperationkey']) == str:
            date = dt.datetime.strptime(self.fc.bufferList['dateoperationkey'], '%Y-%m-%d').date()
        tex2 = dt.date.strftime(date, '%d.%m.%Y')
        button_Date = tk.Button(self.frameMain, name='button_Date', text=tex2,
                                bg='#708090', font="Arial 25", foreground="#F5F5F5")
        button_Date.place(x=50, y=250, width=300, height=40)
        Data2 = (1, 50, 250, 300, 40, tex2, 'button_Date', 'Arial 25', '#708090', '#F5F5F5', tex2, 0)
        button_Date.bind('<Button-1>', lambda eventbutton: self.open_field_for_change_data(Data2))

        # Кнопка ввода суммы
        l5 = tk.Label(self.frameMain, text="Сумма операции:", bg="black", foreground="#ccc", font="Arial 16")
        l5.place(x=450, y=220)
        tex3 = get_string_from_number(self.fc.bufferList['sumoperationkey'])
        tex3_2 = self.fc.bufferList['sumoperationkey']
        button_SumItem = tk.Button(self.frameMain, text=tex3, name='button_Sum',
                                   font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_SumItem.place(x=450, y=250, width=300, height=40)
        Data3 = (2, 450, 250, 300, 40, tex3, 'button_Sum', 'Arial 14', '#A9A9A9', '#F5F5F5', tex3_2, 0)
        button_SumItem.bind('<Button-1>', lambda eventbutton: self.open_field_for_change_data(Data3))

        # Поле ввода описания статьи
        l6 = tk.Label(self.frameMain, text="Описание операции:", bg="black", foreground="#ccc", font="Arial 16")
        l6.place(x=50, y=320)
        button_DescriptionItem = tk.Button(self.frameMain, text=self.fc.bufferList['descriptionkey'],
                                           name='button_Description', wraplength=680, font="Arial 14",
                                           bg="#A9A9A9", foreground="#F5F5F5")
        button_DescriptionItem.place(x=50, y=350, width=700, height=50)
        Data4 = (3, 50, 350, 700, 50, self.fc.bufferList['descriptionkey'], 'button_Description', 'Arial 14',
                 '#A9A9A9', '#F5F5F5', self.fc.bufferList['descriptionkey'], 0)
        button_DescriptionItem.bind('<Button-1>', lambda eventbutton: self.open_field_for_change_data(Data4))

    def open_field_for_change_data(self, DATA):
        """ Открываем поле ввода для внесения изменений
        Заменяем кнопку на поле ввода со кнопками отмены и подтверждения

        # DATA - кортеж 0 - номер (тип) поля ввода, 1 - х, 2 - у, 3 - width, 4 - height,
        # 5 - text, 6 - name, 7 - font, 8 - bg, 9 - foreground, 10 - значение для корректировки,
        # 11 - новая(0)/текущая == id статьи """

        # Прерываем функцию, если поле ввода уже есть на фрейме
        listobject = self.frameMain.place_slaves()
        for obj in listobject:
            if obj.winfo_name() == 'entry_DATA':
                return

        # Заменяем кнопку на поле ввода со кнопками отмены и подтверждения
        for obj in listobject:
            if obj.winfo_name() == DATA[6]:
                obj.destroy()

        # Поле ввода данных
        entry_Data = ttk.Entry(self.frameMain, name='entry_DATA', width=20, font="Arial 25")
        entry_Data.insert(0, DATA[10])
        entry_Data.place(x=DATA[1], y=DATA[2], width=DATA[3])

        # Кнопка утверждения изменений
        xx = DATA[1] + DATA[3] + 2
        button_DataOK = tk.Button(self.frameMain, image=self.active_images.get('forward_img'), bg='#2f4f4f',
                                  name='button_DataOK')
        button_DataOK.place(x=xx, y=DATA[2], height=45, width=45)
        button_DataOK.bind('<Button-1>', lambda event: self.fc.enter_data_in_input_field(DATA, entry_Data.get()))

        # Кнопка отмены изменений
        xxx = DATA[1] + DATA[3] + 49
        button_DataNO = tk.Button(self.frameMain, image=self.active_images.get('exit_img'), bg='#2f4f4f',
                                  name='button_DataNO')
        button_DataNO.place(x=xxx, y=DATA[2], height=45, width=45)
        button_DataNO.bind('<Button-1>', lambda event: self.cancel_change_data(DATA))

    def cancel_change_data(self, DATA):
        """ Закрывем поле ввода от внесения изменений
            Заменяем поле ввода со кнопками отмены и подтверждения на кнопку """
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
        button_DataItem.bind('<Button-1>', lambda event: self.open_field_for_change_data(DATA))

    def create_button_after_entering_data(self, new_data, DATA):
        """ Создание кнопки вместо поля ввода после ввода данных """
        button_DataItem = tk.Button(self.frameMain, text=new_data, name=DATA[6], wraplength=680, font=DATA[7],
                                    bg=DATA[8], foreground=DATA[9])

        button_DataItem.place(x=DATA[1], y=DATA[2], width=DATA[3], height=DATA[4])
        button_DataItem.bind('<Button-1>', lambda event: self.open_field_for_change_data(DATA))

    def draw_list_item_for_to_select_wallet(self, TYPEOPERATIONS, DATAITEM, NOTE=()):
        """ Отрисовка страницы со списком кошельков для выбора """
        self.clear_main_frame()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black',
                                name='button_Back')
        button_back.place(x=0, y=0)
        if TYPEOPERATIONS == 'NEW':
            button_back.bind('<Button-1>', lambda event: self.create_correct_data_window(TYPEOPERATIONS, DATAITEM))
        elif TYPEOPERATIONS == 'COPY' or 'CORRECTION':
            button_back.bind('<Button-1>', lambda event: self.create_correct_data_window(TYPEOPERATIONS, DATAITEM,
                                                                                         NOTE))

        # Запрашиваем список статей, которые можно выбрать
        wallets = self.fc.fm.request_select_DB('*', 'items', 'typeitem_id!=1 AND typeitem_id!=2 AND id!={}'
                                               ' AND workingitem=1'.format(DATAITEM[0]))

        # Картинка статьи
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('item_image'))
        Main_paint.place(x=820, y=45)

        # Запрос на наименование раздела и цвет кнопок
        nameandcolor = self.define_text_and_color(DATAITEM[1])

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
                self.draw_button_change_source(TYPEOPERATIONS, DATA, DATAITEM, NOTE, X, Y)
                i += 1

        elif len(wallets) > 20:
            # Определяем количество страниц и список для отрисовки
            count = len(wallets) // 20
            if len(wallets) % 20 != 0:
                count += 1

            if self.fc.setting_filter['currentPage'] > count:
                self.fc.setting_filter['currentPage'] = 1
            self.fc.setting_filter['countPage'] = count

            # Отбираем записи в зависимости от текущей страницы
            sortedPageList = list()
            countnotes = len(wallets)

            if self.fc.setting_filter['currentPage'] == 1:
                iBegin = 0
            else:
                iBegin = self.fc.setting_filter['currentPage'] * 20 - 20
            iEnd = self.fc.setting_filter['currentPage'] * 20
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
                self.draw_button_change_source(TYPEOPERATIONS, DATA, DATAITEM, NOTE, X, Y)
                i += 1

            # Блок постраничного пейджинга
            pagetext = '{} из {}'.format(self.fc.setting_filter['currentPage'], self.fc.setting_filter['countPage'])
            # Кнопка перелистывания страниц влево
            buttonPageLeft = tk.Button(self.frameMain, name='page_Left', background="black",
                                       image=self.active_images.get('arrowLeft_img'))
            buttonPageLeft.place(x=255, y=650, width=40, height=40)
            buttonPageLeft.bind('<Button-1>', lambda eventbutton: self.fc.change_page_source_item(
                'PageForward', TYPEOPERATIONS, DATAITEM, NOTE))

            # Счетчик страниц
            lPageCounter = tk.Label(self.frameMain, name='page_Counter', text=pagetext, bg="#808080", foreground="#ccc",
                                    font="Arial 12")
            lPageCounter.place(x=300, y=650, width=100, height=40)

            # Кнопка перелистывания страниц вправо
            buttonPageRight = tk.Button(self.frameMain, name='page_Right', background="black",
                                        image=self.active_images.get('arrowRight_img'))
            buttonPageRight.place(x=405, y=650, width=40, height=40)
            buttonPageRight.bind('<Button-1>', lambda eventbutton: self.fc.change_page_source_item(
                'PageBack', TYPEOPERATIONS, DATAITEM, NOTE))

        elif len(wallets) == 0:
            # Надпись о том, что статьи в разделе отсутствуют
            l2 = tk.Label(self.frameMain, text="Отсутствуют доступные статьи для ввода выбора статьи."
                                               "\nСоздайте их и окне настроек.",
                          bg="black", foreground="#ccc", justify='left', font="Arial 16")
            l2.place(x=50, y=100)

    def draw_button_change_source(self, TYPEOPERATIONS, DATA, DATAITEM, NOTE, X, Y):
        """ Отображение кнопки выбора статьи при отрисовке списка доступных кошельков """
        COLOR = self.define_text_and_color(DATA[1])[1]

        # Кнопка выбора статьи
        button_Item = tk.Button(self.frameMain, text=DATA[2], bg=COLOR, font="Arial 12", foreground="#F5F5F5")
        button_Item.place(x=X, y=Y, width=200, height=40)
        button_Item.bind('<Button-1>', lambda event: self.fc.change_source_operation(TYPEOPERATIONS, DATA,
                                                                                     DATAITEM, NOTE))

    def install_new_values_after_change_increase(self, dict_field, name_wallet=''):
        """ Перебираем элементы страницы и устанавливливаем новые свойства """
        listobject = self.frameMain.place_slaves()
        for obj in listobject:
            if obj.winfo_name() == 'button_Increase':
                obj.config(image=self.active_images.get(dict_field.get('icon')))
            if obj.winfo_name() == 'label_signature_item':
                obj.config(text=dict_field.get('textitem'))
            if obj.winfo_name() == 'label_signature_wallet':
                obj.config(text=dict_field.get('textwallet'))
            if obj.winfo_name() == 'label_Increase':
                obj.config(image=self.active_images.get(dict_field.get('icon')))
            if name_wallet and obj.winfo_name() == 'label_Payment':
                obj.config(text=name_wallet)

    # ****************************** СТРАНИЦА СО СПИСКОМ ЗАПИСЕЙ ДЛЯ ПРОСМОТРА ДАННЫХ ПО СТАТЬЕ ****************
    def draw_list_operations_in_item_window(self, DATA):
        """ Окно для отображения данных, заведенных по статье, содержит постраничный пэйджинг, фильтр по дате и
        кнопки дополнительных опций для редактирования, копирования и удаления записей при входе из вышестоящего окна
        статей для ввода и просмотра данных ListItemForEnterDataWindow """
        # Список обновляемых элементов
        elements_to_draw = list()

        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)

        # Устанавливаем идентификатор текущей страницы
        self.fc.current_window = TypesWindows.listDataInItemWindow
        self.clear_main_frame()

        # Подгрузка картинок для страницы
        self.update_dict_active_images(DATA[8])

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black',
                                name='button_Back')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.fc.do_back_ward(DATA[1]))

        # Картинка статьи
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('item_image'))
        Main_paint.place(x=820, y=45)

        # Наименование раздела
        nameandcolor = self.define_text_and_color(DATA[1])
        textheaders = nameandcolor[0] + '/' + DATA[2] + '/Просмотр данных:'
        l1 = tk.Label(self.frameMain, text=textheaders, bg='black', foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=50)

        # Отрисовка списка строк с данными, постраничного пэйджинга и фильтра
        self.draw_list_of_operations(DATA[0], elements_to_draw)

    def draw_list_of_operations(self, ITEMID, OBJECTLIST, DATE_BEGIN='', DATE_END=dt.date(2200, 12, 31)):
        """ Отрисовка реестра строк с данными, постраничного пэйджинга и фильтра
        для метода draw_list_in_item_window. """

        if DATE_BEGIN == '':
            DATE_BEGIN = self.fc.fm.beginDate
        listnotes_page_date = {}
        DATE1 = DATE_BEGIN if self.fc.current_window == TypesWindows.listDataInItemInReportWindow else \
            self.fc.setting_filter['beginDate']
        DATE2 = DATE_END if self.fc.current_window == TypesWindows.listDataInItemInReportWindow else \
            self.fc.setting_filter['endDate']

        # Очищаем строки и удаляем блок фильтра и блок постраничного пэйджинга
        if len(OBJECTLIST) != 0:
            for obj in OBJECTLIST:
                obj.destroy()

        # Запрашиваем общее количество записей по статье
        requestAll = 'item_id={} or source={}'.format(ITEMID, ITEMID)
        listnotesAll = self.fc.fm.request_select_DB('COUNT(*)', 'notes', requestAll)[0]

        if listnotesAll != 0:

            # Запрашиваем количество записей по статье с учетом фильтра по дате
            requestDate = """(item_id={} or source={}) and dateoperation Between \'{}\' and \'{}\'""".format(
                ITEMID, ITEMID, DATE1, DATE2)
            listnotes_date = self.fc.fm.request_select_DB('COUNT(*)', 'notes', requestDate)[0][0]
            if listnotes_date != 0:
                count = listnotes_date // 15
                if listnotes_date % 15 != 0:
                    count += 1

                if self.fc.setting_filter.get('countPage') != count:
                    self.fc.setting_filter['countPage'] = count

                if self.fc.setting_filter.get('currentPage') > count:
                    self.fc.setting_filter['currentPage'] = count

                offset = self.fc.setting_filter.get('currentPage') * 15 - 15
                request_wish_pages = f"""(item_id={ITEMID} or source={ITEMID}) and dateoperation 
                                         Between \'{DATE1}\' and \'{DATE2}\' 
                                         ORDER BY dateoperation DESC LIMIT 15 OFFSET {offset} """
                listnotes_page_date = self.fc.fm.request_select_DB('*', 'notes', request_wish_pages)
            else:
                # Данные по статье есть, но они не попали под сортировку по периоду
                # Надпись о том, что данные в статье отсутствуют при заданной фильтрации по периоду
                tf = "Отсутствуют данные при данной фильтрации.\nИзмените фильтрацию по периоду"
                l2 = tk.Label(self.frameMain, text=tf, bg="black", foreground="#ccc", justify='left',
                              font="Arial 16")
                l2.place(x=50, y=100)
                self.fc.setting_filter['currentPage'] = 1
                self.fc.setting_filter['countPage'] = 1
                OBJECTLIST.append(l2)

            # Блок фильтра по периоду, если это не расшифровка из Отчета
            if self.fc.current_window != TypesWindows.listDataInItemInReportWindow:
                if self.fc.setting_filter['period'] != 'AllPeriod':
                    # Кнопка фильтрации на период назад
                    buttonPeriodLeft = tk.Button(self.frameMain, name='period_Left', background="black",
                                                 image=self.active_images.get('arrowLeft_img'))
                    buttonPeriodLeft.place(x=250, y=630, width=40, height=40)
                    buttonPeriodLeft.bind('<Button-1>',
                                          lambda eventbutton: self.fc.change_filter('PeriodBack', ITEMID,
                                                                                    OBJECTLIST))
                    OBJECTLIST.append(buttonPeriodLeft)

                    # Кнопка фильтрации на период вперёд
                    buttonPeriodRight = tk.Button(self.frameMain, name='period_Right', background="black",
                                                  image=self.active_images.get('arrowRight_img'))
                    buttonPeriodRight.place(x=330, y=630, width=40, height=40)
                    buttonPeriodRight.bind('<Button-1>',
                                           lambda eventbutton: self.fc.change_filter('PeriodForward', ITEMID,
                                                                                     OBJECTLIST))
                    OBJECTLIST.append(buttonPeriodRight)

                # Кнопка изменения размера периода фильтрации вверх
                buttonPeriodUp = tk.Button(self.frameMain, name='period_Up', background="black",
                                           image=self.active_images.get('arrowUp_img'))
                buttonPeriodUp.place(x=290, y=610, width=40, height=40)
                buttonPeriodUp.bind('<Button-1>',
                                    lambda eventbutton: self.fc.change_filter('PeriodUp', ITEMID, OBJECTLIST))
                OBJECTLIST.append(buttonPeriodUp)

                # Кнопка изменения размера периода фильтрации вниз
                buttonPeriodDown = tk.Button(self.frameMain, name='period_Down', background="black",
                                             image=self.active_images.get('arrowDown_img'))
                buttonPeriodDown.place(x=290, y=650, width=40, height=40)
                buttonPeriodDown.bind('<Button-1>', lambda eventbutton: self.fc.change_filter('PeriodDown', ITEMID,
                                                                                              OBJECTLIST))
                OBJECTLIST.append(buttonPeriodDown)

                # Выставленное значение фильтра
                lFilterValue = tk.Label(self.frameMain, name='filter_Text', text=self.fc.set_filter_text(),
                                        bg="#808080",
                                        foreground="#ccc", font="Arial 12")
                lFilterValue.place(x=375, y=630, width=200, height=40)
                OBJECTLIST.append(lFilterValue)
            else:
                # Выставленное значение фильтра
                if self.fc.setting_filter['period'] == 'AllPeriod':
                    textFilter = '{}-...'.format(self.fc.fm.beginDate.strftime('%d.%m.%Y'))
                else:
                    textFilter = '{}-{}'.format(DATE_BEGIN.strftime('%d.%m.%Y'), DATE_END.strftime('%d.%m.%Y'))

                lFilterValue = tk.Label(self.frameMain, name='filter_Text', text=textFilter, bg="#808080",
                                        foreground="#ccc", font="Arial 12")
                lFilterValue.place(x=250, y=630, width=200, height=40)
                OBJECTLIST.append(lFilterValue)
        else:
            # Надпись о том, что данные в статье отсутствуют
            l2 = tk.Label(self.frameMain, text="В статье отсутствуют данные.\nСоздайте их по кнопке +.", bg="black",
                          foreground="#ccc", justify='left', font="Arial 16")
            l2.place(x=50, y=100)
            self.fc.setting_filter['currentPage'] = 1
            self.fc.setting_filter['countPage'] = 1

        if listnotes_page_date:
            # Отрисовываем итоговую строку
            self.draw_total_line(ITEMID, OBJECTLIST, DATE1, DATE2)

            # Отрисовываем строки с данными
            # Фон/область для отображения строк
            Fon_report = tk.Label(self.frameMain, bg='#2F4F4F')
            Fon_report.place(x=20, y=145, width=780, height=460)
            OBJECTLIST.append(Fon_report)

            HY = 150
            for note in listnotes_page_date:
                # Отрисовываем строки
                self.draw_row_operation(ITEMID, note, HY, OBJECTLIST)
                HY += 30

            # Блок постраничного пейджинга
        if self.fc.setting_filter['countPage'] > 1:
            pagetext = '{} из {}'.format(self.fc.setting_filter['currentPage'], self.fc.setting_filter['countPage'])
            # Кнопка перелистывания страниц влево
            buttonPageLeft = tk.Button(self.frameMain, name='page_Left', background="black",
                                       image=self.active_images.get('arrowLeft_img'))
            buttonPageLeft.place(x=50, y=630, width=40, height=40)
            buttonPageLeft.bind('<Button-1>',
                                lambda eventbutton: self.fc.change_filter('PageBack', ITEMID, OBJECTLIST,
                                                                          DATE_BEGIN, DATE_END))
            OBJECTLIST.append(buttonPageLeft)

            # Счетчик страниц
            lPageCounter = tk.Label(self.frameMain, name='page_Counter', text=pagetext, bg="#808080",
                                    foreground="#ccc",
                                    font="Arial 12")
            lPageCounter.place(x=95, y=630, width=100, height=40)
            OBJECTLIST.append(lPageCounter)

            # Кнопка перелистывания страниц вправо
            buttonPageRight = tk.Button(self.frameMain, name='page_Right', background="black",
                                        image=self.active_images.get('arrowRight_img'))
            buttonPageRight.place(x=200, y=630, width=40, height=40)
            buttonPageRight.bind('<Button-1>',
                                 lambda eventbutton: self.fc.change_filter('PageForward', ITEMID, OBJECTLIST,
                                                                           DATE_BEGIN, DATE_END))
            OBJECTLIST.append(buttonPageRight)

    def draw_total_line(self, ITEMID, OBJECTLIST, DATE_BEGIN, DATE_END):
        """ Итоговая строка в реестре данных по статье """
        section = self.fc.fm.request_select_DB('typeitem_id', 'items', 'id={}'.format(ITEMID))[0][0]
        total_dict = self.fc.fm.get_values_for_total_line(ITEMID, DATE_BEGIN, DATE_END, section)

        # Отображение виджетов с остатками и оборотами
        l_ini = tk.Label(self.frameMain, text='Начальный остаток', bg="black", foreground="#ccc", font="Arial 9")
        l_ini.place(x=100, y=97, width=150, height=13)
        OBJECTLIST.append(l_ini)

        lSum_ini = tk.Label(self.frameMain, text=get_string_from_number(total_dict.get('initial_balance_item')),
                            bg="#696969", foreground="#ccc", font="Arial 12")
        lSum_ini.place(x=100, y=110, width=150, height=30)
        OBJECTLIST.append(lSum_ini)

        l_plus = tk.Label(self.frameMain, text='Положительный оборот', bg="black", foreground="#ccc", font="Arial 9")
        l_plus.place(x=260, y=97, width=150, height=13)
        OBJECTLIST.append(l_plus)

        lSum_plus = tk.Label(self.frameMain, text=get_string_from_number(total_dict.get('sumitem_plus')), bg="green",
                             foreground="#ccc", font="Arial 12")
        lSum_plus.place(x=260, y=110, width=150, height=30)
        OBJECTLIST.append(lSum_plus)

        if section != 1 or section != 2:
            l_minus = tk.Label(self.frameMain, text='Отрицательный оборот', bg="black", foreground="#ccc",
                               font="Arial 9")
            l_minus.place(x=420, y=97, width=150, height=13)
            OBJECTLIST.append(l_minus)

            lSum_minus = tk.Label(self.frameMain, text=get_string_from_number(total_dict.get('sumitem_minus')),
                                  bg="red", foreground="#ccc", font="Arial 12")
            lSum_minus.place(x=420, y=110, width=150, height=30)
            OBJECTLIST.append(lSum_minus)

        l_fin = tk.Label(self.frameMain, text='Конечный остаток', bg="black", foreground="#ccc", font="Arial 9")

        lSum_fin = tk.Label(self.frameMain, text=get_string_from_number(total_dict.get('final_balance_item')),
                            bg="#696969", foreground="#ccc", font="Arial 12")
        if section == 1 or section == 2:
            lSum_fin.place(x=420, y=110, width=150, height=30)
            l_fin.place(x=420, y=97, width=150, height=13)
        else:
            lSum_fin.place(x=580, y=110, width=150, height=30)
            l_fin.place(x=580, y=97, width=150, height=13)
        OBJECTLIST.append(lSum_fin)
        OBJECTLIST.append(l_fin)

    def draw_row_operation(self, itemNotes, drawNotes, HightY, OBJECTLIST):
        """ Отрисовка строки с данными """
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
        lSum = tk.Label(self.frameMain, text=get_string_from_number(drawNotes[5]), bg=colorbutton,
                        foreground="#ccc", font="Arial 12")
        lSum.place(x=125, y=HightY, width=140, height=25)
        OBJECTLIST.append(lSum)

        # Корреспондирующая статья
        namesource = ''
        if itemNotes == drawNotes[1]:
            namesource = self.fc.fm.request_select_DB('nameitem', 'items', 'id={}'.format(drawNotes[7]))
        elif itemNotes == drawNotes[7]:
            namesource = self.fc.fm.request_select_DB('nameitem', 'items', 'id={}'.format(drawNotes[1]))
        lSource = tk.Label(self.frameMain, text=namesource[0][0], bg=colorbutton, foreground="#ccc",
                           font="Arial 10")
        lSource.place(x=270, y=HightY, width=180, height=25)
        OBJECTLIST.append(lSource)

        # Кнопка отображения/скрытия дополнительных опций(удаления, корректировки, копирования)
        if self.fc.current_window != TypesWindows.listDataInItemInReportWindow:
            buttonOptions = tk.Button(self.frameMain, background="black", image=self.active_images.get('forward25_img'))
            buttonOptions.place(x=455, y=HightY, width=25, height=25)
            buttonOptions.bind('<Button-1>', lambda eventbutton: self.display_options_buttons(drawNotes, itemNotes,
                                                                                              HightY, OBJECTLIST))
            OBJECTLIST.append(buttonOptions)

        # Описание операции
        if drawNotes[4]:
            lDescription = tk.Label(self.frameMain, text=drawNotes[4], bg="#808080", foreground="#ccc",
                                    font="Arial 10")
            lDescription.place(x=485, y=HightY, width=300, height=25)
            OBJECTLIST.append(lDescription)

    def display_options_buttons(self, NOTE, ITEMID, HightY, OBJECTLIST):
        """ Отображение кнопок с опциями (удалить, редактировать, копировать) в реестре операций """
        # Удаление кнопок допопций, если они уже есть
        for obj in OBJECTLIST:
            if obj.winfo_name == 'delete_button' or obj.winfo_name == 'correction_button' or \
                    obj.winfo_name == 'copy_button':
                obj.destroy()

        # Кнопка удаления
        buttonDelete = tk.Button(self.frameMain, background="black", name='delete_button',
                                 image=self.active_images.get('delete25_img'))
        buttonDelete.place(x=505, y=HightY, width=25, height=25)
        buttonDelete.bind('<Button-1>', lambda eventbutton: self.ask_question_about_deleting(NOTE, ITEMID, OBJECTLIST))
        OBJECTLIST.append(buttonDelete)

        DATA = self.fc.fm.request_select_DB('*', 'items', 'id={}'.format(ITEMID))[0]

        # Кнопка корректировки записи
        buttonCorrection = tk.Button(self.frameMain, background="black", name='correction_button',
                                     image=self.active_images.get('correction25_img'))
        buttonCorrection.place(x=535, y=HightY, width=25, height=25)
        buttonCorrection.bind('<Button-1>', lambda eventbutton: self.create_correct_data_window('CORRECTION',
                                                                                                DATA, NOTE))
        OBJECTLIST.append(buttonCorrection)

        # Кнопка копирования
        buttonCopy = tk.Button(self.frameMain, background="black", name='copy_button',
                               image=self.active_images.get('copy_img'))
        buttonCopy.place(x=565, y=HightY, width=25, height=25)
        buttonCopy.bind('<Button-1>', lambda eventbutton: self.create_correct_data_window('COPY', DATA, NOTE))
        OBJECTLIST.append(buttonCopy)

    def ask_question_about_deleting(self, NOTE, ITEMID, OBJECTLIST):
        """ Вопрос об удалении записи """
        # Очищаем строки и удаляем блок фильтра и блок постраничного пэйджинга
        if len(OBJECTLIST) != 0:
            for obj in OBJECTLIST:
                obj.destroy()

        # Надпись с вопросом
        nameitem = self.fc.fm.request_select_DB('nameitem', 'items', 'id={}'.format(ITEMID))[0][0]
        textQuestion = 'Удалить запись по статье:\n {} на сумму {} руб.\nВосстановление записи невозможно'.format(
            nameitem, NOTE[5])
        lQuestion = tk.Label(self.frameMain, text=textQuestion, bg='black', foreground="#ccc", font="Arial 16",
                             justify='center')
        lQuestion.place(x=100, y=150, width=600, height=70)
        OBJECTLIST.append(lQuestion)

        # Кнопка подтверждения
        buttonYes = tk.Button(self.frameMain, text='ДА', font="Arial 16", bg="#708090", foreground="#F5F5F5")
        buttonYes.place(x=320, y=250, width=80, height=40)
        buttonYes.bind('<Button-1>', lambda eventbutton: self.fc.delete_operation_from_registry(NOTE, ITEMID))
        OBJECTLIST.append(buttonYes)

        # Кнопка отмены
        buttonNo = tk.Button(self.frameMain, text='НЕТ', font="Arial 12", bg="#708090", foreground="#F5F5F5")
        buttonNo.place(x=420, y=250, width=80, height=40)
        buttonNo.bind('<Button-1>', lambda eventbutton: self.draw_list_of_operations(ITEMID, OBJECTLIST))
        OBJECTLIST.append(buttonNo)

        # Картинка с шредером
        shreder_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('shreder_img'))
        shreder_paint.place(x=200, y=320)
        OBJECTLIST.append(shreder_paint)

    # ****************************** СТРАНИЦА ОТРИСОВКИ ОТЧЕТА ПО ОСТАТКАМ И ДВИЖЕНИЮ ПО СТАТЬЯМ ****************
    def report_window(self, REQUEST_LIST='', VIEW='narrow', TOPLINE=0):
        """ Окно просмотра отчета с пэйджингом и фильтром """
        self.fc.current_window = TypesWindows.reportWindow
        self.update_dict_active_images()
        self.fc.setting_filter['currentPage'] = 1
        self.fc.setting_filter['countPage'] = 1

        if REQUEST_LIST == '':
            REQUEST_LIST = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]

        # Отключаем отображаемые фреймы
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.clear_main_frame()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black',
                                name='button_Back')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.fc.do_back_ward(0))

        # Наименование страницы
        l1 = tk.Label(self.frameMain, text="ПРОСМОТР ОТЧЕТА:", bg="black", foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=50)

        self.draw_rows_report(REQUEST_LIST, VIEW, TOPLINE)

    def draw_rows_report(self, REQUEST_LIST, VIEW='narrow', TOPLINE=0):
        """ Отображение строк отчета и фильтра по периоду
        narrow - узкий вид; wide - широкий вид"""
        # Список строк для отображения
        LIST_STRING = list()

        # Запрашиваем данные для отрисовки разделов
        # Для узкого вида
        if VIEW == 'narrow':
            LIST_STRING = self.fc.fm.get_data_for_row_report_narrow(REQUEST_LIST)
        # Дляширокого вида
        elif VIEW == 'wide':
            LIST_STRING = self.fc.fm.get_data_for_row_report_wide(REQUEST_LIST)

        # Список обновляемых объектов
        OBJECTLIST = list()

        # Отображение картинки, фона и заголовков для узкого вида
        if VIEW == 'narrow':
            # Картинка статьи
            Main_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('report_img'))
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

            tex_d1 = '{} - {}'.format(dt.date.strftime(REQUEST_LIST[0][2], '%d.%m.%Y'),
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
        self.draw_strings(LIST_STRING, OBJECTLIST, REQUEST_LIST, VIEW, TOPLINE)

        # Блок фильтра по периоду
        if self.fc.setting_filter.get('period') != 'AllPeriod':
            # Кнопка фильтрации на период назад
            buttonPeriodLeft = tk.Button(self.frameMain, name='period_Left', background="black",
                                         image=self.active_images.get('arrowLeft_img'))
            buttonPeriodLeft.place(x=250, y=640, width=40, height=40)
            buttonPeriodLeft.bind('<Button-1>', lambda eventbutton: self.fc.change_filter_report(
                'PeriodBack', REQUEST_LIST, OBJECTLIST, VIEW))
            OBJECTLIST.append(buttonPeriodLeft)

            # Кнопка фильтрации на период вперёд
            buttonPeriodRight = tk.Button(self.frameMain, name='period_Right', background="black",
                                          image=self.active_images.get('arrowRight_img'))
            buttonPeriodRight.place(x=330, y=640, width=40, height=40)
            buttonPeriodRight.bind('<Button-1>', lambda eventbutton: self.fc.change_filter_report(
                'PeriodForward', REQUEST_LIST, OBJECTLIST, VIEW))
            OBJECTLIST.append(buttonPeriodRight)

        # Кнопка изменения размера периода фильтрации вверх
        buttonPeriodUp = tk.Button(self.frameMain, name='period_Up', background="black",
                                   image=self.active_images.get('arrowUp_img'))
        buttonPeriodUp.place(x=290, y=620, width=40, height=40)
        buttonPeriodUp.bind('<Button-1>', lambda eventbutton: self.fc.change_filter_report('PeriodUp', REQUEST_LIST,
                                                                                           OBJECTLIST, VIEW))
        OBJECTLIST.append(buttonPeriodUp)

        # Кнопка изменения размера периода фильтрации вниз
        buttonPeriodDown = tk.Button(self.frameMain, name='period_Down', background="black",
                                     image=self.active_images.get('arrowDown_img'))
        buttonPeriodDown.place(x=290, y=660, width=40, height=40)
        buttonPeriodDown.bind('<Button-1>', lambda eventbutton: self.fc.change_filter_report('PeriodDown', REQUEST_LIST,
                                                                                             OBJECTLIST, VIEW))
        OBJECTLIST.append(buttonPeriodDown)

        # Выставленное значение фильтра
        lFilterValue = tk.Label(self.frameMain, name='filter_Text', text=self.fc.set_filter_text(), bg="#808080",
                                foreground="#ccc", font="Arial 12")
        lFilterValue.place(x=375, y=640, width=200, height=40)
        OBJECTLIST.append(lFilterValue)

        # Кнопка переключения на широкий вид
        if self.fc.setting_filter.get('period') != 'AllPeriod':
            if VIEW == 'narrow':
                paint_view = self.active_images.get('forward_img')
            else:
                paint_view = self.active_images.get('Wrap_img')

            # Кнопка переключения узкого и широкого вида
            button_view = tk.Button(self.frameMain, background="black", image=paint_view)
            button_view.place(x=580, y=640, width=40, height=40)
            button_view.bind('<Button-1>', lambda eventbutton: self.fc.change_view_report(REQUEST_LIST, OBJECTLIST,
                                                                                          VIEW))
            OBJECTLIST.append(button_view)

    def draw_strings(self, LIST_STRING, OBJECTLIST, REQUEST_LIST, VIEW, TOPLINE):
        """ Отображение строк отчета """
        # Список обновляемых объектов при скроллировании
        OBJSTRING = list()

        Y = 129
        if len(LIST_STRING) <= 16:
            for STRING in LIST_STRING:
                if STRING.get('type_row') in ('aktiv', 'passiv'):
                    Y += 5
                self.draw_one_string_report(OBJECTLIST, OBJSTRING, STRING, Y, REQUEST_LIST, TOPLINE, VIEW)
                Y += 27
        else:
            length = len(LIST_STRING)
            count = length - TOPLINE
            count = TOPLINE + count if count < 16 else TOPLINE + 16
            for i in range(TOPLINE, count):
                if LIST_STRING[i].get('type_row') in ('aktiv', 'passiv'):
                    Y += 5
                self.draw_one_string_report(OBJECTLIST, OBJSTRING, LIST_STRING[i], Y, REQUEST_LIST, TOPLINE, VIEW)
                Y += 27

        if len(LIST_STRING) > 16:
            # Кнопка прокрутки реестра вверх
            buttonUp = tk.Button(self.frameMain, background="black", image=self.active_images.get('arrowUp_img'))
            buttonUp.place(x=10, y=300, width=40, height=40)
            buttonUp.bind('<Button-1>', lambda eventbutton: self.fc.scroll_registry_report(
                'UP', LIST_STRING, OBJECTLIST, OBJSTRING, REQUEST_LIST, VIEW, TOPLINE))
            OBJECTLIST.append(buttonUp)

            # Кнопка прокрутки реестра вниз
            buttonDown = tk.Button(self.frameMain, background="black", image=self.active_images.get('arrowDown_img'))
            buttonDown.place(x=10, y=340, width=40, height=40)
            buttonDown.bind('<Button-1>', lambda eventbutton: self.fc.scroll_registry_report(
                'DOWN', LIST_STRING, OBJECTLIST, OBJSTRING, REQUEST_LIST, VIEW, TOPLINE))
            OBJECTLIST.append(buttonDown)

    def draw_one_string_report(self, OBJECTLIST, OBJSTRING, STRING, Y, REQUEST_LIST, TOPLINE, VIEW='narrow'):
        """ Отображение одной строки отчета """
        COLOR, FONT, X, WIDTH = '', '', 0, 0

        if STRING.get('type_row') == 'item':
            typeitem = self.fc.fm.request_select_DB('typeitem_id', 'items', 'id={}'.format(
                STRING.get('item')))[0][0]
            COLOR = self.define_text_and_color(typeitem)[1]
            X = 125
            WIDTH = 200
        elif STRING.get('type_row') == 'section':
            if STRING.get('type_item') == 1:
                COLOR = '#F08080'
            elif STRING.get('type_item') == 2:
                COLOR = '#BA55D3'
            elif STRING.get('type_item') in (7, 8, 9):
                COLOR = '#DA70D6'
            else:
                COLOR = '#DB7093'
            X = 95
            WIDTH = 230

        elif STRING.get('type_row') == 'result':
            COLOR = '#DAA520'
            X = 55
            WIDTH = 270

        elif STRING.get('type_row') == 'aktiv':
            COLOR = '#C71585'
            X = 55
            WIDTH = 270

        elif STRING.get('type_row') == 'passiv':
            COLOR = '#800080'
            X = 55
            WIDTH = 270

        # Кнопка раскрытия узла
        if STRING.get('is_node') == 1 and STRING.get('type_row') == 'section':
            if STRING.get('node_is_open') == 0:
                IMAGE = self.active_images.get('forward25_img')
            else:
                IMAGE = self.active_images.get('deployed25_img')

            button_node = tk.Button(self.frameMain, background="black", image=IMAGE)
            button_node.place(x=67, y=Y, width=25, height=25)
            button_node.bind('<Button-1>', lambda eventbutton: self.fc.node_click_report(
                OBJECTLIST, STRING, REQUEST_LIST, VIEW))
            OBJECTLIST.append(button_node)
            OBJSTRING.append(button_node)

        tex_font = "Arial 12" if STRING.get('type_item') == 'item' else "Arial 14"
        l_name = tk.Label(self.frameMain, text=STRING.get('name'), bg=COLOR, foreground="#F5F5F5", font=tex_font)
        l_name.place(x=X, y=Y, width=WIDTH, height=25)
        OBJECTLIST.append(l_name)
        OBJSTRING.append(l_name)

        l_initial_balance = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('initial_balance_item')),
                                     bg="#A9A9A9", foreground="#F5F5F5", font="Arial 12")
        l_initial_balance.place(x=329, y=Y, width=150, height=25)
        OBJECTLIST.append(l_initial_balance)
        OBJSTRING.append(l_initial_balance)

        if VIEW == 'narrow':
            if STRING.get('opener1') == 1 and STRING.get('type_row') == 'item':

                button1_turnover = tk.Button(self.frameMain, text=get_string_from_number(STRING.get('turnover1')),
                                             bg="#808080", foreground="#F5F5F5", font="Arial 12")
                button1_turnover.place(x=483, y=Y, width=150, height=25)
                DATE1 = REQUEST_LIST[0][2] if self.fc.setting_filter['period'] != 'AllPeriod' else \
                    self.fc.setting_filter['beginDate']
                DATE2 = REQUEST_LIST[0][3] if self.fc.setting_filter['period'] != 'AllPeriod' else \
                    self.fc.setting_filter['endDate']
                button1_turnover.bind('<Button-1>', lambda eventbutton: self.draw_data_item_in_report_window(
                    STRING, (DATE1, DATE2), REQUEST_LIST, VIEW, TOPLINE))

                OBJECTLIST.append(button1_turnover)
                OBJSTRING.append(button1_turnover)
            else:
                l1_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover1')),
                                       bg="#808080", foreground="#F5F5F5", font="Arial 12")
                l1_turnover.place(x=483, y=Y, width=150, height=25)
                OBJECTLIST.append(l1_turnover)
                OBJSTRING.append(l1_turnover)

            l_final_balance = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('final_balance_item')),
                                       bg="#A9A9A9", foreground="#F5F5F5", font="Arial 12")
            l_final_balance.place(x=637, y=Y, width=150, height=25)
            OBJECTLIST.append(l_final_balance)
            OBJSTRING.append(l_final_balance)

        elif VIEW == 'wide':
            if STRING.get('opener1') == 1 and STRING.get('type_row') == 'item':
                button1_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover1')),
                                            bg="#808080", foreground="#F5F5F5", font="Arial 12")
                button1_turnover.place(x=483, y=Y, width=150, height=25)
                DATE3 = REQUEST_LIST[0][2]
                DATE4 = REQUEST_LIST[0][3]
                button1_turnover.bind('<Button-1>', lambda eventbutton: self.draw_data_item_in_report_window(
                    STRING, (DATE3, DATE4), REQUEST_LIST, VIEW, TOPLINE))
                OBJECTLIST.append(button1_turnover)
                OBJSTRING.append(button1_turnover)
            else:
                l1_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover1')),
                                       bg="#808080", foreground="#F5F5F5", font="Arial 12")
                l1_turnover.place(x=483, y=Y, width=150, height=25)
                OBJECTLIST.append(l1_turnover)
                OBJSTRING.append(l1_turnover)

            if STRING.get('opener2') == 1 and STRING.get('type_row') == 'item':
                button2_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover2')),
                                            bg="#808080", foreground="#F5F5F5", font="Arial 12")
                button2_turnover.place(x=637, y=Y, width=150, height=25)
                DATE5 = REQUEST_LIST[0][4]
                DATE6 = REQUEST_LIST[0][5]
                button2_turnover.bind('<Button-1>', lambda eventbutton: self.draw_data_item_in_report_window(
                    STRING, (DATE5, DATE6), REQUEST_LIST, VIEW, TOPLINE))
                OBJECTLIST.append(button2_turnover)
                OBJSTRING.append(button2_turnover)
            else:
                l2_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover2')),
                                       bg="#808080", foreground="#F5F5F5", font="Arial 12")
                l2_turnover.place(x=637, y=Y, width=150, height=25)
                OBJECTLIST.append(l2_turnover)
                OBJSTRING.append(l2_turnover)

            if STRING.get('opener3') == 1 and STRING.get('type_row') == 'item':
                button3_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover3')),
                                            bg="#808080", foreground="#F5F5F5", font="Arial 12")
                button3_turnover.place(x=791, y=Y, width=150, height=25)
                DATE7 = REQUEST_LIST[0][6]
                DATE8 = REQUEST_LIST[0][7]
                button3_turnover.bind('<Button-1>', lambda eventbutton: self.draw_data_item_in_report_window(
                    STRING, (DATE7, DATE8), REQUEST_LIST, VIEW, TOPLINE))
                OBJECTLIST.append(button3_turnover)
                OBJSTRING.append(button3_turnover)
            else:
                l3_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover3')),
                                       bg="#808080", foreground="#F5F5F5", font="Arial 12")
                l3_turnover.place(x=791, y=Y, width=150, height=25)
                OBJECTLIST.append(l3_turnover)
                OBJSTRING.append(l3_turnover)

            if STRING.get('opener4') == 1 and STRING.get('type_row') == 'item':
                button4_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover4')),
                                            bg="#808080", foreground="#F5F5F5", font="Arial 12")
                button4_turnover.place(x=945, y=Y, width=150, height=25)
                DATE9 = REQUEST_LIST[0][8]
                DATE10 = REQUEST_LIST[0][9]
                button4_turnover.bind('<Button-1>', lambda eventbutton: self.draw_data_item_in_report_window(
                    STRING, (DATE9, DATE10), REQUEST_LIST, VIEW, TOPLINE))
                OBJECTLIST.append(button4_turnover)
                OBJSTRING.append(button4_turnover)
            else:
                l4_turnover = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('turnover4')),
                                       bg="#808080", foreground="#F5F5F5", font="Arial 12")
                l4_turnover.place(x=945, y=Y, width=150, height=25)
                OBJECTLIST.append(l4_turnover)
                OBJSTRING.append(l4_turnover)

            l_final_balance = tk.Label(self.frameMain, text=get_string_from_number(STRING.get('final_balance_item')),
                                       bg="#A9A9A9", foreground="#F5F5F5", font="Arial 12")
            l_final_balance.place(x=1099, y=Y, width=150, height=25)
            OBJECTLIST.append(l_final_balance)
            OBJSTRING.append(l_final_balance)

    def draw_data_item_in_report_window(self, STRING, DATES, REQUEST_LIST, VIEW, TOPLINE):
        """ Окно для отображения данных по статье за период фильтрации из Отчета, содержит постраничный пэйджинг """
        # Список обновляемых элементов
        ElementsToDraw = list()

        # Устанавливаем идентификатоо текущей страницы
        self.fc.current_window = TypesWindows.listDataInItemInReportWindow
        self.update_dict_active_images()

        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)

        # Очищаем страницу
        self.clear_main_frame()

        # Кнопка назад
        button_back = tk.Button(self.toolbarMenu, image=self.active_images.get('back_img'), bg='black',
                                name='button_Back')
        button_back.place(x=130, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.report_window(REQUEST_LIST, VIEW, TOPLINE))

        # Картинка отчета
        Main_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('report_img'))
        Main_paint.place(x=820, y=45)

        # Заголовок страницы
        textheaders = 'ПРОСМОТР ОТЧЕТА' + '/' + STRING.get('name') + '/Расшифровка :'
        l1 = tk.Label(self.frameMain, text=textheaders, bg='black', foreground="#ccc", font="Arial 25")
        l1.place(x=50, y=0)
        item_id = STRING.get('item')
        # Отрисовка списка строк с данными, постраничного пэйджинга и фильтра
        self.draw_list_of_operations(item_id, ElementsToDraw, DATES[0], DATES[1])

    # ****************************** СТРАНИЦА МЕНЮ ПРИЛОЖЕНИЯ ****************************************************
    def menu_window(self):
        """ Окно меню программы с опциями: Продолжить, Настройки, О программе, Выйти """
        if self.fc.current_window != TypesWindows.settingWindow:
            self.fc.previous_window = self.fc.current_window

        self.fc.current_window = TypesWindows.menuWindow
        self.update_dict_active_images()

        # Отключаем отображаемые фреймы
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.clear_main_frame()

        # Фрейм меню
        label_menu = tk.Label(self.frameMain, text='МЕНЮ:', bg="black", foreground="#ccc", font="Arial 25")
        label_menu.place(x=500, y=149)
        label_menu_icon = tk.Label(self.frameMain, image=self.active_images.get('menu_img'))
        label_menu_icon.place(x=620, y=150)

        section = 0
        if self.fc.previous_window == TypesWindows.listItemForEnterDataWindow:
            section = self.fc.section

        buttonResume = tk.Button(self.frameMain, text="Продолжить  ", background="#222", foreground="#ccc",
                                 highlightcolor="#C0C0C0", padx="10", pady="1", font="16", compound=tk.RIGHT,
                                 image=self.active_images.get('baks_img'), command=self.fc.do_back_ward)
        buttonResume.bind('<Button-1>', lambda eventbutton: self.fc.do_back_ward(section))
        buttonResume.place(x=500, y=199)

        buttonSetting2 = tk.Button(self.frameMain, text='Настроить     ', background="#222", foreground="#ccc",
                                   highlightcolor="#C0C0C0", padx="10", command=self.setting_window,
                                   pady="1", font="16", compound=tk.RIGHT, image=self.active_images.get('setting_img'))
        buttonSetting2.place(x=500, y=259)

        buttonInfo = tk.Button(self.frameMain, text='О программе', background="#222", foreground="#ccc",
                               highlightcolor="#C0C0C0",
                               padx="10", pady="1", font="16", compound=tk.RIGHT,
                               image=self.active_images.get('info_img'))
        buttonInfo.place(x=500, y=320)

        buttonExit = tk.Button(self.frameMain, text='Выйти             ', background="#222", foreground="#ccc",
                               highlightcolor="#C0C0C0", padx="10", pady="1", font="16", compound=tk.RIGHT,
                               image=self.active_images.get('exit_img'), command=self.fc.exit_the_program)
        buttonExit.place(x=500, y=379)

        # Картинка с битками
        coin_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('coin_img'))
        coin_paint.place(x=775, y=50)

    # ****************************** СТРАНИЦА НАСТРОЙКИ УЧЕТА ****************************************************
    def setting_window(self):
        """ Окно настройки системы """
        self.fc.current_window = TypesWindows.settingWindow
        self.clear_main_frame()
        self.toolbarMenu.pack_forget()
        self.frameMain.place(x=0, y=0, height=720, width=1280)
        self.update_dict_active_images()

        # Кнопка назад
        if self.fc.fm.use == 1:
            button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black',
                                    command=self.menu_window)
            button_back.place(x=0, y=0)

        # Наименование страницы
        l0 = tk.Label(self.frameMain, text="Настройка:", bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        # Картинка часового механизма
        time_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('time_img'))
        time_paint.place(x=820, y=75)

        # Поле ввода даты
        l1 = tk.Label(self.frameMain, text="Дата начала учета:", bg="black", foreground="#ccc", font="Arial 20")
        l1.place(x=50, y=60)
        date = dt.date.strftime(self.fc.fm.beginDate, '%d.%m.%Y')
        button_Date = tk.Button(self.frameMain, name='button_Date', text=date,
                                bg='#708090', font="Arial 25", foreground="#F5F5F5")
        button_Date.place(x=50, y=100, width=300, height=40)
        Data = (1, 50, 100, 300, 40, date, 'button_Date', 'Arial 25', '#708090', '#F5F5F5', date, 0)
        button_Date.bind('<Button-1>', lambda event: self.open_field_for_change_data(Data))

        # Предупреждение о смысле даты начала учета
        if self.fc.fm.use == 0:
            info_paint2 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('info_img'))
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
        button_IncomeSetting.bind('<Button-1>', lambda event: self.list_item_setting_window(1))

        button_CostsSetting = tk.Button(self.frameMain, text='Настройка статей расходов', bg='#BA55D3', font="Arial 16",
                                        foreground="#F5F5F5")
        button_CostsSetting.place(x=450, y=200, width=360, height=40)
        button_CostsSetting.bind('<Button-1>', lambda event: self.list_item_setting_window(2))

        # Запрос к БД на данные по разделам
        data = self.fc.fm.request_select_DB('*', 'typeitems')

        # Блок настройки статей актива
        l3 = tk.Label(self.frameMain, text="АКТИВ:", bg="black", foreground="#C71585", font="Arial 25")
        l3.place(x=50, y=250)

        button_MoneySetting = tk.Button(self.frameMain, text=data[2][2], bg='#DB7093', font="Arial 14",
                                        foreground="#F5F5F5")
        button_MoneySetting.place(x=50, y=300, width=200, height=40)
        button_MoneySetting.bind('<Button-1>', lambda event: self.list_item_setting_window(3))
        s1 = tk.Label(self.frameMain, text=get_string_from_number(data[2][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s1.place(x=255, y=300, width=150, height=40)

        button_PropertySetting = tk.Button(self.frameMain, text=data[3][2], bg='#DB7093', font="Arial 14",
                                           foreground="#F5F5F5")
        button_PropertySetting.place(x=50, y=350, width=200, height=40)
        button_PropertySetting.bind('<Button-1>', lambda event: self.list_item_setting_window(4))
        s2 = tk.Label(self.frameMain, text=get_string_from_number(data[3][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s2.place(x=255, y=350, width=150, height=40)

        button_InvestmentsSetting = tk.Button(self.frameMain, text=data[4][2], bg='#DB7093', font="Arial 14",
                                              foreground="#F5F5F5")
        button_InvestmentsSetting.place(x=50, y=400, width=200, height=40)
        button_InvestmentsSetting.bind('<Button-1>', lambda event: self.list_item_setting_window(5))
        s3 = tk.Label(self.frameMain, text=get_string_from_number(data[4][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s3.place(x=255, y=400, width=150, height=40)

        button_LoansIssuedSetting = tk.Button(self.frameMain, text=data[5][2], bg='#DB7093', font="Arial 14",
                                              foreground="#F5F5F5")
        button_LoansIssuedSetting.place(x=50, y=450, width=200, height=40)
        button_LoansIssuedSetting.bind('<Button-1>', lambda event: self.list_item_setting_window(6))
        s4 = tk.Label(self.frameMain, text=get_string_from_number(data[5][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s4.place(x=255, y=450, width=150, height=40)

        # Блок настройки статей пассива
        l4 = tk.Label(self.frameMain, text="ПАССИВ:", bg="black", foreground="#800080", font="Arial 25")
        l4.place(x=450, y=250)

        button_CreditSetting = tk.Button(self.frameMain, text=data[6][2], bg='#DA70D6', font="Arial 14",
                                         foreground="#F5F5F5")
        button_CreditSetting.place(x=450, y=300, width=200, height=40)
        button_CreditSetting.bind('<Button-1>', lambda event: self.list_item_setting_window(7))
        s5 = tk.Label(self.frameMain, text=get_string_from_number(data[6][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s5.place(x=655, y=300, width=150, height=40)

        button_LoansSetting = tk.Button(self.frameMain, text=data[7][2], bg='#DA70D6', font="Arial 14",
                                        foreground="#F5F5F5")
        button_LoansSetting.place(x=450, y=350, width=200, height=40)
        button_LoansSetting.bind('<Button-1>', lambda event: self.list_item_setting_window(8))
        s6 = tk.Label(self.frameMain, text=get_string_from_number(data[7][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s6.place(x=655, y=350, width=150, height=40)

        # Информация об собственном капитале
        l5 = tk.Label(self.frameMain, text=data[8][2], bg='#DA70D6', foreground="#F5F5F5", font="Arial 14")
        l5.place(x=450, y=450, width=200, height=40)
        s7 = tk.Label(self.frameMain, text=get_string_from_number(data[8][4]), bg="#A9A9A9", foreground="#F5F5F5",
                      font="Arial 12")
        s7.place(x=655, y=450, width=150, height=40)

        # Блок дополнительных настроек
        l6 = tk.Label(self.frameMain, text="Дополнительные настройки:", bg="black", foreground="#ccc",
                      font="Arial 20")
        l6.place(x=50, y=510)

        parol_Setting = tk.Button(self.frameMain, text='Смена пароля', bg='#708090', font="Arial 16",
                                  foreground="#F5F5F5")
        parol_Setting.place(x=50, y=550, width=350, height=40)
        # parol_Setting.bind('<Button-1>', lambda event: self.ChangeTheDate())

        image_Setting = tk.Button(self.frameMain, text='Настройка изображений', bg='#708090', font="Arial 16",
                                  foreground="#F5F5F5")
        image_Setting.place(x=50, y=600, width=350, height=40)
        # image_Setting.bind('<Button-1>', lambda event: self.ChangeTheDate())

        # Блок начала работы
        if self.fc.fm.use == 0:
            info_paint1 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('info_img'))
            info_paint1.place(x=580, y=5)
            l7 = tk.Label(self.frameMain,
                          text="После настройки необходимых параметров \nнажмите кнопку начать для начала работы:",
                          bg="black", foreground="#ccc", font="Arial 14")
            l7.place(x=630, y=1)
            info_paint3 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('right_img'))
            info_paint3.place(x=1030, y=3)
            button_Begin = tk.Button(self.frameMain, text='Начать', bg='#708090', font="Arial 20", foreground="#F5F5F5")
            button_Begin.place(x=1077, y=5, width=200, height=40)
            button_Begin.bind('<Button-1>', lambda event: self.start_of_work())

    def start_of_work(self):
        """ Перевод приложения в рабочее состояние и переход на основную страницу """
        self.clear_main_frame()
        self.toolbarMenu.pack(side=tk.TOP, fill=tk.X)
        self.frameMain.place(x=0, y=55, height=665, width=1280)
        if op.exists('Financier.db'):
            # Запрос к БД на id кошелька и изменение даты стартовых статей на дату начала учета
            data = self.fc.fm.request_select_DB('*', 'items', 'typeitem_id=3')
            tex = data[0][0]

            # Запрос к БД на запись параметра рабочей программы и кошелька по умолчанию
            self.fc.fm.update_note_DB('setting', 'use', 'id', 1, 1)
            self.fc.fm.update_note_DB('setting', 'wallet', 'id', tex, 1)
            self.fc.fm.use = 1
        else:
            print('WARNING!!! No Financier.db')

        # Запускаем основное окно программы
        self.main_window()

    def list_item_setting_window(self, idtypeitem):
        """Окно настройки статей"""
        self.fc.current_window = TypesWindows.listItemSettingWindow
        self.clear_main_frame()
        self.update_dict_active_images(idtypeitem)

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda event: self.fc.do_back_ward(0))

        # Наименование страницы
        TextAndColor = self.define_text_and_color(idtypeitem)
        texthead = 'Настройка/{}:'.format(TextAndColor[0])
        l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        # Запрос к БД на перечень статей в разделе
        data = self.fc.fm.request_select_DB('*', 'items', 'typeitem_id={}'.format(idtypeitem))

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

                self.button_item(DATA, COLOR, X, Y)
                i += 1

            if X == 50:
                X = 450
            else:
                X = 50
                Y = Y + 50

            # Кнопка создания новой статьи
            button_AddItem = tk.Button(self.frameMain, text=' Добавить статью ', compound=tk.RIGHT,
                                       image=self.active_images.get('plus_img'),
                                       bg=TextAndColor[1], font="Arial 14", foreground="#F5F5F5")
            button_AddItem.place(x=X, y=Y, width=200, height=40)
            button_AddItem.bind('<Button-1>', lambda event: self.draw_item_create_new_window(idtypeitem))

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

                self.button_item(DATA, COLOR, X, Y)
                i += 1

            # Кнопка создания новой статьи
            button_AddItem = tk.Button(self.frameMain, text=' Добавить статью ', compound=tk.RIGHT,
                                       image=self.active_images.get('plus_img'),
                                       bg=TextAndColor[1], font="Arial 14", foreground="#F5F5F5")
            button_AddItem.place(x=50, y=650, width=200, height=40)
            button_AddItem.bind('<Button-1>', lambda event: self.draw_item_create_new_window(idtypeitem))

        elif len(data) > 20:
            # Определяем количество страниц и список для отрисовки
            count = len(data) // 20
            if len(data) % 20 != 0:
                count += 1

            if self.fc.setting_filter.get('currentPage') > count:
                self.fc.setting_filter['currentPage'] = 1
            self.fc.setting_filter['countPage'] = count

            # Отбираем записи в зависимости от текущей страницы
            sortedPageList = list()
            countnotes = len(data)

            if self.fc.setting_filter.get('currentPage') == 1:
                iBegin = 0
            else:
                iBegin = self.fc.setting_filter['currentPage'] * 20 - 20
            iEnd = self.fc.setting_filter['currentPage'] * 20
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

                self.button_item(DATA, COLOR, X, Y)
                i += 1

            # Кнопка создания новой статьи
            button_AddItem = tk.Button(self.frameMain, text=' Добавить статью ', compound=tk.RIGHT,
                                       image=self.active_images.get('plus_img'),
                                       bg=TextAndColor[1], font="Arial 14", foreground="#F5F5F5")
            button_AddItem.place(x=50, y=650, width=200, height=40)
            button_AddItem.bind('<Button-1>', lambda event: self.draw_item_create_new_window(idtypeitem))

            # Блок постраничного пейджинга
            pagetext = '{} из {}'.format(self.fc.setting_filter.get('currentPage'),
                                         self.fc.setting_filter.get('countPage'))
            # Кнопка перелистывания страниц влево
            buttonPageLeft = tk.Button(self.frameMain, name='page_Left', background="black",
                                       image=self.active_images.get('arrowLeft_img'))
            buttonPageLeft.place(x=255, y=650, width=40, height=40)
            buttonPageLeft.bind('<Button-1>', lambda eventbutton: self.fc.change_page_setting_item('PageForward',
                                                                                                   idtypeitem))

            # Счетчик страниц
            lPageCounter = tk.Label(self.frameMain, name='page_Counter', text=pagetext, bg="#808080", foreground="#ccc",
                                    font="Arial 12")
            lPageCounter.place(x=300, y=650, width=100, height=40)

            # Кнопка перелистывания страниц вправо
            buttonPageRight = tk.Button(self.frameMain, name='page_Right', background="black",
                                        image=self.active_images.get('arrowRight_img'))
            buttonPageRight.place(x=405, y=650, width=40, height=40)
            buttonPageRight.bind('<Button-1>', lambda eventbutton: self.fc.change_page_setting_item('PageBack',
                                                                                                    idtypeitem))

        elif len(data) == 0:
            # Кнопка создания новой статьи
            button_AddItem = tk.Button(self.frameMain, text=' Добавить статью ', compound=tk.RIGHT,
                                       image=self.active_images.get('plus_img'),
                                       bg=TextAndColor[1], font="Arial 14", foreground="#F5F5F5")
            button_AddItem.place(x=50, y=100, width=200, height=40)
            button_AddItem.bind('<Button-1>', lambda event: self.draw_item_create_new_window(idtypeitem))

        # Картинка  типа статьи
        time_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('section_image'))
        time_paint.place(x=820, y=75)

    def button_item(self, DATA, COLOR, X, Y):
        """ Кнопка настройки статьи """
        button_Item = tk.Button(self.frameMain, text=DATA[2], bg=COLOR, font="Arial 12", foreground="#F5F5F5")
        button_Item.place(x=X, y=Y, width=200, height=40)
        button_Item.bind('<Button-1>', lambda eventbutton: self.draw_item_correct_window(DATA))

        if DATA[1] == 3 or DATA[1] == 4 or DATA[1] == 5 or DATA[1] == 6 or DATA[1] == 7 or DATA[1] == 8:
            tex = get_string_from_number(DATA[6])
            sumItem = tk.Label(self.frameMain, text=tex, bg="#A9A9A9", foreground="#F5F5F5", font="Arial 12")
            sumItem.place(x=X + 205, y=Y, width=150, height=40)

    # ****************************** СТРАНИЦЫ СОЗДАНИЯ И ИЗМЕНЕНИЯ СТАТЬИ *******************************************
    def draw_item_create_new_window(self, idtypeitem):
        """ Окно создания новой статьи """
        if len(self.fc.fm.request_select_DB('*', 'items', 'typeitem_id={} AND workingitem=1'.format(idtypeitem))) >= 20:
            mb.showerror("Ошибка", "Рабочих статей на может быть больше 20\n"
                                   "Удалите или закрой неиспользуемые статьи")
            return

        self.fc.current_window = TypesWindows.itemCreateNewWindow
        self.clear_main_frame()

        if not self.fc.bufferList:
            # Установка заначений в буферном динамическим массиве
            self.fc.bufferList = [idtypeitem, '', 1, '', 0, 0, ViewWindows.get_number_image_section(idtypeitem)]
        self.update_dict_active_images(self.fc.bufferList[6])

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda event: self.fc.do_back_ward(idtypeitem))

        # Наименование страницы
        nametypeitem = self.define_text_and_color(idtypeitem)[0]
        texthead = 'Настройка/{}/Создание новой статьи:'.format(nametypeitem)
        l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        # Картинка статьи
        time_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('section_image'))
        time_paint.place(x=820, y=75)

        # Поле ввода наименования статьи
        l1 = tk.Label(self.frameMain, text="Наименование статьи:", bg="black", foreground="#ccc", font="Arial 20")
        l1.place(x=50, y=60)

        if self.fc.bufferList[1] == '':
            tex1 = 'Новая статья'
        else:
            tex1 = self.fc.bufferList[1]
        button_NameItem = tk.Button(self.frameMain, text=tex1, name='button_Name',
                                    font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_NameItem.place(x=50, y=100, width=700, height=50)

        Data1 = (0, 50, 100, 700, 40, tex1, 'button_Name', 'Arial 14', '#A9A9A9', '#F5F5F5', '', 0)
        button_NameItem.bind('<Button-1>', lambda event: self.open_field_for_change_data(Data1))

        # Кнопка редактирования суммы
        if idtypeitem != 1 and idtypeitem != 2:
            l3 = tk.Label(self.frameMain, text="Начальный остаток:", bg="black", foreground="#ccc", font="Arial 20")
            l3.place(x=50, y=160)

            tex3 = get_string_from_number(self.fc.bufferList[5])
            button_SumItem = tk.Button(self.frameMain, text=tex3, name='button_Sum', font="Arial 14", bg="#A9A9A9",
                                       foreground="#F5F5F5")
            button_SumItem.place(x=50, y=200, width=300, height=40)
            Data3 = (2, 50, 200, 300, 40, tex3, 'button_Sum', 'Arial 14', '#A9A9A9', '#F5F5F5', tex3, 0)
            button_SumItem.bind('<Button-1>', lambda event: self.open_field_for_change_data(Data3))

        # Кнопка изменения картинки для статьи
        button_Image = tk.Button(self.frameMain, name='button_Date', text='Картинка', bg='#708090', font="Arial 25",
                                 foreground="#F5F5F5")
        button_Image.place(x=450, y=200, width=300, height=40)
        button_Image.bind('<Button-1>', lambda event: self.select_image_window('NEW', idtypeitem,
                                                                               self.fc.bufferList[6]))

        # Поле ввода описания статьи
        l4 = tk.Label(self.frameMain, text="Описание статьи:", bg="black", foreground="#ccc", font="Arial 20")
        l4.place(x=50, y=260)

        if self.fc.bufferList[3] == '':
            tex4 = 'Описание новой статьи'
        else:
            tex4 = self.fc.bufferList[3]
        button_DescriptionItem = tk.Button(self.frameMain, text=tex4, name='button_Description', wraplength=680,
                                           font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_DescriptionItem.place(x=50, y=300, width=700, height=40)
        Data4 = (3, 50, 300, 700, 50, tex4, 'button_Description', 'Arial 14', '#A9A9A9', '#F5F5F5', '', 0)
        button_DescriptionItem.bind('<Button-1>', lambda event: self.open_field_for_change_data(Data4))

        # Кнопка назначения кредитной картой
        if idtypeitem == 7:
            texcredit = ''
            if self.fc.bufferList[4] == 0:
                texcredit = 'Не  кредитная карта'
            elif self.fc.bufferList[4] == 1:
                texcredit = 'Кредитная карта'

            button_Credit = tk.Button(self.frameMain, text=texcredit, name='button_Credit', font="Arial 14",
                                      bg="#696969", foreground="#F5F5F5")
            button_Credit.place(x=50, y=370, width=200, height=40)
            button_Credit.bind('<Button-1>', lambda event: self.credit_item_switch())

            # Информация о смысле назначить статью кредитной картой
            info_paint2 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('info_img'))
            info_paint2.place(x=270, y=367)
            texinfo = "Кредитная карта будет добавлена в список кошельков\nдля быстого выбора при оплате расходов"
            l5 = tk.Label(self.frameMain, text=texinfo, bg="black", foreground="#ccc", font="Arial 14", justify='left')
            l5.place(x=320, y=365)

        # Кнопка сохранения новой  статьи
        button_SaveItem = tk.Button(self.frameMain, text='Сохранить', name='button_Save', font="Arial 14", bg="#708090",
                                    foreground="#F5F5F5")
        button_SaveItem.place(x=50, y=600, width=200, height=40)
        button_SaveItem.bind('<Button-1>', lambda event: self.fc.save_new_item())

    def draw_item_correct_window(self, DATA):
        """ Окно корректировки статьи """
        self.fc.current_window = TypesWindows.correctItemWindow
        self.clear_main_frame()
        self.update_dict_active_images(DATA[8])

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black')
        button_back.place(x=0, y=0)
        button_back.bind('<Button-1>', lambda eventbutton: self.fc.do_back_ward(DATA[1]))

        # Наименование страницы
        TextAndColor = self.define_text_and_color(DATA[1])
        texthead = 'Настройка/{}/Корректировка статьи:'.format(TextAndColor[0])
        l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        # Картинка статьи
        time_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('section_image'))
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
        button_NameItem.bind('<Button-1>', lambda eventbutton: self.open_field_for_change_data(Data1))

        # Кнопка редактирования суммы
        if DATA[1] != 1 and DATA[1] != 2:
            l3 = tk.Label(self.frameMain, text="Начальный остаток:", bg="black", foreground="#ccc", font="Arial 20")
            l3.place(x=50, y=160)
            tex3 = get_string_from_number(DATA[6])
            tex33 = '{0:.2f}'.format(DATA[6])
            button_SumItem = tk.Button(self.frameMain, text=tex3, name='button_Sum', font="Arial 14", bg="#A9A9A9",
                                       foreground="#F5F5F5")
            button_SumItem.place(x=50, y=200, width=300, height=40)
            Data3 = (2, 50, 200, 300, 40, tex3, 'button_Sum', 'Arial 14', '#A9A9A9', '#F5F5F5', tex33, DATA[0])
            button_SumItem.bind('<Button-1>', lambda eventbutton: self.open_field_for_change_data(Data3))

        # Кнопка изменения картинки для статьи
        button_Image = tk.Button(self.frameMain, name='button_Date', text='Картинка', bg='#708090', font="Arial 25",
                                 foreground="#F5F5F5")
        button_Image.place(x=450, y=200, width=300, height=40)
        button_Image.bind('<Button-1>', lambda event: self.select_image_window('CORRECTION', DATA, DATA[8]))

        # Поле ввода описания статьи
        l4 = tk.Label(self.frameMain, text="Описание статьи:", bg="black", foreground="#ccc", font="Arial 20")
        l4.place(x=50, y=260)
        tex4 = DATA[4]
        button_DescriptionItem = tk.Button(self.frameMain, text=tex4, name='button_Description', wraplength=680,
                                           font="Arial 14", bg="#A9A9A9", foreground="#F5F5F5")
        button_DescriptionItem.place(x=50, y=300, width=700, height=50)
        Data4 = (3, 50, 300, 700, 50, tex4, 'button_Description', 'Arial 14', '#A9A9A9', '#F5F5F5', tex4, DATA[0])
        button_DescriptionItem.bind('<Button-1>', lambda eventbutton: self.open_field_for_change_data(Data4))

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
            button_Credit.bind('<Button-1>', lambda event: self.credit_item_switch(DATA[0]))

            # Информация о смысле назначить статью кредитной картой
            info_paint2 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('info_img'))
            info_paint2.place(x=270, y=367)
            texinfo = "Кредитная карта будет добавлена в список кошельков\nдля быстого выбора при оплате расходов"
            l5 = tk.Label(self.frameMain, text=texinfo, bg="black", foreground="#ccc", font="Arial 14", justify='left')
            l5.place(x=320, y=365)

        if self.fc.fm.use != 0:
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
            button_Close.bind('<Button-1>', lambda event: self.fc.close_item_switch(DATA[0]))

            # Информация о смысле назначить статью кредитной картой
            info_paint3 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('info_img'))
            info_paint3.place(x=270, y=477)
            texinfo = "Закрытую статью нельзя выбрать\nпри созданиии и корректировке данных"
            l7 = tk.Label(self.frameMain, text=texinfo, bg="black", foreground="#ccc", font="Arial 14", justify='left')
            l7.place(x=320, y=475)

        if DATA[9] == 1:
            # Кнопка удаления статьи
            button_DeleteItem = tk.Button(self.frameMain, text='Удалить', name='button_Delete',
                                          font="Arial 14", bg="#FF0000", foreground="#F5F5F5")
            button_DeleteItem.place(x=50, y=600, width=200, height=40)
            button_DeleteItem.bind('<Button-1>', lambda event: self.ask_question_item(DATA))
        elif DATA[9] == 0:
            label_StartItem = tk.Label(self.frameMain, text='Не удалить', font="Arial 14", bg="#5F9EA0",
                                       foreground="#F5F5F5")
            label_StartItem.place(x=50, y=600, width=200, height=40)

    def ask_question_item(self, DATA):
        """ Вопрос об удалении статьи"""
        notes = list()
        if self.fc.fm.use == 1:
            notes = self.fc.fm.request_select_DB('*', 'notes', 'item_id={} OR source={}'.format(DATA[0], DATA[0]))

        if not notes:
            # Очищаем страницу
            self.clear_main_frame()

            # Наименование страницы
            TextAndColor = self.define_text_and_color(DATA[1])
            texthead = 'Настройка/{}/Удаление статьи:'.format(TextAndColor[0])
            l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
            l0.place(x=50, y=0)

            # Картинка часового механизма
            time_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('time_img'))
            time_paint.place(x=820, y=75)

            # Надпись с вопросом
            textQuestion = 'Удалить статью: {}?\nВосстановление статьи невозможно'.format(DATA[2])
            lQuestion = tk.Label(self.frameMain, text=textQuestion, bg='black', foreground="#ccc", font="Arial 16",
                                 justify='center')
            lQuestion.place(x=100, y=150, width=600, height=70)

            # Кнопка подтверждения
            buttonYes = tk.Button(self.frameMain, text='ДА', font="Arial 16", bg="#708090", foreground="#F5F5F5")
            buttonYes.place(x=320, y=250, width=80, height=40)
            buttonYes.bind('<Button-1>', lambda eventbutton: self.fc.delete_item(DATA))

            # Кнопка отмены
            buttonNo = tk.Button(self.frameMain, text='НЕТ', font="Arial 12", bg="#708090", foreground="#F5F5F5")
            buttonNo.place(x=420, y=250, width=80, height=40)
            buttonNo.bind('<Button-1>', lambda eventbutton: self.draw_item_correct_window(DATA))

            # Картинка с шредером
            shreder_paint = tk.Label(self.frameMain, bg='black', image=self.active_images.get('shreder_img'))
            shreder_paint.place(x=200, y=320)
        else:
            mb.showerror("Ошибка", "Нельзя удалить статью, содержащую записи об операциях, удалите все записи!!!")

    def select_image_window(self, TYPE, DATAITEM, IND=100):
        """ Страница выбора картинки статьи """
        self.clear_main_frame()
        self.fc.current_window = TypesWindows.selectImageWindow
        self.update_dict_active_images()

        # Кнопка назад
        button_back = tk.Button(self.frameMain, image=self.active_images.get('back_img'), bg='black')
        button_back.place(x=0, y=0)
        if TYPE == 'NEW':
            button_back.bind('<Button-1>', lambda eventbutton: self.draw_item_create_new_window(DATAITEM))
        elif TYPE == 'CORRECTION':
            button_back.bind('<Button-1>', lambda eventbutton: self.draw_item_correct_window(DATAITEM))

        # Наименование страницы
        if TYPE == 'NEW':
            TextAndColor = self.define_text_and_color(DATAITEM)
        else:
            TextAndColor = self.define_text_and_color(DATAITEM[1])

        texthead = 'Настройка/{}/Выбор изображения:'.format(TextAndColor[0])
        l0 = tk.Label(self.frameMain, text=texthead, bg="black", foreground="#ccc", font="Arial 25")
        l0.place(x=50, y=0)

        countImage = len(self.active_images.get('image_setting_list'))

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

        # Картинки слева
        l_paint1 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('image_setting_list')[listInd[5]])
        l_paint1.place(x=0, y=110)

        l_paint2 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('image_setting_list')[listInd[3]])
        l_paint2.place(x=140, y=105)

        l_paint3 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('image_setting_list')[listInd[1]])
        l_paint3.place(x=280, y=100)

        # Картинки справа
        l_paint4 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('image_setting_list')[listInd[4]])
        l_paint4.place(x=840, y=40)

        l_paint5 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('image_setting_list')[listInd[2]])
        l_paint5.place(x=700, y=45)

        l_paint6 = tk.Label(self.frameMain, bg='black', image=self.active_images.get('image_setting_list')[listInd[0]])
        l_paint6.place(x=560, y=50)

        # Кнопка выбора
        button_image = tk.Button(self.frameMain, image=self.active_images.get('image_setting_list')[numberImageItem],
                                 bg='black')
        button_image.place(x=420, y=75, width=440, height=600)
        button_image.bind('<Button-1>', lambda eventbutton: self.button_image_item(TYPE, numberImageItem, DATAITEM))

        # Блок постраничного пейджинга
        pagetext = '{} из {}'.format(numberImageItem + 1, countImage)
        # Кнопка перелистывания страниц влево
        buttonPageLeft = tk.Button(self.frameMain, name='page_Left', background="black",
                                   image=self.active_images.get('arrowLeft_img'))
        buttonPageLeft.place(x=535, y=680, width=40, height=40)
        buttonPageLeft.bind('<Button-1>',
                            lambda eventbutton: self.select_image_window(TYPE, DATAITEM, numberImageItem - 1))

        # Счетчик страниц
        lPageCounter = tk.Label(self.frameMain, name='page_Counter', text=pagetext, bg="#808080", foreground="#ccc",
                                font="Arial 12")
        lPageCounter.place(x=580, y=680, width=100, height=40)

        # Кнопка перелистывания страниц вправо
        buttonPageRight = tk.Button(self.frameMain, name='page_Right', background="black",
                                    image=self.active_images.get('arrowRight_img'))
        buttonPageRight.place(x=685, y=680, width=40, height=40)
        buttonPageRight.bind('<Button-1>',
                             lambda eventbutton: self.select_image_window(TYPE, DATAITEM, numberImageItem + 1))

    def button_image_item(self, TYPE, IND, DATAITEM):
        """ Кнопка картинка выбора изображения для статьи """
        if TYPE == 'NEW':
            self.fc.bufferList[6] = IND
            self.draw_item_create_new_window(DATAITEM)
        elif TYPE == 'CORRECTION':
            self.fc.fm.update_note_DB('items', 'paintitem', 'id', IND, DATAITEM[0])
            DATAITEM = self.fc.fm.request_select_DB('*', 'items', 'id={}'.format(DATAITEM[0]))[0]
            self.draw_item_correct_window(DATAITEM)

    def close_item_switch(self, IDITEM):
        """ Закрытие статьи - статья не подбирается при создании """
        DATA = self.fc.fm.request_select_DB('*', 'items', 'id={}'.format(IDITEM))[0]
        LIST = self.fc.fm.request_select_DB('*', 'items', 'typeitem_id={} AND workingitem=1'.format(DATA[1]))

        if DATA[3] == 0 and len(LIST) >= 20:
            mb.showerror("Ошибка", "Рабочих статей на может быть больше 20\n"
                                   "Удалите или закрой неиспользуемые статьи")
            return

        TextAndColor = self.define_text_and_color(DATA[1])
        listobject = self.frameMain.place_slaves()
        for obj in listobject:
            if obj.winfo_name() == 'button_Close':
                if DATA[3] == 0:
                    obj.config(text='Рабочая статья', bg=TextAndColor[1])
                    self.fc.fm.update_note_DB('items', 'workingitem', 'id', 1, DATA[0])
                elif DATA[3] == 1:
                    obj.config(text='Закрытая статья', bg="#696969")
                    self.fc.fm.update_note_DB('items', 'workingitem', 'id', 0, DATA[0])

    def credit_item_switch(self, IDITEM=1):
        """ Переключение значения Кредитная карта """
        listobject = self.frameMain.place_slaves()
        for obj in listobject:
            if obj.winfo_name() == 'button_Credit':
                if self.fc.current_window == TypesWindows.itemCreateNewWindow:
                    if self.fc.bufferList[4] == 0:
                        obj.config(text='Кредитная карта', bg="#DA70D6")
                        self.fc.bufferList[4] = 1
                    elif self.fc.bufferList[4] == 1:
                        obj.config(text='Не  кредитная карта', bg="#696969")
                        self.fc.bufferList[4] = 0
                elif self.fc.current_window == TypesWindows.correctItemWindow:
                    DATA = self.fc.fm.request_select_DB('*', 'items', 'id={}'.format(IDITEM))[0]
                    if DATA[5] == 0:
                        obj.config(text='Кредитная карта', bg="#DA70D6")
                        self.fc.fm.update_note_DB('items', 'creditcard', 'id', 1, DATA[0])
                    elif DATA[5] == 1:
                        obj.config(text='Не  кредитная карта', bg="#696969")
                        self.fc.fm.update_note_DB('items', 'creditcard', 'id', 0, DATA[0])
