import typer
from urllib.parse import urlparse
import yaml

app = typer.Typer()
url_app = typer.Typer()
username_app = typer.Typer()
app.add_typer(url_app, name='url')
app.add_typer(username_app, name='username')


class Config:
    def __init__(self, url: str, username: str, password: str):
        self.url = urlparse(url)
        self.username = username
        self.password = password

    def save_config(self, file_name=".config.yaml") -> bool:
        pass

    def load_config(self, file_name=".config.yaml") -> bool:
        
        with open(r) as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

        print(config)

    @url_app.command("set")
    def set_url(self, url):
        self.url = urlparse(url)

    @url_app.command("list")
    def get_url(self) -> str:
        return self.url.geturl()

    @username_app.command("set")
    def set_username(self, username):
        self.username = username

    @username_app.command("list")
    def get_username(self) -> str:
        return self.username


if __name__ == '__main__':
    app()
