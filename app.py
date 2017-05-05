from Game import Game


def setup():
    g = Game()
    g.instructions()

    if g.want_to_play():
        play(g)
    else:
        print("Okay, come back soon!")


def play(game):
    game.check_server_ready()
    print("Sorry, the cowbull game isn't available right now; "
          "please come back later. The issue has been logged.")


if __name__ == "__main__":
    setup()
