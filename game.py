"""CLI number guessing game."""

import random


MIN_NUMBER = 1
MAX_NUMBER = 100


def main() -> None:
    """Run the number guessing game."""
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    print(f"{MIN_NUMBER}〜{MAX_NUMBER}の数字を当ててください。")

    while True:
        try:
            guess = int(input("予想した数字: "))
        except ValueError:
            print("1〜100の整数を入力してください。")
            continue
        except EOFError:
            print("\nゲームを終了します。")
            return

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print("1〜100の範囲で入力してください。")
            continue

        attempts += 1

        if guess < answer:
            print("もっと大きい数字です。")
        elif guess > answer:
            print("もっと小さい数字です。")
        else:
            print(f"正解です！ {attempts}回で当たりました。")
            return


if __name__ == "__main__":
    main()
