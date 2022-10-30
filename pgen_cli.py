import click
import string
import random


def gen(
    length: int,
    uppercase: bool,
    lowercase: bool,
    digits: bool,
    symbols: bool,
    repeat: bool,
):
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    if repeat:
        return "".join(random.choices(chars, k=length))
    else:
        return "".join(random.sample(chars, k=length))


@click.command()
@click.option(
    "-l", "--length", default=20, show_default=True, help="length of password"
)
@click.option(
    "--uppercase/--no-uppercase",
    "-U/ ",
    default=True,
    show_default=True,
    help="include uppercase letters",
)
@click.option(
    "--lowercase/--no-lowercase",
    "-L/ ",
    default=True,
    show_default=True,
    help="include lowercase letters",
)
@click.option(
    "--digits/--no-digits",
    "-D/ ",
    default=True,
    show_default=True,
    help="include digits",
)
@click.option(
    "--symbols/--no-symbols",
    "-S/ ",
    default=True,
    show_default=True,
    help="include symbols",
)
@click.option(
    "--repeat/--no-repeat",
    "-R/ ",
    default=True,
    show_default=True,
    help="allow repeat characters",
)
@click.version_option()
def run(
    length: int,
    uppercase: bool,
    lowercase: bool,
    digits: bool,
    symbols: bool,
    repeat: bool,
):
    click.echo(gen(length, uppercase, lowercase, digits, symbols, repeat))
