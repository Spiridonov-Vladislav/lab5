class FileReader:
    SUPPORTED_FORMATS = [".txt", ".md", ".yaml", ".yml"]

    def __init__(self, content: str, source_path: str = None):
        self.content = content
        self.source_path = source_path

    def display_info(self):
        print(f"Фаил: {self.source_path or 'неизвестен'}")
        print(f"Размер: {len(self.content)} символов")
        print(f"Строк: {len(self.content.splitlines())}")
        # Доступ к атрибуту класса через имя класса
        print(f"Поддерживаемые форматы: {', '.join(FileReader.SUPPORTED_FORMATS)}")

if __name__ == "__main__":

    reader1 = FileReader("Привет, мир!", source_path="hello.txt")
    reader2 = FileReader("# Заголовок", source_path="doc.md")

    # Изменение атрибута класса влияет на ВСЕ экземпляры
    print("=== Добавляем поддержку .json ===\n")
    FileReader.SUPPORTED_FORMATS.append(".json")

    reader1.display_info()
    reader2.display_info()