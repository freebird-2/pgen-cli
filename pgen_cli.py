import click
import string
import random


def generate(
    length: int,
    uppercase: bool,
    lowercase: bool,
    digits: bool,
    symbols: bool,
    repeat: bool,
) -> str:
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    return generate_from(length, chars, repeat)


def generate_from(length: int, chars: str, repeat: bool) -> str:
    if not repeat and length > len(chars):
        raise click.UsageError(f"Not enough characters for a password of length {length}")
    if repeat:
        return "".join(random.choices(chars, k=length))
    else:
        return "".join(random.sample(chars, k=length))


@click.group
@click.version_option()
def pgen():
    pass


@pgen.command()
@click.option(
    "-l", "--length", default=20, show_default=True, help="length of password"
)
@click.option(
    "--uppercase/--no-uppercase",
    default=True,
    show_default=True,
    help="include uppercase letters",
)
@click.option(
    "--lowercase/--no-lowercase",
    default=True,
    show_default=True,
    help="include lowercase letters",
)
@click.option(
    "--digits/--no-digits",
    default=True,
    show_default=True,
    help="include digits",
)
@click.option(
    "--symbols/--no-symbols",
    default=True,
    show_default=True,
    help="include symbols",
)
@click.option(
    "--repeat/--no-repeat",
    default=True,
    show_default=True,
    help="allow repeat characters",
)
def gen(
    length: int,
    uppercase: bool,
    lowercase: bool,
    digits: bool,
    symbols: bool,
    repeat: bool,
):
    click.echo(generate(length, uppercase, lowercase, digits, symbols, repeat))


@pgen.command("from")
@click.option(
    "-l", "--length", default=20, show_default=True, help="length of password"
)
@click.argument("chars")
@click.option(
    "--repeat/--no-repeat",
    default=True,
    show_default=True,
    help="allow repeat characters",
)
def from_(length: int, chars: str, repeat: bool):
    click.echo(generate_from(length, chars, repeat))
