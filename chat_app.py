import customtkinter as ctk
import tkinter as tk

#scherm setup
root = ctk.CTk()
root.title("Chat-app")
root.minsize(400, 700)
root.maxsize(400, 700)
root.configure(background= "black")

#functies
def on_key_press(event):
    key = event.keysym
    if key in keybinds:
        keybinds[key]()

def send_message():
    if text_input.get():
        label = ctk.CTkLabel(root, text= text_input.get(), font = ("Arial", (20)), bg_color="#384348", corner_radius=1, anchor = "e")

        label.place(x=0, y=30 * text_order)
        label.update_idletasks()

        x_pos = root.winfo_width() - label.winfo_reqwidth() - 10
        label.place(x= x_pos,y= 30 * text_order)

        text_input.delete(0, ctk.END)
        text_order += 1


keybinds = {
    "Return": send_message
}

#Entry's, Buttons en andere dingen
text_order = 1
text_input = ctk.CTkEntry(root, width= 300, height= 80, font=("Arial",(20)))
text_input.place(x= 10, y= 600)
send_button = ctk.CTkButton(root, command=send_message, width= 50, height= 80, text="SEND", font=("Arial",(20)))
send_button.place(x= 320, y= 600)

root.bind("<KeyPress>", on_key_press)
root.mainloop()