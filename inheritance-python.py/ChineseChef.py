from Chef import Chef


class ChineseChef(Chef):

    ''' we dont have to define duplicate functions again,
    because we have the inheritance defined. This is the purpose of 
    the inheritance to reduce the duplicate code

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")
    '''

    '''
    we need to overwrite this function, because chinese chef is making 
    different special dish than the Chef class
    '''

    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_friend_rice(self):
        print("The chef makes friend rice")
