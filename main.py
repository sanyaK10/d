from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import random

console = Console()

history = []

while True:
    # Головне меню
    menu = Panel.fit(
        "[bold magenta]Головне меню[/bold magenta]\n\n"
        "[cyan]1.[/cyan] Почати гру\n"
        "[cyan]2.[/cyan] Історія ігор\n"
        "[cyan]3.[/cyan] Вихід",
        title="[bold green]Вітаємо в Аркаді! 🎮[/bold green]",
        border_style="white"
    )

    console.print(menu)

    choice = Prompt.ask(
        "[bold white]Оберіть дію [1/2/3][/bold white]",
        choices=["1", "2", "3"]
    )

    # Почати гру
    if choice == "1":
        variants = ["Камінь", "Ножиці", "Папір"]

        player = Prompt.ask(
            "[bold yellow]Ваш вибір [Камінь/Ножиці/Папір][/bold yellow]",
            choices=["Камінь", "Ножиці", "Папір"]
        )

        computer = random.choice(variants)

        console.print(f"[white]Комп'ютер обрав:[/white] [cyan]{computer}[/cyan]")

        # Визначення результату
        if player == computer:
            result = "Нічия"
            color = "yellow"

        elif (
            (player == "Камінь" and computer == "Ножиці") or
            (player == "Ножиці" and computer == "Папір") or
            (player == "Папір" and computer == "Камінь")
        ):
            result = "Перемога"
            color = "green"

        else:
            result = "Поразка"
            color = "red"

        console.print(f"[bold {color}]Результат: {result}![/bold {color}]")

        # Збереження історії
        history.append({
            "player": player,
            "computer": computer,
            "result": result
        })

    elif choice == "2":
        table = Table(title="[bold magenta]Історія матчів[/bold magenta]")

        table.add_column("Раунд", justify="center", style="cyan")
        table.add_column("Гравець", justify="center")
        table.add_column("Комп'ютер", justify="center")
        table.add_column("Результат", justify="center")

        wins = 0
        loses = 0
        draws = 0

        for i, game in enumerate(history, start=1):

            if game["result"] == "Перемога":
                result_text = "[green]Перемога[/green]"
                wins += 1

            elif game["result"] == "Поразка":
                result_text = "[red]Поразка[/red]"
                loses += 1

            else:
                result_text = "[yellow]Нічия[/yellow]"
                draws += 1

            table.add_row(
                str(i),
                game["player"],
                game["computer"],
                result_text
            )

        console.print(table)

        console.print(
            f"\n[bold green]Перемог:[/bold green] {wins}   "
            f"[bold red]Поразок:[/bold red] {loses}   "
            f"[bold yellow]Нічиїх:[/bold yellow] {draws}"
        )

    elif choice == "3":
        console.print("[bold red]Гру завершено![/bold red]")
        break