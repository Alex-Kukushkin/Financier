import Assets.PythonScripts.FinancierModels as FM
import Assets.PythonScripts.FinancierView as FV
from tkinter import messagebox as mb
import datetime as dt
from datetime import timedelta
import calendar
import os.path as op


class FinancierControls:
    def __init__(self, root):
        self.root = root
        # Хранилище данных заполняемых полей
        self.bufferList = dict()
        self.section = 0

        # Ссылка на экземпляр класса Баз данных/ инициилизация экземпляра класса Баз данных
        self.fm = FM.DataBases()

        # Текущая страница
        self.current_window = FV.TypesWindows.passwordWindow
        # Предыдущая страница
        self.previous_window = FV.TypesWindows.passwordWindow
        # Настройка фильтра списков
        self.__setting_filter = {'currentPage': 1, 'countPage': 1, 'period': 'AllPeriod',
                                 'beginDate': self.fm.beginDate, 'endDate': dt.date(2200, 12, 31)}
        # Ссылка на экземпляр класса Отрисовки/ инициилизация экземпляра класса Отрисовки
        self.fv = FV.ViewWindows(root, self)

        # Словарь возможных значений элементов на диалоге операций
        self.list_dict_values_payment_states = {
            'default': {'textitem': '', 'textwallet': '', 'icon': 'arrowGreenRight_img', 'increase': 0},
            # 1. Получена зп на карту/Получен доход наличными/Получена прибыль от продажи имущества, акциями/
            # Подарены деньги, имущество
            'operation_1': {'textitem': 'Статья дохода', 'textwallet': 'Статья пополнения',
                            'icon': 'arrowGreenRight_img', 'increase': 2},

            # 2. Списан выданный займ, кредит
            'operation_2': {'textitem': 'Статья дохода:', 'textwallet': 'Статья списания:',
                            'icon': 'arrowDoubleRed_img', 'increase': 3},

            # 3. Покупка за наличные/Потеряны деньги/Списано имущество/Списана отрицательная курсовая разница/
            # Получен убыток от продажи имущества
            'operation_3': {'textitem': 'Статья расхода:', 'textwallet': 'Статья списания:',
                            'icon': 'arrowGreenLeft_img', 'increase': 1},

            # 4. Покупка по кредитной карте, покупка в кредит
            'operation_4': {'textitem': 'Статья расхода:', 'textwallet': 'Статья пополнения:',
                            'icon': 'arrowDoubleGreen_img', 'increase': 2},

            # 5. Получен кредит(займ) наличными, на авто, имущество
            'operation_5': {'textitem': 'Статья пополнения:', 'textwallet': 'Статья пополнения:',
                            'icon': 'arrowDoubleGreen_img', 'increase': 2},

            # 6. Снятие наличных/переуступка выданного займа с одного заёмщика на другого
            # 7. Пополнение карты, поступление денежных средств от продажи имущества
            # 8. Переуступка выданного займа с одного кредитора на другого
            # 9.  Рефинансирование
            'operation_6': {'textitem': 'Статья пополнения:', 'textwallet': 'Статья списания:',
                            'icon': 'arrowGreenLeft_img', 'increase': 1},

            # 6. Снятие наличных/переуступка выданного займа с одного заёмщика на другого
            # 7. Пополнение карты, поступление денежных средств от продажи имущества
            # 8. Переуступка выданного займа с одного кредитора на другого
            # 9.  Рефинансирование
            'operation_7': {'textitem': 'Статья списания:', 'textwallet': 'Статья пополнения:',
                            'icon': 'arrowRedRight_img', 'increase': 0},

            # 10. Погашен кредит(займ) наличными,  авто, имуществом, полученный займ погашен выданным
            # 2. Списан выданный займ, кредит
            'operation_8': {'textitem': 'Статья списания:', 'textwallet': 'Статья списания:',
                            'icon': 'arrowDoubleRed_img', 'increase': 3},
        }

    # ****************************** ОБЩИЕ СОБЫТИЯ И МЕТОДЫ *******************************************
    def entrance_action(self, password):
        """ Переход после ввода верного пароля на страницу стартовых настроек если программа не активирована
        или на основную страницу, если активирована """
        data = self.fm.request_select_DB('parol', 'setting')
        passworddb = data[0][0]

        if passworddb == password:
            print('OK! Пароль верен, осуществлен вход в программу')
            if self.fm.use == 0:
                # Работа не начата, переходим в окно настройки системы для начала работы
                self.fv.setting_window()
            else:
                # Работа начата, переходим в основное окно программы
                self.fv.main_window()
        else:
            mb.showerror("Ошибка", "Введен неверный пароль")

    def do_back_ward(self, section=1):
        """" Метод возврата в на предыдущую страницу """
        # Сбрасываем настройку фильтра
        self.set_default_filter()
        # Очищаем буферный массив
        self.bufferList = dict()

        if self.current_window == FV.TypesWindows.listItemSettingWindow:
            self.fv.setting_window()
        elif self.current_window == FV.TypesWindows.correctItemWindow or \
                self.current_window == FV.TypesWindows.itemCreateNewWindow:
            self.fv.list_item_setting_window(section)
        elif self.current_window == FV.TypesWindows.settingWindow:
            self.fv.menu_window()
        elif self.current_window == FV.TypesWindows.menuWindow:
            if self.previous_window == FV.TypesWindows.mainWindow:
                self.fv.main_window()
            elif self.previous_window == FV.TypesWindows.listItemForEnterDataWindow:
                self.fv.draw_list_item_for_enter_data_window(section)
            elif self.previous_window == FV.TypesWindows.listDataInItemWindow:
                self.fv.draw_list_item_for_enter_data_window(section)
            elif self.previous_window == FV.TypesWindows.correctItemWindow:
                self.fv.setting_window()
        elif self.current_window == FV.TypesWindows.listItemForEnterDataWindow:
            self.fv.main_window()
        elif self.current_window == FV.TypesWindows.listDataInItemWindow or \
                self.current_window == FV.TypesWindows.dataCreateNewWindow:
            self.fv.draw_list_item_for_enter_data_window(section)
        elif self.current_window == FV.TypesWindows.dataCorrectWindow:
            self.fv.draw_list_operations_in_item_window(section)
        elif self.current_window == FV.TypesWindows.dataCreateNewWindowCopy:
            self.fv.draw_list_operations_in_item_window(section)
        elif self.current_window == FV.TypesWindows.reportWindow:
            self.fv.main_window()

    def exit_the_program(self):
        """ Выход из программы """
        self.root.quit()

    def enter_data_in_input_field(self, DATA, NewData):
        """ Ввод  данных в поле ввода
        # DATA - кортеж: 0 - номер (тип) поля ввода, 1 - х, 2 - у, 3 - width, 4 - height,
        # 5 - text, 6 - name, 7 - font, 8 - bg, 9 - foreground, 10 - значение для корректировки,
        # 11 - новая(0)/текущая == id статьи

        # 0 -строка - Наименование статьи, 1 - дата, 2- число, 3 - строка - описание статьи   """

        dateNew = ''
        NewData1 = ''
        try:
            # Поле ввода даты
            if DATA[0] == 1:
                dateNew = dt.datetime.strptime(NewData, '%d.%m.%Y').date()
                NewData = dt.date.strftime(dateNew, '%d.%m.%Y')
                NewData1 = NewData
            # Поле ввода суммы в рублях и копейках
            elif DATA[0] == 2:
                dateNew = round(float(NewData), 2)
                NewData1 = FV.get_string_from_number(dateNew)
                NewData = '{0:.2f}'.format(dateNew)
            # Поле ввода текста
            elif DATA[0] == 0 or DATA[0 == 4]:
                dateNew = NewData
                NewData1 = NewData

            # Удаление поля ввода и кнопок
            listobject = self.fv.frameMain.place_slaves()
            for obj in listobject:
                if obj.winfo_name() == 'entry_DATA' or obj.winfo_name() == 'button_DataOK' or \
                        obj.winfo_name() == 'button_DataNO':
                    obj.destroy()

            # Корректируем существующую запись статьи
            if DATA[11] != 0:
                # Корректировка данных по статям в базе данных
                if self.current_window == FV.TypesWindows.correctItemWindow:
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
                    self.fm.update_note_DB(database, field, idname, dateNew, DATA[11])
                else:
                    mb.showerror("Ошибка", "При вводе значений в поле ввода ничего не произошло\n" +
                                 "Ошибка условий в методе enter_data_in_input_field")

            # Изменение значения поля при создании новой записи и корректировки операции
            elif DATA[11] == 0:
                # Изменение значения поля при создании новой статьи
                if self.current_window == FV.TypesWindows.itemCreateNewWindow:
                    if DATA[0] == 1:
                        self.bufferList[2] = dateNew
                    elif DATA[0] == 2:
                        self.bufferList[5] = dateNew
                    elif DATA[0] == 0:
                        self.bufferList[1] = dateNew
                    elif DATA[0 == 3]:
                        self.bufferList[3] = dateNew
                # Изменение значение поля при создании новой, скопированной, корректировки существующей операции
                elif self.current_window == FV.TypesWindows.dataCreateNewWindow or \
                        self.current_window == FV.TypesWindows.dataCorrectWindow or \
                        self.current_window == FV.TypesWindows.dataCreateNewWindowCopy:
                    if DATA[0] == 1:
                        self.bufferList['dateoperationkey'] = dateNew
                    elif DATA[0] == 2:
                        self.bufferList['sumoperationkey'] = dateNew
                    elif DATA[0 == 3]:
                        self.bufferList['descriptionkey'] = dateNew

                # Изменение даты начала учета на странице настроек
                elif self.current_window == FV.TypesWindows.settingWindow:
                    # Запрет на изменение даты начала учета на дату больше даты самой ранней операции
                    if op.exists('notes.db'):
                        # Запрос массива дат операций
                        data2 = self.fm.request_select_DB('dateoperation', 'notes')

                        for i in data2:
                            dateOperations = dt.datetime.strptime(i[0], '%Y-%m-%d').date()
                            if dateOperations < dateNew:
                                mb.showerror("Ошибка", "Есть операции с более ранними датами, чем новая дата начала "
                                                       "учета. Измените их")
                                break

                    listobject = self.fv.frameMain.place_slaves()
                    for obj in listobject:
                        if obj.winfo_name() == 'entry_date' or obj.winfo_name() == 'button_dateOK' or \
                                obj.winfo_name() == 'button_dateNo':
                            obj.destroy()
                    if self.fm.beginDate != dateNew:
                        self.fm.beginDate = dateNew
                        # Внесение новой даты в файл настроек
                        self.fm.update_note_DB('setting', 'date', 'id', self.fm.beginDate, 1)

                else:
                    mb.showerror("Ошибка", "При вводе значений в поле ввода ничего не произошло\n" +
                                 "Ошибка условий в методе enter_data_in_input_field")

            # Сборка нового кортежа и создание кнопки
            DATA1 = (DATA[0], DATA[1], DATA[2], DATA[3], DATA[4], NewData1, DATA[6], DATA[7], DATA[8], DATA[9], NewData,
                     DATA[11])
            self.fv.create_button_after_entering_data(NewData1, DATA1)

        except ValueError:
            if DATA[0] == 1:
                mb.showerror("Ошибка", "Дата должна быть в формате ДД.ММ.ГГГГ")
            elif DATA[0] == 2:
                mb.showerror("Ошибка", "Должно быть введено число")

    # ****************************** СОБЫТИЯ И МЕТОДЫ ДЛЯ РАБОТЫ С ОПЕРАЦИЯМИ **************************************
    def get_value_increase_and_payment_states(self, id_type_item, id_type_wallet, old_increase=None):
        """ Вычисляет значения increase, надписи над статьей и кошельком, и ключ к иконке на основании значений
         типа статей статьи и кошелька из операции, и старой статьи при смене increase
         old_increase=None - устанавливается дефолтное значение словаря на увеличение статьи

        Xарактер приращения/уменьшения статей INCREACE:
        0 - левая уменьшается, правая увеличивается
        1 - левая увеличивается, правая уменьшается
        2 - обе увеличиваются
        3 - обе уменьшаются) """
        dict_payment_states = dict()
        if id_type_item == 1:
            if id_type_wallet in (3, 4, 5, 6):
                dict_payment_states = self.list_dict_values_payment_states.get('operation_1')
            elif id_type_wallet in (7, 8):
                dict_payment_states = self.list_dict_values_payment_states.get('operation_2')

        elif id_type_item == 2:
            if id_type_wallet in (3, 4, 5, 6):
                dict_payment_states = self.list_dict_values_payment_states.get('operation_3')
            elif id_type_wallet in (7, 8):
                dict_payment_states = self.list_dict_values_payment_states.get('operation_4')

        elif id_type_item in (7, 8):
            if id_type_wallet in (3, 4, 5, 6):
                if old_increase in (3, 0, None):
                    dict_payment_states = self.list_dict_values_payment_states.get('operation_5')
                elif old_increase in (2, 1):
                    dict_payment_states = self.list_dict_values_payment_states.get('operation_8')

            elif id_type_wallet in (7, 8):
                if old_increase in (0, 3, None):
                    dict_payment_states = self.list_dict_values_payment_states.get('operation_6')
                elif old_increase in (2, 1):
                    dict_payment_states = self.list_dict_values_payment_states.get('operation_7')

        elif id_type_item in (3, 4, 5, 6):
            if id_type_wallet in (3, 4, 5, 6):
                if old_increase in (0, 3, None):
                    dict_payment_states = self.list_dict_values_payment_states.get('operation_6')
                elif old_increase in (2, 1):
                    dict_payment_states = self.list_dict_values_payment_states.get('operation_7')

            elif id_type_wallet in (7, 8):
                if old_increase in (3, 0, None):
                    dict_payment_states = self.list_dict_values_payment_states.get('operation_5')
                elif old_increase in (2, 1):
                    dict_payment_states = self.list_dict_values_payment_states.get('operation_8')

        return dict_payment_states

    def prepare_data_for_rendering_operation(self, TYPEOPERATIONS, DATAITEM, NOTE=()):
        """ Готовит данные для отрисовки данных при открытии страницы операции.
            Заполняет буферный массив данными по новой операции при создании или копировании,
            заполняет буферный массив данными по существующей операции при изменении;
            извлекает значения increase, надписи над статьей и кошельком, и ключ к иконке

        # TYPEOPERATIONS: "NEW", 'COPY', 'CORRECTION'
        # Установка заначений в буферном словаре
        # [0"iditemkey"] - id статьи; [1"idtypeitemkey"] - id статьи; [2'dateoperationkey'] - дата операции;
        # [3'descriptionkey'] - Описание операции; # [4'sumoperationkey'] - сумма операции;
        # [5'increasekey'] - Направление (Уменьшение/Увеличение);
        # [6'sourcekey'] - Источник пополнения/ Изъятия(id статьи);
        # [7'typeinvestmentidkey'] - тип вложений (id типа вложений);
        # [8'countnotekey'] - количество вложений; [9'priseunit'] - цена единицы вложений """

        # Извлекаемый словарь
        values_payment_states = dict()

        if TYPEOPERATIONS == "NEW" and not self.bufferList:
            # Запрос к БД на id кошелька
            wallet = self.search_suitable_wallet(DATAITEM)

            if not wallet:
                idwallet = 0
                values_payment_states = self.list_dict_values_payment_states.get('default')
            else:
                idtypewallet = wallet[1]
                idwallet = wallet[0]
                values_payment_states = self.get_value_increase_and_payment_states(DATAITEM[1], idtypewallet)

            # Если bufferList пустой, устанавливаем значения
            if not self.bufferList:
                self.bufferList = {
                    'iditemkey': DATAITEM[0], 'idtypeitemkey': DATAITEM[1],
                    'dateoperationkey': self.fm.todayDate, 'descriptionkey': '', 'sumoperationkey': 0,
                    'increasekey': values_payment_states.get('increase'),
                    'sourcekey': idwallet, 'typeinvestmentidkey': None, 'countnotekey': 0, 'priseunit': 0
                }

        elif TYPEOPERATIONS == 'COPY' or TYPEOPERATIONS == 'CORRECTION' or \
                (TYPEOPERATIONS == "NEW" and self.bufferList):
            # Если bufferList пустой, устанавливаем значения
            if not self.bufferList:
                self.bufferList = {
                    'iditemkey': NOTE[1], 'idtypeitemkey': NOTE[2], 'dateoperationkey': NOTE[3],
                    'descriptionkey': NOTE[4], 'sumoperationkey': NOTE[5], 'increasekey': NOTE[6],
                    'sourcekey': NOTE[7], 'typeinvestmentidkey': None, 'countnotekey': 0, 'priseunit': 0
                }
                if TYPEOPERATIONS == 'COPY':
                    self.bufferList['dateoperationkey'] = self.fm.todayDate

            # Определяем раздел кошелька
            idtypeitemsourse = self.fm.request_select_DB('typeitem_id', 'items', 'id={}'.format(
                self.bufferList['sourcekey']))

            if idtypeitemsourse:
                idtypeitemsourse = idtypeitemsourse[0][0]
                values_payment_states = self.get_value_increase_and_payment_states(DATAITEM[1], idtypeitemsourse)

        return values_payment_states

    def switch_increase_decrease_mode(self):
        """Переключение режима уменьшения/увеличения статьи"""
        # Запрос ID раздела кошелька
        idtypeitemsourse = self.fm.request_select_DB('typeitem_id', 'items', 'id={}'.format(
            self.bufferList.get('sourcekey')))
        if idtypeitemsourse:
            idtypeitemsourse = idtypeitemsourse[0][0]
            dict_field1 = self.get_value_increase_and_payment_states(
                self.bufferList.get('idtypeitemkey'), idtypeitemsourse, old_increase=self.bufferList.get('increasekey'))

            # Перебираем элементы страницы и устанавливливаем новые свойства
            self.fv.install_new_values_after_change_increase(dict_field1)

            # Устанавливаем новое значение приращение статьи increase
            self.bufferList['increasekey'] = dict_field1.get('increase')

    def switch_wallet(self, side, DATAITEM):
        """ Изменение кошелька при переключении по стрелочкам на диалоге операции """
        # Берем из буферного массива ID текущего кошелька
        currentwallet = self.bufferList.get('sourcekey')

        # Запрос к БД на массив кошельков
        wallets = self.search_other_wallets(DATAITEM[1])

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
            self.bufferList['sourcekey'] = newwallet

            # Устанавливаем кнопки направления операции и описание кошелька на фрейме
            dict_field = self.get_value_increase_and_payment_states(DATAITEM[1], wallets[ind][1])

            # Изменяем наименование текущего кошелька, кнопки направления операции и описание кошелька на фрейме
            self.fv.install_new_values_after_change_increase(dict_field, wallets[ind][2])

            # Устанавливаем новое значение приращение статьи increase
            self.bufferList['increasekey'] = dict_field.get('increase')

    def search_suitable_wallet(self, DATAITEM):
        """" Извлечение подходящего кошелька для создания операции """
        # Запрос к БД на id последнего использовавшегося кошелька из настроек
        idwallet = self.fm.request_select_DB('*', 'setting')[0][4]
        wallet = self.fm.request_select_DB('*', 'items', 'id={}'.format(idwallet))

        # Если не нашли такой кошелёк в БД, или кошелёк не рабочий - ищем другой
        if not wallet and wallet[0][3] == 0:
            wallet = self.search_other_wallets(DATAITEM[1])

        # Нашли кошелёк
        if wallet:
            wallet = wallet[0]
            # Кошелёк - кредитная карта: проверяем что тип статьи - затраты, кошелёк не совпадает со статьёй
            # и кошелёк с типом кредита имеет атрибут кредитная карта
            if wallet[1] == 7:
                if DATAITEM[1] == 2 and wallet[0] != DATAITEM[0] and wallet[0][3] == 1:
                    return wallet
                elif DATAITEM[1] != 2 or wallet[0] == DATAITEM[0] or wallet[0][3] == 0:
                    wallet = self.search_other_wallets(DATAITEM[1])
                    if wallet:
                        return wallet[0]
            # Остальные кошельки: проверяем, что кошелёк не совпадает со статьёй
            else:
                if wallet[0] == DATAITEM[0]:
                    wallet = self.search_other_wallets(DATAITEM[1])
                    if wallet:
                        return wallet[0]
                else:
                    return wallet

    def search_other_wallets(self, type_item):
        """ Извлекает список кошельков, подходящих для типа статьи, или пустой кортеж, если кошельков нет  """
        if type_item == 2:
            wallets = self.fm.request_select_DB('*', 'items', 'typeitem_id=3 or (typeitem_id=7 AND creditcard=1)'
                                                              ' AND id!={} AND workingitem=1'.format(type_item))
        else:
            wallets = self.fm.request_select_DB('*', 'items', 'typeitem_id=3 AND id!={} '
                                                              'AND workingitem=1'.format(type_item))
        return wallets

    def save_new_operation(self, DATA=()):
        """ Сохранение операции """
        if self.bufferList.get('sumoperationkey') != 0 and self.bufferList.get('sourcekey') != 0:
            # Сохранение индекса нового текущего кошелька в БД
            wallets = self.fm.request_select_DB('*', 'items', '(typeitem_id=3 or (typeitem_id=7 AND creditcard=1)) '
                                                ' AND workingitem=1')
            wall = list()
            for wa in wallets:
                wall.append(wa[0])
            if self.bufferList['sourcekey'] in wall:
                self.fm.update_note_DB('setting', 'wallet', 'id', self.bufferList['sourcekey'], 1)

            # Сохранение операции
            self.fm.add_new_operation(self.bufferList)

            # Очищаем фрейм и отрисовываем список статей
            self.fv.clear_main_frame()
            if self.current_window == FV.TypesWindows.dataCreateNewWindow:
                self.do_back_ward(self.bufferList.get('idtypeitemkey'))
            elif self.current_window == FV.TypesWindows.dataCreateNewWindowCopy:
                self.do_back_ward(DATA)

            # чистим буферный словарь
            self.bufferList = dict()
        else:
            if self.bufferList['sumoperationkey'] == 0:
                mb.showerror("Ошибка", "Сумма операции должна быть заполнена и не равняться нулю!!!")
            if self.bufferList['sourcekey'] == 0:
                mb.showerror("Ошибка", "Не выбрана коррелирующая статья для  сохранения операции!!!")

    def save_changes_operation(self, DATA, NOTE):
        """ Сохранение изменений после корректировки """

        if self.bufferList['sumoperationkey'] != 0:
            # Сохранение операции
            self.fm.update_operation(self.bufferList, NOTE)

            # Очищаем фрейм и отрисовываем список статей
            self.fv.clear_main_frame()
            if self.current_window == FV.TypesWindows.dataCorrectWindow:
                self.do_back_ward(DATA)

            # чистим буферный словарь
            self.bufferList = dict()
        else:
            mb.showerror("Ошибка", "Сумма операции должна быть заполнена и не равняться нулю!!!")

    def change_page_source_item(self, change, TYPEOPERATIONS, DATAITEM, NOTE):
        """ Перелистывание страниц при нажатии кнопок навигации
        change: 'PageForward', 'PageBack'  """
        if change == 'PageForward':
            if self.setting_filter.get('currentPage') == self.setting_filter.get('countPage'):
                self.setting_filter['currentPage'] = 1
            else:
                self.setting_filter['currentPage'] += 1

        elif change == 'PageBack':
            if self.setting_filter.get('currentPage') == 1:
                self.setting_filter['currentPage'] = self.setting_filter['countPage']
            else:
                self.setting_filter['currentPage'] -= 1

        # Отрисовываем новые данные, пейджинг и фильтр
        self.fv.draw_list_item_for_to_select_wallet(TYPEOPERATIONS, DATAITEM, NOTE)

    def change_source_operation(self, TYPEOPERATIONS, DATA, DATAITEM, NOTE):
        """ Изменяем статью2 и возвращаемся обратно """
        self.fv.clear_main_frame()
        self.bufferList['sourcekey'] = DATA[0]
        self.fv.create_correct_data_window(TYPEOPERATIONS, DATAITEM, NOTE)

    def delete_operation_from_registry(self, NOTE, ITEMID):
        """Удаление записи из реестра"""
        # Удаляем запись из БД
        self.fm.delete_note_DB(NOTE)
        # Перерисовываем строки с данными
        ITEM_DATA = self.fm.request_select_DB('*', 'items', f'id={ITEMID}')[0]
        self.fv.draw_list_operations_in_item_window(ITEM_DATA)
        # Пересчет и установка остатков при удалении операции
        self.fm.recalculating_balances(NOTE[1], NOTE[7], NOTE[6], - (NOTE[5]))

    # ****************************** СОБЫТИЯ И МЕТОДЫ ДЛЯ РАБОТЫ С ФИЛЬТРОМ *******************************************
    @property
    def setting_filter(self):
        return self.__setting_filter

    @setting_filter.setter
    def setting_filter(self, current_page=1, count_page=1, period='AllPeriod', beg_date='',
                       end_date=dt.date(2200, 12, 31)):
        date = beg_date
        if beg_date == '':
            date = self.fm.beginDate

        self.__setting_filter['currentPage'] = current_page
        self.__setting_filter['countPage'] = count_page
        self.__setting_filter['period'] = period
        self.__setting_filter['beginDate'] = date
        self.__setting_filter['endDate'] = end_date

    def set_default_filter(self):
        """ Установка дефолтных настроек фильтра и роутинга в словаре SettingFilter """
        self.__setting_filter['currentPage'] = 1
        self.__setting_filter['countPage'] = 1
        self.__setting_filter['period'] = 'AllPeriod'
        self.__setting_filter['beginDate'] = self.fm.beginDate
        self.__setting_filter['endDate'] = dt.date(2200, 12, 31)

    def set_filter_text(self):
        """ Извлекает надпись для фильтра по дате в зависимости от значений в словаре SettingFilter """
        textFilter = ''
        if self.setting_filter.get('period') == 'AllPeriod':
            textFilter = 'Весь период: \n {} - ...'.format(self.setting_filter.get('beginDate').strftime('%d.%m.%Y'),
                                                           self.setting_filter.get('endDate').strftime('%d.%m.%Y'))
        elif self.setting_filter.get('period') == 'YearPeriod':
            textFilter = 'По годам: \n {} - {}'.format(self.setting_filter.get('beginDate').strftime('%d.%m.%Y'),
                                                       self.setting_filter.get('endDate').strftime('%d.%m.%Y'))
        elif self.setting_filter.get('period') == 'MonthPeriod':
            textFilter = 'По месяцам: \n {} - {}'.format(self.setting_filter.get('beginDate').strftime('%d.%m.%Y'),
                                                         self.setting_filter.get('endDate').strftime('%d.%m.%Y'))
        elif self.setting_filter.get('period') == 'WeekPeriod':
            textFilter = 'По неделям: \n {} - {}'.format(self.setting_filter.get('beginDate').strftime('%d.%m.%Y'),
                                                         self.setting_filter.get('endDate').strftime('%d.%m.%Y'))
        elif self.setting_filter.get('period') == 'DayPeriod':
            textFilter = 'По дням: \n {} - {}'.format(self.setting_filter.get('beginDate').strftime('%d.%m.%Y'),
                                                      self.setting_filter.get('endDate').strftime('%d.%m.%Y'))
        return textFilter

    def get_period_when_filter_changes(self, ChangePeriod):
        """ Вычисляем даты начала и конца периода в зависимости от смецения по периоду и изменения размеров периода.
         Изменение значений SettingFilter если период не уперся в дату начала учета """
        if ChangePeriod == 'PeriodUp' or ChangePeriod == 'PeriodDown':
            period = ''
            if ChangePeriod == 'PeriodUp':
                if self.setting_filter.get('period') == 'AllPeriod':
                    period = 'DayPeriod'
                elif self.setting_filter.get('period') == 'DayPeriod':
                    period = 'WeekPeriod'
                elif self.setting_filter.get('period') == 'WeekPeriod':
                    period = 'MonthPeriod'
                elif self.setting_filter.get('period') == 'MonthPeriod':
                    period = 'YearPeriod'
                elif self.setting_filter.get('period') == 'YearPeriod':
                    self.setting_filter['period'] = 'AllPeriod'

            elif ChangePeriod == 'PeriodDown':
                if self.setting_filter.get('period') == 'AllPeriod':
                    period = 'YearPeriod'
                elif self.setting_filter.get('period') == 'YearPeriod':
                    period = 'MonthPeriod'
                elif self.setting_filter.get('period') == 'MonthPeriod':
                    period = 'WeekPeriod'
                elif self.setting_filter.get('period') == 'WeekPeriod':
                    period = 'DayPeriod'
                elif self.setting_filter.get('period') == 'DayPeriod':
                    period = 'AllPeriod'

            # Если период меняем на "Весь период", то устанавливаем дату начала периода и условную дальнюю дату
            if period == 'AllPeriod':
                self.setting_filter['period'] = 'AllPeriod'
                self.setting_filter['beginDate'] = self.fm.beginDate
                self.setting_filter['endDate'] = dt.date(2200, 12, 31)

            # Если период меняем на Год, то устанавливаем год текущей даты, если двигаемся с "Весь период",
            # или берем год даты конца периода, если двигаемся из "Месяц"
            elif period == 'YearPeriod':
                if self.setting_filter.get('period') == 'AllPeriod':
                    self.setting_filter['beginDate'] = dt.date(self.fm.todayDate.year, 1, 1)
                    self.setting_filter['endDate'] = dt.date(self.fm.todayDate.year, 12, 31)
                elif self.setting_filter.get('period') == 'MonthPeriod':
                    self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('endDate').year, 1, 1)
                    self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year, 12, 31)
                self.setting_filter['period'] = 'YearPeriod'

            # Если период меняем на Месяц, то устанавливаем месяц текущей даты, если двигаемся с текущего года c  "Год",
            # если двигаемся с прошлых лет - то устанавливаем месяц Декабрь
            # если двигаемся с будущих лет - то устанавливаем месяц Январь
            # или берем месяц и год с даты конца периода, если двигаемся из "Неделя"
            elif period == 'MonthPeriod':
                if self.setting_filter.get('period') == 'YearPeriod':
                    if self.setting_filter.get('endDate').year == self.fm.todayDate.year:
                        endDay = calendar.monthrange(self.fm.todayDate.year, self.fm.todayDate.month)[1]
                        self.setting_filter['beginDate'] = dt.date(self.fm.todayDate.year, self.fm.todayDate.month, 1)
                        self.setting_filter['endDate'] = dt.date(self.fm.todayDate.year, self.fm.todayDate.month,
                                                                 endDay)
                    elif self.setting_filter.get('endDate').year < self.fm.todayDate.year:
                        self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('endDate').year, 12, 1)
                        self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year, 12, 31)
                    elif self.setting_filter.get('endDate').year < self.fm.todayDate.year:
                        self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('endDate').year, 1, 1)
                        self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year, 1, 31)
                elif self.setting_filter.get('period') == 'WeekPeriod':
                    endDay = calendar.monthrange(self.setting_filter.get('endDate').year,
                                                 self.setting_filter.get('endDate').month)[1]
                    self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('endDate').year,
                                                               self.setting_filter.get('endDate').month, 1)
                    self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year,
                                                             self.setting_filter.get('endDate').month, endDay)
                self.setting_filter['period'] = 'MonthPeriod'

            # Если период меняем на Неделю, то устанавливаем неделю текущйй даты, если двигаемся с текущего месяца
            # c "Месяц", если двигаемся с прошлых месяцев - то устанавливаем неделю конца месяца
            # если двигаемся с будущих месяцев - то устанавливаем неделю начала месяца
            # или берем неделю выбранной даты, если двигаемся из "День"
            elif period == 'WeekPeriod':
                if self.setting_filter.get('period') == 'MonthPeriod':
                    if self.setting_filter.get('endDate').month == self.fm.todayDate.month:
                        dayWeek = calendar.monthrange(self.fm.todayDate.year, self.fm.todayDate.month)[0]
                        self.setting_filter['beginDate'] = self.fm.todayDate - timedelta(dayWeek)
                        self.setting_filter['endDate'] = self.fm.todayDate + timedelta(6 - dayWeek)
                    elif self.setting_filter['endDate'].month > self.fm.todayDate.month:
                        dayWeekOne = calendar.monthrange(self.setting_filter.get('beginDate').year,
                                                         self.setting_filter.get('beginDate').month)[0]
                        self.setting_filter['beginDate'] = self.setting_filter.get('endDate') - timedelta(dayWeekOne)
                        self.setting_filter['endDate'] = self.setting_filter.get('endDate') + timedelta(6 - dayWeekOne)
                    elif self.setting_filter.get('endDate').month < self.fm.todayDate.month:
                        dayWeek = calendar.monthrange(self.setting_filter.get('beginDate').year,
                                                      self.setting_filter.get('beginDate').month)[0]
                        dayMonthEnd = self.setting_filter.get('beginDate') + timedelta(28)
                        self.setting_filter['beginDate'] = dayMonthEnd - timedelta(dayWeek)
                        self.setting_filter['endDate'] = dayMonthEnd + timedelta(6 - dayWeek)
                elif self.setting_filter.get('period') == 'DayPeriod':
                    weekDay = self.setting_filter.get('beginDate').weekday()
                    self.setting_filter['beginDate'] = self.setting_filter.get('beginDate') - timedelta(weekDay)
                    self.setting_filter['endDate'] = self.setting_filter.get('endDate') + timedelta(6 - weekDay)
                self.setting_filter['period'] = 'WeekPeriod'

            # Если период меняем на день, то устанавливаем текущую дату, если двигаемся с "Весь период"
            # Если двигаемся с "Недели", включающую текущий день - то устанавливаем текущий день
            # если двигаемся с будущей недели, то устанавливаем первый день недели
            # если двигаемся с прошедшей недели то устанавливаем  последний день недели
            elif period == 'DayPeriod':
                if self.setting_filter.get('period') == 'AllPeriod':
                    self.setting_filter['beginDate'] = self.fm.todayDate
                    self.setting_filter['endDate'] = self.fm.todayDate
                elif self.setting_filter.get('period') == 'WeekPeriod':
                    if self.setting_filter.get('beginDate') >= self.fm.todayDate >= self.setting_filter.get('endDate'):
                        self.setting_filter['beginDate'] = self.fm.todayDate
                        self.setting_filter['endDate'] = self.fm.todayDate
                    elif self.setting_filter.get('beginDate') > self.fm.todayDate:
                        self.setting_filter['endDate'] = self.setting_filter.get('beginDate')
                    elif self.setting_filter.get('endDate') < self.fm.todayDate:
                        self.setting_filter['beginDate'] = self.setting_filter.get('endDate')
                self.setting_filter['period'] = 'DayPeriod'

            # Если дата начала периода получилась < даты начала учета, делаем датой начала периода дату начала учета
            if self.setting_filter.get('beginDate') < self.fm.beginDate:
                self.setting_filter['beginDate'] = self.fm.beginDate

        # Листаем отрезок времени назад
        elif ChangePeriod == 'PeriodBack':
            # Листаем годы назад, пока не дойдем до года начала учета
            if self.setting_filter.get('period') == 'YearPeriod':
                if self.setting_filter.get('endDate').year == self.fm.beginDate.year:
                    self.setting_filter['beginDate'] = self.fm.beginDate
                elif self.setting_filter.get('endDate').year > self.fm.beginDate.year:
                    if (self.setting_filter.get('endDate').year - 1) == self.fm.beginDate.year:
                        self.setting_filter['beginDate'] = self.fm.beginDate
                        self.setting_filter['endDate'] = dt.date(self.fm.beginDate.year, 12, 31)
                    else:
                        self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('beginDate').year - 1, 1, 1)
                        self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year - 1, 12, 31)

            # Листаем месяцы назад, пока не дойдем до месяца начала учета
            elif self.setting_filter.get('period') == 'MonthPeriod':
                if self.setting_filter.get('beginDate') == self.fm.beginDate:
                    self.setting_filter['beginDate'] = self.fm.beginDate
                else:
                    if self.setting_filter.get('endDate').month != 1:
                        dayMonth = calendar.monthrange(self.setting_filter.get('endDate').year,
                                                       self.setting_filter.get('endDate').month - 1)[1]
                        self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('endDate').year,
                                                                   self.setting_filter.get('endDate').month - 1, 1)

                        self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year,
                                                                 self.setting_filter.get('endDate').month - 1, dayMonth)
                    else:
                        dayMonth = calendar.monthrange(self.setting_filter.get('endDate').year - 1, 1)[1]
                        self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('endDate').year - 1, 12, 1)

                        self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year - 1, 12,
                                                                 dayMonth)

            # Листаем недели назад, пока не дойдем до недели начала учета
            elif self.setting_filter.get('period') == 'WeekPeriod':
                if self.setting_filter.get('beginDate') == self.fm.beginDate:
                    self.setting_filter['beginDate'] = self.fm.beginDate
                else:
                    self.setting_filter['beginDate'] = self.setting_filter.get('beginDate') - timedelta(weeks=1)
                    self.setting_filter['endDate'] = self.setting_filter.get('endDate') - timedelta(weeks=1)

            # Листаем дни назад, пока не дойдем до дня начала учета
            elif self.setting_filter.get('period') == 'DayPeriod':
                if self.setting_filter.get('beginDate') == self.fm.beginDate:
                    self.setting_filter['beginDate'] = self.fm.beginDate
                else:
                    self.setting_filter['beginDate'] = self.setting_filter.get('beginDate') - timedelta(1)
                    self.setting_filter['endDate'] = self.setting_filter.get('endDate') - timedelta(1)

            # Если дата начала периода получилась < даты начала учета, делаем датой начала периода дату начала учета
            if self.setting_filter.get('beginDate') < self.fm.beginDate:
                self.setting_filter['beginDate'] = self.fm.beginDate

        # Листаем отрезок времени вперед
        elif ChangePeriod == 'PeriodForward':
            # Листаем годы вперед
            if self.setting_filter.get('period') == 'YearPeriod':
                self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('beginDate').year + 1, 1, 1)
                self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year + 1, 12, 31)

            # Листаем месяцы вперед
            elif self.setting_filter.get('period') == 'MonthPeriod':
                if self.setting_filter.get('endDate').month != 12:
                    dayMonth = calendar.monthrange(self.setting_filter.get('endDate').year,
                                                   self.setting_filter.get('endDate').month + 1)[1]
                    self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('endDate').year,
                                                               self.setting_filter.get('endDate').month + 1, 1)

                    self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year,
                                                             self.setting_filter.get('endDate').month + 1, dayMonth)
                else:
                    dayMonth = calendar.monthrange(self.setting_filter.get('endDate').year + 1, 1)[1]
                    self.setting_filter['beginDate'] = dt.date(self.setting_filter.get('endDate').year + 1, 1, 1)

                    self.setting_filter['endDate'] = dt.date(self.setting_filter.get('endDate').year + 1, 1, dayMonth)

            # Листаем недели вперед
            elif self.setting_filter.get('period') == 'WeekPeriod':
                self.setting_filter['beginDate'] = self.setting_filter.get('endDate') + timedelta(weeks=1)
                self.setting_filter['endDate'] = self.setting_filter.get('endDate') + timedelta(6)

            # Листаем дни вперед
            elif self.setting_filter.get('period') == 'DayPeriod':
                self.setting_filter['beginDate'] = self.setting_filter.get('beginDate') + timedelta(1)
                self.setting_filter['endDate'] = self.setting_filter.get('endDate') + timedelta(1)

            # Если дата начала периода получилась < даты начала учета, делаем датой начала периода дату начала учета
            if self.setting_filter.get('beginDate') < self.fm.beginDate:
                self.setting_filter['beginDate'] = self.fm.beginDate

    def change_filter(self, change, ITEMID, OBJECTLIST, DATE_BEGIN=dt.date(2200, 12, 31),
                      DATE_END=dt.date(2200, 12, 31)):
        """ Изменение значений словаря SettingFilter при нажатии на кнопки роутинга и
        фильтра по дате при помощи вызова метода FindPeriod.
        Вызов метода обновления реестра и кнопок пэйджинга и фильтра DrawListOfRow"""
        # Изменение значений фильтрации при нажатии кнопок
        if change == 'PageForward':
            if self.setting_filter['currentPage'] == self.setting_filter['countPage']:
                self.setting_filter['currentPage'] = 1
            else:
                self.setting_filter['currentPage'] += 1

        elif change == 'PageBack':
            if self.setting_filter['currentPage'] == 1:
                self.setting_filter['currentPage'] = self.setting_filter['countPage']
            else:
                self.setting_filter['currentPage'] -= 1
        else:
            # Устанавливаем новые значения в SettingFilter для отбора по периоду
            self.get_period_when_filter_changes(change)

        # Отрисовываем новые данные, пейджинг и фильтр
        if self.current_window == FV.TypesWindows.listDataInItemInReportWindow:
            self.fv.draw_list_of_operations(ITEMID, OBJECTLIST, DATE_BEGIN, DATE_END)
        else:
            self.fv.draw_list_of_operations(ITEMID, OBJECTLIST)

    # ****************************** СОБЫТИЯ ДЛЯ РАБОТЫ С ОТЧЕТОМ *******************************************
    def node_click_report(self, OBJECTLIST, STRING, REQUEST_LIST, VIEW):
        """ Раскрытие/сворачивание узла раздела в отчете """
        NEW_REQUEST_LIST = list()
        for STR in REQUEST_LIST:
            if STR[1] == STRING.get('type_item'):
                if STR[0] == 0:
                    STR[0] = 1
                else:
                    STR[0] = 0
                NEW_REQUEST_LIST.append(STR)
            else:
                NEW_REQUEST_LIST.append(STR)

        # Очищаем область отчета
        for obj in OBJECTLIST:
            obj.destroy()

        # Строим обновленный очтет
        self.fv.draw_rows_report(NEW_REQUEST_LIST, VIEW)

    def scroll_registry_report(self, SIDE, LIST_STRING, OBJECTLIST, OBJSTRING, REQUEST_LIST, VIEW, TOPLINE):
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

                self.fv.draw_strings(LIST_STRING, OBJECTLIST, REQUEST_LIST, VIEW, TOPLINE)

        elif SIDE == 'DOWN':
            if (len(LIST_STRING) - TOPLINE) <= 16:
                return
            else:
                TOPLINE += 3

                for obj in OBJSTRING:
                    if obj in OBJECTLIST:
                        OBJECTLIST.remove(obj)
                        obj.destroy()

                self.fv.draw_strings(LIST_STRING, OBJECTLIST, REQUEST_LIST, VIEW, TOPLINE)

    def change_view_report(self, REQUEST_LIST, OBJECTLIST, VIEW):
        """ Переключение на широкий/узкий вид """
        NEW_REQUEST_LIST = list()
        view = 'narrow' if VIEW == 'wide' else 'wide'
        if view == 'narrow':
            for section in REQUEST_LIST:
                section_list = [section[0], section[1], self.setting_filter.get('beginDate'),
                                self.setting_filter.get('endDate')]
                NEW_REQUEST_LIST.append(section_list)
        elif view == 'wide':
            FourPeriod = self.calculate_four_periods()
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
        self.fv.draw_rows_report(NEW_REQUEST_LIST, view)

    def change_filter_report(self, change, REQUEST_LIST, OBJECTLIST, VIEW='narrow'):
        """ Изменение значений словаря SettingFilter при нажатии на кнопку фильтра по дате при помощи вызова
         метода FindPeriod.
        Вызов метода обновления реестра и кнопок пэйджинга и фильтра ReportWindow"""
        # Изменение значений фильтрации при нажатии кнопок

        # Устанавливаем новые значения в SettingFilter для отбора по периоду
        self.get_period_when_filter_changes(change)

        NEW_REQUEST_LIST = list()

        if self.setting_filter['period'] == 'AllPeriod':
            VIEW = 'narrow'
            for section in REQUEST_LIST:
                section_list = [section[0], section[1]]
                NEW_REQUEST_LIST.append(section_list)

        elif self.setting_filter['period'] != 'AllPeriod' and VIEW == 'narrow':
            for section in REQUEST_LIST:
                section_list = [section[0], section[1], self.setting_filter['beginDate'],
                                self.setting_filter['endDate']]
                NEW_REQUEST_LIST.append(section_list)

        elif self.setting_filter['period'] != 'AllPeriod' and VIEW == 'wide':
            FourPeriod = self.calculate_four_periods()
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
        self.fv.draw_rows_report(NEW_REQUEST_LIST, VIEW)

    def calculate_four_periods(self):
        """ Расчет 4 периодов для широкого вида """
        FourPeriods = list()
        FourPeriods.append([self.setting_filter['beginDate'], self.setting_filter['endDate']])

        # Подбираем 3 периода года, ищем сначала сзади, если там упираемся, то спереди
        if self.setting_filter['period'] == 'YearPeriod':
            if self.setting_filter['beginDate'] == self.fm.beginDate:
                for i in range(3):
                    new_date_begin = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 1, 1)
                    new_date_end = dt.date(FourPeriods[len(FourPeriods) - 1][1].year + 1, 12, 31)
                    FourPeriods.append([new_date_begin, new_date_end])
            else:
                for i in range(3):
                    new_date_begin = dt.date(FourPeriods[0][1].year - 1, 1, 1)
                    new_date_end = dt.date(FourPeriods[0][1].year - 1, 12, 31)
                    if new_date_begin.year == self.fm.beginDate.year:
                        new_date_begin = self.fm.beginDate
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
        elif self.setting_filter['period'] == 'MonthPeriod':
            if self.setting_filter['beginDate'] == self.fm.beginDate:
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

                    if new_date_begin <= self.fm.beginDate:
                        new_date_begin = self.fm.beginDate
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
        elif self.setting_filter['period'] == 'WeekPeriod':
            if self.setting_filter['beginDate'] == self.fm.beginDate:
                for i in range(3):
                    new_date_begin = FourPeriods[len(FourPeriods) - 1][0] + timedelta(weeks=1)
                    new_date_end = FourPeriods[len(FourPeriods) - 1][1] + timedelta(6)
                    FourPeriods.append([new_date_begin, new_date_end])
            else:
                for i in range(3):
                    new_date_begin = FourPeriods[0][0] - timedelta(weeks=1)
                    new_date_end = FourPeriods[0][1] - timedelta(weeks=1)

                    if new_date_begin <= self.fm.beginDate:
                        new_date_begin = self.fm.beginDate
                        FourPeriods.insert(0, [new_date_begin, new_date_end])
                        break
                    FourPeriods.insert(0, [new_date_begin, new_date_end])
            if len(FourPeriods) < 4:
                for i in range(4 - len(FourPeriods)):
                    new_date_begin = FourPeriods[len(FourPeriods) - 1][0] + timedelta(weeks=1)
                    new_date_end = FourPeriods[len(FourPeriods) - 1][1] - timedelta(6)
                    FourPeriods.append([new_date_begin, new_date_end])

        # Подбираем 3 периода дня, ищем сначала сзади, если там упираемся, то спереди
        elif self.setting_filter['period'] == 'DayPeriod':
            if self.setting_filter['beginDate'] == self.fm.beginDate:
                for i in range(3):
                    new_date_begin = FourPeriods[len(FourPeriods) - 1][0] + timedelta(1)
                    new_date_end = FourPeriods[len(FourPeriods) - 1][1] + timedelta(1)
                    FourPeriods.append([new_date_begin, new_date_end])
            else:
                for i in range(3):
                    new_date_begin = FourPeriods[0][0] - timedelta(1)
                    new_date_end = FourPeriods[0][1] - timedelta(1)

                    if new_date_begin <= self.fm.beginDate:
                        new_date_begin = self.fm.beginDate
                        FourPeriods.insert(0, [new_date_begin, new_date_end])
                        break
                    FourPeriods.insert(0, [new_date_begin, new_date_end])

            if len(FourPeriods) < 4:
                for i in range(4 - len(FourPeriods)):
                    new_date_begin = FourPeriods[len(FourPeriods) - 1][0] + timedelta(1)
                    new_date_end = FourPeriods[len(FourPeriods) - 1][1] + timedelta(1)
                    FourPeriods.append([new_date_begin, new_date_end])

        return FourPeriods

    # ****************************** СОБЫТИЯ ДЛЯ РАБОТЫ НАСТРОЙКАМИ *******************************************
    def delete_item(self, DATA):
        """ Удаление статьи из БД """

        # Удаляем  статью из БД
        self.fm.delete_itemDB(DATA[0])

        # Отрисовываем список статей
        self.fv.list_item_setting_window(DATA[1])

        # чистим буферный динамический массив
        self.bufferList = list()

    def save_new_item(self):
        """ Сохранение новой статьи """
        # Проверяем, что наименование статьи заполнено
        if self.bufferList[1] == '':
            mb.showerror("Ошибка", "Наименование статьи должно быть заполнено!!!")
        else:
            # Собираем кортеж для записи в БД
            adddata = (self.bufferList[0], self.bufferList[1], self.bufferList[2], self.bufferList[3],
                       self.bufferList[4], self.bufferList[5],
                       self.bufferList[5], self.bufferList[6], 1, 0, None, 0, 0, '2200-01-01')

            # Записываем новую статью в БД
            self.fm.add_new_item(adddata)

            # Очищаем фрейм и отрисовываем список статей
            self.fv.clear_main_frame()
            self.do_back_ward(self.bufferList[0])

            # чистим буферный динамический массив
            self.bufferList = list()

    def change_page_setting_item(self, change, ITEMID):
        """ Изменение значений фильтрации при нажатии кнопок когда статей больше 20 """
        if change == 'PageForward':
            if self.setting_filter['currentPage'] == self.setting_filter['countPage']:
                self.setting_filter['currentPage'] = 1
            else:
                self.setting_filter['currentPage'] += 1

        elif change == 'PageBack':
            if self.setting_filter['currentPage'] == 1:
                self.setting_filter['currentPage'] = self.setting_filter['countPage']
            else:
                self.setting_filter['currentPage'] -= 1

        # Отрисовываем новые данные, пейджинг и фильтр
        self.fv.list_item_setting_window(ITEMID)
