import pickle
from warnings import catch_warnings


class Records:
    """Класс для управления записями игр."""

    def __init__(self):
        """Инициализирует класс Records и загружает существующие записи."""

        with open('game_results.txt', 'rb') as file:
            try:
                self.records = pickle.load(file)
            except Exception as e:
                self.records = {}

    def save_records_to_file(self):
        """Сохраняет текущие записи в файл."""

        with open('game_results.txt', 'wb') as file:
            pickle.dump(self.records, file)

    def save_record(self, complexity, level, value):
        """Сохраняет новую запись, если она лучше существующей."""

        level_key = self.get_level_key( complexity, level)
        if level_key in self.records:
            if value < self.records[level_key]:
                self.records[level_key] = value
                self.save_records_to_file()
        else:
            self.records[level_key] = value
            self.save_records_to_file()


    def get_record(self, complexity, level):
        """Получает запись для заданной сложности и уровня."""

        level_key = self.get_level_key(complexity, level)
        return self.records.get(level_key)

    def get_level_key(self,complexity, level):
        """Генерирует ключ для записи на основе сложности и уровня."""

        return f'level_{complexity}_{level}'


