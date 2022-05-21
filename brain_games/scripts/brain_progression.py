#!/usr/bin/env python

from brain_games.game_engine import launch_game
from brain_games.games.progression import progression


def main():
    launch_game(progression)


if __name__ == '__main__':
    main()
