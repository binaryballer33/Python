# This is a application that will calculate compound interest over a certain amount of time
from termcolor import colored

starting_capital = 10000
monthly_contribution = 1000
current_capital = starting_capital
ending_capital = 0
total_profits = 0
time_frame_for_investment = 5  # number of years that you want to invest
total_contribution = monthly_contribution * 12 * time_frame_for_investment
weekly_rate_of_return = 1.01  # 4 % monthly if rate is 1.01
weekly_profits_calculator = weekly_rate_of_return - 1
tax_amount = 0
tax_rate = .37  # blinding assuming that you are going to be paying 37% in taxes
year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def summary():
    print()
    print(f"Printing Summary Report For Year {years + 1}")

    print("**********GROSS SUMMARY**********************")
    print(f"Starting Investment: ${int(start_of_the_year_capital):,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {int(weekly_rate_of_return * 100 - 100)}%")
    print(f"{colored('Profits for the Year: ', 'green')}${int(total_profits):,d}")
    print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
    print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = {round(ending_capital / total_capital, 2)}X Your Money")
    print("**********GROSS SUMMARY**********************")
    print()

    print("**********NET SUMMARY************************")
    print(f"Tax Rate: {int(tax_rate * 100)}%")
    print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
    print(f"{colored('Profits for the Year: ', 'green')}${round(total_profits - tax_amount):,d}")
    print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
    print(f"{int(net_realized_gains):,d} / {total_capital:,d} {round(net_realized_gains / total_capital, 2)}X Your Money")
    print(f"Total Contributions: ${total_capital: ,d}(All time Total Contribution)")
    print("**********NET SUMMARY************************")


for years in range(time_frame_for_investment):  # This specifies how many years you will be investing your money
    # helps me keep tracking of the profits for just the current year
    start_of_the_year_capital = current_capital - tax_amount
    current_capital = start_of_the_year_capital
    print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
    print(f"Monthly Additional Contribution = ${monthly_contribution:,d}")

    for month in year:  # the month of the loop that we are currently on
        current_capital = current_capital + monthly_contribution
        print(f"\n\t\tYEAR {years + 1} {month.upper()}")
        print(f"Adding Monthly Contribution: [+] ${monthly_contribution:,d}")
        weekly_profits = []

        for week in range(4):  # 4 weeks in a month (weekly compound interest)
            weekly_profits.append(round(current_capital * weekly_profits_calculator))
            print(f"Start of Week {week + 1}: ${round(current_capital):,d} [+] ${int(weekly_profits[week]):,d} ")
            current_capital = current_capital * weekly_rate_of_return

        weekly_profits_total = 0  # get the total for the week and display the profits(This is gross)
        for each_weekly_profit in weekly_profits:
            weekly_profits_total = weekly_profits_total + each_weekly_profit
        print(f"Total Profits for the Month: ${weekly_profits_total:,d}")
        print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")

    # WITH TAXES THIS IS THE ACTUAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALY
    total_profits = current_capital - start_of_the_year_capital - monthly_contribution * 12  # total profits for the current year
    total_profits_total = current_capital - starting_capital - total_contribution # total profits total
    total_capital = starting_capital + monthly_contribution * 12 * (years + 1)
    tax_amount = total_profits * tax_rate  # just blindly assuming you are paying a total of 37% taxes
    ending_capital = current_capital
    net_realized_gains = ending_capital - tax_amount

    summary()
