
budget_dict = [{
    "category": "food",
    "amount": 0,
}, {
    "category": "cloths",
    "amount": 0,
}, {
    "category": "entertainment",
    "amount": 0,
}]


class Budget:

    def __init__(self):
        pass

    def deposit(self):
        print("Budget Options")
        print("1. Food")
        print("2. cloth")
        print("3. entertainment")
        selected_budget = int(input("select your budget \n"))

        if selected_budget == 1:
            print("FOOD BALANCE: ", budget_dict[0]["amount"])
            food_option = int(input("What would you like to do? 1(Deposit), 2(Transfer), 3(Withdraw), 4(Check Balance) \n"))
            if food_option == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budget_dict[0]["amount"] + deposit
                budget_dict[0]["amount"] = budget_dict[0]["amount"] + deposit
                print("FOOD NEW BALANCE: ", budget_dict[0]["amount"])
                food_option2 = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if food_option2 == 1:
                    self.transfer()

                elif food_option2 == 2:
                    self.withdraw_from_budget()

                elif food_option2 == 3:
                    exit()
                else:
                    print("Invalid option")

            elif food_option == 2:
                self.transfer()
            elif food_option == 3:
                self.withdraw_from_budget()
            elif food_option == 4:
                print("FOOD NEW BALANCE: ", budget_dict[0]["amount"])
                self.deposit()


            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()




        elif selected_budget == 2:
            print("CLOTH BALANCE: ", budget_dict[1]["amount"])
            cloth_option = int(input("What would you like to do? 1(Deposit), 2(Transfer), 3(Withdraw), 4(Check Balance) \n"))
            if cloth_option == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budget_dict[1]["amount"] + deposit
                budget_dict[0]["amount"] = budget_dict[1]["amount"] + deposit
                print("CLOTH NEW BALANCE: ", budget_dict[1]["amount"])
                cloth_option2 = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if cloth_option2 == 1:
                    self.transfer()

                elif cloth_option2 == 2:
                    self.withdraw_from_budget()

                elif cloth_option2 == 3:
                    exit()
                else:
                    print("Invalid option")

            elif cloth_option == 2:
                self.transfer()
            elif cloth_option == 3:
                self.withdraw_from_budget()
            elif cloth_option == 4:
                print("FOOD NEW BALANCE: ", budget_dict[1]["amount"])
                self.deposit()


            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()




        elif selected_budget == 3:
            print("ENTERTAINMENT BALANCE: ", budget_dict[2]["amount"])
            ent_option = int(input("What would you like to do? 1(Deposit), 2(Transfer), 3(Withdraw), 4(Check Balance) \n"))
            if ent_option == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budget_dict[2]["amount"] + deposit
                budget_dict[2]["amount"] = budget_dict[2]["amount"] + deposit
                print("ENTERTAINMENT NEW BALANCE: ", budget_dict[2]["amount"])
                ent_option2 = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if ent_option2 == 1:
                    self.transfer()

                elif ent_option2 == 2:
                    self.withdraw_from_budget()

                elif ent_option2 == 3:
                    exit()
                else:
                    print("Invalid option")

            elif ent_option == 2:
                self.transfer()
            elif ent_option == 3:
                self.withdraw_from_budget()
            elif ent_option == 4:
                print("ENTERTAINMENT NEW BALANCE: ", budget_dict[2]["amount"])
                self.deposit()
            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()

        else:
            print("Invalid option")
            self.deposit()

    def withdraw_from_budget(self):
        print(budget_dict)
        print("withdraw Options")
        print("1. Food")
        print("2. cloth")
        print("3. entertainment")
        selected_budget_Option = int(input("select withdraw Options \n"))

        if selected_budget_Option == 1:
            print("FOOD BALANCE: ", budget_dict[0]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budget_dict[0]["amount"]:
                print("insufficient Funds")
                withdraw2 = int(input("do you want to  1(transfer), 2(deposit), 3(quit)\n"))
                if withdraw2 == 1:
                    self.transfer()

                elif withdraw2 == 2:
                    self.deposit()

                elif withdraw2 == 3:
                    exit()
                else:
                    print("Invalid option")

            else:
                withdraw1 = budget_dict[0]["amount"] - withdraw
                budget_dict[0]["amount"] = budget_dict[0]["amount"] - withdraw
                print("Withdrawal Successful")
                print("FOOD NEW BALANCE: ", budget_dict[0]["amount"])
                withdraw2 = int(input("do you want to  1(transfer), 2(deposit), 3(quit)\n"))
                if withdraw2 == 1:
                    self.transfer()

                elif withdraw2 == 2:
                    self.deposit()

                elif withdraw2 == 3:
                    exit()
                else:
                    print("Invalid option")

        elif selected_budget_Option == 2:
            print("CLOTH BALANCE: ", budget_dict[1]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budget_dict[1]["amount"]:
                print("insufficient Funds")
                withdraw2 = int(input("do you want to  1(transfer), 2(deposit), 3(quit)\n"))
                if withdraw2 == 1:
                    self.transfer()

                elif withdraw2 == 2:
                    self.deposit()

                elif withdraw2 == 3:
                    exit()
                else:
                    print("Invalid option")

            else:
                withdraw1 = budget_dict[1]["amount"] - withdraw
                budget_dict[1]["amount"] = budget_dict[1]["amount"] - withdraw
                print("Withdrawal Successful")
                print("CLOTH NEW BALANCE: ", budget_dict[1]["amount"])
                withdraw2 = int(input("do you want to  1(transfer), 2(deposit), 3(quit)\n"))
                if withdraw2 == 1:
                    self.transfer()

                elif withdraw2 == 2:
                    self.deposit()

                elif withdraw2 == 3:
                    exit()
                else:
                    print("Invalid option")

        elif selected_budget_Option == 3:
            print("ENTERTAINMENT BALANCE: ", budget_dict[2]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budget_dict[2]["amount"]:
                print("insufficient Funds")
                withdraw2 = int(input("do you want to  1(transfer), 2(deposit), 3(quit)\n"))
                if withdraw2 == 1:
                    self.transfer()

                elif withdraw2 == 2:
                    self.deposit()

                elif withdraw2 == 3:
                    exit()
                else:
                    print("Invalid option")

            else:
                withdraw1 = budget_dict[2]["amount"] - withdraw
                budget_dict[2]["amount"] = budget_dict[2]["amount"] - withdraw
                print("Withdrawal Successful")
                print("ENTERTAINMENT NEW BALANCE: ", budget_dict[2]["amount"])
                withdraw2 = int(input("do you want to  1(transfer), 2(deposit), 3(quit)\n"))
                if withdraw2 == 1:
                    self.transfer()

                elif withdraw2 == 2:
                    self.deposit()

                elif withdraw2 == 3:
                    exit()
                else:
                    print("Invalid option")

        else:
            print("invalid Selection\nSELECT A VALID OPTION")
            self.withdraw_from_budget()

    def transfer(self):
        print(budget_dict)
        print("Transfer Options")
        print("1.From  Food")
        print("2.From cloth")
        print("3.From entertainment")
        print("4. exit")
        select_transfer_option = int(input("select destination\n"))

        if select_transfer_option == 1:
            print("FOOD BALANCE: ", budget_dict[0]["amount"])
            transfer = int(input("1.(Transfer to Cloth), 2.(Transfer to Entertainment)\n"))
            if transfer == 1:
                transfer_amount = int(input("Enter Amount\n"))
                if transfer_amount <= budget_dict[0]["amount"]:
                    transfer_amount1 = budget_dict[0]["amount"] - transfer_amount
                    transfer_amount2 = budget_dict[1]["amount"] + transfer_amount
                    budget_dict[0]["amount"] = budget_dict[0]["amount"] - transfer_amount
                    budget_dict[1]["amount"] = budget_dict[1]["amount"] + transfer_amount
                    transfer_amount2 = budget_dict[1]["amount"] + transfer_amount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW FOOD BALANCE: ", budget_dict[0]["amount"])
                    print("NEW CLOTH BALANCE: ", budget_dict[1]["amount"])
                    transfer2 = int(input("do you want to  1(withdraw), 2(deposit), 3(quit)\n"))
                    if transfer2 == 1:
                        self.withdraw_from_budget()

                    elif transfer2 == 2:
                        self.deposit()

                    elif transfer2 == 3:
                        exit()
                    else:
                        print("Invalid option")
                else:
                    print("insufficient funds")
                    print("FOOD BALANCE: ", budget_dict[0]["amount"])
                    self.deposit()

            elif transfer == 2:
                transfer_amount = int(input("Enter Amount\n"))
                if transfer_amount <= budget_dict[0]["amount"]:
                    transfer_amount1 = budget_dict[0]["amount"] - transfer_amount
                    transfer_amount2 = budget_dict[2]["amount"] + transfer_amount
                    budget_dict[0]["amount"] = budget_dict[0]["amount"] - transfer_amount
                    budget_dict[2]["amount"] = budget_dict[2]["amount"] + transfer_amount
                    transfer_amount2 = budget_dict[1]["amount"] + transfer_amount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW FOOD BALANCE: ", budget_dict[0]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: ", budget_dict[2]["amount"])
                    transfer2 = int(input("do you want to  1(withdraw), 2(deposit), 3(quit)\n"))
                    if transfer2 == 1:
                        self.withdraw_from_budget()

                    elif transfer2 == 2:
                        self.deposit()

                    elif transfer2 == 3:
                        exit()
                    else:
                        print("Invalid option")

                else:
                    print("insufficient funds")
                    print("FOOD BALANCE: ", budget_dict[0]["amount"])
                    self.transfer()

        elif select_transfer_option == 2:
            print("CLOTH BALANCE: ", budget_dict[1]["amount"])
            transfer = int(input("1.(TF to Entertainment), 2.(TF to Food)\n"))
            if transfer == 1:
                transfer_amount = int(input("Enter Amount\n"))
                if transfer_amount <= budget_dict[1]["amount"]:
                    transfer_amount1 = budget_dict[1]["amount"] - transfer_amount
                    transfer_amount2 = budget_dict[2]["amount"] + transfer_amount
                    budget_dict[1]["amount"] = budget_dict[1]["amount"] - transfer_amount
                    budget_dict[2]["amount"] = budget_dict[2]["amount"] + transfer_amount
                    transfer_amount2 = budget_dict[1]["amount"] + transfer_amount
                    print("TF SUCCESSFUL!!!")
                    print("NEW CLOTH BALANCE: ", budget_dict[1]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: ", budget_dict[2]["amount"])
                    transfer2 = int(input("do you want to  1(withdraw), 2(deposit), 3(quit)\n"))
                    if transfer2 == 1:
                        self.withdraw_from_budget()

                    elif transfer2 == 2:
                        self.deposit()

                    elif transfer2 == 3:
                        exit()
                    else:
                        print("Invalid option")
                else:
                    print("insufficient funds")
                    print("FOOD BALANCE: ", budget_dict[0]["amount"])
                    self.transfer()

            elif transfer == 2:
                transfer_amount = int(input("Enter Amount\n"))
                if transfer_amount <= budget_dict[1]["amount"]:
                    transfer_amount1 = budget_dict[1]["amount"] - transfer_amount
                    transfer_amount2 = budget_dict[0]["amount"] + transfer_amount
                    budget_dict[1]["amount"] = budget_dict[1]["amount"] - transfer_amount
                    budget_dict[0]["amount"] = budget_dict[0]["amount"] + transfer_amount
                    transfer_amount2 = budget_dict[0]["amount"] + transfer_amount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW CLOTH BALANCE: ", budget_dict[1]["amount"])
                    print("NEW FOOD BALANCE: ", budget_dict[0]["amount"])
                    transfer2 = int(input("do you want to  1(withdraw), 2(deposit), 3(quit)\n"))
                    if transfer2 == 1:
                        self.withdraw_from_budget()

                    elif transfer2 == 2:
                        self.deposit()

                    elif transfer2 == 3:
                        exit()
                    else:
                        print("Invalid option")

                else:
                    print("insufficient funds")
                    print("CLOTH BALANCE: ", budget_dict[1]["amount"])
                    self.transfer()

        elif select_transfer_option == 3:
            print("ENTERTAINMENT BALANCE: ", budget_dict[2]["amount"])
            transfer = int(input("1.(TRANSFER to cloth), 2.(TRANSFER to Food)\n"))
            if transfer == 1:
                transfer_amount = int(input("Enter Amount\n"))
                if transfer_amount <= budget_dict[2]["amount"]:
                    transfer_amount1 = budget_dict[2]["amount"] - transfer_amount
                    transfer_amount2 = budget_dict[1]["amount"] + transfer_amount
                    budget_dict[2]["amount"] = budget_dict[2]["amount"] - transfer_amount
                    budget_dict[1]["amount"] = budget_dict[1]["amount"] + transfer_amount
                    transfer_amount2 = budget_dict[1]["amount"] + transfer_amount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW ENTERTAINMENT BALANCE: ", budget_dict[2]["amount"])
                    print("NEW CLOTH BALANCE: ", budget_dict[1]["amount"])
                    transfer2 = int(input("do you want to  1(withdraw), 2(deposit), 3(quit)\n"))
                    if transfer2 == 1:
                        self.withdraw_from_budget()

                    elif transfer2 == 2:
                        self.deposit()

                    elif transfer2 == 3:
                        exit()
                    else:
                        print("Invalid option")

                else:
                    print("insufficient funds")
                    print("FOOD BALANCE: ", budget_dict[0]["amount"])
                    self.transfer()

            elif transfer == 2:
                transfer_amount = int(input("Enter Amount\n"))
                if transfer_amount <= budget_dict[2]["amount"]:
                    transfer_amount1 = budget_dict[2]["amount"] - transfer_amount
                    transfer_amount2 = budget_dict[0]["amount"] + transfer_amount
                    budget_dict[2]["amount"] = budget_dict[2]["amount"] - transfer_amount
                    budget_dict[0]["amount"] = budget_dict[0]["amount"] + transfer_amount
                    transfer_amount2 = budget_dict[0]["amount"] + transfer_amount
                    print("TRANSFER SUCCESSFUL!!!")
                    print("NEW ENTERTAINMENT BALANCE: ", budget_dict[2]["amount"])
                    print("NEW FOOD BALANCE: ", budget_dict[0]["amount"])
                    transfer2 = int(input("do you want to  1(withdraw), 2(deposit), 3(quit)\n"))
                    if transfer2 == 1:
                        self.withdraw_from_budget()

                    elif transfer2 == 2:
                        self.deposit()

                    elif transfer2 == 3:
                        exit()
                    else:
                        print("Invalid option")

                else:
                    print("insufficient funds")
                    print("CLOTH BALANCE: ", budget_dict[1]["amount"])
                    self.transfer()

        elif select_transfer_option == 4:
            print("have a nice day!!!")
            exit()

        else:
            print("have a nice day!!!")


transaction = Budget()
transaction.deposit()