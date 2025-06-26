import dearpygui.dearpygui as dpg
import csv
import os


def save_user():
    print("User saved")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

def submit(sender, data):
    print("SUBMIT BUTTON")
    input_name = dpg.get_value("#name_input")
    print(input_name)
    print(os.getcwd())

    with open ("newfile.csv","a", newline="") as csvfile:
        fields = ["Name", "Age", "Sex", "N2", "P3", "RSPM", "SF-36"]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        
        if not os.path.isfile("newfile.csv") or  os.path.getsize("newfile.csv") == 0:
            writer.writeheader()

        writer.writerow({
                "Name": "Atif",
                "Age": "30",
                "Sex": "M",
                "N2": "2",
                "P3": "3",
                "RSPM": "4",
                "SF-36": "5"
            })

with dpg.font_registry():
    default_font = dpg.add_font("Roboto-VariableFont_wdth,wght.ttf", 40)

with dpg.window(label="Create User", height=1080, width=1920):
    with dpg.group(horizontal=True):
        with dpg.group(horizontal=False):
            dpg.add_text("Name")
            dpg.add_text("Age")
            dpg.add_text("Sex")
            dpg.add_text("N2 Amplitude (absolute)")
            dpg.add_text("P3 Amplitude (absolute)")
            dpg.add_text("RSPM Score")
            dpg.add_text("SF-36 Score")
            dpg.add_button(label="Submit", callback=submit)

        with dpg.group(horizontal=False):
            name = dpg.add_input_text(tag="#name_input")
            age = dpg.add_input_float()
            sex = dpg.add_input_text()
            n2 = dpg.add_input_float()
            p3 = dpg.add_input_float()
            rspm = dpg.add_input_float()

            with dpg.table(header_row=False):
                # use add_table_column to add columns to the table,
                # table columns use child slot 0
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                # add_table_next_column will jump to the next row
                # once it reaches the end of the columns
                # table next column use slot 1
                for i in range(0, 4):
                    with dpg.table_row():
                        for j in range(0, 4):
                            dpg.add_text(f"Row{i} Column{j}")

# This sets the font for the specific widget
dpg.bind_font(default_font)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()