from pyexcel_xlsx import get_data
import json
import manager

# Runs till sheet 1

class Reader:

    def __init__(self, filename):
        self.parsed_json = self.load(filename)
        self.entry_obj = []
    
    def load(self, filename):
        data = json.dumps(get_data(filename))
        parsed_json = json.loads(data)
        return parsed_json
    
    def get_sheets(self):
        return list(self.parsed_json.keys())
    
    def get_categories(self):
        # pass
        sheet_origin = self.get_sheets()[0]
        return self.parsed_json[sheet_origin][0]

    def generate_info(self):
        for sheet, contents in self.parsed_json.items():
            for info in contents[1:]:
                meta_data = [i for i in info if i] # Clear empty strings
                self.entry_obj.append(manager.Entry(meta_data[0], meta_data[1], meta_data[2], meta_data[3], meta_data[4]))


a = Reader("budget.xlsx")
a.generate_info()

for i in a.entry_obj:
    # i.display()
    print(i)
    



# info = {}
# print(a.get_sheets())
# print(load_file())

# for sheets, content in parsed_json.items():

#     print(content)
