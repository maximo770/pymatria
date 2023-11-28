import tkinter as tk
import module


def process_user_input():
    user_input = entry.get()
    output_label.delete('1.0', tk.END)  # Clear the existing text before updating

    if not user_input:  # Check if the input is empty
        output_text = "Please enter a valid numerical value or a Hebrew word from the Bereshit list."
    elif user_input.isalpha():  # Check if the input is a Hebrew word (alphabetic characters)
        output_text = process_hebrew_word(user_input)
    elif user_input.isdigit():
        output_text = process_numerical_value(int(user_input))
    else:
        output_text = "Invalid input. Please enter a valid numerical value or a Hebrew word from the Bereshit list."

    output_label.insert(tk.END, output_text)


def process_hebrew_word(word):
    if word in module.BERESHIT_LIB:
        gematria_value = module.calculate_gematria_value(word)
        corresponding_words = module.find_all_hebrew_words_by_numerical_value(gematria_value)
        output_text = f"The gematria value of the word '{word}' is {gematria_value}."
        output_text += f"\nCorresponding words with the same gematria value:\n {', '.join(corresponding_words)}" if corresponding_words else \
            "\nNo corresponding words found with the gematria value."
    else:
        output_text = f"Invalid Hebrew word. Please enter a valid Hebrew word from the Bereshit list."
    return output_text


def process_numerical_value(value):
    corresponding_words = module.find_all_hebrew_words_by_numerical_value(value)
    return f"The Corresponding words with the numerical value {value} in Bereshit are:\n {', '.join(corresponding_words)}"


def clear():
    output_label.delete('1.0', tk.END)
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Pymatria")
root.geometry("500x400")
root.resizable(False, False)

title = tk.Label(root, text="Pymatria", font=("Roboto", 22))
title.grid(row=0, column=0, padx=(50, 10), pady=10)

label = tk.Label(root, text="Enter a Hebrew word or numerical value: ", pady=5)
label.grid(row=1, column=0, padx=(50, 10))

entry = tk.Entry(root, justify="right", width=50)
entry.grid(row=2, column=0, padx=(50, 10))

output_label = tk.Text(root, height=5, width=50)
output_label.grid(row=3, column=0, padx=(50, 10), pady=10)

submit_button = tk.Button(root, text="Submit", command=process_user_input, width=15)
submit_button.grid(row=4, column=0, padx=(50, 10))

clear_button = tk.Button(root, text="Clear", command=clear, width=15)
clear_button.grid(row=5, column=0, padx=(50, 10), pady=10)

root.mainloop()
