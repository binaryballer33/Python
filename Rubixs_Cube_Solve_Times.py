"""
Shaquille's
Rubix's Cube Statisics

"""
import datetime


def rubix_cube_stats(solve_times, date=datetime.datetime.today()):
    import statistics
    """
    Expects a list of rubix cube solve times for the parameter solve_times
        -Prints out todays date and time. the sum, avg, and amount of solves in your list of solve_times


    """
    print("=" * 100)
    print("Rubix Cube Stats:")
    print(f'\t\tToday is {date} yyyy-mm-dd: hh:mm:sec:ms')

    # Generates the Number for the amount of times you solved the rubix cube
    amount_of_solves = 0
    for each_solve in solve_times:
        amount_of_solves = amount_of_solves + 1
    print(f'\t\tThis information is based on {amount_of_solves} solves:')

    # Generates the Sum for you
    sum = 0
    for number in solve_times:
        sum = sum + number

    print(f'\t\tYour Average time is: {sum / amount_of_solves} seconds' )
    print(f'\t\tYou solve the rubix\'s cube in {statistics.mode(solve_times)} seconds the most')
    print("\t\tThe Sum of all your solves is: " + str(sum))

    print("_" * 100)

    # Prints out the solve and how many times you solved it in that amount of time
    # Only prints out the solve if it's in the list, if you never solved it in 10 seconds 10 won't be printed out
    # Example: You solved the rubix cube in 16 seconds 2 times
    starter_count = 5
    for each_rubix_completion in range(5, 61):
        if each_rubix_completion in solve_times:
            print(f'\t\tYou solved the rubix cube in {each_rubix_completion} seconds {solve_times.count(starter_count)} times out of {amount_of_solves}: {(solve_times.count(starter_count) / amount_of_solves) * 100 }%')
            starter_count += 1
        else:
            starter_count += 1
    print("=" * 100)
    print(), print(), print()


solves = [19, 16, 24, 18, 19, 20, 21, 24, 20, 17, 16, 20, 19, 23, 19, 22, 17, 16, 17, 20, 19, 18, 21, 17, 23, 17, 20, 17, 22, 19]
rubix_cube_stats(solves)


