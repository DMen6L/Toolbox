from textual.app import App
from textual.widgets import Label


class ToolboxApp(App[None]):
    TITLE = "Toolbox"

    def compose(self):
        yield Label("Hello to my app")


if __name__ == "__main__":
    app = ToolboxApp()
    app.run()
