import re
for i in range(?): # total number of files
    exampleFile = open(r'news_item_%s.txt' % (i + 1), encoding='utf-8') #a file with a news item
    exampleFile1 = exampleFile.read()
    with open(r'results.txt', 'a', encoding='utf-8') as file: #a file for the results
        print('--------------------------%s--------------------------' % (i+1), file=file)
        with open (r'spelling_new.txt', encoding='utf-8') as f: #a vocabulary with new spelling
            print('***ПРЕФІКСИ***', file=file)
            Ze = re.compile(r'\bпів\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bпів.\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bекс\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bвіце\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bмедіа\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bтоп\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bфлеш\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bміні\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bультра\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)

            print('***ЧЕРЕЗ ДЕФІС***', file=file)

            Ze = re.compile(r'\bпів-\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bекс-\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bвіце-\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bмедіа-\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bтоп-\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bфлеш-\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bміні-\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'\bультра-\w+')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)

            
            print('***ОКРЕМІ СЛОВА***', file=file)

            Ze = re.compile(r'\b\мі[фт]\w\b')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            Ze = re.compile(r'фойє')
            li = Ze.findall(exampleFile1)
            print('\n'.join(li), file=file)
            
            
            new_items = [row.strip() for row in f]
            print('***NEW***', file=file)
            for i in range(len(new_items)):
                ze = re.compile(new_items[i])
                zef = ze.findall(exampleFile1)
       
                for u in zef:
                    p = ('%s' % (u))
                    print(p, file=file)
            
        with open (r'spelling_old.txt', encoding='utf-8') as f:
            print('***OLD***', file=file)  #a vocabulary with old spelling
            old_items = [row.strip() for row in f]
            for i in range(len(old_items)):
                ze = re.compile(old_items[i])
                zef = ze.findall(exampleFile1)
        
                for u in zef:
                    p = ('%s' % (u))
                    print(p, file=file)
