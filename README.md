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

### Закономерности: <br/>
Большинство устройств имеют мощность батареи в пределах среднего диапазона. Меньшее количество устройств имеет как очень низкую, так и очень высокую мощность батареи.
Пик распределения находится примерно в диапазоне 1000-1500 мАч, что указывает на то, что большинство телефонов попадают в этот сегмент.
### Выводы: <br/>
Телефоны с батареями средней мощности преобладают на рынке, что может говорить о предпочтениях производителей или потребителей.
Устройства с батареями с очень низкой или очень высокой мощностью менее распространены, возможно, из-за специфики спроса или стоимости производства.

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

### Закономерности: <br/>
Столбчатая диаграмма показывает, что устройства с двумя SIM-картами в среднем попадают в более высокий ценовой диапазон, чем устройства с одной SIM-картой.
Телефоны, поддерживающие только одну SIM-карту, имеют более низкую среднюю цену.

### Выводы: <br/>
Наличие двух SIM-карт оказывает влияние на ценовую категорию устройства. Это может быть связано с тем, что телефоны с поддержкой двух SIM-карт часто имеют более современные функции или рассчитаны на более требовательных пользователей.

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

### Закономерности: <br/>
График четко показывает положительную корреляцию между объемом оперативной памяти (RAM) и ценовым диапазоном: устройства с большим объемом RAM чаще попадают в более высокий ценовой сегмент.
Чем больше оперативной памяти у телефона, тем выше его цена. Устройства с RAM около 3000 МБ и выше обычно находятся в высшем ценовом диапазоне (ценовая категория 3).
Устройства с небольшим объемом RAM (например, около 500-1000 МБ) почти всегда находятся в низких ценовых категориях.

### Выводы: <br/>
Объем оперативной памяти является одним из ключевых факторов, влияющих на цену мобильного телефона. Это объясняет, почему более дорогие устройства оснащены большими объемами RAM, чтобы удовлетворить спрос на производительность.

4) Correlation Heatmap (тепловая карта корреляции):
```
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
```
![image](https://github.com/user-attachments/assets/f987a5b5-573a-4f84-8fab-160c6c1439d0)

Correlation Heatmap — это визуальное представление корреляционной матрицы, которое показывает, насколько сильна связь между различными переменными в наборе данных.Каждая ячейка тепловой карты отображает коэффициент корреляции для пары переменных.

### Закономерности: <br/>
Высокая корреляция между RAM и ценовым диапазоном (price_range): Коэффициент корреляции между этими переменными очень высокий и положительный (близкий к 0.9). Это говорит о том, что телефоны с большей оперативной памятью (RAM) чаще находятся в более высоких ценовых категориях.
Слабая корреляция между тактовой частотой процессора (clock_speed) и ценой: Корреляция между clock_speed и price_range очень слабая (близкая к 0), что говорит о том, что тактовая частота не является значимым фактором, влияющим на цену мобильных телефонов.
Положительная корреляция между мощностью батареи (battery_power) и ценой: Хотя корреляция между battery_power и price_range не такая сильная, как у RAM, она положительная (~0.5), что означает, что устройства с более мощными батареями чаще находятся в более высоких ценовых категориях.
Отрицательная корреляция между весом устройства (mobile_wt) и ценой: Хотя корреляция незначительная, видно, что устройства, которые легче, чаще попадают в более высокие ценовые диапазоны (слабая отрицательная корреляция).

### Выводы: <br/>
Оперативная память (RAM) является самым важным показателем, сильно влияющим на цену телефона.
Мощность батареи также оказывает влияние на цену, но не столь значительное, как оперативная память. Это объясняет, почему устройства с более мощной батареей могут стоить дороже, но этот параметр не является главным фактором.
Тактовая частота процессора (clock_speed) и вес устройства (mobile_wt) имеют слабую корреляцию с ценой, что указывает на то, что они не являются основными характеристиками, влияющими на стоимость телефона.

5) Pair plot (парный график):
 ```
sns.pairplot(df[['ram', 'battery_power', 'price_range']], hue='price_range', palette='coolwarm')
plt.show()
```   
![image](https://github.com/user-attachments/assets/06a7790f-6037-424d-8dd0-55382126ae95)

### Закономерности: <br/>
Корреляция между RAM и ценовым диапазоном: при увеличении объема RAM устройства его ценовая категория также возрастает. Графики рассеяния для ram и price_range показывают четко выраженную тенденцию: телефоны с большим объемом RAM (3000-4000 МБ) относятся к высшим ценовым категориям, тогда как устройства с малым объемом RAM находятся в низших ценовых категориях. <br/>
Корреляция между мощностью батареи (battery_power) и ценой: График рассеяния между battery_power и price_range показывает более размытые данные, но также можно заметить тенденцию: устройства с более мощными батареями чаще попадают в высокие ценовые категории. Но связь менее явная, чем у RAM. <br/>
Распределения признаков: По диагонали парного графика отображаются гистограммы распределения каждого признака. Здесь видно, что распределение RAM значительно различается для разных ценовых категорий: более дорогие телефоны имеют больший объем RAM, тогда как дешевые телефоны сгруппированы в нижней части диапазона.

### Выводы: <br/>
На парном графике особенно видно, что оперативная память (RAM) является ключевым фактором, определяющим ценовую категорию телефона. <br/>
Мощность батареи также оказывает влияние на цену телефона, хотя его корреляция с ценой не столь сильна. Тем не менее, устройства с мощной батареей чаще попадают в более дорогие ценовые категории, что подтверждает тенденцию, заметную на тепловой карте. <br/>

6) Зависимость объема оперативной памяти (RAM) от ценового диапазона:
 ```
p1 = figure(title="RAM vs Price Range", x_axis_label="RAM (MB)", y_axis_label="Price Range",
 tools="pan,wheel_zoom,box_zoom,reset,hover", tooltips=[("RAM", "@ram"), ("Price Range", "@price_range")])
p1.circle('ram', 'price_range', size=8, source=source, color="navy", alpha=0.6)

show(p1)
```
![image](https://github.com/user-attachments/assets/591abd61-df23-4443-b5cc-4fa57ed804a0)

### Закономерности: <br/>
Зависимость между объемом оперативной памяти (RAM) и ценовым диапазоном (Price Range) четко выражена. Чем больше объем RAM, тем выше ценовая категория устройства.
Телефоны с низким объемом оперативной памяти (например, 512 МБ или 1 ГБ) обычно попадают в самые низкие ценовые диапазоны.
Устройства с большим объемом RAM (например, 4 ГБ и выше) чаще находятся в более высоких ценовых категориях.

### Выводы: <br/>
Объем оперативной памяти является одним из ключевых факторов, определяющих ценовую категорию телефона. Это связано с тем, что телефоны с большим объемом RAM обладают лучшей производительностью, что приводит к их более высокой цене.

7) Зависимость Зависимость мощности батареи от ценового диапазона:
 ```
p2 = figure(title="Battery Power vs Price Range", x_axis_label="Battery Power (mAh)", y_axis_label="Price Range",
            tools="pan,wheel_zoom,box_zoom,reset,hover", tooltips=[("Battery Power", "@battery_power"), ("Price Range", "@price_range")])
p2.circle('battery_power', 'price_range', size=8, source=source, color="green", alpha=0.6)

show(p2)
```
![image](https://github.com/user-attachments/assets/c48f3448-89b4-4927-b9d6-aea035afdc48)

### Закономерности: <br/>
Телефоны с большей мощностью батареи, как правило, относятся к более высоким ценовым диапазонам, но эта зависимость не так сильно выражена, как у RAM.
Устройства с маленькой батареей (например, 1200-1500 мАч) чаще находятся в низких ценовых категориях.
Устройства с батареей 2500 мАч и выше чаще принадлежат к средним и высоким ценовым категориям.

### Выводы: <br/>
Мощность батареи влияет на ценовую категорию телефона, но не так явно, как объем оперативной памяти. Устройства с более мощной батареей, вероятно, обладают лучшими характеристиками и позиционируются как более дорогие модели.

8) Зависимость тактовой частоты процессора от ценового диапазона:
```
p3 = figure(title="Clock Speed vs Price Range", x_axis_label="Clock Speed (GHz)", y_axis_label="Price Range",
            tools="pan,wheel_zoom,box_zoom,reset,hover", tooltips=[("Clock Speed", "@clock_speed"), ("Price Range", "@price_range")])
p3.circle('clock_speed', 'price_range', size=8, source=source, color="red", alpha=0.6)

show(p3)
```
![image](https://github.com/user-attachments/assets/9d7ac601-1637-4991-b852-1cbb848e5e2d)

### Закономерности: <br/>
Зависимость между тактовой частотой процессора (Clock Speed) и ценовым диапазоном менее выражена по сравнению с RAM и Battery Power.
Устройства с низкой тактовой частотой (около 0.5-1.0 ГГц) обычно находятся в низких и средних ценовых диапазонах.
Устройства с тактовой частотой процессора около 2.0 ГГц и выше могут попадать в более высокие ценовые диапазоны, но зависимости здесь менее выражены.

### Выводы: <br/>
Тактовая частота процессора влияет на ценовую категорию, но эта зависимость не так сильно выражена, как у других характеристик, таких как RAM. 
Модели с более высокой тактовой частотой могут находиться как в среднем, так и в высоком ценовом сегменте, однако данный параметр не является единственным критерием для определения ценовой категории.

## Общие выводы: <br/>
- Оперативная память (RAM) является самым важным показателем, влияющим на цену телефона. Чем больше оперативной памяти у устройства, тем выше его цена. <br/>
- Мощность батареи также влияет на ценовую категорию, хотя и не так сильно, как RAM. Она может служить дополнительным признаком для классификации. <br/>
- Тактовая частота процессора и вес телефона имеют слабую корреляцию с ценой и не являются основными характеристиками для предсказания ценовой категории, что можно учитывать при оптимизации моделей. <br/>

# Запуск MLFlow
1. Перейти в директорию ./mlflow:
```
   cd mlflow/
```
2. Выполнить скрипт для запуска сервера:
```
   sh run.sh
```
# Результаты исследования
Лучший результат показала модель rfe_sfs_feature_selection:

Метрики:
• pression: 0.9058798186142433 <br/>
• recall: 0.9025787965616046 <br/>
• f1: 0.9030920972173959 <br/>

```
   run_id = "7617979ddc414cccb6465d6d1cfc02b7"
```
