import random

def generate_random_numbers(start, end, count):
    return [random.randint(start, end) for _ in range(count)]

def get_even_streaks(numbers):
    streaks = []
    current_streak = 0
    for number in numbers:
        if number % 2 == 0:
            current_streak += 1
        else:
            if current_streak > 0:
                streaks.append(current_streak)
                current_streak = 0
    if current_streak > 0:
        streaks.append(current_streak)
    return max(streaks) if streaks else 0

def get_odd_streaks(numbers):
    streaks = []
    current_streak = 0
    for number in numbers:
        if number % 2 == 1:
            current_streak += 1
        else:
            if current_streak > 0:
                streaks.append(current_streak)
                current_streak = 0
    if current_streak > 0:
        streaks.append(current_streak)
    return max(streaks) if streaks else 0

def main():
    start = 1
    end = 2
    count = 100
    runs = int(input("Enter the number of times to run the program: "))
    even_tops = []
    odd_tops = []
    for i in range(runs):
        numbers = generate_random_numbers(start, end, count)
        even_top = get_even_streaks(numbers)
        odd_top = get_odd_streaks(numbers)
        even_tops.append(even_top)
        odd_tops.append(odd_top)
        print(f"Run {i+1}: Longest streak of even numbers: {even_top}, Longest streak of odd numbers: {odd_top}")
    average_even_top = sum(even_tops) / len(even_tops)
    average_odd_top = sum(odd_tops) / len(odd_tops)
    print(f"Average longest streak of even numbers over {runs} runs: {average_even_top}")
    print(f"Average longest streak of odd numbers over {runs} runs: {average_odd_top}")

if __name__ == "__main__":
    main()
