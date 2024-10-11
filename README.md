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

Этот график отображает распределение мощности батареи для мобильных телефонов. По оси X — значения мощности батареи, по оси Y — частота (количество) телефонов с определенной мощностью. <br/>

2)  Столбчатая диаграмма средней цены по наличию двух SIM-карт:
```
plt.figure(figsize=(6, 4))
plt.scatter(df['ram'], df['price_range'], color='purple')
plt.title('RAM vs Price Range')
plt.xlabel('RAM')
plt.ylabel('Price Range')
plt.show()
```
![image](https://github.com/user-attachments/assets/086c5c35-8abe-4b5d-a1ce-86befc3b47ca)

Этот график показывает средний ценовой диапазон телефонов с одной SIM-картой и двумя SIM-картами. По оси X — наличие двойной SIM (0 — одна SIM, 1 — две SIM), по оси Y — средняя цена для каждой категории. <br/>

3) Точечный график зависимости RAM от ценового диапазона:
```
plt.figure(figsize=(6, 4))
plt.plot(df['px_height'], df['px_width'], color='red')
plt.title('Pixel Height vs Pixel Width')
plt.xlabel('Pixel Height')
plt.ylabel('Pixel Width')
plt.show()
```
![image](https://github.com/user-attachments/assets/f72b6508-196d-442a-ab52-aff01c8f4137)

Точечный график показывает зависимость объема оперативной памяти (RAM) от ценового диапазона. По оси X — объем RAM, по оси Y — ценовой диапазон устройства. <br/>

4) Correlation Heatmap (тепловая карта корреляции):
```
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
```
![image](https://github.com/user-attachments/assets/f987a5b5-573a-4f84-8fab-160c6c1439d0)

5) Pair plot (парный график):
 ```
sns.pairplot(df[['ram', 'battery_power', 'price_range']], hue='price_range', palette='coolwarm')
plt.show()
```   
![image](https://github.com/user-attachments/assets/06a7790f-6037-424d-8dd0-55382126ae95)
