# coding = utf -8
# author    Christopher_Lam

import os

class Counters():

    def __init__(self, send_to_phone):
        self.send_to_phone_count = send_to_phone
        # self.free_phone_count = free_phone
        # self.text_str = text_str

    # count the phone which regist the YIXIN APP.想法不可达，仍需花钱=3=，这个方法可以忽略不用。
    def FreePhoneCounter(self, free_phone, text_str):  # every single phone numbers can send 10 free texts
        self.free_phone_count = free_phone
        self.text_str = text_str
        FreePhoneCount = self.free_phone_count
        text_str = self.text_str
        counts = len(text_str)

        TextContain = 0  # 短信占多少条,仅计算中文。中文每条70字。
        ans = counts / 70
        if ans > 10:
            print('[*]You can\'t use me to send message which more than ten text!')
            os._exit(0)
        elif ans == 0:
            print('[*]Exm? Are you sure you can send message contain nothing? ')
            os._exit(0)

        if counts % 70:
            TextContain = ans + 1
        else:
            TextContain = ans

        how_many_times_can_each_phone_send = 10//TextContain  # 如果占了三条，每个手机号少发一条，直接舍弃
        left_free_text = 10 - how_many_times_can_each_phone_send  # 每个手机号剩余条数
        total = how_many_times_can_each_phone_send * FreePhoneCount
        return total, left_free_text

    # count how many people i should send to
    def SendToCounter(self, free_people):  # free_people接受以上的total参数
        people = self.send_to_phone_count
        send_counts = people
        i_can_only_send = free_people
        if i_can_only_send >= send_counts:
            print('[*]You can send %s people\'s message. Do you want to send now?') %(i_can_only_send)
            return 123
        else:
            print('[*]You can only send %s people\'s message.Do you want to send now?' % (i_can_only_send))
            return 321

if __name__ == '__main__':
    a = Counters(100)
    a1 = a.FreePhoneCounter(100, '123')