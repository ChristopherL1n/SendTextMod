# coding = utf -8
# author    Christopher_Lam

import xlrd
# get their names and phones
class ReadExcel():

    def __init__(self, address, the_num_of_sheet=0):
        num = the_num_of_sheet
        if isinstance(num, int) and isinstance(address, str):  # 确保用户输入
            self.sheet_num = num
            self.address = address
        else:
            print('[*]Check your xls file address or the num of sheet you\'ve input. ')

# Read the sheet and count the nums of phone.
    def ReadSheet(self):
        where_is_the_xls = self.address
        which_sheet_i_choose = self.sheet_num  # 选择哪个sheet，ini中配置
        data = xlrd.open_workbook(where_is_the_xls)
        table = data.sheets()[which_sheet_i_choose]  # 获取表

        show_me_lines = table.nrows  # 行数
        # show_me_columns = table.ncols
        return table,show_me_lines

        '''# get phone nums
        phone_nums = []
        for counts in range(show_me_lines):
            #table.cell_value((x,0) for x in (range(show_me_lines)))
            phone_nums.append(table.cell(counts,1))
        # print(phone_nums)
        return phone_nums
'''
    def get_phones(self, which_columns_i_choose = 1):
        # addre = self.address
        table, show_me_lines = self.ReadSheet()
        self.columns = which_columns_i_choose
        phone_nums = []
        for counts in range(show_me_lines):
            phone_nums.append(table.cell(counts, self.columns))
        return phone_nums
    def get_names(self, which_columns_i_choose = 0):
        # self.addr = address
        # addr = self.addr
        self.columns = which_columns_i_choose
        table, show_me_lines = self.ReadSheet()
        person_names = []
        for counts in range(show_me_lines):
            person_names.append(table.cell(self.columns, counts))
        return person_names

    def write_excel(self):
        pass

'''
# test code below
if __name__ == '__main__':
    # there are test codes below
    addr = 'C:\\Users\\Vincent\\Desktop\\123.xls'
    a = ReadExcel(addr,the_num_of_sheet=0)  # 这里的 addr 和 the num of sheet可以在ini文件中配置
    phones = a.get_phones()
    names = a.get_names()
    print(phones,names)
'''
