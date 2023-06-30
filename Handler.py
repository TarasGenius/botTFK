from onedrivedownloader import download
import os
from openpyxl import load_workbook
import configparser


class AnswersHandler:
    column_value = {}
    _url = 'https://elearninglutsk-my.sharepoint.com/:x:/g/personal/tarasliabuk_tac_lutsk_ua/EWyrLPoLfBlJjzJfN1V4dVYBrvCcXW6T1rZbbXQlT2xlxQ?e=PKXkj2'
    _file_with_answers = 'Bot_Answers.xlsx'
    _col_names = ('B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V')

    def __init__(self):
        self.wb = load_workbook(self._file_with_answers)
        self.worksheet = self.wb.active
        self.get_column(self._col_names)

        # Блок видалення та скачування файлу
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), self._file_with_answers)
        os.remove(path)

        download(url=self._url, filename='')

    # Метод повертає список видаляючи всі елементи з значенняи None
    @staticmethod
    def clear_none_cell(answer_list: list):
        format_list = []
        [format_list.append(item) if item is not None else item for item in answer_list]
        return format_list

    # Створює словник зі всіх колонок
    def get_column(self, col_names):
        for letter in col_names:
            column_list = self.clear_none_cell([item.value for item in self.worksheet[letter]])
            self.column_value[column_list[0]] = column_list[2:]


class HandlerForConfig:
    config_str = ''

    def __init__(self):
        # Отримання значення токена з конфіг файлу
        config = configparser.ConfigParser()
        config.read('config.cfg')
        self.topsecret = config['token']
        self.config_str = self.topsecret['token']

    def get_token(self):
        return self.config_str
