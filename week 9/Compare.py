import pandas as pd
class Compare:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.df1 = None
        self.df2 = None
    def load_data(self):
        try:
            self.df1 = pd.read_csv(self.file1, usecols=[0])
            self.df2 = pd.read_csv(self.file2, usecols=[0])
        except FileNotFoundError as e:
            print(f"Ошибка: Файл не найден — {e}")
        except Exception as e:
            print(f"Произошла ошибка при загрузке: {e}")
    def compare_columns(self):
        if self.df1 is None or self.df2 is None:
            print("Сравнение невозможно: данные не загружены.")
            return
        if self.df1.equals(self.df2):
            print("Столбцы идентичны.")
        else:
            print("Найдены расхождения в столбцах.")
start = Compare("metrics.csv","regions.csv")
start.load_data()
start.compare_columns()