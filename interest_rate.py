sara = 1000
account = []

for i in range(20):
    sara += sara * 0.02
    account.append(sara)


print("Total amount in bank account: {:.2f} Euros".format(sum(account)))

