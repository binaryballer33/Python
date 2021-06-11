# This is a application that will calculate compound interest over a certain amount of time
# given certain interest rates, starting amounts, weekly rate of returns and your tax rate
from termcolor import colored

weekly_rate_of_returns_list = [1.01, 1.015]  # 4 % monthly if rate is 1.01
starting_capitals_list = [10000, 15000, 20000]  # using *args so the user can put in multiple starting capitals


# want to display just a little bit of information for different interest rates, starting capitals, etc
def brief_summary(years, net_realized_gains, total_capital, initial_investment_for_brief_summary,
                  each_weekly_rate_of_return, monthly_contribution, tax_rate):
    """
    Display a less detailed Summary report of your investments, takes in the variable as parameters from your
    compound() function
    :param tax_rate:
    :param monthly_contribution:
    :param each_weekly_rate_of_return:
    :param initial_investment_for_brief_summary:
    :param years:
    :param net_realized_gains:
    :param total_capital:
    :return:
    """
    print()
    print(f"Printing Summary Report For Year {years + 1}")
    print("**********NET SUMMARY************************")
    print(f"Initial Investment: ${initial_investment_for_brief_summary:,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {round(each_weekly_rate_of_return * 100 - 100, 2)}%")
    print(f"Tax Rate: {int(tax_rate * 100)}%")
    print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
    print(f"Total Contributions To Date: ${total_capital:,d}")
    print(f"{int(net_realized_gains):,d} / {total_capital:,d} ({round(net_realized_gains / total_capital, 2)}X Return)")
    print("**********NET SUMMARY************************")


def summary(years, start_of_the_year_capital, total_capital, net_realized_gains, tax_rate, ending_capital,
            total_profits, tax_amount, total_profits_total, initial_investment_for_brief_summary,
            each_weekly_rate_of_return, monthly_contribution):
    """
    Display a Summary report of your investments, takes in the variable as parameters from your compound() function
    :param tax_rate:
    :param monthly_contribution:
    :param each_weekly_rate_of_return:
    :param initial_investment_for_brief_summary:
    :param total_profits_total:
    :param years:
    :param start_of_the_year_capital:
    :param total_capital:
    :param net_realized_gains:
    :param ending_capital:
    :param total_profits:
    :param tax_amount:
    :return:
    """
    print()
    print(f"Printing Summary Report For Year {years + 1}")

    print("**********GROSS SUMMARY**********************")
    print(f"Initial Investment: ${initial_investment_for_brief_summary:,d}")
    print(f"Start of The Current Year Investment: ${int(start_of_the_year_capital):,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {round(each_weekly_rate_of_return * 100 - 100, 2)}%")
    print(f"{colored('Profits for the Year: ', 'green')}${int(total_profits):,d}")
    print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
    print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = "
          f"{round(ending_capital / total_capital, 2)}X Return")
    print("**********GROSS SUMMARY**********************")
    print()

    print("**********NET SUMMARY************************")
    print(f"Tax Rate: {int(tax_rate * 100)}%")
    print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
    print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
    print(f"Total Contributions To Date: ${total_capital:,d}")
    print(f"Profits for the Year: ${round(total_profits - tax_amount):,d}")
    print(f"Total Profits All Time: ${round(total_profits_total):,d}")
    print(f"{int(net_realized_gains):,d} / {total_capital:,d}"
          f" {round(net_realized_gains / total_capital, 2)}X Return")
    print("**********NET SUMMARY************************")


# fix the shadow names and the tax_amount=0 parameter value not being used
def compound(brief='', *starting_capitals):  # needs current_capital and tax_amount in order to work
    """
    This function will figure out how much money you will make after a certain amount of time, will take into
    consideration how much money you started with and your interest rate every week, etc

    :param brief: print brief summary or long summary, prints long summary by default
    :return: nothing
    """
    year = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']
    monthly_contribution = 1000
    time_frame_for_investment = 5  # number of years that you want to invest
    tax_rate = .37  # blinding assuming that you are going to be paying 37% in taxes

    for each_weekly_rate_of_return in weekly_rate_of_returns_list:
        weekly_rate_of_return = each_weekly_rate_of_return
        weekly_profits_calculator = weekly_rate_of_return - 1

        for each_starting_capital in starting_capitals:  # gets me the first paramater in the *args
            for current_capital in each_starting_capital:  # gets me the first element in the first parameter in *args
                # resets tax amount each time you get a new starting value from the starting_capitals_list
                tax_amount = 0
                # for brief_summary can keep track of initial inv
                initial_investment_for_brief_summary = current_capital

                # This specifies how many years you will be investing your money
                for years in range(time_frame_for_investment):
                    # helps me keep tracking of the profits for just the current year
                    start_of_the_year_capital = current_capital - tax_amount
                    current_capital = start_of_the_year_capital
                    if brief.lower() == 'brief':
                        pass
                    else:
                        print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
                        print(f"Monthly Additional Contribution = ${monthly_contribution:,d}")

                    for month in year:  # the month of the loop that we are currently on
                        current_capital = current_capital + monthly_contribution
                        if brief.lower() == 'brief':
                            pass
                        else:
                            print(f"\n\t\tYEAR {years + 1} {month.upper()}")
                            print(f"Adding Monthly Contribution: [+] ${monthly_contribution:,d}")
                        weekly_profits = []

                        for week in range(4):  # 4 weeks in a month (weekly compound interest)
                            weekly_profits.append(round(current_capital * weekly_profits_calculator))
                            if brief.lower() == 'brief':
                                pass
                            else:
                                print(f"Start of Week {week + 1}: ${round(current_capital):,d} "
                                      f"[+] ${int(weekly_profits[week]):,d} ")
                            current_capital = current_capital * weekly_rate_of_return

                        weekly_profits_total = 0  # get the total for the week and display the profits(This is gross)
                        for each_weekly_profit in weekly_profits:
                            weekly_profits_total = weekly_profits_total + each_weekly_profit
                        if brief.lower() == 'brief':
                            pass
                        else:
                            print(f"Total Profits for the Month: ${weekly_profits_total:,d}")
                            print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")

                    # THIS IS THE TAX INFORMATION SECTION THAT HELPS GET THE NET AMOUNT, PROFITS, TAXES DUE EACH YEAR
                    # WITH TAXES THIS IS THE ACTUAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALY
                    # total profits for the current year
                    total_profits = current_capital - start_of_the_year_capital - monthly_contribution * 12
                    total_capital = initial_investment_for_brief_summary + monthly_contribution * 12 * (years + 1)
                    # just blindly assuming you are paying a total of 37% taxes
                    tax_amount = total_profits * tax_rate
                    # total profits total (since week 1)
                    total_profits_total = current_capital - total_capital - tax_amount
                    ending_capital = current_capital
                    net_realized_gains = ending_capital - tax_amount

                    # on year 5 print the brief summary
                    if (years + 1) == time_frame_for_investment and brief.lower() == 'brief':
                        brief_summary(years, net_realized_gains, total_capital, initial_investment_for_brief_summary,
                                      each_weekly_rate_of_return, monthly_contribution, tax_rate)

                    if brief.lower() != 'brief':  # print the long summary
                        summary(years, start_of_the_year_capital, total_capital, net_realized_gains, tax_rate,
                                ending_capital, total_profits, tax_amount, total_profits_total,
                                initial_investment_for_brief_summary, each_weekly_rate_of_return, monthly_contribution)


def compound_summary_brief():  # needs current_capital and tax_amount in order to work
    """
    Calls the Compound Function
    This function will display the 5 year summaries. It will not display the monthly information or gross information
    """
    compound('brief', starting_capitals_list)


def compound_summary_long():
    """
    Calls the Compound Function and it will display all the information available
    :return:
    """
    compound('', starting_capitals_list)


# compound_summary_long()
compound_summary_brief()


























































# ----------------------------------------------------------------------------------------------------------------------
# # # adding the capability to take in more than 1 starting capital (ie 10,000, 20,000, 30,000) and get the results
# # This is a application that will calculate compound interest over a certain amount of time
# from termcolor import colored
#
# monthly_contribution = 1000
# ending_capital = 0
# total_profits = 0
# time_frame_for_investment = 5  # number of years that you want to invest
# weekly_rate_of_return = 1.01  # 4 % monthly if rate is 1.01
# weekly_profits_calculator = weekly_rate_of_return - 1
# tax_amount = 0
# tax_rate = .37  # blinding assuming that you are going to be paying 37% in taxes
# year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# # learn how to use *args
# weekly_rate_of_returns_list = [1.01, 1.025, 1.05]  # learn how to use *args with this
# starting_capitals_list = [10000, 15000, 20000]  # learn how to use *args with this
#
#
# def brief_summary(years, net_realized_gains, total_capital, tax_amount, initial_investment_for_brief_summary):  # want to display just a little bit of information for different interest rates, starting capitals, etc
#     """
#     Display a less detailed Summary report of your investments, takes in the variable as parameters from your compound() function
#     :param initial_investment_for_brief_summary:
#     :param tax_amount:
#     :param years:
#     :param net_realized_gains:
#     :param total_capital:
#     :return:
#     """
#     print()
#     print(f"Printing Summary Report For Year {years + 1}")
#     print("**********NET SUMMARY************************")
#     print(f"Initial Investment: ${initial_investment_for_brief_summary:,d}")
#     print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
#     print(f"Weekly Rate Of Return: {round(weekly_rate_of_return * 100 - 100, 2)}%")
#     print(f"Tax Rate: {int(tax_rate * 100)}%")
#     print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
#     print(f"Total Contributions To Date: ${total_capital:,d}")
#     print(f"{int(net_realized_gains):,d} / {total_capital:,d} {round(net_realized_gains / total_capital, 2)}X Your Money")
#     print("**********NET SUMMARY************************")
#
#
# def summary(years, start_of_the_year_capital, total_capital, net_realized_gains, ending_capital, total_profits, tax_amount, total_profits_total, initial_investment_for_brief_summary):
#     """
#     Display a Summary report of your investments, takes in the variable as parameters from your compound() function
#     :param total_profits_total:
#     :param years:
#     :param start_of_the_year_capital:
#     :param total_capital:
#     :param net_realized_gains:
#     :param ending_capital:
#     :param total_profits:
#     :param tax_amount:
#     :return:
#     """
#     print()
#     print(f"Printing Summary Report For Year {years + 1}")
#
#     print("**********GROSS SUMMARY**********************")
#     print(f"Initial Investment: ${initial_investment_for_brief_summary:,d}")
#     print(f"Start of The Current Year Investment: ${int(start_of_the_year_capital):,d}")
#     print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
#     print(f"Weekly Rate Of Return: {round(weekly_rate_of_return * 100 - 100, 2)}%")
#     print(f"{colored('Profits for the Year: ', 'green')}${int(total_profits):,d}")
#     print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
#     print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = {round(ending_capital / total_capital, 2)}X Your Money")
#     print("**********GROSS SUMMARY**********************")
#     print()
#
#     print("**********NET SUMMARY************************")
#     print(f"Tax Rate: {int(tax_rate * 100)}%")
#     print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
#     print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
#     print(f"Total Contributions To Date: ${total_capital:,d}")
#     print(f"Profits for the Year: ${round(total_profits - tax_amount):,d}")
#     print(f"Total Profits All Time: ${round(total_profits_total):,d}")
#     print(f"{int(net_realized_gains):,d} / {total_capital:,d} {round(net_realized_gains / total_capital, 2)}X Your Money")
#     print("**********NET SUMMARY************************")
#     return years, net_realized_gains, total_capital
#
#
# def compound(brief='', tax_amount=0, *starting_capitals_list):  # needs current_capital and tax_amount in order to work
#     """
#     This function will figure out how much money you will make after a certain amount of time, will take into
#     consideration how much money you started with and your interest rate every week, etc
#
#     :param brief: print brief summary or long summary, prints long summary by default
#     :param tax_amount: This value will start at zero but will compute itself at the end of each year
#     :return: nothing
#     """
#     for each_starting_capital in starting_capitals_list:  # gets me the first paramater in the *args
#         for current_capital in each_starting_capital:  # gets me the first element in the first parameter in *args
#             tax_amount = 0  # resets tax amount each time you get a new starting value from the starting_capitals_list
#             initial_investment_for_brief_summary = current_capital  # for brief_summary can keep track of initial inv
#
#             for years in range(time_frame_for_investment):  # This specifies how many years you will be investing your money
#                 # helps me keep tracking of the profits for just the current year
#                 start_of_the_year_capital = current_capital - tax_amount
#                 current_capital = start_of_the_year_capital
#                 if brief.lower() == 'brief':
#                     pass
#                 else:
#                     print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
#                     print(f"Monthly Additional Contribution = ${monthly_contribution:,d}")
#
#                 for month in year:  # the month of the loop that we are currently on
#                     current_capital = current_capital + monthly_contribution
#                     if brief.lower() == 'brief':
#                         pass
#                     else:
#                         print(f"\n\t\tYEAR {years + 1} {month.upper()}")
#                         print(f"Adding Monthly Contribution: [+] ${monthly_contribution:,d}")
#                     weekly_profits = []
#
#                     for week in range(4):  # 4 weeks in a month (weekly compound interest)
#                         weekly_profits.append(round(current_capital * weekly_profits_calculator))
#                         if brief.lower() == 'brief':
#                             pass
#                         else:
#                             print(f"Start of Week {week + 1}: ${round(current_capital):,d} [+] ${int(weekly_profits[week]):,d} ")
#                         current_capital = current_capital * weekly_rate_of_return
#
#                     weekly_profits_total = 0  # get the total for the week and display the profits(This is gross)
#                     for each_weekly_profit in weekly_profits:
#                         weekly_profits_total = weekly_profits_total + each_weekly_profit
#                     if brief.lower() == 'brief':
#                         pass
#                     else:
#                         print(f"Total Profits for the Month: ${weekly_profits_total:,d}")
#                         print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")
#
#                 # THIS IS THE TAX INFORMATION SECTION THAT HELPS CALCULATE THE NET AMOUNT, PROFITS, TAXES OWED EACH YEAR
#                 # WITH TAXES THIS IS THE ACTUAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALY
#                 total_profits = current_capital - start_of_the_year_capital - monthly_contribution * 12  # total profits for the current year
#                 total_capital = initial_investment_for_brief_summary + monthly_contribution * 12 * (years + 1)
#                 tax_amount = total_profits * tax_rate  # just blindly assuming you are paying a total of 37% taxes
#                 total_profits_total = current_capital - total_capital - tax_amount  # total profits total (since week 1)
#                 ending_capital = current_capital
#                 net_realized_gains = ending_capital - tax_amount
#
#                 # on year 5 print the brief summary
#                 if (years + 1) == time_frame_for_investment and brief.lower() == 'brief':
#                     brief_summary(years, net_realized_gains, total_capital, tax_amount, initial_investment_for_brief_summary)
#
#                 if brief.lower() != 'brief':  # print the long summary
#                     summary(years, start_of_the_year_capital, total_capital, net_realized_gains, ending_capital, total_profits, tax_amount, total_profits_total, initial_investment_for_brief_summary)
#
#
# def compound_summary_brief():  # needs current_capital and tax_amount in order to work
#     """
#     Calls the Compound Function
#     This function will display the 5 year summaries. It will not display the monthly information or gross information
#     """
#     compound('brief', 0, starting_capitals_list)
#
#
# def compound_summary_long():
#     """
#     Calls the Compound Function and it will display all the information available
#     :return:
#     """
#     compound('', 0, starting_capitals_list)
#
#
# # compound_summary_long()
# compound_summary_brief()
# ----------------------------------------------------------------------------------------------------------------------
# # did some refactoring turned the loops into a function named compound()
# # This is a application that will calculate compound interest over a certain amount of time
# from termcolor import colored
#
# starting_capital = 10000
# monthly_contribution = 1000
# current_capital = starting_capital
# ending_capital = 0
# total_profits = 0
# time_frame_for_investment = 5  # number of years that you want to invest
# total_contribution = monthly_contribution * 12 * time_frame_for_investment
# weekly_rate_of_return = 1.01  # 4 % monthly if rate is 1.01
# weekly_profits_calculator = weekly_rate_of_return - 1
# tax_amount = 0
# tax_rate = .37  # blinding assuming that you are going to be paying 37% in taxes
# year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
#
# def brief_summary(years, net_realized_gains, total_capital, tax_amount):  # want to display just a little bit of information for different interest rates, starting capitals, etc
#     """
#     Display a less detailed Summary report of your investments, takes in the variable as parameters from your compound() function
#     :param years:
#     :param net_realized_gains:
#     :param total_capital:
#     :return:
#     """
#     print()
#     print(f"Printing Summary Report For Year {years + 1}")
#     print("**********NET SUMMARY************************")
#     print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
#     print(f"Weekly Rate Of Return: {int(weekly_rate_of_return * 100 - 100)}%")
#     print(f"Tax Rate: {int(tax_rate * 100)}%")
#     print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
#     print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
#     print(f"{int(net_realized_gains):,d} / {total_capital:,d} {round(net_realized_gains / total_capital, 2)}X Your Money")
#     print(f"Total Contributions To Date: ${total_capital:,d}")
#     print("**********NET SUMMARY************************")
#
#
# def summary(years, start_of_the_year_capital, total_capital, net_realized_gains, ending_capital, total_profits, tax_amount, total_profits_total):
#     """
#     Display a Summary report of your investments, takes in the variable as parameters from your compound() function
#     :param years:
#     :param start_of_the_year_capital:
#     :param total_capital:
#     :param net_realized_gains:
#     :param ending_capital:
#     :param total_profits:
#     :param tax_amount:
#     :return:
#     """
#     print()
#     print(f"Printing Summary Report For Year {years + 1}")
#
#     print("**********GROSS SUMMARY**********************")
#     print(f"Starting Investment: ${int(start_of_the_year_capital):,d}")
#     print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
#     print(f"Weekly Rate Of Return: {int(weekly_rate_of_return * 100 - 100)}%")
#     print(f"{colored('Profits for the Year: ', 'green')}${int(total_profits):,d}")
#     print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
#     print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = {round(ending_capital / total_capital, 2)}X Your Money")
#     print("**********GROSS SUMMARY**********************")
#     print()
#
#     print("**********NET SUMMARY************************")
#     print(f"Tax Rate: {int(tax_rate * 100)}%")
#     print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
#     print(f"{colored('Profits for the Year: ', 'green')}${round(total_profits - tax_amount):,d}")
#     print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
#     print(f"{int(net_realized_gains):,d} / {total_capital:,d} {round(net_realized_gains / total_capital, 2)}X Your Money")
#     print(f"Total Contributions To Date: ${total_capital:,d}")
#     print(f"Total Profits All Time: ${round(total_profits_total):,d}")
#     print("**********NET SUMMARY************************")
#     return years, net_realized_gains, total_capital
#
#
# def compound(current_capital, brief='', tax_amount=0):  # needs current_capital and tax_amount in order to work
#     """
#     This function will figure out how much money you will make after a certain amount of time, will take into
#     consideration how much money you started with and your interest rate every week, etc
#
#     :param brief: print brief summary or long summary, prints long summary by default
#     :param current_capital: needs to know what your current capital is Ex: 10,000 (insert without commas)
#     :param tax_amount: This value will start at zero but will compute itself at the end of each year
#     :return: nothing
#     """
#     for years in range(time_frame_for_investment):  # This specifies how many years you will be investing your money
#         # helps me keep tracking of the profits for just the current year
#         start_of_the_year_capital = current_capital - tax_amount
#         current_capital = start_of_the_year_capital
#         if brief.lower() == 'brief':
#             pass
#         else:
#             print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
#             print(f"Monthly Additional Contribution = ${monthly_contribution:,d}")
#
#         for month in year:  # the month of the loop that we are currently on
#             current_capital = current_capital + monthly_contribution
#             if brief.lower() == 'brief':
#                 pass
#             else:
#                 print(f"\n\t\tYEAR {years + 1} {month.upper()}")
#                 print(f"Adding Monthly Contribution: [+] ${monthly_contribution:,d}")
#             weekly_profits = []
#
#             for week in range(4):  # 4 weeks in a month (weekly compound interest)
#                 weekly_profits.append(round(current_capital * weekly_profits_calculator))
#                 if brief.lower() == 'brief':
#                     pass
#                 else:
#                     print(f"Start of Week {week + 1}: ${round(current_capital):,d} [+] ${int(weekly_profits[week]):,d} ")
#                 current_capital = current_capital * weekly_rate_of_return
#
#             weekly_profits_total = 0  # get the total for the week and display the profits(This is gross)
#             for each_weekly_profit in weekly_profits:
#                 weekly_profits_total = weekly_profits_total + each_weekly_profit
#             if brief.lower() == 'brief':
#                 pass
#             else:
#                 print(f"Total Profits for the Month: ${weekly_profits_total:,d}")
#                 print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")
#
#         # WITH TAXES THIS IS THE ACTUAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALY
#         total_profits = current_capital - start_of_the_year_capital - monthly_contribution * 12  # total profits for the current year
#         total_capital = starting_capital + monthly_contribution * 12 * (years + 1)
#         tax_amount = total_profits * tax_rate  # just blindly assuming you are paying a total of 37% taxes
#         total_profits_total = current_capital - starting_capital - total_contribution - tax_amount  # total profits total
#         ending_capital = current_capital
#         net_realized_gains = ending_capital - tax_amount
#
#         if brief.lower() == 'brief':  # print the brief summary
#             brief_summary(years, net_realized_gains, total_capital, tax_amount)
#         else:  # print the long summary
#             summary(years, start_of_the_year_capital, total_capital, net_realized_gains, ending_capital, total_profits, tax_amount, total_profits_total)
#
#
# def compound_summary_brief():  # needs current_capital and tax_amount in order to work
#     """
#     Builds off the Compound function
#     This function will display the yearly summaries. It will not display the monthly information or gross information
#     """
#     compound(current_capital, 'brief')
#
#
# compound(current_capital)
# compound_summary_brief()
#-----------------------------------------------------------------------------------------------------------------------









 # This is a application that will calculate compound interest over a certain amount of time
# from termcolor import colored
#
# starting_capital = 10000
# monthly_contribution = 1000
# current_capital = starting_capital
# ending_capital = 0
# total_profits = 0
# time_frame_for_investment = 5  # number of years that you want to invest
# total_contribution = monthly_contribution * 12 * time_frame_for_investment
# weekly_rate_of_return = 1.01  # 4 % monthly if rate is 1.01
# weekly_profits_calculator = weekly_rate_of_return - 1
# tax_amount = 0
# tax_rate = .37  # blinding assuming that you are going to be paying 37% in taxes
# year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
#
# def summary():
#     print()
#     print(f"Printing Summary Report For Year {years + 1}")
#
#     print("**********GROSS SUMMARY**********************")
#     print(f"Starting Investment: ${int(start_of_the_year_capital):,d}")
#     print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
#     print(f"Weekly Rate Of Return: {int(weekly_rate_of_return * 100 - 100)}%")
#     print(f"{colored('Profits for the Year: ', 'green')}${int(total_profits):,d}")
#     print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
#     print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = {round(ending_capital / total_capital, 2)}X Your Money")
#     print("**********GROSS SUMMARY**********************")
#     print()
#
#     print("**********NET SUMMARY************************")
#     print(f"Tax Rate: {int(tax_rate * 100)}%")
#     print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
#     print(f"{colored('Profits for the Year: ', 'green')}${round(total_profits - tax_amount):,d}")
#     print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
#     print(f"{int(net_realized_gains):,d} / {total_capital:,d} {round(net_realized_gains / total_capital, 2)}X Your Money")
#     print(f"Total Contributions: ${total_capital: ,d}(All time Total Contribution)")
#     print("**********NET SUMMARY************************")
#
#
# for years in range(time_frame_for_investment):  # This specifies how many years you will be investing your money
#     # helps me keep tracking of the profits for just the current year
#     start_of_the_year_capital = current_capital - tax_amount
#     current_capital = start_of_the_year_capital
#     print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
#     print(f"Monthly Additional Contribution = ${monthly_contribution:,d}")
#
#     for month in year:  # the month of the loop that we are currently on
#         current_capital = current_capital + monthly_contribution
#         print(f"\n\t\tYEAR {years + 1} {month.upper()}")
#         print(f"Adding Monthly Contribution: [+] ${monthly_contribution:,d}")
#         weekly_profits = []
#
#         for week in range(4):  # 4 weeks in a month (weekly compound interest)
#             weekly_profits.append(round(current_capital * weekly_profits_calculator))
#             print(f"Start of Week {week + 1}: ${round(current_capital):,d} [+] ${int(weekly_profits[week]):,d} ")
#             current_capital = current_capital * weekly_rate_of_return
#
#         weekly_profits_total = 0  # get the total for the week and display the profits(This is gross)
#         for each_weekly_profit in weekly_profits:
#             weekly_profits_total = weekly_profits_total + each_weekly_profit
#         print(f"Total Profits for the Month: ${weekly_profits_total:,d}")
#         print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")
#
#     # WITH TAXES THIS IS THE ACTUAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALY
#     total_profits = current_capital - start_of_the_year_capital - monthly_contribution * 12  # total profits for the current year
#     total_profits_total = current_capital - starting_capital - total_contribution # total profits total
#     total_capital = starting_capital + monthly_contribution * 12 * (years + 1)
#     tax_amount = total_profits * tax_rate  # just blindly assuming you are paying a total of 37% taxes
#     ending_capital = current_capital
#     net_realized_gains = ending_capital - tax_amount
#
#     summary()
