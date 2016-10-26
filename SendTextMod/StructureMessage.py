# coding = utf -8
# author    Christopher_Lam

# if you want to test your message context , you can run this main code below.

class StructureMessage():
    def __init__(self):
        self.designation = []

    def structure_message(self, pro_designation, people_name, pos_designation):

        self.designation.append(pos_designation)
        self.designation.append(pro_designation)
        self.people_name = people_name
        message_strings = self.designation.pop() + self.people_name + self.designation.pop()
        return message_strings

'''
if __name__ == '__main__':
    a = StructureMessage().structure_message('亲爱的', 'Christopher_Lam', '同学')
    print(a)
'''