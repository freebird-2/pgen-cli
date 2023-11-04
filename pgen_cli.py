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
    include_all: bool,
) -> str:
    if include_all:
        groups = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
        mask = [uppercase, lowercase, digits, symbols]
        groups = [group for ]
        return generate_from_all(length, [], repeat)
    chars = (
        string.ascii_uppercase * uppercase
        + string.ascii_lowercase * lowercase
        + string.digits * digits
        + string.punctuation * symbols
    )
    return generate_from(length, chars, repeat)


def generate_from(length: int, chars: str, repeat: bool) -> str:
    if len(chars) == 0:
        raise click.UsageError(f"No characters available to construct password")
    if not repeat and length > len(chars):
        raise click.UsageError(
            f"Not enough characters for a password of length {length} without repetition"
        )
    randomizer = random.choices if repeat else random.sample
    return "".join(randomizer(chars, k=length))


def generate_from_all(length: int, groups: list[str], repeat: bool) -> str:
    part1 = [random.choice(group) for group in groups]
    if not repeat:
        for i, group in enumerate(groups):
            groups[i] = group.replace(part1[i], "", count=1)
    part2 = list(generate_from(length - len(part1), "".join(groups), repeat))
    char_list = part1 + part2
    random.shuffle(char_list)
    return "".join(char_list)


@click.group
@click.version_option()
def pgen():
    pass


@pgen.command()
@click.option(
    "-l",
    "--length",
    type=click.IntRange(min=1),
    default=20,
    show_default=True,
    help="length of password",
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
@click.option(
    "--include-all/--no-include-all",
    default=True,
    show_default=True,
    help="include at least one character from each group",
)
def gen(
    length: int,
    uppercase: bool,
    lowercase: bool,
    digits: bool,
    symbols: bool,
    repeat: bool,
    include_all: bool,
):
    click.echo(
        generate(length, uppercase, lowercase, digits, symbols, repeat, include_all)
    )


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
