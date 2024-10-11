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
• Была сделана проверка на дубликаты: df.duplicated().sum(). Дубликатов не было обнаружено. <br/>
• Для столбцов 'blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi', 'price_range' изменен тип данных на category. <br/>
• Для столбцов 'fc', 'int_memory', 'n_cores', 'pc', 'sc_h', 'sc_w', 'talk_time' изменен тип данных на int8. <br/>
• Для столбцов 'battery_power', 'mobile_wt', 'px_height', 'px_width', 'ram' изменен тип данных на int16. <br/>
• Для столбцов 'clock_speed', 'm_dep' изменен тип данных на float16. <br/>
• Были убраны нулевые значения у 'sc_w', 'pc', 'px_height', 'fc'. <br/>

Итоговый размер составил 55.7 KB против 328.3 KB. <br/>
Обработанная выборка сохранена в файл `./data/clean_data.pkl` <br/>

1) Гистограмма распределения мощности батареи:
```
plt.figure(figsize=(6, 4))
plt.hist(df['battery_power'], bins=30, color='blue', edgecolor='black')
plt.title('Distribution of Battery Power')
plt.xlabel('Battery Power')
plt.ylabel('Frequency')
plt.show()
```
![image](https://github.com/user-attachments/assets/364b0988-f4d3-44df-810a-cf86b9f94e65)


