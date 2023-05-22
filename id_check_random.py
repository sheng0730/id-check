import random
import sys
arear = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34,
                'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25,
                'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33}

def check(text):
        
        check = False
        text_list = list(text)
        text_arear = str(arear[text_list[0]])

        check_arrar = list(text_arear)
        check_arrar[0] = int(check_arrar[0])
        check_arrar[1] = int(check_arrar[1])*9
        sex = check_arrar[1]
        if sex!='1' and sex!='2':
                check_arrar.append(int(sex)*8)
        for i in range(7):
                check_arrar.append(int(text_list[i+2])*(7-i))
        check_num = 10 - sum(check_arrar) % 10
        if check_num != int(text_list[9]):
                check = True

        if check == False:
                print('fake')
        else:
                print('real')


def output(text_int):
        global id_text
        
        for i in range(text_int):
            ar_text = random.choice(list(arear.keys()))
            check_text = list(str(arear[ar_text]))
            check_text[0] = int(check_text[0])
            check_text[1] = int(check_text[1])*9
            fer_text = random.choice([1, 2])
            check_text.append(fer_text*8)

            num = ""

            for i in range(8):
                nums = random.randint(0, 9)
                num = num+str(nums)
                check_text.append(num*(7-i))
            id_text=str(ar_text)+str(fer_text)+num
                
            print(id_text)
while True:
        print("-------------------\n"+"1:檢查身分證\n"+"2:產生身分證\n"+"3:產生身分證跟檢查\n"+"4:離開\n"+"-------------------")
        idorcheck=str(input())
        match idorcheck:
                case '2':
                        number_inpur=int(input("需要產生多少身份證："))
                        output(number_inpur)
                case '1':
                        id_input=str(input("請輸入身分證："))
                        check(id_input)
                case '3':
                        number_inpur=int(input("要產生多少身份證："))
                        output(number_inpur)
                        check(id_text)  
                case '4':
                    print("bye")
                    exit()

        



