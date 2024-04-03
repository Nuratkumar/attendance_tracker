import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

class AttendanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Tracker")
        self.students = pd.DataFrame(columns=['Name'])
        self.attendance = pd.DataFrame(columns=['Date'])

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        self.label_name = tk.Label(self.main_frame, text="Student Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.main_frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.main_frame, text="Add Student", command=self.add_student)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        self.mark_button = tk.Button(self.main_frame, text="Mark Attendance", command=self.mark_attendance)
        self.mark_button.grid(row=1, column=1, padx=5, pady=5)

        self.report_button = tk.Button(self.main_frame, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=2, column=1, padx=5, pady=5)

    def add_student(self):
     name = self.entry_name.get()
     if name.strip() != "":
        new_student = pd.DataFrame({'Name': [name]})
        self.students = pd.concat([self.students, new_student], ignore_index=True)
        self.entry_name.delete(0, tk.END)
        messagebox.showinfo("Success", f"{name} added successfully!")
     else:
        messagebox.showerror("Error", "Please enter a valid name.")

    def mark_attendance(self):
        today = date.today().strftime("%Y-%m-%d")
        self.attendance[today] = ""
        messagebox.showinfo("Success", f"Attendance marked for {today}.")

    def generate_report(self):
        total_days = len(self.attendance.columns) - 1
        present_counts = self.attendance.drop(columns=['Date']).count()
        absent_counts = total_days - present_counts

        plt.figure(figsize=(8, 5))
        plt.bar(['Present', 'Absent'], [present_counts.values[0], absent_counts.values[0]], color=['green', 'red'])
        plt.title('Attendance Report')
        plt.xlabel('Status')
        plt.ylabel('Count')
        plt.show()

def main():
    root = tk.Tk()
    app = AttendanceTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
