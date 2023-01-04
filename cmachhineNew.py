from Menus import MENU,resources,profit
untung = profit
def report(choice, untungNiaga):
    print(resources)
    print(untung)


# ------------------------------------------------------------------
def checkResources(choice, choosenIng):
    for i in choosenIng:
        # j merujuk kepada wwater,milk dan cofee tp dalam resources
        for j in resources:
            # contoh "water" == "water"
            if i == j:
                # contoh resources[water] - MENU[latte][ingredient][water]
                resources[j] -= choosenIng[i]
                if resources[j] < 0:
                    resourceLow is True
                    print(f'Sorry bro there is not enough {j}')
#------------------------------------------------------------------------
def process_coin(resourceLow):
    if resourceLow == False:
        print("Please insert your coin")
        q = int(input("Quarters :"))
        d = int(input("dimes    :"))
        n = int(input("Nickles  :"))
        p = int(input("Pennies  :"))

        totalQ = q * 0.25
        totalD = d * 0.10
        totalN = n * 0.05
        totalP = p * 0.01

        totalAll = totalQ + totalD +totalN + totalP

        print(totalAll)
        return totalAll


def transactionSuccess(cost,totalValue):
    if totalValue >= cost:
        global untung
        untung += cost
        remainder = totalValue - cost
        print(f"Your remainder is {remainder}")
        print(untung)
        return True



    else:
        print(f"Sorry not enough money. Money refunded")
        return False


def makeCoffee(variable, choice):
    if variable == True:
        print(f"Here is your {choice}..enjoy boskurrr")



is_on = True
resourceLow = False
while is_on is True:
    choice = input("Nak minum nape(espresso/latte/cappucino)")

    if choice == "report" or choice == "off":

        if choice == "report":
            report(choice, untung)

        elif choice == "off":
            is_on = False
            print("Thank you for using our services!!")
    else:
        choosen = MENU[choice]
        choosenIng = MENU[choice]["ingredients"]
        checkResources(choice, choosenIng)
        # process_coin(resourceLow) kenapa read 2 kali

        variable = transactionSuccess(choosen["cost"], process_coin(resourceLow))
        makeCoffee(variable, choice)


        # totalPrice = transactionSuccess(choosen["cost"], process_coin(resourceLow), profit)
        # makeCoffee(totalPrice,choosen["cost"], choice)


        # if transactionSuccess(choosen["cost"], process_coin(resourceLow), profit)
        #
        #     print(f"Here is your {choice}..enjoy")
        #

    #
    # print(choosenIng)
    # for j in resources:

    # if choice == "off":
    #     is_on = False
    #
    # if choice == "report":
    #     report()
    #
    # if choice == "espresso"



