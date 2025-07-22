import dearpygui.dearpygui as dpg
import csv
import os
from participant import Participant
from screeninfo import get_monitors

def load_existing_participants():
    if not os.path.isfile("newfile.csv"):
        return  # No file, nothing to load

    with open("newfile.csv", "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            with dpg.table_row(parent="PARTICIPANTS"):
                dpg.add_text(row["Name"])
                dpg.add_text(row["Age"])
                dpg.add_text(row["Sex"])
                dpg.add_text(round(float(row["N2"]), 2))
                dpg.add_text(round(float(row["P3"]), 2))
                dpg.add_text(round(float(row["RSPM"]), 2))
                dpg.add_text(round(float(row["SF-36"]), 2))

def save_user():
    print("User saved")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

## SUBMIT
def submit(sender, data):
    input_name = dpg.get_value("#name_input")

    ## Add to table
    with dpg.table_row(parent="PARTICIPANTS"):
        dpg.add_text(dpg.get_value("#name_input"))
        dpg.add_text(dpg.get_value("#age_input"))
        dpg.add_text(dpg.get_value("#sex_input"))
        dpg.add_text(round(dpg.get_value("#n2_input"), 2))
        dpg.add_text(round(dpg.get_value("#p3_input"), 2))
        dpg.add_text(round(dpg.get_value("#rspm_input"), 2))
        dpg.add_text(round(dpg.get_value("#sf36_input"), 2))      
    
    ## Create CSV/add header
    with open ("newfile.csv","a", newline="") as csvfile:
        fields = ["Name", "Age", "Sex", "N2", "P3", "RSPM", "SF-36"]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        
        if not os.path.isfile("newfile.csv") or  os.path.getsize("newfile.csv") == 0:
            writer.writeheader()
        
        writer.writerow({
            "Name": dpg.get_value("#name_input"),
            "Age": dpg.get_value("#age_input"),
            "Sex": dpg.get_value("#sex_input"),
            "N2": dpg.get_value("#n2_input"),
            "P3": dpg.get_value("#p3_input"),
            "RSPM": dpg.get_value("#rspm_input"),
            "SF-36": dpg.get_value("#sf36_input"),
            }
        )

with dpg.font_registry():
    default_font = dpg.add_font("Roboto-VariableFont_wdth,wght.ttf", 40)

# 🧬 Medical-Grade Dark Theme: Professional & Clean
with dpg.theme() as medtech_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (28, 30, 34), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (38, 40, 45), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (40, 42, 48), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (230, 230, 230), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (150, 150, 150), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (50, 53, 60), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (65, 70, 80), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (90, 100, 110), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (60, 65, 75), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (80, 90, 100), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (100, 110, 130), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (150, 180, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (180, 210, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 20, 20, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 8, category=dpg.mvThemeCat_Core)

dpg.bind_theme(medtech_theme)

## MAIN WINDOW
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height
with dpg.window(label="Create User", height=screen_height, width=screen_width, tag="MAIN_WINDOW"):
    # BIND THE THEME TO THAT WINDOW
    dpg.bind_item_theme("MAIN_WINDOW", medtech_theme)
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
            age = dpg.add_input_int(tag="#age_input", step=0)
            sex = dpg.add_input_text(tag="#sex_input")
            n2 = dpg.add_input_float(tag="#n2_input", step=0)
            p3 = dpg.add_input_float(tag="#p3_input", step=0)
            rspm = dpg.add_input_float(tag="#rspm_input", step=0)
            sf36 = dpg.add_input_float(tag="#sf36_input", step=0)

    dpg.add_spacer(height=20)
    dpg.add_spacer(height=20)
    dpg.add_spacer(height=20)

    ## TABLE DISPLAY OF USERS
    with dpg.child_window(height=screen_height/4, width=screen_width * 0.95):
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
load_existing_participants()
dpg.show_viewport()


dpg.start_dearpygui()
dpg.destroy_context()

