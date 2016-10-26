# coding = utf -8
# author    Christopher_Lam

# It's main module which include read ini files and connect all modules to finish work.

from ReadEx import ReadExcel
from StructureMessage import StructureMessage
import top.api
import os
import argparse
import configparser
import sys

def ReadIni(ini_address):
    ini = ini_address
    IniAddress = ini + '\\Settings.ini'
    config = configparser.ConfigParser()
    config.read(IniAddress, encoding='utf-8')

    # 读取ini配置变量。极其繁琐，有没有更好的方法？、
    xls_address = config.get('address', 'send_to_addr')
    sheet_num = config.getint('sheet_num', 'send_to_sheet_num')
    people_names = config.get('where_are_their_names_and_phone_numbers', 'name_columns')
    people_phone_numbers = config.getint('where_are_their_names_and_phone_numbers', 'phone_columns')
    pro_designation = config.get('message_module', 'extend_pro_designation')
    pos_designation = config.get('message_module', 'extend_pos_designation')
    message_strings = config.get('message_module', 'extend_message_strings')
    appkey = config.get('extend', 'appkey')
    secrect = config.get('extend', 'secrect')
    temple_code = config.get('extend', 'temple_code')
    sign_name = config.get('extend', 'sign_name')

    return xls_address, sheet_num, people_names, people_phone_numbers, pro_designation, pos_designation, \
        message_strings, appkey, secrect, temple_code, sign_name


# 转义
def TransferredMeaning(address):
    if isinstance(address, str):
        address = address.strip('\\').replace('\\', '\\\\')
        return address
    else:
        print('[*]Your file address is wrong.Find and check.')
        os._exit(0)

def Parser():
    parser = argparse.ArgumentParser(description='Send messages using Alidayu.')
    parser.add_argument('-mh', '--more_help', 'f:一键式，所有配置在settings中设置；'
                                              're:读取excel，包含了读取姓名和手机号；'
                        'ri:读取ini文件；'
                        'sm:构造短信；'
                        'sr:发送短信请求；'
                        '基本步骤：要么一键式直接跑完，要么-ri -re -sm -sr这样的步骤。')
    parser.add_argument('-f', '--fool', help='一键式')
    parser.add_argument('-re', '--read_excel', help='读取excel')
    parser.add_argument('-ri', '--read_ini', help='读取ini文件')
    parser.add_argument('-sm', '--structure_message', help='构造短信')
    parser.add_argument('-sr', '--send_request', help='发送短信请求')
    parser.add_argument('-oi', 'open_ini', help='回显ini文件')
    args = parser.parse_args()

    one_button = args.fool
    read_excel = args.read_excel
    read_ini = args.read_ini
    structure_message = args.structure_message
    send_message = args.send_request
    open_ini = args.open_ini

    return one_button, read_excel, read_ini, structure_message, send_message, open_ini

def RequestForSending(phone_number, sign_name, appkey_num, secret_num, template_code):
    formal_url = 'https://eco.taobao.com/router/rest'
    # test_url = 'https://gw.api.tbsandbox.com/router/rest'
    req = top.api.AlibabaAliqinFcSmsNumSendRequest(formal_url, 80)
    req.set_app_info(top.appinfo(appkey=int(appkey_num), secret=int(secret_num)))  # 申请的appkey，和secret

    req.sms_type = 'normal'  # 固定传入的短信类型
    req.sms_free_sign_name = str(sign_name)  # 签名模板
    req.sms_param = '{\'}'  # 模板中的变量
    req.rec_num = str(phone_number)  # 手机号
    req.sms_template_code = str(template_code)  # 短信模板id
    '''
    这里面一般变动的只有模板中的变量和手机号，为了避免每次都要传入多余的东西，可以把他们分离，不过我懒得分了。。。
    '''

def main():


    default_ini_address = sys.path[0]  # 获取脚本当前路径
    default_ini_address = TransferredMeaning(default_ini_address)

    xls_address, sheet_num, people_names, phone_numbers, pro_designation, pos_designation, message_strings,\
    appkey, secrect, temple_code, sign_name = ReadIni(default_ini_address)
    xls_address = TransferredMeaning(xls_address)

    name_list = ReadExcel(xls_address, sheet_num).get_names(people_names)
    phone_list = ReadExcel(xls_address, sheet_num).get_phones(phone_numbers)

    for name, phone_list in name_list, phone_list:
        message_content = StructureMessage().structure_message(pro_designation, name, pos_designation)




