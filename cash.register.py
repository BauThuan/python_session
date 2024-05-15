import tkinter as tk
from tkinter import messagebox

def check_data(valueItem):
    if not valueItem.strip():       
        return False
    elif any(char.isalpha() for char in valueItem):
        return False
    else:
        return True

def calc_total_price(apple_weight, app_price_kg):
    if not check_data(apple_weight):
        raise ValueError("Kiểm tra lại thông tin vừa nhập không đúng!")
    return float(apple_weight) * app_price_kg

def calc_return(total_price, money_give):
    if not check_data(money_give):
        raise ValueError("Kiểm tra lại thông tin vừa nhập không đúng!")
    return float(money_give) - total_price

def check_return_money(total_money):
    denominations = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000]
    result = {}
    for denom in denominations:
        count = total_money // denom
        if count > 0:
            # lưu số tờ tiền vào vị trí trong object
            result[denom] = count
            # cập nhật số tiền còn lại
        total_money = total_money % denom
    return result

def print_return_money(total_money):
    if(total_money > 0):
        result = check_return_money(total_money)
        result_str = "Số tiền trả lại:\n"
        for denom, count in result.items():
            result_str += f"{denom // 1000}k : {count} tờ\n"
        messagebox.showinfo("Kết quả", result_str)
    else:
        result = check_return_money(abs(total_money))
        result_str = "Số người dùng cần đưa thêm:\n"
        for denom, count in result.items():
            result_str += f"{denom // 1000}k : {count} tờ\n"
        messagebox.showinfo("Kết quả", result_str)

def calculate():
    try:
        app_price_kg = 20000
        apple_weight = weight_entry.get()
        money_give = money_entry.get()

        total_price = calc_total_price(apple_weight, app_price_kg)
        money_return = calc_return(total_price, money_give)
        
        if money_return != 0:
           print_return_money(money_return)
        else:
            messagebox.showinfo("Kết quả", "Người dùng trả đủ tiền rồi!")
    except ValueError as e:
        messagebox.showerror("Lỗi", e)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Tính tiền trả lại")

# Tạo các widget
weight_label = tk.Label(root, text="Nhập khối lượng táo (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

money_label = tk.Label(root, text="Nhập số tiền khách hàng đưa (VND):")
money_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
money_entry = tk.Entry(root)
money_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Tính toán", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Chạy ứng dụng
root.mainloop()
