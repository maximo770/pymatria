# Bereshit Hebrew Word List with gematria value
BERESHIT_LIB = {}

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
with open("output.txt") as f:
    for line in f:
        word, value = line.strip().split(",")
        BERESHIT_LIB[word] = int(value)

def find_all_hebrew_words_by_numerical_value(numerical_value):
    matching_words = [word for word, value in BERESHIT_LIB.items() if value == numerical_value]
    return matching_words

def reduce_number_to_hebrew_word(number):
    """Converts a given number to its corresponding Hebrew word using gematria."""
    # Initialize an empty string to store the Hebrew word
    hebrew_word = ""

    # Check if the input number is valid
    if number < 1 or number > 7000:
        raise ValueError("The input number must be between 1 and 7000.")

    # Iterate while the number is greater than zero
    while number > 0:
        # Find the largest gematria value that is less than or equal to the remaining number
        largest_gematria_value = 0
        for value in GEMATRIA_CHART.values():
            if value <= number and value > largest_gematria_value:
                largest_gematria_value = value

        # Find the corresponding Hebrew letter for the largest gematria value
        hebrew_letter = ""
        for letter, value in GEMATRIA_CHART.items():
            if value == largest_gematria_value:
                hebrew_letter = letter
                break

        # Append the Hebrew letter to the word
        hebrew_word += hebrew_letter

        # Subtract the largest gematria value from the remaining number
        number -= largest_gematria_value

    # Return the Hebrew word
    return hebrew_word

def calculate_gematria_value(hebrew_word):
    gematria_value = 0

    for letter in hebrew_word:
        letter_value = GEMATRIA_CHART.get(letter, 0)
        gematria_value += letter_value

    return gematria_value

def process_user_input(user_input):
    if not user_input:  # Check if the input is empty
        print("Please enter a valid numerical value or a Hebrew word from the Bereshit list.")
    elif user_input.isalpha():  # Check if the input is a Hebrew word (alphabetic characters)
        if user_input in BERESHIT_LIB:
            print("The gematria value of the word", user_input, "is", BERESHIT_LIB[user_input])
        else:
            print("The word", user_input, "is not found in the Bereshit Hebrew word list.")
    else:  # The input is a numerical value
        try:
            number = int(user_input)
            hebrew_word = reduce_number_to_hebrew_word(number)
        except ValueError:
            print("Invalid input. Please enter a valid numerical value or a Hebrew word from the Bereshit list.")

if __name__ == "__main__":
    user_input = input("Enter a Hebrew word or a numerical value to find the corresponding gematria: ")
    process_user_input(user_input)

# Check if the input is a number
try:
    number = int(user_input)
    # Convert the number to a Hebrew word
    hebrew_word = reduce_number_to_hebrew_word(number)
    # Print the Hebrew word
    print("The gematria value of the number", user_input, "is", hebrew_word)

    # Find all corresponding Hebrew words for the numerical value
    try:
        corresponding_hebrew_words = find_all_hebrew_words_by_numerical_value(number)
    except ValueError:
        print(f"No corresponding Hebrew word found for numerical value {number}.")
    else:
        if corresponding_hebrew_words:
            print(f"The corresponding Hebrew words for the numerical value {number} are:")
            try:
                for word in corresponding_hebrew_words:
                    try:
                        print(word)
                    except (TypeError, ValueError) as e:
                        print(f"Error printing Hebrew word: {e}")
            except Exception as e:
                print(f"Error iterating through Hebrew words: {e}")
                
except Exception as e:
    print()