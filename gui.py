import tkinter as tk
import module

root = tk.Tk()

root.title("Pymatria")
root.geometry("500x400")

title = tk.Label(root, text="Pymatria", font=("Roboto", 22), padx=50, pady=20)
title.pack()

label = tk.Label(root, text="Enter a Hebrew word or numerical value: ", pady=5)
label.pack()

entry = tk.Entry(root, justify="right", width=50)
entry.pack()

output_label = tk.Text(root, height=5, width=50)
output_label.pack()


def process_user_input():
    user_input = entry.get()

    if not user_input:  # Check if the input is empty
        output_label.delete('1.0', tk.END)  # Clear the existing text before updating
        output_label.insert(tk.END, "Please enter a valid numerical value or a Hebrew word from the Bereshit list.")
    elif user_input.isalpha():  # Check if the input is a Hebrew word (alphabetic characters)
        if user_input in module.BERESHIT_LIB:
            gematria_value = module.calculate_gematria_value(user_input)
            corresponding_words = module.find_all_hebrew_words_by_numerical_value(gematria_value)
            output_text = f"The gematria value of the word '{user_input}' is {gematria_value}."

            if corresponding_words:
                output_text += f"\nCorresponding words with the same gematria value:\n {', '.join(corresponding_words)}"
            else:
                output_text += "\nNo corresponding words found with the gematria value."
        else:
            output_text = f"Invalid Hebrew word. Please enter a valid Hebrew word from the Bereshit list."

    elif user_input.isdigit():
        numerical_value = int(user_input)
        corresponding_words = module.find_all_hebrew_words_by_numerical_value(numerical_value)
        output_text = f"The Corresponding words with the numerical value {numerical_value} in Bereshit are:\n {', '.join(corresponding_words)}"
    else:
        output_text = "Invalid input. Please enter a valid numerical value or a Hebrew word from the Bereshit list."

    output_label.delete('1.0', tk.END)  # Clear the existing text before updating
    output_label.insert(tk.END, output_text)


def clear():
    output_label.delete('1.0', tk.END)
    entry.delete(0, tk.END)


button = tk.Button(root, text="Submit", command=process_user_input, width=15)
button.pack()

button = tk.Button(root, text="Clear", command=clear, width=15)
button.pack()

root.mainloop()
