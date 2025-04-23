from nicegui import ui
import httpx


def render():
    with ui.column().classes('flex-1 p-4'):
        ui.label('News').classes('text-2xl font-bold')
        response = httpx.get('http://localhost:8000/api/news')
        for news_item in response.json():
            with ui.card().classes('mb-2'):
                ui.label(news_item['title']).classes('text-lg font-bold')
                ui.label(news_item['content']).classes('text-sm')
