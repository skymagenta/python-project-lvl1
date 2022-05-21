#!/usr/bin/env python

from brain_games.game_engine import launch_game
from brain_games.games.calc import calc


def main():
    launch_game(calc)


if __name__ == '__main__':
    main()
