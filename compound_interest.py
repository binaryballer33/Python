# COMPOUND INTEREST
# .04 = 1.6X, .05945 = 2X, .07934 = 2.5X, .09588 = 3X, .14353 = 5X, .21155 = 10X
# gamestop_money_glitch = initial_starting_capital * 2  # just a little jokey joke hahaha

from termcolor import colored
print()

initial_starting_capital = 10400
monthly_investment = 1000
monthly_profits = 0
monthly_roi = .145  # monthly ROI
weekly_roi = monthly_roi / 4  # weekly ROI
total_profits = 0
ending_capital = 10400
year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(f"{colored('Starting Capital:', 'green')} ${initial_starting_capital:,d}")


def summary():
    print()
    print("**********SUMMARY**********************")
    print(f"Initial Investment: ${initial_starting_capital:,d}")
    print(f"Additional Monthly Investments: ${monthly_investment:,d}")
    print(f"Ending Investment: ${ending_capital:,d}")
    print(f"RoI Weekly: {round(weekly_roi * 100, 4)}% / Monthly: {round(monthly_roi * 100, 4)}%")
    print(f"*** TOTAL PROFITS *** ${total_profits:,d}")
    print(f"${round(ending_capital):,d} / ${round(initial_starting_capital):,d} = {round(ending_capital / initial_starting_capital, 2)}X Your Money")
    print("**********SUMMARY**********************")

    print()
    # WITH TAXES THIS IS THE ACTUAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALY
    tax = total_profits * .37  # just blindly assuming you are paying a total of 37% taxes
    net_realized_gains = ending_capital - tax
    print(f"Gross Gains for the Year: ${int(ending_capital):,d}")
    print(f"You OWE ${round(tax):,d} in {colored('Taxes', 'red')}")
    print(f"Net Gains for the Year: ${int(net_realized_gains):,d}")
    print(f"After TAXES {int(net_realized_gains):,d} / {initial_starting_capital:,d} {round(net_realized_gains / initial_starting_capital, 2)}X Your Money")


for month in year:
    ending_capital = ending_capital + monthly_investment
    weekly_profits = []

    print()
    print(f"For the Month of {month.upper()}:")
    print(f"You added your monthly investment of ${monthly_investment:,d}")

    for week in range(4):
        weekly_profits.append(round(ending_capital * weekly_roi))
        print(f"End of Week {week+1}: ${round(ending_capital):,d} [+] ${int(weekly_profits[week]):,d}")
        ending_capital = ending_capital + weekly_profits[week]
        total_profits = total_profits + weekly_profits[week]

    print(f"{colored('End of Month:', 'green')}  ${ending_capital:,d}")

    for each_weeks_profit in weekly_profits:
        monthly_profits = monthly_profits + each_weeks_profit

    print(f"Total Profits for the Month: ${monthly_profits:,d}")
    monthly_profits = 0

summary()


# -----------------------------------OLD CODE---------------------------------------------------
# from termcolor import colored
# # COMPOUND INTEREST
# # .04 = 1.6X, .05945 = 2X, .07934 = 2.5X, .09588 = 3X, .14353 = 5X, .21155 = 10X
#
# print()
# ending_capital = 11400
# starting_capital = 11400
# return_on_investment_rate = .145 / 4
# gamestop_money_glitch = starting_capital * 2  # just a little jokey joke hahaha
# month = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
# profit = 0
# monthly_investment = 0
# total_profits = 0
#
# print(f"Starting Net Worth: ${starting_capital}")
# print()
# for day in range(12):
#     try:
#         profit = starting_capital * return_on_investment_rate
#         profit = profit * 4
#         total_profits = total_profits + profit
#         print(f"{month[day]} I made ${round(profit):,d} in profits")
#         print(f"Total Profits: ${round(total_profits):,d}")
#         starting_capital = starting_capital + profit
#         print(f"Net Worth: ${round(starting_capital):,d}")
#         print()
#         print(f"[+]Adding ${monthly_investment} to Portfolio")
#         print(f"{colored('New Net Worth: $', 'green')}{colored(round(starting_capital + monthly_investment), 'green')}")
#         starting_capital = starting_capital + monthly_investment
#         print(f"{round(starting_capital):,d} / {round(ending_capital):,d} = {round(starting_capital / ending_capital, 3)}X Your Money")
#     except IndexError:
#         pass
#
#
# print()
#
# # WITH TAXES THIS IS THE ACUTAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALY
# tax = total_profits * .37  # just blindly assuming you are paying a total of 37% taxes
# print(f"You paid ${round(tax)} in Taxes")
