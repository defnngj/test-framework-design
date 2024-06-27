# click_demo.py
import click


@click.command()
@click.option("-c", "--count", default=1, help="执行次数，默认1。")
@click.option("-n", "--name", prompt="Your name", help="请输入name名字。")
def hello(count, name):
    """简单的CLI，问候 count 次 name."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")


if __name__ == '__main__':
    hello()
