#!/usr/bin/env python

from brain_games.game_engine import launch_game
from brain_games.games.gcd import gcd


def main():
    launch_game(gcd)


if __name__ == '__main__':
    main()
