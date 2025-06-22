import dearpygui.dearpygui as dpg

def save_user():
    print("User saved")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.font_registry():
    default_font = dpg.add_font("Roboto-VariableFont_wdth,wght.ttf", 40)

with dpg.window(label="Create User", height=1080, width=1920):
    with dpg.group(horizontal=True):
        with dpg.group(horizontal=False):
            dpg.add_text("Name")
            dpg.add_text("Age")
            dpg.add_text("Sex")

        with dpg.group(horizontal=False):
            dpg.add_input_text()
            dpg.add_input_text()
            dpg.add_input_text()

# This sets the font for the specific widget
dpg.bind_font(default_font)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()