import re
for i in range(41):
    exampleFile = open(r'file_with_news_items_%s.txt' % (i + 1), encoding='utf-8')
    exampleFile1 = exampleFile.read()
    with open(r'results_old_spelling.txt', 'a', encoding='utf-8') as file:
        ex = re.compile(r'\bекс-\w+')
        ex_t = ex.findall(exampleFile1)
        vice = re.compile(r'\bвіце-\w+')
        vice_t = vice.findall(exampleFile1)
        ex_t.extend(vice_t)
        media = re.compile(r'\bмедіа-\w+')
        media_t = media.findall(exampleFile1)
        ex_t.extend(media_t)
        top = re.compile(r'\bтоп-\w+')
        top_t = top.findall(exampleFile1)
        ex_t.extend(top_t)
        pres = re.compile(r'\bпрес-\w+')
        pres_t = pres.findall(exampleFile1)
        ex_t.extend(pres_t)
        mini = re.compile(r'\bміні-\w+')
        mini_t = mini.findall(exampleFile1)
        ex_t.extend(mini_t)
        web = re.compile(r'\bвеб-\w+')
        web_t = web.findall(exampleFile1)
        ex_t.extend(web_t)
        top = re.compile(r'\bтоп-\w+')
        top_t = top.findall(exampleFile1)
        ex_t.extend(top_t)
        result = '\n'.join(ex_t)
        print(result, file=file)
    with open(r'results_all_21.txt', 'a', encoding='utf-8') as file:
        ex = re.compile(r'\bекс\w+')
        ex_t = ex.findall(exampleFile1)
        vice = re.compile(r'\bвіце\w+')
        vice_t = vice.findall(exampleFile1)
        ex_t.extend(vice_t)
        media = re.compile(r'\bмедіа\w+')
        media_t = media.findall(exampleFile1)
        ex_t.extend(media_t)
        top = re.compile(r'\bтоп\w+')
        top_t = top.findall(exampleFile1)
        ex_t.extend(top_t)
        pres = re.compile(r'\bпрес\w+')
        pres_t = pres.findall(exampleFile1)
        ex_t.extend(pres_t)
        mini = re.compile(r'\bміні\w+')
        mini_t = mini.findall(exampleFile1)
        ex_t.extend(mini_t)
        web = re.compile(r'\bвеб\w+')
        web_t = web.findall(exampleFile1)
        ex_t.extend(web_t)
        top = re.compile(r'\bтоп\w+')
        top_t = top.findall(exampleFile1)
        ex_t.extend(top_t)
        result = '\n'.join(ex_t)
        print(result, file=file)

exampleFile = open(r'results_all_21.txt', encoding='utf-8')
exampleF = exampleFile.read()
stoplist = set('''
вебінару
ексклаву
ексклюзивний
ексклюзивним
ексклюзивних
ексклюзивні
ексклюзивному
екскурсій
екскурсійне
екскурсію
експансивної
експансії
експансіоністська
експансіоністський
експансіоністську
експансія
експедиції
експедицій
експедицію
експерестест
експеримент
експериментальний
експериментальними
експериментальних
експериментально
експериментального
експериментах
експерименти
експериментів
експериментом
експерименту
експерт
експерта
експертам
експертами
експерти
експертиз
експертиза
експертизами
експертизи
експертизі
експертизу
експертів
експертка
експерткою
експертна
експертних
експертні
експертній
експертно
експертного
експертної
експертною
експертну
експертом
експерту
експлуатацією
експлуатації
експлуатаційник
експлуатаційних
експлуатацію
експлуатували
експлуатувати
експлуатують
експозиції
експозицію
експозиція
експонатів
експонуватися
експонує
експорт
експортера
експортерам
експортерів
експортером
експортний
експортним
експортними
експортних
експортні
експортній
експортно
експортного
експортної
експортному
експортну
експортовано
експортом
експортоорієнтованого
експорту
експортувала
експортувати
експортує
експрес
експресії
експрестестів
експресуються
екстенсивний
екстрадиції
екстрадицію
екстрадиціювали
екстрадують
екстракорпорального
екстракт
екстраординарна
екстраординарні
екстраполюється
екстремальними
екстремальних
екстремальної
екстремізму
екстремістами
екстремісти
екстремістів
екстремістський
екстремістським
екстремістськими
екстремістські
екстремістського
екстремістської
екстремістському
екстремістською
екстремістську
екстремітсткімі
екстрене
екстрений
екстрених
екстрені
екстрено
екстреного
екстреної
екстреному
екстреною
ексцентрики
ексцесом
медіації
мініатюрі
мініатюрних
мінімалістично
мінімалка
мінімалки
мінімальна
мінімальне
мінімальний
мінімальними
мінімальних
мінімальні
мінімально
мінімального
мінімальної
мінімальному
мінімальною
мінімальну
мінімізації
мінімізацію
мінімізація
мінімізували
мінімізувати
мінімізують
мінімізуються
мінімум
мінімуми
мінімумів
мінімуму
міністерка
міністерки
міністеркою
міністерств
міністерства
міністерствам
міністерствами
міністерстваприйшли
міністерствах
міністерстві
міністерство
міністерством
міністерству
міністерських
міністерські
міністерській
міністерському
міністр
міністра
міністрам
міністрами
міністрамі
міністрах
міністри
міністрів
міністрові
міністром
міністру
преса
преси
пресинг
пресингу
пресингує
пресі
пресою
пресрелізи
престиж
престижного
престижної
престижності
престижною
престижну
престижу
престол
престолів
топа
топі
топку
топовий
топових
топографії
топографія
топоніми
топонімії
топтати
топу
'''.split('\n'))
new_text = [word for word in exampleF.split() if word not in stoplist]
new_text_1 = ' '.join(new_text)
with open(r'results_new_spelling.txt', 'a', encoding='utf-8') as file:
    print(new_text_1, file=file)

newfile = open(r'results_new_spelling.txt', 'r')
read_data = newfile.read()
per_wordN = read_data.split()
oldfile = open(r'results_old_spelling.txt', 'r')
read_data = oldfile.read()
per_wordO = read_data.split()

print('NEW international component:', len(per_wordN))
print('OLD international component:', len(per_wordO))


import re
for i in range(41):
    exampleFile = open(r'file_with_news_items_%s.txt' % (i + 1), encoding='utf-8')
    exampleFile1 = exampleFile.read()
    with open(r'results_old_piv_all.txt', 'a', encoding='utf-8') as file:
        pivO = re.compile(r'\bпів\w+')
        pivO_t = pivO.findall(exampleFile1)
        print('\n'.join(pivO_t), file=file)
    with open(r'results_new_piv.txt', 'a', encoding='utf-8') as file:
        pivN = re.compile(r' пів\s\w+')
        pivN_t = pivN.findall(exampleFile1)
        print('\n'.join(pivN_t), file=file)
exampleFile = open(r'results_old_piv_all.txt', encoding='utf-8')
exampleF = exampleFile.read()
stoplist = set('''
півгодинні
півгодинну
південна
південний
південних
південні
південній
південно
південноафриканський
південноафриканській
південного
південноєвропейських
південної
південнокорейського
південному
південну
південь
півдні
півдня
півдорозі

півкулі
півкуль
північ
північна
північний
північних
північні
північній
північніше
північно
північноамериканського
північноатлантичного
північного
північної
північнокорейська
північнокорейський
північнокорейськими
північнокорейські
північнокорейського
північнокорейської
північному
північчю
півночі
півострів
півострова
півострові
півостровом
півострову
піврічними
півріччі
півріччя
півтора
півтораразовому
півторарічних
півтори
'''.split('\n'))
new_text = [word for word in exampleF.split() if word not in stoplist]
new_text_1 = ' '.join(new_text)
with open(r'E:\py_files\Belapan\spelling\results_old_piv.txt', 'a', encoding='utf-8') as file:
    print(new_text_1, file=file)
    
newfile = open(r'E:\py_files\Belapan\spelling\results_new_piv.txt', 'r')
read_data = newfile.read()
per_wordN = read_data.split()
oldfile = open(r'E:\py_files\Belapan\spelling\results_old_piv.txt', 'r')
read_data = oldfile.read()
per_wordO = read_data.split()

print('NEW piv:', len(per_wordN))
print('OLD piv:', len(per_wordO))
