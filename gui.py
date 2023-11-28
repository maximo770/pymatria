import tkinter as tk
import module

root = tk.Tk()
root.title("Pymatria")
root.geometry("500x400", )
root.resizable(False, False)
root.configure(bg="#30363d")

entry = tk.Entry(root, justify="center", width=50, font=("Roboto", 12), bg="#b3bbc4", borderwidth=0, highlightthickness=0)
output_label = tk.Text(root, height=5, width=50, font=("Roboto", 12), bg="#b3bbc4", borderwidth=0, highlightthickness=0, wrap=tk.WORD)


def process_user_input():
    user_input = entry.get()  # Get the user input
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
        output_text = f"The gematria value of the word '{word[::-1]}' is {gematria_value}."
        output_text += f"\nCorresponding words with the same gematria value:\n {', '.join(corresponding_words[::-1])}" if corresponding_words[::-1] else "\nNo corresponding words found with the gematria value."
    else:
        output_text = f"Invalid Hebrew word. Please enter a valid Hebrew word from the Bereshit list."
    return output_text


def process_numerical_value(value):
    corresponding_words = module.find_all_hebrew_words_by_numerical_value(value)
    return f"The Corresponding words with the numerical value {value} in Bereshit are:\n {', '.join(corresponding_words[::-1])}"


def clear():
    output_label.delete('1.0', tk.END)
    entry.delete(0, tk.END)


title = tk.Label(root, text="Pymatria", font=("Roboto", 22), fg="#0080ff", bg="#30363d")
title.grid(row=0, column=0, padx=(25, 10), pady=(25, 10))

label = tk.Label(root, text="Enter a Hebrew word or numerical value: ", pady=5, font=("Roboto", 12), fg="#ffffff", bg="#30363d")
label.grid(row=1, column=0, padx=(25, 10))

entry.grid(row=2, column=0, padx=(25, 10))

output_label.grid(row=3, column=0, padx=(25, 10), pady=10)

submit_button = tk.Button(root, text="Submit",
                          command=process_user_input,
                          width=15,
                          bg="#0080ff",
                          fg="#ffffff",
                          activebackground="#4a90d9",
                          activeforeground="#000000",
                          borderwidth=0,
                          highlightthickness=0)
submit_button.grid(row=4, column=0, padx=(25, 10))

clear_button = tk.Button(root, text="Clear",
                         command=clear,
                         width=15,
                         bg="#0080ff",
                         fg="#ffffff",
                         activebackground="#4a90d9",
                         activeforeground="#000000",
                         borderwidth=0,
                         highlightthickness=0)
clear_button.grid(row=5, column=0, padx=(25, 10), pady=10)

root.mainloop()
