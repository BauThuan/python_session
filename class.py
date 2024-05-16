import random
import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, age, math_score, literatures_score, english_score, geography_score, chemistry_score):
        self.name = name
        self.age = age
        self.math_score = float(math_score)
        self.literatures_score = float(literatures_score)
        self.english_score = float(english_score)
        self.geography_score = float(geography_score)
        self.chemistry_score = float(chemistry_score)

    def medium_score(self):
        total_score = (self.math_score + self.literatures_score + self.english_score + self.geography_score + self.chemistry_score) / 5
        return round(total_score, 2)

    def rank_academic(self):
        total_score = self.medium_score()
        if total_score > 8.0:
            return "Học lực: Giỏi"
        elif 6.5 < total_score <= 8.0:
            return "Học lực: Khá"
        elif 5.0 <= total_score <= 6.5:
            return "Học lực: Trung Bình"
        else:
            return "Học lực: Yếu"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information")
        
        self.create_widgets()
        
        self.submit_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.submit_button.grid(row=8, column=0, columnspan=2, pady=10)
        
        self.students = []

    def create_widgets(self):
        labels = ["Tên học sinh:", "Tuổi:", "Điểm Toán:", "Điểm Văn:", "Điểm Anh:", "Điểm Địa:", "Điểm Hóa:"]
        self.entries = []
        
        for i, label in enumerate(labels):
            tk.Label(self.root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

    def add_student(self):
        try:
            name = self.entries[0].get()
            age = self.entries[1].get()
            math_score = float(self.entries[2].get())
            literatures_score = float(self.entries[3].get())
            english_score = float(self.entries[4].get())
            geography_score = float(self.entries[5].get())
            chemistry_score = float(self.entries[6].get())
            
            student = Student(name, age, math_score, literatures_score, english_score, geography_score, chemistry_score)
            self.students.append(student)
            
            messagebox.showinfo("Success", f"Student {name} added successfully!")
            
            for entry in self.entries:
                entry.delete(0, tk.END)
                
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for scores.")

    def save_to_file(self):
        if not self.students:
            messagebox.showerror("No Students", "No students to save.")
            return

        random_number = random.randint(1000, 9999)
        file_name = f"students_{random_number}.txt"

        with open(file_name, "w", encoding="utf-8") as file:
            for student in self.students:
                file.write(f"Tên: {student.name}, Tuổi: {student.age}, Điểm trung bình: {student.medium_score()}, {student.rank_academic()}\n")
        
        messagebox.showinfo("Success", f"Student information saved to {file_name}")

root = tk.Tk()
app = App(root)

save_button = tk.Button(root, text="Save to File", command=app.save_to_file)
save_button.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
