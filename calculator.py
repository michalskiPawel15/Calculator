from tkinter import *


class Calculator:
    def clear_entry(self):
        self.entryVar.set('0')

    def oper_on_end(self, entry_val):
        e_len = len(entry_val)
        for i in range(0, len(self.oper)):
            if entry_val[e_len-1] == self.oper[i] or entry_val[e_len-1] == ',':
                return True

    def oper_handle(self, entry_val, btn_val):
        oper_on_end = self.oper_on_end(entry_val)
        if entry_val != '0' and not oper_on_end:
            self.entryVar.set(entry_val+btn_val)

    def check_oper(self, value):
        for j in range(0, len(self.oper)):
            if value == self.oper[j]:
                return True

    def rep_str(self, item, old, new):
        if item.find(old, 0, len(item)) >= 0:
            new_item = item.replace(old, new)
            return new_item
        else:
            return item

    def calc_entry(self, calc_arr):
        if len(calc_arr) > 1:
            try:
                calc_str = ''
                for i in range(0, len(calc_arr)):
                    try:
                        arr_item = self.rep_str(calc_arr[i], ',', '.')
                        calc_str += str(float(arr_item))
                    except ValueError:
                        is_oper = self.check_oper(calc_arr[i])
                        if is_oper:
                            calc_str += calc_arr[i]
                        else:
                            break
                calc = eval(calc_str)
                final_calc = self.rep_str(str(calc), '.', ',')
                self.entryVar.set(final_calc)
            except:
                self.entryVar.set('ERROR')
        else:
            self.entryVar.set('0')

    def entry_handle(self, value):
        oper_on_end = self.oper_on_end(value)
        if not oper_on_end:
            val_list = list(value)
            list_len = len(val_list)
            i = 0
            while i < list_len:
                list_item = val_list[i].strip()
                is_oper = self.check_oper(list_item)
                if not is_oper:
                    next_val = i+1
                    if next_val < list_len:
                        next_item = val_list[next_val].strip()
                        next_is_oper = self.check_oper(next_item)
                        if not next_is_oper:
                            val_list[i] = list_item + next_item
                            val_list.remove(val_list[next_val])
                            list_len = len(val_list)
                            i = i
                        else:
                            i += 1
                    else:
                        break
                else:
                    i += 1
            self.calc_entry(val_list)

    def btn_handle(self, event):
        btn_val = event.widget.cget('text')
        get_entry = self.user_input.get()
        if btn_val == 'C':
            self.clear_entry()
        elif btn_val == '=':
            self.entry_handle(get_entry)
        else:
            try:
                btn_int = int(btn_val)
                if get_entry == '0':
                    self.entryVar.set(str(btn_int))
                else:
                    self.entryVar.set(get_entry+str(btn_int))
            except ValueError:
                self.oper_handle(get_entry, btn_val)

    def make_btn(self, row_num, col_num, col_span, txt):
        eval_btn = Button(
            self.frame,
            text=txt,
            font=('Arial', 14),
            padx=3,
            pady=3,
            bd=1)
        eval_btn.grid(
            row=row_num,
            column=col_num,
            columnspan=col_span,
            sticky='E' + 'W',
            padx=3,
            pady=3)
        eval_btn.bind('<Button-1>', self.btn_handle)

    def __init__(self, root):
        self.width = 300
        self.height = 300
        self.entryVar = StringVar()
        self.entryVar.set('0')
        self.oper = ['+', '-', '*', '/']
        root.title('Calculator')
        root.geometry(
            str(self.width) +
            'x' +
            str(self.height) +
            '+100+0')
        self.frame = Frame(root)
        self.user_input = Entry(
            self.frame,
            textvariable=self.entryVar,
            font=('Arial', 18),
            justify=RIGHT,
            bd=1)
        self.frame.columnconfigure(0, weight=1)
        self.user_input.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky=E+W,
            )
        for row_num in range(1, 5):
            if row_num == 1:
                btn_num = 6
                oper_sign = self.oper[row_num-1]
            elif row_num == 2:
                btn_num = 3
                oper_sign = self.oper[row_num-1]
            elif row_num == 3:
                btn_num = 0
                oper_sign = self.oper[row_num-1]
            elif row_num == 4:
                btn_oper = ['C', 0, ',', self.oper[row_num-1]]
            for col_num in range(0, 4):
                self.frame.columnconfigure(col_num, weight=1)
                if row_num != 4 and col_num == 3:
                    btn_txt = oper_sign
                elif row_num == 4:
                    btn_txt = btn_oper[col_num]
                else:
                    btn_num += 1
                    btn_txt = btn_num
                num_btn = self.make_btn(row_num, col_num, 1, str(btn_txt))
            eval_btn = self.make_btn(5, 0, 4, '=')
        root.columnconfigure(0, weight=1, minsize=self.width)
        self.frame.grid(row=0, column=0, sticky=E+W)
root = Tk()
calc = Calculator(root)
root.mainloop()
