from nicegui import ui


def render():
    with ui.column().classes('flex-1 p-4'):
        ui.label('About Us').classes('text-2xl font-bold')
        ui.label('Welcome to our company! Here is some information about us...').classes(
            'text-sm')
