import dearpygui.dearpygui as dpg

def save_user():
    print("User saved")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

def submit(sender, data):
    print("SUBMIT BUTTON")
    input_name = dpg.get_value("#name_input")
    print(input_name)

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

            
# This sets the font for the specific widget
dpg.bind_font(default_font)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()