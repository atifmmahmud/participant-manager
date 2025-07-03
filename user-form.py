import dearpygui.dearpygui as dpg
import csv
import os
from participant import Participant

def save_user():
    print("User saved")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()



## SUBMIT: Add to CSV
def submit(sender, data):
    input_name = dpg.get_value("#name_input")

    with dpg.table_row(parent="PARTICIPANTS"):
        dpg.add_text(dpg.get_value("#name_input"))
        dpg.add_text(dpg.get_value("#age_input"))
        dpg.add_text(dpg.get_value("#sex_input"))
        dpg.add_text(round(dpg.get_value("#n2_input"), 2))
        dpg.add_text(round(dpg.get_value("#p3_input"), 2))
        dpg.add_text(round(dpg.get_value("#rspm_input"), 2))
        dpg.add_text(round(dpg.get_value("#sf36_input"), 2))      
    
    with open ("newfile.csv","a", newline="") as csvfile:
        fields = ["Name", "Age", "Sex", "N2", "P3", "RSPM", "SF-36"]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        
        if not os.path.isfile("newfile.csv") or  os.path.getsize("newfile.csv") == 0:
            writer.writeheader()

with dpg.font_registry():
    default_font = dpg.add_font("Roboto-VariableFont_wdth,wght.ttf", 40)

## MAIN WINDOW
with dpg.window(label="Create User", height=1080, width=1920):
    
    ## INPUT AREA
    with dpg.group(horizontal=True):
        ## INPUT TITLE
        with dpg.group(horizontal=False):
            dpg.add_text("Name", tag="NAME_TEXT")
            dpg.add_text("Age")
            dpg.add_text("Sex")
            dpg.add_text("N2 Amplitude (absolute)")
            dpg.add_text("P3 Amplitude (absolute)")
            dpg.add_text("RSPM Score")
            dpg.add_text("SF-36 Score")
            dpg.add_spacer(height=20)
            dpg.add_spacer(height=20)
            dpg.add_button(label="Submit", callback=submit)
        ## INPUT FIELD
        with dpg.group(horizontal=False):
            name = dpg.add_input_text(tag="#name_input")
            age = dpg.add_input_int(tag="#age_input")
            sex = dpg.add_input_text(tag="#sex_input")
            n2 = dpg.add_input_float(tag="#n2_input")
            p3 = dpg.add_input_float(tag="#p3_input")
            rspm = dpg.add_input_float(tag="#rspm_input")
            sf36 = dpg.add_input_float(tag="#sf36_input")

    dpg.add_spacer(height=20)
    dpg.add_spacer(height=20)
    dpg.add_spacer(height=20)
    dpg.add_spacer(height=20)

    ## TABLE DISPLAY OF USERS
    with dpg.child_window(height=800, width=1920):
        with dpg.group(horizontal=True):
            with dpg.table(header_row=True, tag="PARTICIPANTS"):
                # use add_table_column to add columns to the table,
                # table columns use child slot 0
                # dpg.add_table_column(tag="column 1")
                dpg.add_table_column(label="Name")
                dpg.add_table_column(label="Age")
                dpg.add_table_column(label="Sex")
                dpg.add_table_column(label="N2 Amplitude")
                dpg.add_table_column(label="P3 Amplitude")
                dpg.add_table_column(label="RSPM Score")
                dpg.add_table_column(label="SF-36 Score")

                #dpg.add_table_column()
                #dpg.add_table_column()
                #dpg.add_table_column()

                # add_table_next_column will jump to the next row
                # once it reaches the end of the columns
                # table next column use slot 1
                #for i in range(0, 4):
                #   with dpg.table_row():
                #      for j in range(0, 4):
                #          dpg.add_text(f"Row{i} Column{j}")

# This sets the font for the specific widget
dpg.bind_font(default_font)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()