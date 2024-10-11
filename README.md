# Описание проекта
Необходимо разработать модель классификации, которая на основе различных характеристик мобильного телефона сможет предсказать его ценовой диапазон (price_range). <br/>Целевой переменной является price_range, которая принимает значения от 0 до 3, где: <br/>
• 0: бюджетные телефоны, <br/>
• 1: телефоны низко-среднего сегмента, <br/>
• 2: телефоны среднего и высокого сегмента, <br/>
• 3: премиум телефоны. <br/>
#  Запуск
Для запуска проекта необходимо выполнить следующие команды: <br/>
```
git clone https://github.com/Alexandr-Fenske/IIS-lab1.git
cd IIS-lab1
python -m venv .venv_lr-1
.venv_lr-1/Scripts/activate
pip install -r requirements.txt
```
# Исследование данных
Находится в `./eda/eda.ipynb`. Основные результаты: <br/>
В ходе исследования были проведены действия: <br/>
• Загрузка данных: df = pd.read_csv('../data/train.csv') <br/>
• Была сделана проверка на дубликаты: df.duplicated().sum(). <br/>
Дубликатов не было обнаружено. <br/>
• Для столбцов 'blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi', 'price_range' изменен тип данных на category.
