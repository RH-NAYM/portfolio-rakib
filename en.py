
class MYINFO:
    def __init__(self):
        self.data = {
                        "a":"qwpi ",
                        "b":"sokax ",
                        "c":"czji ",
                        "d":"hvkt",
                    }
        
    def get_data(self):
        my_data = []
        for i in self.data:
            my_data.append(self.data[i])

        result = ''.join(my_data)
        return result