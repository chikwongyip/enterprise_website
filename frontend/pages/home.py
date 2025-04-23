from nicegui import ui
from components.common import custom_button


def render():
    with ui.column().classes('flex-1 p-4'):
        ui.label('Welcome to Our Enterprise Website!').classes(
            'text-2xl font-bold')
        custom_button('Learn More', lambda: ui.open('/about'))
