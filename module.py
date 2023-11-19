# Bereshit Hebrew Word List with gematria value
from typing import Any

BERESHIT_LIB: dict[Any, int] = {}

# Define the gematria chart
GEMATRIA_CHART = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "כ": 20,
    "ל": 30,
    "מ": 40,
    "נ": 50,
    "ס": 60,
    "ע": 70,
    "פ": 80,
    "צ": 90,
    "ק": 100,
    "ר": 200,
    "ש": 300,
    "ת": 400,
    "ך": 500,
    "ם": 600,
    "ן": 700,
    "ף": 800,
    "ץ": 900,
}

# Read the output.txt file and populate BERESHIT_LIB
with open("bereshit.txt") as f:
    for line in f:
        word, value = line.strip().split(',')
        BERESHIT_LIB[word] = int(value)


def find_all_hebrew_words_by_numerical_value(numerical_value):
    matching_words = []
    for words, values in BERESHIT_LIB.items():
        if values == numerical_value:
            matching_words.append(words)
    return matching_words


def reduce_number_to_hebrew_word(numbers):
    """Converts a given number to its corresponding Hebrew word using gematria."""
    # Initialize an empty string to store the Hebrew word
    hebrew_words = ""

    # Check if the input number is valid
    if numbers < 1 or numbers > 7000:
        raise ValueError("The input number must be between 1 and 7000.")

    # Iterate while the number is greater than zero
    while numbers > 0:
        # Find the largest gematria value that is less than or equal to the remaining number
        largest_gematria_value = 0
        for values in GEMATRIA_CHART.values():
            if numbers >= values > largest_gematria_value:
                largest_gematria_value = values

        # Find the corresponding Hebrew letter for the largest gematria value
        hebrew_letter = ""
        for letter, values in GEMATRIA_CHART.items():
            if values == largest_gematria_value:
                hebrew_letter = letter
                break

        # Append the Hebrew letter to the word
        hebrew_words += hebrew_letter

        # Subtract the largest gematria value from the remaining number
        numbers -= largest_gematria_value

    # Return the Hebrew word
    return hebrew_words


def calculate_gematria_value(hebrew_words):
    gematria_value = 0

    for letter in hebrew_words:
        letter_value = GEMATRIA_CHART.get(letter, 0)
        gematria_value += letter_value

    return gematria_value


def process_user_input(users_input):
    if not users_input:  # Check if the input is empty
        print("Please enter a valid numerical value or a Hebrew word from the Bereshit list.")
    elif users_input.isalpha():  # Check if the input is a Hebrew word (alphabetic characters)
        if users_input in BERESHIT_LIB:
            gematria_value = calculate_gematria_value(users_input)
            corresponding_words = [words for words in BERESHIT_LIB if BERESHIT_LIB[words] == gematria_value]
            if corresponding_words:
                print("The gematria value of the word", users_input, "is", gematria_value)
                print("Corresponding words with the same gematria value:")
                for words in corresponding_words:
                    print(words)
            else:
                print("No corresponding words found with the gematria value:", gematria_value)
    else:  # The input is a numerical value
        try:
            gematria_value = calculate_gematria_value(users_input)

            if gematria_value in BERESHIT_LIB.values():
                corresponding_words = [words for words in BERESHIT_LIB if BERESHIT_LIB[word] == gematria_value]
                if corresponding_words:
                    print("Corresponding words with the same gematria value:", ", ".join(corresponding_words))
                else:
                    print("No corresponding words found with the gematria value:", gematria_value)
        except ValueError:
            print("Invalid input. Please enter a valid numerical value or a Hebrew word from the Bereshit list.")


def main():
    while True:
        user_input = input("Enter a valid numerical value or a Hebrew word from the Bereshit list: ")
        process_user_input(user_input)

        response = input("Continue? (y/n): ")
        if response.lower() != "y":
            break


if __name__ == "__main__":
    main()
