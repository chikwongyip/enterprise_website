from nicegui import ui
import httpx


def render(product_id):
    with ui.column().classes('flex-1 p-4'):
        response = httpx.get(
            f'http://localhost:8000/api/products/{product_id}')
        product = response.json()
        ui.label(product['name']).classes('text-2xl font-bold')
        ui.label(product['description']).classes('text-sm')
        ui.image(product['image_url']).classes('w-full')
        ui.button('Download Attachment', on_click=lambda: ui.download(
            product['attachment_url']))
