#!/usr/local/bin/python3
"""
Shaquille's
Rubix's Cube Statisics

"""
import datetime

# get's the avearge time of the last n(number) of solves that you specify
def last_n_solves_average(solve_times, n, rubix_cube_stats_report):
    # n = 3 if you want your average from the last 3
    # n = 5 if you want your average from the last 5
    # n = 10 if you want your average from the last 10
    sum = 0

    if len(solve_times) >= n:
        for index in range(len(solve_times) - 1, len(solve_times) - n - 1, -1):
            sum += solve_times[index]
    else:
        print(f"\t\tYou have not solved the cube {n} times yet")
        rubix_cube_stats_report.write(f"\t\tYou have not solved the cube {n} times yet\n")
        
        return 0
    
    print(f"\t\tYour average solve time for the last {n} solves is: {sum / n}") 
    rubix_cube_stats_report.write(f"\t\tYour average solve time for the last {n} solves is: {sum / n}\n") 
    
    return sum / n

def rubix_cube_stats(solve_times, date=datetime.datetime.today()):
    import statistics
    """
    Expects a list of rubix cube solve times for the parameter solve_times
        -Prints out todays date and time. the sum, avg, and amount of solves in your list of solve_times
    """
    with open('rubix_cube_stats.txt', 'a', encoding='UTF-8') as rubix_cube_stats_report:
        print("=" * 100)
        print("Rubix Cube Stats:")
        print(f'\t\tToday is {date}')
        rubix_cube_stats_report.write("=" * 100)
        rubix_cube_stats_report.write("\n")
        rubix_cube_stats_report.write("Rubix Cube Stats:\n")
        rubix_cube_stats_report.write(f"\t\tToday is {date}\n")

        # Generates the Number for the amount of times you solved the rubix cube
        amount_of_solves = len(solve_times)
        print(f'\t\tThis information is based on {amount_of_solves} solves:')
        rubix_cube_stats_report.write(f"\t\tThis information is based on {amount_of_solves} solves:\n")

        # Generates the Sum for you
        sum = 0
        for number in solve_times:
            sum = sum + number

        print(f'\t\tYour Average time is: {sum / amount_of_solves} seconds' )
        print(f'\t\tYou solve the rubix\'s cube in {statistics.mode(solve_times)} seconds the most')
        print("\t\tThe Sum of all your solves is: " + str(sum))
        rubix_cube_stats_report.write(f'\t\tYour Average time is: {sum / amount_of_solves} seconds\n')
        rubix_cube_stats_report.write(f'\t\tYou solve the rubix\'s cube in {statistics.mode(solve_times)} seconds the most\n')
        rubix_cube_stats_report.write("\t\tThe Sum of all your solves is: " + str(sum) + "\n")

        # get the averages
        print()
        rubix_cube_stats_report.write("\n")
        last_n_solves_average(solve_times, 3, rubix_cube_stats_report)
        last_n_solves_average(solve_times, 5, rubix_cube_stats_report)
        last_n_solves_average(solve_times, 10, rubix_cube_stats_report)
        last_n_solves_average(solve_times, 20, rubix_cube_stats_report)
        last_n_solves_average(solve_times, 25, rubix_cube_stats_report)
        print()
        rubix_cube_stats_report.write("\n")

        print("_" * 100)
        rubix_cube_stats_report.write("_" * 100 + "\n")

        # Prints out the solve and how many times you solved it in that amount of time
        # Only prints out the solve if it's in the list, if you never solved it in 10 seconds 10 won't be printed out
        # Example: You solved the rubix cube in 16 seconds 2 times
        for each_rubix_completion in range(5, 61):
            if each_rubix_completion in solve_times:
                print(f'\t\tYou solved the rubix cube in {each_rubix_completion} seconds {solve_times.count(each_rubix_completion)} times out of {amount_of_solves}: {(solve_times.count(each_rubix_completion) / amount_of_solves) * 100 }%')
                rubix_cube_stats_report.write(f'\t\tYou solved the rubix cube in {each_rubix_completion} seconds {solve_times.count(each_rubix_completion)} times out of {amount_of_solves}: {(solve_times.count(each_rubix_completion) / amount_of_solves) * 100 }%\n')
            


        print("=" * 100)
        rubix_cube_stats_report.write("=" * 100 + "\n\n\n\n\n")
        print(), print(), print()


def random_list_generator(): # generates a random list
    import random
    random_list = []
    for number in range(1, 31):
        random_list.append(random.randint(16, 24))
    print("Random List:",random_list)
    return random_list


# rubix_cube_stats(random_list_generator())

# solves = [19, 16, 24, 18, 19, 20, 21, 24, 20, 17, 16, 20, 19, 23, 19, 22, 17, 16, 17, 20, 19, 18, 21, 17, 23, 17, 20, 17, 22, 19]
# rubix_cube_stats(solves, 'March 30th, 2020)

# rubix_cube_stats([12, 18, 14, 19, 16, 18, 18, 14, 16, 19, 14, 15, 15, 14, 17, 13, 19, 16, 16, 15, 14, 18, 16, 15, 17], "Thrusday December 1st, 2022")
# rubix_cube_stats([16, 16, 16, 18, 17, 19, 17, 19, 18, 15, 19, 18, 19, 17, 16, 14, 18, 18, 16, 18, 18, 15, 18, 18, 19, 16], "Thrusday December 1st, 2022")
rubix_cube_stats([15, 19, 19, 17, 17, 17, 18, 17, 14, 16, 17, 17, 17, 21, 19, 18, 18, 14, 15, 18, 15, 16, 16, 15, 16, 16, 16], "Thrusday December 1st, 2022")

