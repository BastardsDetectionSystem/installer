# -*- coding: utf-8 -*-
import os, shutil

#установка програм
programinstall = os.system ('apt-get install minicom monit nload mc htop nmap ifenslave atop sudo vlan mtr snmpd libsnmp-dev wget cmake -y')

#настройка lacp с копирование фала интерфейсов в рабочую папку пользователя.
configurelacp = raw_input ('customize LACP : yes ? \n')
if configurelacp == 'yes':
		lacp = os.system('cp /etc/network/interfaces /home/melon/interfaces')
		lacp = os.system('rm -f /etc/network/interfaces')
		lacp = os.system('cp /home/melon/python/install/lacpconfig/interfaces /etc/network/interfaces')
		print('program install, lacp configured')

elif configurelacp != 'yes':
		print('program no install, lacp no configured')

#установка астры и копировние конфигов.	
configuredastra = raw_input ('customize astra :yes? \n')
if configuredastra == 'yes':
		astra = os.system('wget http://dev.cesbo.com/download/astra/4.4.182/free/x86/linux-64bit/astra')
        astra = os.system('chmod +x astra')
        astra = os.system('mv astra /usr/bin')
        astra = os.system('mkdir /etc/astra')
        astra = ('/home/melon/python/install/astraconfig/') 
        names = os.listdir(astra) #список файлов и поддиректорий в данной директории.
        for name in names:
		fullname = os.path.join(astra, name) #получаем полное имя из директории.
                shutil.copy(fullname, '/etc/astra/') #копируем файлы в нужную директорию.

elif configuredastra != 'yes':
		print('astra no installed end configured')

#настройка монита
configuredmonit = raw_input ('configure monit :yes? \n')
if configuredmonit = 'yes':
        monit = shutil.copy(r'/home/melon/python/install/monit/monitconfig/astra', r'/etc/monit/conf.d/')
        monit = os.system('rm -f /etc/monit/monitrc')
        monit = shutil.copy(r'/home/melon/python/install/monit/monitconfig/monitrc', r'/etc/monit/')
        monit = shutil.copy(r'/home/melon/python/install/monit/monitconfig/monit', r'/usr/bin')
        monit = os.system('chmod +x /usr/bin/monit')
        monitdefault = shutil.copy(r'/home/melon/python/install/monit/monitdefault/monit', r'/etc/default/')

elif configuredmonit !='yes'
		print('monit not configured')

#перезагрузка сервера после установки всех нужных капонентов.		
reboot = raw_input ('reboot server :yes? \n')
if reboot == 'yes':
		boot = os.system('reboot')
elif reboot != 'yes':
		print('server reboot leter')
		
