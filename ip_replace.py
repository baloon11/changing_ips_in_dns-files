# coding: utf-8
import os

'''
Программа изменяет ip в dns файлах.

Список доменов, превоначальный ip (или страшие байты), новый ip (или страшие байты) -- список replace_list
изначальные dns файлы --папка `old`
обновленные dns файлы --папка `new`
'''

curr_dir=os.path.dirname(os.path.realpath(__file__))
#cleaning `new` directory
new_dir='%s/%s' % (curr_dir,'new')
names = os.listdir(new_dir)
map(lambda name: os.remove('new/'+name),names)

    replace_list=[
                # domain        old high bytes  new high bytes
                ['example1.com','10.10.10.',    '10.10.11.'],
                ['example2.com','12.12.10.',    '12.12.11.']
            ]

for line in replace_list:
    domain=line[0]
    old_part=line[1]
    new_part=line[2]
    old_domain_file=open (curr_dir+'/old/'+domain+'.db','r')
    for old_line in old_domain_file:
        new_domain_file=open (curr_dir+'/new/'+domain+'.db','a')
        if old_part in old_line:
            old_line=old_line.replace(old_part,new_part)
            new_domain_file.write(old_line)
        else:
            new_domain_file.write(old_line)
        new_domain_file.close()
    old_domain_file.close()