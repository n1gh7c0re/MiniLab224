import requests
import tkinter as tk
from tkinter import font

def send_request_and_display_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text  # Просто используйте текстовое содержимое ответа
        show_text(data)
    except requests.exceptions.RequestException as e:
        show_text(f"An error occurred: {e}")

def show_text(text_content):
    window = tk.Toplevel(root)
    window.title("Вывод текста")
    custom_font = font.Font(family="Helvetica", size=12)

    text_widget = tk.Text(window, height=10, width=40, font=custom_font)
    text_widget.insert(tk.END, text_content)
    text_widget.pack(padx=10, pady=10)

def exit_application():
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("Application")
    root.geometry("500x450")

    custom_font = font.Font(family="Helvetica", size=14, weight="bold")

    bg_color = "#dfe3ee"
    button_bg_color = "#a3c1ad"

    root.configure(bg=bg_color)

    button1 = tk.Button(root, text="date", command=lambda: send_request_and_display_response("http://numbersapi.com/random/date"), bg=button_bg_color, fg="black", font=custom_font, height=2, width=20)
    button2 = tk.Button(root, text="year", command=lambda: send_request_and_display_response("http://numbersapi.com/random/year"), bg=button_bg_color, fg="black", font=custom_font, height=2, width=20)
    button3 = tk.Button(root, text="number", command=lambda: send_request_and_display_response("http://numbersapi.com/random/trivia"), bg=button_bg_color, fg="black", font=custom_font, height=2, width=20)
    exit_button = tk.Button(root, text="exit", command=exit_application, bg="#ff6f61", fg="white", font=custom_font, height=2, width=20)

    button1.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=10)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()