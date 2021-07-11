import sqlite3
import datetime as dt
from datetime import timedelta
import os.path as op


# Создание и управление базами данных
class DataBases:
    def __init__(self):
        # Сегодняшняя дата и дата начала учета для быстрого доступа
        self.__today = dt.date.today()
        self.__beginDate = dt.date.today()
        # Переменная рабочей/нерабочей программы
        self.__use = 0

        if not op.exists('Financier.db'):
            # Создаем базу данных настроек при первом входе
            with sqlite3.connect('Financier.db') as con:
                print('Создаём базу данных Financier')
                cur = con.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS setting (id integer primary key, parol text, date date,
                                  use integer, wallet integer references typeitems(id),  costkm integer)''')
                con.commit()
                cur.execute('''INSERT INTO setting(parol, date, use, wallet, costkm) VALUES (?, ?, ?, ?, ?)''',
                            ('777', self.todayDate, self.use, None, 0))
                con.commit()
                print('OK! Таблица настроек создана')

                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS typeitems (id integer primary key, typetypeitems integer,
                     nametypeitems text, descriptoiontypeitems text, suminitialtypeitems real,
                      sumcurrenttypeitems real)''')
                # Доходы = 0, Расходы = 1, Актив = 2, Пассив = 3, Собственный капитал = 4;
                data = [(
                    0, 'Доходы', 'Поступление доходов: зарплаты, процентов по депозитам, ареднных платежей и прочих', 0,
                    0),
                    (
                        1, 'Расходы', 'Расход денежных средств на еду, бытовые расходы, процентные платежи и прочее', 0,
                        0),
                    (2, 'Денежные средства', 'Рублевые денежные средства наличными и на картах ', 0, 0),
                    (2, 'Имущество', 'Квартиры, автотранспорт, земельные участки и иное дорогостоящее имущество', 0, 0),
                    (2, 'Вложения', 'Депозиты, валюта, акции, золото и другие ликвидные активы', 0, 0),
                    (2, 'Выданные займы', 'Денежные средства выданные третьим лицам на условиях возврата', 0, 0),
                    (3, 'Кредиты', 'Задолженность по основному долгу по кредитам, кредитным картам, ипотеке и прочим '
                                   'продуктам перед банками', 0, 0),
                    (3, 'Полученные займы', 'Задолженность перед родственниками, друзьями, и прочими лицами', 0, 0),
                    (4, 'Собственный капитал', 'Разница между активом и пассивом', 0, 0)]
                cur.executemany('''INSERT INTO typeitems(typetypeitems, nametypeitems, descriptoiontypeitems, 
                                             suminitialtypeitems, sumcurrenttypeitems) VALUES( ?, ?, ?, ?, ?)''', data)
                con.commit()
                print('OK! Таблица с типами статей создана')

                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS typeinvestments (id integer primary key,nametypeinvestments text )''')
                con.commit()
                print('OK! Таблица для хранения видов вложений создана')

                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS items (id integer primary key, typeitem_id, nameitem text,
                           workingitem integer,
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

                cur.executemany('''INSERT INTO items(typeitem_id, nameitem, workingitem, descriptoionitem, creditcard, 
                                       initialbalanceitem, currentbalanceitem, paintitem, candelete,
                                       quantitativeaccounting, 
                                       typeinvestment_id, countinvestment, priceunit, dateclose) 
                                       VALUES(  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
                con.commit()
                print('OK! Таблица с перечнем инсталляционных статей создана')

                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS notes (id integer primary key, item_id integer references items(id),
                           typeitem_id integer references typeitems(id), dateoperation date, descriptoionoperation text,
                           sumoperation real, increase integer, source integer references items(id),
                           typeinvestment_id integer references typeinvestment(id), countnote real, priseunit real )''')
                con.commit()
                print('ОК! Таблица для внесения записей создана')

        else:
            print('OK! База данных Financier уже существует')
            data = self.request_select_DB('date, use', 'setting')
            self.beginDate = dt.datetime.strptime(data[0][0], '%Y-%m-%d').date()
            self.use = data[0][1]
            self.hard_recalculating_balances()

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

    def add_new_item(self, data):
        """ Метод добавления новой статьи """
        with sqlite3.connect('Financier.db') as con:
            cur = con.cursor()
            cur.execute(''' INSERT INTO items (typeitem_id, nameitem, workingitem, descriptoionitem, creditcard,
                           initialbalanceitem, currentbalanceitem, paintitem, candelete, quantitativeaccounting, 
                           typeinvestment_id, countinvestment, priceunit, dateclose)
                           VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
            con.commit()

            # Пересчитываем остатки при создании новой статьи
            self.recalculating_balances_item('NEW', data[0], data[5])

    """ Метод удаления статьи """
    def delete_itemDB(self, iditem):
        # Пересчитываем остатки при удалении статьи
        self.recalculating_balances_item('DELETE', iditem)

        with sqlite3.connect('Financier.db') as con:
            cur = con.cursor()
            cur.execute('''DELETE FROM items WHERE id=?''', (iditem,))
            con.commit()

    def update_operation(self, DATA, NOTE):
        """ Метод изменения данных операции """
        print(DATA)
        with sqlite3.connect('Financier.db') as con:
            cur = con.cursor()
            cur.execute(''' UPDATE notes SET item_id=?, typeitem_id=?, dateoperation=?, descriptoionoperation=?,
                               sumoperation=?, increase=?, source=?, typeinvestment_id=?, countnote=?, priseunit=? 
                                WHERE id=? ''', (DATA['iditemkey'], DATA['idtypeitemkey'], DATA['dateoperationkey'],
                                                 DATA['descriptionkey'], DATA['sumoperationkey'], DATA['increasekey'],
                                                 DATA['sourcekey'], DATA['typeinvestmentidkey'], DATA['countnotekey'],
                                                 DATA['priseunit'], NOTE[0]))
            con.commit()

        # Пересчитываем остатки
        # Сторнируем операцию до изменения
        self.recalculating_balances(NOTE[1], NOTE[7], NOTE[6], -NOTE[5])
        # Пересчитываем остатки с учетом измененной операции
        self.recalculating_balances(DATA['iditemkey'], DATA['sourcekey'], DATA['increasekey'], DATA['sumoperationkey'])

    def update_note_DB(self, database, field, idname, data, iditem):
        """ Метод изменения данных одного поля """
        # Пересчитываем остатки при изменении начального остатка статьи
        if field == 'initialbalanceitem':
            self.recalculating_balances_item('CORRECTION', iditem, data)

        with sqlite3.connect('Financier.db') as con:
            cur = con.cursor()
            request = 'UPDATE {} SET {}=? WHERE {}=?'.format(database, field, idname)
            cur.execute(request, (data, iditem))
            con.commit()

    def request_select_DB(self, selectionfields, database, conditionfields=''):
        """ Метод запроса данных """
        with sqlite3.connect('Financier.db') as con:
            cur = con.cursor()

            if conditionfields == '':
                request = 'SELECT {} FROM {} '.format(selectionfields, database)
            else:
                request = 'SELECT {} FROM {} WHERE {}'.format(selectionfields, database, conditionfields)

            cur.execute(request)
            data = cur.fetchall()

            return data

    def add_new_operation(self, data):
        """ Метод добавления новой операции """
        datalist = list()
        for value in data.values():
            datalist.append(value)

        with sqlite3.connect('Financier.db') as con:
            cur = con.cursor()
            cur.execute('''INSERT INTO notes (item_id, typeitem_id, dateoperation, descriptoionoperation,
                           sumoperation, increase, source, typeinvestment_id, countnote, priseunit) 
                           VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', datalist)
            con.commit()

            # Пересчитываем остатки
            self.recalculating_balances(data['iditemkey'], data['sourcekey'], data['increasekey'],
                                        data['sumoperationkey'])

    def delete_note_DB(self, DATA):
        """ Метод удаления записи с данными по операции """
        with sqlite3.connect('Financier.db') as con:
            cur = con.cursor()
            cur.execute('''DELETE FROM notes WHERE id=?''', (DATA[0],))
            con.commit()

    def recalculating_balances(self, ITEM1, ITEM2, INCREASE, SUMOPERATIONS):
        """ Пересчет и установка остатков при создании/изменении операции """
        # Расчет и установка нового текущего остатка по статьям
        balance_item = self.request_select_DB('currentbalanceitem', 'items', 'id={}'.format(ITEM1))
        balance_source = self.request_select_DB('currentbalanceitem', 'items', 'id={}'.format(ITEM2))

        if INCREASE == 0:
            balanceitem = balance_item[0][0] - SUMOPERATIONS
            balancesource = balance_source[0][0] + SUMOPERATIONS
            self.update_note_DB('items', 'currentbalanceitem', 'id', balanceitem, ITEM1)
            self.update_note_DB('items', 'currentbalanceitem', 'id', balancesource, ITEM2)
        elif INCREASE == 1:
            balanceitem = balance_item[0][0] + SUMOPERATIONS
            balancesource = balance_source[0][0] - SUMOPERATIONS
            self.update_note_DB('items', 'currentbalanceitem', 'id', balanceitem, ITEM1)
            self.update_note_DB('items', 'currentbalanceitem', 'id', balancesource, ITEM2)
        elif INCREASE == 2:
            balanceitem = balance_item[0][0] + SUMOPERATIONS
            balancesource = balance_source[0][0] + SUMOPERATIONS
            self.update_note_DB('items', 'currentbalanceitem', 'id', balanceitem, ITEM1)
            self.update_note_DB('items', 'currentbalanceitem', 'id', balancesource, ITEM2)
        elif INCREASE == 3:
            balanceitem = balance_item[0][0] - SUMOPERATIONS
            balancesource = balance_source[0][0] - SUMOPERATIONS
            self.update_note_DB('items', 'currentbalanceitem', 'id', balanceitem, ITEM1)
            self.update_note_DB('items', 'currentbalanceitem', 'id', balancesource, ITEM2)

        # Расчет и установка нового текущего остатка по разделам
        sectionItem1 = self.request_select_DB('typeitem_id', 'items', 'id={}'.format(ITEM1))[0][0]
        sectionItem2 = self.request_select_DB('typeitem_id', 'items', 'id={}'.format(ITEM2))[0][0]
        if sectionItem1 != sectionItem2:
            balans_sectionItem1 = self.request_select_DB('sumcurrenttypeitems', 'typeitems', 'id={}'.format(
                sectionItem1))[0][0]
            balans_sectionItem2 = self.request_select_DB('sumcurrenttypeitems', 'typeitems', 'id={}'.format(
                sectionItem2))[0][0]

            if INCREASE == 0:
                balanssectionItem1 = balans_sectionItem1 - SUMOPERATIONS
                balanssectionItem2 = balans_sectionItem2 + SUMOPERATIONS
                self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem1, sectionItem1)
                self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem2, sectionItem2)
            elif INCREASE == 1:
                balanssectionItem1 = balans_sectionItem1 + SUMOPERATIONS
                balanssectionItem2 = balans_sectionItem2 - SUMOPERATIONS
                self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem1, sectionItem1)
                self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem2, sectionItem2)
            elif INCREASE == 2:
                balanssectionItem1 = balans_sectionItem1 + SUMOPERATIONS
                balanssectionItem2 = balans_sectionItem2 + SUMOPERATIONS
                self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem1, sectionItem1)
                self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem2, sectionItem2)
            elif INCREASE == 3:
                balanssectionItem1 = balans_sectionItem1 - SUMOPERATIONS
                balanssectionItem2 = balans_sectionItem2 - SUMOPERATIONS
                self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem1, sectionItem1)
                self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', balanssectionItem2, sectionItem2)

            # Рассчитываем и устанавливаем текущий собственный капитал
            data5 = self.request_select_DB('*', 'typeitems')
            sumcurrent = data5[2][5] + data5[3][5] + data5[4][5] + data5[5][5] - data5[6][5] - data5[7][5]
            self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', sumcurrent, 9)

    def recalculating_balances_item(self, TYPE, ITEMID, SUM=0):
        """ Пересчет остатков при внесении изменений в начальные остатки статей """
        if TYPE == 'DELETE':
            SUM = -self.request_select_DB('initialbalanceitem', 'items', 'id={}'.format(ITEMID))[0][0]

        elif TYPE == 'CORRECTION':
            SUM = SUM - self.request_select_DB('initialbalanceitem', 'items', 'id={}'.format(ITEMID))[0][0]
            SUM2 = self.request_select_DB('currentbalanceitem', 'items', 'id={}'.format(ITEMID))[0][0]
            self.update_note_DB('items', 'currentbalanceitem', 'id', SUM2 + SUM, ITEMID)

        # Изменяем остатки в разделе статьи
        type_id = ITEMID if TYPE == 'NEW' else self.request_select_DB('typeitem_id', 'items', 'id={}'.format(
            ITEMID))[0][0]
        sums = self.request_select_DB('suminitialtypeitems, sumcurrenttypeitems', 'typeitems', 'id={}'.format(
            type_id))[0]
        self.update_note_DB('typeitems', 'suminitialtypeitems', 'id', sums[0] + SUM, type_id)
        self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', sums[1] + SUM, type_id)
        # Изменяем остаток собственного капитала
        SUM = SUM if type_id in (3, 4, 5, 6) else -SUM

        sums2 = self.request_select_DB('suminitialtypeitems, sumcurrenttypeitems', 'typeitems', 'id=9')[0]
        self.update_note_DB('typeitems', 'suminitialtypeitems', 'id', sums2[0] + SUM, 9)
        self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id', sums2[1] + SUM, 9)

    @staticmethod
    def check_result_for_none(DATA):
        """ Проверяем результат запроса суммы на None """
        if DATA[0][0] is None:
            data = 0
        else:
            data = DATA[0][0]
        return data

    def get_values_for_total_line(self, ITEMID, DATE_BEGIN, DATE_END, section):
        """ Расчет значений итоговой строки в реестре данных по статье
        извлекает словарь с ключами: 'initial_balance_item', 'sumitem_plus', 'sumitem_minus', 'final_balance_item'
        """

        result = {'initial_balance_item': 0, 'sumitem_plus': 0, 'sumitem_minus': 0, 'final_balance_item': 0}

        if section in (1, 2):
            request = f""" SELECT COALESCE(sum(sumoperation), 0), 
                    COALESCE((SELECT sum(sumoperation) FROM notes 
                    WHERE item_id={ITEMID} and dateoperation Between \'{DATE_BEGIN}\' and 
                    \'{DATE_END}\'), 0)
                    FROM notes WHERE item_id={ITEMID} and 
                    dateoperation Between \'{self.beginDate - timedelta(1)}\' and \'{DATE_BEGIN - timedelta(1)}\' """
            with sqlite3.connect('Financier.db') as con:
                cur = con.cursor()
                cur.execute(request)
                data = cur.fetchall()

                result['initial_balance_item'] = data[0][0]
                result['sumitem_plus'] = data[0][1]
                result['final_balance_item'] = data[0][0] + data[0][1]

        else:
            request = f""" 
                SELECT 
                    COALESCE(sum(sumoperation), 0) + 
                    (SELECT COALESCE(initialbalanceitem, 0) FROM items WHERE id={ITEMID}) - 
                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                        WHERE ((item_id={ITEMID} AND (increase=0 or increase=3)) or 
                            (source={ITEMID} AND (increase=1 or  increase=3))) and 
                            dateoperation Between \'{self.beginDate - timedelta(1)}\' and
                            \'{DATE_BEGIN - timedelta(1)}\'), 

                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                        WHERE ((item_id={ITEMID} AND (increase=1 or increase=2)) or (source={ITEMID} AND 
                           (increase=0 or increase=2)))  and dateoperation Between \'{DATE_BEGIN}\' and \'{DATE_END}\'), 

                   (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                        WHERE ((item_id={ITEMID} AND (increase=0 or increase=3)) or (source={ITEMID} AND 
                            (increase=1 or increase=3))) AND dateoperation Between \'{DATE_BEGIN}\' and
                            \'{DATE_END}\')   


                FROM notes 
                WHERE ((item_id={ITEMID} AND (increase=1 or increase=2)) or (source={ITEMID} AND 
                    (increase=0 or increase=2)))  and 
                    dateoperation Between \'{self.beginDate - timedelta(1)}\' and \'{DATE_BEGIN - timedelta(1)}\' 
            """

            with sqlite3.connect('Financier.db') as con:
                cur = con.cursor()
                cur.execute(request)
                data = cur.fetchall()

                result['initial_balance_item'] = data[0][0]
                result['sumitem_plus'] = data[0][1]
                result['sumitem_minus'] = data[0][2]
                result['final_balance_item'] = data[0][0] + data[0][1] - data[0][2]

        return result

    # Пересчет и установка остатков при загрузке программы
    def hard_recalculating_balances(self):
        """ Тестовый метод для проверки расчетных значений сохраненным в базе, и создания сообщений при расхождениях """
        print('Тяжелый пересчет остатков запущен')
        # Получаем кортеж значений остатков по разделам и статьям
        dict_data = self.get_data_for_row_report_narrow(
            [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8]])

        typeitemdata = self.request_select_DB('*', 'typeitems')
        # Перебираем все разделы
        for TYPEITEM in typeitemdata:
            # Прерываем, если добрались до собственного капитала

            for section in dict_data:
                if section.get('type_row') == 'section' and section.get('type_item') == TYPEITEM[0]:
                    # Сравниваем полученный остаток по разделу с остатком в базе, выкидываем сообщение и
                    # перезаписываем остаток в базе, если они различаются

                    # Сравниваем  начальный остаток с сохраненным в базе
                    if TYPEITEM[4] != section.get('initial_balance_item'):
                        print(f"WARNING: Начальный остаток раздела {TYPEITEM[2]} рассчитан"
                              f" {section.get('initial_balance_item')} и не равен остатку в базе {TYPEITEM[4]},"
                              f" перезаписан на расчетный")
                        self.update_note_DB('typeitems', 'suminitialtypeitems', 'id',
                                            section.get('initial_balance_item'), TYPEITEM[0])

                    # Сравниваем  текущий остаток с сохраненным в базе
                    if TYPEITEM[5] != section.get('final_balance_item'):
                        print(f"WARNING: Текущий остаток раздела {TYPEITEM[2]} рассчитан "
                              f"{section.get('final_balance_item')} и не равен остатку в базе {TYPEITEM[5]},"
                              f" перезаписан на рассчетный")
                        self.update_note_DB('typeitems', 'sumcurrenttypeitems', 'id',
                                            section.get('final_balance_item'), TYPEITEM[0])
            if TYPEITEM[0] != 9:
                # Получаем кортеж всех статей в разделе
                itemdata = self.request_select_DB('*', 'items', 'typeitem_id={}'.format(TYPEITEM[0]))
                # Перебираем все статьи
                for ITEM in itemdata:
                    for item in dict_data:
                        if item.get('type_row') == 'item' and item.get('item') == itemdata[0]:
                            # Сравниваем полученный остаток по статье с остатком в базе, выкидываем сообщение и
                            # перезаписываем остаток в базе, если они различаются
                            if ITEM[7] != item.get('final_balance_item'):
                                print(f'WARNING: Остаток статьи {ITEM[2]} рассчитан {item.get("final_balance_item")} и '
                                      f'не равен остатку в базе {ITEM[7]}, перезаписан на расчетный')
                                self.update_note_DB('items', 'currentbalanceitem', 'id',
                                                    item.get("final_balance_item"), ITEM[0])

        print('Тяжелый пересчет остатков завершен')

    @staticmethod
    def request_sqlite(request):
        """ Извлечение ответа на запрос """
        with sqlite3.connect('Financier.db') as con:
            cur = con.cursor()
            cur.execute(request)
            data = cur.fetchall()

            return data

    def get_data_for_row_report_narrow(self, REQUEST_LIST):
        """ Расчет значений строк в отчете с узким видом (1 столбец оборотов)
        извлекает словарь с ключами: 'is_node': наличие кнопки раскрытия узла(True==1),
        'node_is_open': узел раскрыт(True==1), 'type_row': тип строки,  'initial_balance_item': начальный остаток,
        'turnover1-4': Оборот в строках, 'final_balance_item': конечный остаток, 'date1-8': значения дат
        """
        response_list = list()

        for SECTION in REQUEST_LIST:
            result = {
                'is_node': 0, 'node_is_open': SECTION[0], 'type_row': 'section', 'name': '',
                'initial_balance_item': 0, 'turnover1': 0, 'final_balance_item': 0,
                'type_item': SECTION[1]
            }

            # Запрашиваем id статей, входящих в раздел
            items = self.request_select_DB('id', 'items', 'typeitem_id={}'.format(SECTION[1]))
            if len(items) == 0:
                # Если статей нет, то возвращаем строку по дефолту с нулевыми суммами
                response_list.append(result)
            else:
                # Список ID статей для вставки
                items_list = []
                for IT in items:
                    items_list.append(IT[0])

                # Установлен фильтр за весь период (в запросе по разделу есть только флаг раскрытия узла и id раздела)
                if len(SECTION) == 2:
                    result['is_node'] = 1
                    request = f""" 
                            SELECT 
                                COALESCE(sum(initialbalanceitem), 0),        
                                (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                    WHERE ((item_id in ({str(items_list)[1:-1]})) AND (increase=1 or increase=2)) or 
                                        ((source in ({str(items_list)[1:-1]})) AND (increase=0 or increase=2))), 
                                (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                    WHERE ((item_id in ({str(items_list)[1:-1]})) AND (increase=0 or increase=3)) or
                                          ((source in ({str(items_list)[1:-1]})) AND (increase=1 or increase=3))),
                                (SELECT nametypeitems FROM typeitems WHERE id = {SECTION[1]})
                                FROM items WHERE typeitem_id = {SECTION[1]} 
                    """

                    data = self.request_sqlite(request)

                    result['initial_balance_item'] = data[0][0]
                    result['turnover1'] = data[0][1] - data[0][2]
                    result['final_balance_item'] = data[0][0] + data[0][1] - data[0][2]
                    result['name'] = data[0][3]
                    response_list.append(result)

                    # Раскрыт узел со статьями, добавляем строки с вложенными статьями
                    if SECTION[0] == 1:
                        for ITEM in items_list:
                            result_item = {
                                'is_node': 0, 'node_is_open': 0, 'type_row': 'item', 'name': '',
                                'initial_balance_item': 0, 'turnover1': 0, 'opener1': 0, 'final_balance_item': 0,
                                'item': ITEM
                            }

                            request_item = f""" 
                                SELECT 
                                    COALESCE(initialbalanceitem, 0),        
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE (item_id = {ITEM} AND (increase=1 or increase=2)) or 
                                            (source = {ITEM} AND (increase=0 or increase=2))), 
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE (item_id = {ITEM} AND (increase=0 or increase=3)) or
                                            (source = {ITEM} AND (increase=1 or increase=3))),
                                    (SELECT nameitem FROM items WHERE id = {ITEM})
                                    FROM items 
                                    WHERE id = {ITEM} 
                            """

                            data_item = self.request_sqlite(request_item)

                            result_item['initial_balance_item'] = data_item[0][0]
                            result_item['turnover1'] = data_item[0][1] - data_item[0][2]
                            result_item['final_balance_item'] = data_item[0][0] + data_item[0][1] - data_item[0][2]
                            result_item['name'] = data_item[0][3]

                            # Если по статьям были обороты, то устанавливаем атрибут opener == 1, чтобы
                            # можно было посмотреть реестр с расшифровкой операций
                            if data_item[0][1] != 0 or data_item[0][2] != 0:
                                result_item['opener1'] = 1
                            response_list.append(result_item)

                # Установлен фильтр за  период, узкий вид (в запросе по разделу есть флаг раскрытия узла, id раздела,
                # дата начала и дата конца периода)
                elif len(SECTION) == 4:
                    result['is_node'] = 1
                    request = f""" 
                        SELECT 
                            COALESCE(sum(initialbalanceitem), 0),   
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE (
                                          (item_id in ({str(items_list)[1:-1]}) AND (increase=1 or increase=2)) or 
                                          (source in ({str(items_list)[1:-1]}) AND (increase=0 or increase=2))
                                      )
                                      and dateoperation Between \'{self.beginDate}\' and 
                                          \'{SECTION[2] - timedelta(1)}\'), 
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE (
                                          (item_id in ({str(items_list)[1:-1]}) AND (increase=0 or increase=3)) or
                                          (source in ({str(items_list)[1:-1]}) AND (increase=1 or increase=3))
                                      )
                                      and dateoperation Between \'{self.beginDate}\' and
                                          \'{SECTION[2] - timedelta(1)}\'),
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE (
                                          (item_id in ({str(items_list)[1:-1]}) AND (increase=1 or increase=2)) or 
                                          (source in ({str(items_list)[1:-1]}) AND (increase=0 or increase=2))
                                      )
                                      and dateoperation Between \'{SECTION[2]}\' and \'{SECTION[3]}\'), 
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ( 
                                          (item_id in ({str(items_list)[1:-1]}) AND (increase=0 or increase=3)) or
                                          (source in ({str(items_list)[1:-1]}) AND (increase=1 or increase=3))
                                      )
                                      and dateoperation Between \'{SECTION[2]}\' and \'{SECTION[3]}\'),
                            (SELECT nametypeitems FROM typeitems WHERE id = {SECTION[1]})
                            FROM items WHERE typeitem_id = {SECTION[1]} 
                    """

                    data = self.request_sqlite(request)

                    result['initial_balance_item'] = data[0][0] + data[0][1] - data[0][2]
                    result['turnover1'] = data[0][3] - data[0][4]
                    result['final_balance_item'] = data[0][0] + data[0][1] - data[0][2] + data[0][3] - data[0][4]
                    result['name'] = data[0][5]
                    response_list.append(result)

                    # Раскрыт узел со статьями, добавляем строки с вложенными статьями
                    if SECTION[0] == 1:
                        for ITEM in items_list:
                            result_item = {
                                'is_node': 0, 'node_is_open': 0, 'type_row': 'item', 'name': '',
                                'initial_balance_item': 0, 'turnover1': 0, 'opener1': 0, 'final_balance_item': 0,
                                'item': ITEM, 'items_list': []
                            }

                            request_item = f""" 
                                SELECT 
                                    COALESCE(initialbalanceitem, 0),        
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE (
                                                  (item_id = {ITEM} AND (increase=1 or increase=2)) or 
                                                  (source = {ITEM} AND (increase=0 or increase=2))
                                              )
                                              and dateoperation Between \'{self.beginDate}\' and 
                                            \'{SECTION[2] - timedelta(1)}\'), 
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=0 or increase=3)) or
                                            (source = {ITEM} AND (increase=1 or increase=3)))
                                            and dateoperation Between \'{self.beginDate}\' and
                                            \'{SECTION[2] - timedelta(1)}\'),
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=1 or increase=2)) or 
                                            (source = {ITEM} AND (increase=0 or increase=2)))
                                            and dateoperation Between \'{SECTION[2]}\' and \'{SECTION[3]}\'), 
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=0 or increase=3)) or
                                            (source = {ITEM} AND (increase=1 or increase=3)))
                                            and dateoperation Between \'{SECTION[2]}\' and \'{SECTION[3]}\'),
                                    (SELECT nameitem FROM items WHERE id = {ITEM})
                                    FROM items 
                                    WHERE id = {ITEM} 
                            """

                            data_item = self.request_sqlite(request_item)

                            result_item['initial_balance_item'] = data_item[0][0] + data_item[0][1] - data_item[0][2]
                            result_item['turnover1'] = data_item[0][3] - data_item[0][4]
                            result_item['final_balance_item'] = \
                                data_item[0][0] + data_item[0][1] - data_item[0][2] + data_item[0][3] - data_item[0][4]
                            result_item['name'] = data_item[0][5]

                            # Если по статьям были обороты, то устанавливаем атрибут opener == 1, чтобы
                            # можно было посмотреть реестр с расшифровкой операций
                            if data_item[0][3] != 0 or data_item[0][4] != 0:
                                result_item['opener1'] = 1

                            response_list.append(result_item)

        # Расчет результирующих строк и собственного капитала
        income, expenditure = 0, 0
        active = list()
        passive = list()

        for ROW in response_list:

            if ROW.get('type_item') == 1:
                income = ROW

            if ROW.get('type_item') == 2:
                expenditure = ROW

            if ROW.get('type_item') in (3, 4, 5, 6):
                active.append(ROW)

            if ROW.get('type_item') in (7, 8):
                passive.append(ROW)

        # Строка с прибылью и убытком
        result_profit = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'result', 'name': 'Прибыль/Убыток',
            'initial_balance_item': income.get('initial_balance_item') - expenditure.get('initial_balance_item'),
            'turnover1': income.get('turnover1') - expenditure.get('turnover1'),
            'final_balance_item': income.get('final_balance_item') - expenditure.get('final_balance_item'),
            'type_item': 0
        }
        response_list.insert(0, result_profit)

        # Строка Актива
        result_active = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'aktiv', 'name': 'АКТИВ',
            'initial_balance_item':
                active[0].get('initial_balance_item') + active[1].get('initial_balance_item') +
                active[2].get('initial_balance_item') + active[3].get('initial_balance_item'),
            'turnover1':
                active[0].get('turnover1') + active[1].get('turnover1') + active[2].get('turnover1') +
                active[3].get('turnover1'),
            'final_balance_item':
                active[0].get('final_balance_item') + active[1].get('final_balance_item') +
                active[2].get('final_balance_item') + active[3].get('final_balance_item'),
            'type_item': 0
        }
        ind = 0
        for ROW in response_list:
            ind += 1
            if ROW.get('type_row') == 'section' and ROW.get('type_item') == 3:
                response_list.insert(ind-1, result_active)
                break
        # Строка пассива
        result_passive = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'passiv', 'name': 'ПАССИВ',
            'initial_balance_item': result_active.get('initial_balance_item'),
            'turnover1': result_active.get('turnover1'),
            'final_balance_item': result_active.get('final_balance_item'),
            'type_item': 0
        }

        ind = 0
        for ROW in response_list:
            ind += 1
            if ROW.get('type_row') == 'section' and ROW.get('type_item') == 7:
                response_list.insert(ind-1, result_passive)
                break

        # Строка заемных средств
        result_borrowed_money = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'result', 'name': 'Заёмные средства',
            'initial_balance_item': passive[0].get('initial_balance_item') + passive[1].get('initial_balance_item'),
            'turnover1': passive[0].get('turnover1') + passive[1].get('turnover1'),
            'final_balance_item': passive[0].get('final_balance_item') + passive[1].get('final_balance_item'),
            'type_item': 0
        }
        response_list.append(result_borrowed_money)

        # Строка с собственным капиталом
        result_own_capital = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'section', 'name': 'Собственный капитал',
            'initial_balance_item':
                result_passive.get('initial_balance_item') - result_borrowed_money.get('initial_balance_item'),
            'turnover1': result_profit.get('turnover1'),
            'final_balance_item':
                result_passive.get('final_balance_item') - result_borrowed_money.get('final_balance_item'),
            'type_item': 9
        }
        response_list.append(result_own_capital)

        return response_list

    def get_data_for_row_report_wide(self, REQUEST_LIST):
        """ Расчет значений строк в отчете с широким видом (4 столбца оборотов)
        извлекает словарь с ключами: 'is_node': наличие кнопки раскрытия узла(True==1),
        'node_is_open': узел раскрыт(True==1), 'type_row': тип строки,  'initial_balance_item': начальный остаток,
        'turnover1-4': Оборот в строках, 'final_balance_item': конечный остаток, 'date1-8': значения дат
        """
        response_list = list()

        for SECTION in REQUEST_LIST:
            result = {
                'is_node': 0, 'node_is_open': SECTION[0], 'type_row': 'section', 'name': '',
                'initial_balance_item': 0, 'turnover1': 0, 'turnover2': 0, 'turnover3': 0, 'turnover4': 0,
                'final_balance_item': 0, 'type_item': SECTION[1]
            }

            # Запрашиваем id статей, входящих в раздел
            items = self.request_select_DB('id', 'items', 'typeitem_id={}'.format(SECTION[1]))
            if len(items) == 0:
                # Если статей нет, то возвращаем строку по дефолту с нулевыми суммами
                response_list.append(result)
            else:
                # Список ID статей для вставки
                items_list = []
                for IT in items:
                    items_list.append(IT[0])

                # Установлен фильтр за весь период (в запросе по разделу есть только флаг раскрытия узла и id раздела)
                if len(SECTION) == 10:
                    result['is_node'] = 1
                    request = f""" 
                        SELECT 
                            COALESCE(sum(initialbalanceitem), 0),        
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=1 or increase=2)) or 
                                    (source in ({str(items_list)[1:-1]}) AND (increase=0 or increase=2)))
                                    and dateoperation Between \'{self.beginDate}\' and \'{SECTION[2] - timedelta(1)}\'), 
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=0 or increase=3)) or
                                    (source in ({str(items_list)[1:-1]}) AND (increase=1 or increase=3)))
                                    and dateoperation Between \'{self.beginDate}\' and \'{SECTION[2] - timedelta(1)}\'),

                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=1 or increase=2)) or 
                                    (source in ({str(items_list)[1:-1]}) AND (increase=0 or increase=2)))
                                    and dateoperation Between \'{SECTION[2]}\' and \'{SECTION[3]}\'), 
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=0 or increase=3)) or
                                    (source in ({str(items_list)[1:-1]}) AND (increase=1 or increase=3)))
                                    and dateoperation Between \'{SECTION[2]}\' and \'{SECTION[3]}\'),

                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=1 or increase=2)) or 
                                    (source in ({str(items_list)[1:-1]}) AND (increase=0 or increase=2)))
                                    and dateoperation Between \'{SECTION[4]}\' and \'{SECTION[5]}\'), 
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=0 or increase=3)) or
                                    (source in ({str(items_list)[1:-1]}) AND (increase=1 or increase=3)))
                                    and dateoperation Between \'{SECTION[4]}\' and \'{SECTION[5]}\'),

                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=1 or increase=2)) or 
                                    (source in ({str(items_list)[1:-1]}) AND (increase=0 or increase=2)))
                                    and dateoperation Between \'{SECTION[6]}\' and \'{SECTION[7]}\'), 
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]} )AND (increase=0 or increase=3)) or
                                    (source in ({str(items_list)[1:-1]}) AND (increase=1 or increase=3)))
                                    and dateoperation Between \'{SECTION[6]}\' and \'{SECTION[7]}\'),

                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=1 or increase=2)) or 
                                   (source in ({str(items_list)[1:-1]}) AND (increase=0 or increase=2)))
                                    and dateoperation Between \'{SECTION[8]}\' and \'{SECTION[9]}\'), 
                            (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                WHERE ((item_id in ({str(items_list)[1:-1]}) AND (increase=0 or increase=3)) or
                                    (source in ({str(items_list)[1:-1]}) AND (increase=1 or increase=3)))
                                    and dateoperation Between \'{SECTION[8]}\' and \'{SECTION[9]}\'),

                            (SELECT nametypeitems FROM typeitems WHERE id = {SECTION[1]})
                            FROM items WHERE typeitem_id = {SECTION[1]} 
                    """

                    data = self.request_sqlite(request)

                    result['initial_balance_item'] = data[0][0] + data[0][1] - data[0][2]
                    result['turnover1'] = data[0][3] - data[0][4]
                    result['turnover2'] = data[0][5] - data[0][6]
                    result['turnover3'] = data[0][7] - data[0][8]
                    result['turnover4'] = data[0][9] - data[0][10]
                    result['final_balance_item'] = result.get('initial_balance_item') + result.get('turnover1') + \
                        result.get('turnover2') + result.get('turnover3') + result.get('turnover4')
                    result['name'] = data[0][11]

                    response_list.append(result)

                    # Раскрыт узел со статьями, добавляем строки с вложенными статьями
                    if SECTION[0] == 1:
                        for ITEM in items_list:
                            result_item = {
                                'is_node': 0, 'node_is_open': 0, 'type_row': 'item', 'name': '',
                                'initial_balance_item': 0, 'turnover1': 0, 'opener1': 0, 'turnover2': 0,
                                'opener2': 0, 'turnover3': 0, 'opener3': 0, 'turnover4': 0, 'opener4': 0,
                                'final_balance_item': 0, 'item': ITEM
                            }

                            request_item = f""" 
                                SELECT 
                                    COALESCE(initialbalanceitem, 0),        
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=1 or increase=2)) or 
                                            (source = {ITEM} AND (increase=0 or increase=2)))
                                            and dateoperation Between \'{self.beginDate}\' and 
                                            \'{SECTION[2] - timedelta(1)}\'), 
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=0 or increase=3)) or
                                            (source = {ITEM} AND (increase=1 or increase=3)))
                                            and dateoperation Between \'{self.beginDate}\' and
                                            \'{SECTION[2] - timedelta(1)}\'),

                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=1 or increase=2)) or 
                                            (source = {ITEM} AND (increase=0 or increase=2)))
                                            and dateoperation Between \'{SECTION[2]}\' and \'{SECTION[3]}\'), 
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=0 or increase=3)) or
                                            (source = {ITEM} AND (increase=1 or increase=3)))
                                            and dateoperation Between \'{SECTION[2]}\' and \'{SECTION[3]}\'),

                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=1 or increase=2)) or 
                                            (source = {ITEM} AND (increase=0 or increase=2)))
                                            and dateoperation Between \'{SECTION[4]}\' and \'{SECTION[5]}\'), 
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=0 or increase=3)) or
                                            (source = {ITEM} AND (increase=1 or increase=3)))
                                            and dateoperation Between \'{SECTION[4]}\' and \'{SECTION[5]}\'),

                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=1 or increase=2)) or 
                                            (source = {ITEM} AND (increase=0 or increase=2)))
                                            and dateoperation Between \'{SECTION[6]}\' and \'{SECTION[7]}\'), 
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=0 or increase=3)) or
                                            (source = {ITEM} AND (increase=1 or increase=3)))
                                            and dateoperation Between \'{SECTION[6]}\' and \'{SECTION[7]}\'),

                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=1 or increase=2)) or 
                                            (source = {ITEM} AND (increase=0 or increase=2)))
                                            and dateoperation Between \'{SECTION[8]}\' and \'{SECTION[9]}\'), 
                                    (SELECT COALESCE(sum(sumoperation), 0) FROM notes 
                                        WHERE ((item_id = {ITEM} AND (increase=0 or increase=3)) or
                                            (source = {ITEM} AND (increase=1 or increase=3)))
                                            and dateoperation Between \'{SECTION[8]}\' and \'{SECTION[9]}\'),

                                    (SELECT nameitem FROM items WHERE id = {ITEM})
                                    FROM items 
                                    WHERE id = {ITEM} 
                            """

                            data = self.request_sqlite(request_item)

                            result_item['initial_balance_item'] = data[0][0] + data[0][1] - data[0][2]
                            result_item['turnover1'] = data[0][3] - data[0][4]
                            result_item['turnover2'] = data[0][5] - data[0][6]
                            result_item['turnover3'] = data[0][7] - data[0][8]
                            result_item['turnover4'] = data[0][9] - data[0][10]
                            result_item['final_balance_item'] = result_item.get('initial_balance_item') + \
                                result_item.get('turnover1') + result_item.get('turnover2') + \
                                result_item.get('turnover3') + result_item.get('turnover4')
                            result_item['name'] = data[0][11]

                            # Если по статьям были обороты, то устанавливаем атрибут opener == 1, чтобы
                            # можно было посмотреть реестр с расшифровкой операций
                            if data[0][3] != 0 or data[0][4] != 0:
                                result_item['opener1'] = 1
                            if data[0][5] != 0 or data[0][6] != 0:
                                result_item['opener1'] = 1
                            if data[0][7] != 0 or data[0][8] != 0:
                                result_item['opener1'] = 1
                            if data[0][9] != 0 or data[0][10] != 0:
                                result_item['opener1'] = 1

                            response_list.append(result_item)

        # Расчет результирующих строк и собственного капитала
        income, expenditure = 0, 0
        active = list()
        passive = list()

        for ROW in response_list:

            if ROW.get('type_item') == 1:
                income = ROW

            if ROW.get('type_item') == 2:
                expenditure = ROW

            if ROW.get('type_item') in (3, 4, 5, 6):
                active.append(ROW)

            if ROW.get('type_item') in (7, 8):
                passive.append(ROW)

        # Строка с прибылью и убытком
        result_profit = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'result', 'name': 'Прибыль/Убыток',
            'initial_balance_item': income.get('initial_balance_item') - expenditure.get('initial_balance_item'),
            'turnover1': income.get('turnover1') - expenditure.get('turnover1'),
            'turnover2': income.get('turnover2') - expenditure.get('turnover2'),
            'turnover3': income.get('turnover3') - expenditure.get('turnover3'),
            'turnover4': income.get('turnover4') - expenditure.get('turnover4'),
            'final_balance_item': income.get('final_balance_item') - expenditure.get('final_balance_item'),
            'type_item': 0
        }
        response_list.insert(0, result_profit)

        # Строка Актива
        result_active = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'aktiv', 'name': 'АКТИВ',
            'initial_balance_item':
                active[0].get('initial_balance_item') + active[1].get('initial_balance_item') +
                active[2].get('initial_balance_item') + active[3].get('initial_balance_item'),
            'turnover1':
                active[0].get('turnover1') + active[1].get('turnover1') + active[2].get('turnover1') +
                active[3].get('turnover1'),
            'turnover2':
                active[0].get('turnover2') + active[1].get('turnover2') + active[2].get('turnover2') +
                active[3].get('turnover2'),
            'turnover3':
                active[0].get('turnover3') + active[1].get('turnover3') + active[2].get('turnover3') +
                active[3].get('turnover3'),
            'turnover4':
                active[0].get('turnover4') + active[1].get('turnover4') + active[2].get('turnover4') +
                active[3].get('turnover4'),
            'final_balance_item':
                active[0].get('final_balance_item') + active[1].get('final_balance_item') +
                active[2].get('final_balance_item') + active[3].get('final_balance_item'),
            'type_item': 0
        }
        ind = 0
        for ROW in response_list:
            ind += 1
            if ROW.get('type_row') == 'section' and ROW.get('type_item') == 3:
                response_list.insert(ind-1, result_active)
                break
        # Строка пассива
        result_passive = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'passiv', 'name': 'ПАССИВ',
            'initial_balance_item': result_active.get('initial_balance_item'),
            'turnover1': result_active.get('turnover1'),
            'turnover2': result_active.get('turnover2'),
            'turnover3': result_active.get('turnover3'),
            'turnover4': result_active.get('turnover4'),
            'final_balance_item': result_active.get('final_balance_item'),
            'type_item': 0
        }

        ind = 0
        for ROW in response_list:
            ind += 1
            if ROW.get('type_row') == 'section' and ROW.get('type_item') == 7:
                response_list.insert(ind-1, result_passive)
                break

        # Строка заемных средств
        result_borrowed_money = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'result', 'name': 'Заёмные средства',
            'initial_balance_item': passive[0].get('initial_balance_item') + passive[1].get('initial_balance_item'),
            'turnover1': passive[0].get('turnover1') + passive[1].get('turnover1'),
            'turnover2': passive[0].get('turnover2') + passive[1].get('turnover2'),
            'turnover3': passive[0].get('turnover3') + passive[1].get('turnover3'),
            'turnover4': passive[0].get('turnover4') + passive[1].get('turnover4'),
            'final_balance_item': passive[0].get('final_balance_item') + passive[1].get('final_balance_item'),
            'type_item': 0
        }
        response_list.append(result_borrowed_money)

        # Строка с собственным капиталом
        result_own_capital = {
            'is_node': 0, 'node_is_open': 0, 'type_row': 'section', 'name': 'Собственный капитал',
            'initial_balance_item':
                result_passive.get('initial_balance_item') - result_borrowed_money.get('initial_balance_item'),
            'turnover1': result_profit.get('turnover1'),
            'turnover2': result_profit.get('turnover2'),
            'turnover3': result_profit.get('turnover3'),
            'turnover4': result_profit.get('turnover4'),
            'final_balance_item':
                result_passive.get('final_balance_item') - result_borrowed_money.get('final_balance_item'),
            'type_item': 9
        }
        response_list.append(result_own_capital)

        return response_list
