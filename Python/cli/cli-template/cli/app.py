import typer

app = typer.Typer()

@app.command()
def print_name(name: str):
    typer.echo(name)

@app.command()
def main():
    pass

if __name__ == '__main__':
    main()
    typer.run(print_name)

