from nicegui import ui
import httpx


def render():
    with ui.column().classes('flex-1 p-4'):
        ui.label('Products').classes('text-2xl font-bold')
        response = httpx.get('http://localhost:8000/api/products')
        for product in response.json():
            with ui.card().classes('mb-2'):
                ui.label(product['name']).classes('text-lg font-bold')
                ui.button('Details', on_click=lambda p=product['id']: ui.open(
                    f'/product/{p}'))
