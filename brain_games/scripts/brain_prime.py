#!/usr/bin/env python

from brain_games.game_engine import launch_game
from brain_games.games.prime import prime


def main():
    launch_game(prime)


if __name__ == '__main__':
    main()
