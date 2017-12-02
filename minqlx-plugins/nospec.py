
import minqlx

class nospec(minqlx.Plugin):
    def __init__(self):
        super().__init__()
        self.add_hook("team_switch_attempt", self.handle_team_switch)
    def handle_team_switch(self, player, old_team, new_team):
        if player in self.players() and player.team != "spectator":
            if (player.privileges == None):
                if self.game.state != "warmup":
                    player.center_print("^1Sorry, you can't spectate now.")

                    return minqlx.RET_STOP_ALL
