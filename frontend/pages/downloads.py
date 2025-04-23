from nicegui import ui
import httpx


def render():
    with ui.column().classes('flex-1 p-4'):
        ui.label('Downloads').classes('text-2xl font-bold')
        response = httpx.get('http://localhost:8000/api/downloads')
        for download in response.json():
            ui.button(
                download['name'], on_click=lambda url=download['url']: ui.download(url))
