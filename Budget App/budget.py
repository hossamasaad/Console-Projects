class Category:

    # Create class Constructor
    def __init__(self, catName):
        self.catName = catName
        self.ledger = []

    def __repr__(self):
        # title centered in 30 *
        title = self.catName.center(30, "*") + "\n"
        
        # item list
        itemList = ""
        for item in self.ledger:
            description = "{:<23}".format(item["description"])
            amount = "{:>7.2f}".format(item["amount"])   
            itemList += "{}{}\n".format(description[:23], amount[:7])

        # calculate total
        total = "Total: {:.2f}".format(self.get_balance())
        
        return title + itemList + total

    def deposit(self, amount, description = ""):
        self.ledger.append({'amount':amount, 'description':description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount':-1 * amount, 'description':description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for d in self.ledger:
            balance += d['amount']
        
        return balance

    def transfer(self, amount, catBudget):
        if self.withdraw(amount, 'Transfer to {}'.format(catBudget.catName)):
            catBudget.deposit(amount, 'Transfer from {}'.format(self.catName))
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True



def create_spend_chart(categories):

    spent_amount = [] # to store spent amounts
    names = []        # to store catigories names
    for category in categories:
        # append name to the list
        names.append(category.catName)


        # calculate spent amounts
        spent = 0
        for d in category.ledger:
            if d['amount'] < 0:
                spent += abs(d['amount'])
        
        # appens spent amount to the list
        spent_amount.append(round(spent,2))

    # calculate total sum of spent amounts
    total = round(sum(spent_amount), 2)
    
    # calculate percentages
    percentage = []
    for amount in spent_amount:
        percentage.append(int((((amount / total) * 10) // 1) * 10))

    # create Chart
    # header
    chart = "Percentage spent by category\n"

    # Barchar
    for value in range(100,-1,-10):
        chart += '{:>3}'.format(str(value)) + '|'
        for spent in percentage:
            if spent >= value:
                chart += ' o '
            else:
                chart += "   "
        chart += ' \n'
    
    # dashes
    chart += '    ' + '-' * (len(spent_amount) * 3 + 1) + '\n'

    # names
    length = len(names)
    max_length = 0
    for name in names:
        max_length = max(len(name), max_length)

    for i in range(max_length):
        chart += '    '
        for j in range(length):
            if len(names[j]) > i:
                chart += ' ' + names[j][i] + ' '
            else:
                chart += '   '
        chart += ' \n'

    return chart.rstrip('\n')