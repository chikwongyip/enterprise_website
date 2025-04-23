from nicegui import ui
from pages import home, news, products, product_detail, downloads, about


def setup_routes():
    @ui.page('/')
    def home_page():
        home.render()

    @ui.page('/news')
    def news_page():
        news.render()

    @ui.page('/products')
    def products_page():
        products.render()

    @ui.page('/product/{product_id}')
    def product_detail_page(product_id: str):
        product_detail.render(product_id)

    @ui.page('/downloads')
    def downloads_page():
        downloads.render()

    @ui.page('/about')
    def about_page():
        about.render()


if __name__ == '__main__':
    setup_routes()
    ui.run()
