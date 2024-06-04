import tkinter as tk

class ToDo:
    def __init__(self):
        self.events = []

    def add_event(self):
        date = self.txt1.get()
        time = self.txt2.get()
        event = self.txt3.get()

        if date and time and event:
            event_dict = {
                "Date": date,
                "Time": time,
                "Event": event
            }
            self.events.append(event_dict)
            self.lb1.insert(tk.END, f"{date}-{time}-{event}")
            self.clear_entries()

    def clear_entries(self):
        self.txt1.delete(0, tk.END)
        self.txt2.delete(0, tk.END)
        self.txt3.delete(0, tk.END)

    def update_event(self):
        index = self.lb1.curselection()
        try:
            index = int(index[0])
            selected_event = self.events[index]
            self.create_update_popup(selected_event, index)
        except IndexError:
            pass

    def create_update_popup(self, selected_event, index):
        update_window = tk.Toplevel()
        update_window.title("Update Event")

        date_label = tk.Label(update_window, text="Date(YYYY-MM-DD):")
        date_entry = tk.Entry(update_window)
        date_entry.insert(tk.END, selected_event['Date'])

        time_label = tk.Label(update_window, text="Time(HH:MM):")
        time_entry = tk.Entry(update_window)
        time_entry.insert(tk.END, selected_event['Time'])

        event_label = tk.Label(update_window, text="Event: ")
        event_entry = tk.Entry(update_window)
        event_entry.insert(tk.END, selected_event['Event'])

        date_label.grid(row=0, column=0)
        date_entry.grid(row=0, column=1)
        time_label.grid(row=1, column=0)
        time_entry.grid(row=1, column=1)
        event_label.grid(row=2, column=0)
        event_entry.grid(row=2, column=1)

        update_button = tk.Button(update_window, text="Update", command=lambda: self.perform_update(index, date_entry.get(), time_entry.get(), event_entry.get(), update_window))
        update_button.grid(row=3, columnspan=2)

    def perform_update(self, index, new_date, new_time, new_event, update_window):
        try:
            selected_event = self.events[index]
            selected_event['Date'] = new_date
            selected_event['Time'] = new_time
            selected_event['Event'] = new_event
            self.lb1.delete(index)
            self.lb1.insert(index, f"{new_date}-{new_time}-{new_event}")
            update_window.destroy()
        except IndexError:
            pass

    def delete_event(self):
        index = self.lb1.curselection()
        try:
            index = int(index[0])
            del self.events[index]
            self.lb1.delete(index)
        except IndexError:
            pass

    def main(self):
        self.window = tk.Tk()
        self.window.geometry("700x400")

        self.date = tk.Label(text="Date(YYYY-MM-DD):")
        self.txt1 = tk.Entry()
        self.date.grid(row=0, column=0)
        self.txt1.grid(row=0, column=1)

        self.time = tk.Label(text="Time(HH:MM):")
        self.txt2 = tk.Entry()
        self.time.grid(row=0, column=2)
        self.txt2.grid(row=0, column=3)

        self.event = tk.Label(text="Event: ")
        self.txt3 = tk.Entry()
        self.event.grid(row=0, column=4)
        self.txt3.grid(row=0, column=5)

        self.btn1 = tk.Button(text="Add", command=self.add_event)
        self.btn2 = tk.Button(text="Update", command=self.update_event)
        self.btn3 = tk.Button(text="Delete", command=self.delete_event)
        self.btn1.grid(row=0, column=6)
        self.btn2.grid(row=3, column=2)
        self.btn3.grid(row=3, column=3)

        self.lb1 = tk.Listbox(self.window, width=50, height=10)
        self.lb1.grid(row=2, columnspan=6)
        self.lb1.bind("<Double-Button-1>", lambda event: self.update_event())
  # left mouse button

        self.window.mainloop()

if __name__ == "__main__":
    to_do_app = ToDo()
    to_do_app.main()
