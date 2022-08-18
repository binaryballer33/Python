import os

for filename in os.listdir('/Users/shaq/PycharmProjects/Python'):
    if filename.endswith('.py') or filename.endswith('.txt'):
        with open(filename) as test:
            for line in test:
                print(line)
            print("=" * 120)