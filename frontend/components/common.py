from nicegui import ui


def custom_button(text, on_click):
    return ui.button(text, on_click=on_click).classes('bg-blue-500 text-white')
