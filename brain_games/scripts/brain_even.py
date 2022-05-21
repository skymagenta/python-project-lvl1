#!/usr/bin/env python

from brain_games.game_engine import launch_game
from brain_games.games.even import even


def main():
    launch_game(even)


if __name__ == '__main__':
    main()
