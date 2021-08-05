import os

RED = '\x1b[1;91m'
BLUE = '\033[1;94m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
ENDC = '\033[0m'

def title():
    print(RED + '''
    Title: 常见的IP格式脚本
    Version: KiteCollection V1.0
    ''' + ENDC)

def len_split(): #适用场景 10010-11010

        return lenss_s

def douhao_split(): # 适用场景 111.111.111.111,111,111,111,112
    with open('./urls_1.txt','r') as f:
        urls = f.read().splitlines() # 去掉\n
        for i in range(0,len(urls)):
            if ',' in urls[i]:
                url_new = urls[i].replace(',','\n')
                with open('./urls_1_output.txt', 'a+') as f:
                    f.write(url_new + '\n')
            else:
                with open('./urls_1_output.txt', 'a+') as f:
                    f.write('\n' + urls[i])

def ip_split_one(): #适用场景 111.111.111.111-111.111.111.129
    with open('./urls_2.txt','r') as f:
        urls = f.read().splitlines() # 去掉\n
        for i in range(0,len(urls)):
            if '-' in urls[i]:
                urls_split = urls[i].split('-')
                urls_split_dian1 = urls_split[0].split('.')
                urls_split_dian1_4 = urls_split_dian1[3]
                urls_split_dian2 = urls_split[1].split('.')
                urls_split_dian2_4 = urls_split_dian2[3]
                dian_len = int(urls_split_dian2_4) - int(urls_split_dian1_4)  # 这里提取前后的第四个ip段，转为整型相减
                # print(dian_len)
                url_get1 = urls_split_dian1[0] + '.' + urls_split_dian1[1] + '.' + urls_split_dian1[2] + '.' # 拼接前三个ip段。如58.221.91.
                # print(url_get1)
                for i in range(0,dian_len+1): # 循环递增并补上第四个ip段
                    url_four = int(urls_split_dian1[3]) + i
                    # print(url_four)
                    url_new_get = url_get1 + str(url_four)
                    # print(url_new_get)
                    with open('./urls_2_output.txt','a+') as f:
                        f.write(url_new_get + '\n' )
            else:
                with open('./urls_2_output.txt', 'a+') as f:
                    f.write(urls[i] + '\n')


def add_head_http():
    http_ip = ''
    with open('./urls_3.txt', 'r') as f:
        for i in range(1,100):
            line = f.readline()
            if  'http' in line:
                continue
            else:
                if line == '':
                    break
                else:
                    http_ip += 'http://' + line
        print(http_ip)
    with open('./urls_3_output.txt', 'w+') as f:
        f.write(http_ip)

if __name__ == '__main__':
    title()
    print( BLUE +("""
    1 = [逗号分割-url，常见场景如：192.168.1.0,192.168.1.88]
    2 = [横线分割，常见场景如：192.168.1.0-192.168.1.88]
    3 = [添加http头，场景场景如：10.30.1.1:8000]
    """) + ENDC)
    #
    # print( RED + 'URL格式:http:xxx.xxx.xx.xx' + ENDC)
    # print( RED + 'Cookie格式: USER_NAME_COOKIE=admin; OA_USER_ID=admin; PHPSESSID=xxxx; SID_1=xxx' + ENDC)
    #
    selection = int(input(GREEN + '请输入你要操作的数字: '+ ENDC))
    if selection == 1:
        print( RED + '请将目标IP放入urls_1.txt,输出结果在urls_1_output.txt' + ENDC)
        input(RED + '按任意键继续' + ENDC)
        douhao_split()
    elif selection == 2:
        print( RED + '请将目标IP放入urls_2.txt,输出结果在urls_2_output.txt' + ENDC)
        input(RED + '按任意键继续' + ENDC)
        ip_split_one()
    elif selection == 3:
        print( RED + '请将目标IP放入urls_3.txt,输出结果在urls_3_output.txt' + ENDC)
        input(RED + '按任意键继续' + ENDC)
        add_head_http()

