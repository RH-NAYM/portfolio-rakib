class MYINFO:
    def __init__(self):
        self.mail = {
                        "a":"umni ",
                        "b":"eonm ",
                        "c":"ninr ",
                        "d":"smyc",
                    }
        
        self.map = {
            "a":"AIzaSyCKzT",
            "b":"gBxJhVdjP",
            "c":"CSMV1AJUxGB",
            "d":"oGHugBGcI",
        }
        
    def get_data(self):
        my_data = []
        for i in self.mail:
            my_data.append(self.mail[i])

        result = ''.join(my_data)
        return result
    
    
    def get_map(self):
        my_data = []
        for i in self.map:
            my_data.append(self.map[i])

        result = ''.join(my_data)
        return result   