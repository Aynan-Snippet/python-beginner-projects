import time

sentence = "Apple is a fruit"

print("Type this sentence:")
print(sentence)

input("Press Enter when you are ready...")

start_time = time.time()

typed = input("Start typing: ")

end_time = time.time()

time_taken = end_time - start_time

words = len(typed.split())
typing_speed = (words / time_taken) * 60

mistakes = 0

for i in range(min(len(sentence), len(typed))):
    if sentence[i] != typed[i]:
        mistakes += 1

mistakes += abs(len(sentence) - len(typed))

print("\nResult:")
print("Time taken:", round(time_taken, 2), "seconds")
print("Typing speed:", round(typing_speed, 2), "WPM")
print("Mistakes:", mistakes)