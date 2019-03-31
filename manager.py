class Entry:

    def __init__(self, date, account_type, category, content, price, notes="None"):
        self.date = date
        self.account_type = account_type
        self.category = category
        self.content = content
        self.price = price
        self.notes = notes

    def display(self, omit=("date", "account", "category", "notes")):
        info = {"date": self.date, "account": self.account_type, "category": self.category,
                "notes": self.notes, "content": self.content, "price": self.price}

        for k, v in info.items():
            if k not in omit:
                print(k.capitalize() + ": " + str(v))

    def __str__(self):
        return f"[{self.date}]\nType: {self.account_type}\nCategory: {self.category}\nContent: {self.content}\nPrice: {self.price}\nNotes: {self.notes}\n"

    def __repr__(self):
        return f'''[{self.date}]\nType: {self.account_type}\nCategory: {self.category}\nContent: {self.content}\nPrice: {self.price}\nNotes: {self.notes}\n'''
