
import minqlx

class justspec(minqlx.Plugin):
    def __init__(self):
        super().__init__()
        self.add_hook("team_switch_attempt", self.handle_team_switch)
    def handle_team_switch(self, player, old_team, new_team):
        if player in self.players() and player.team == "spectator":
            player.center_print("^1You are not permitted to join the game.")
            return minqlx.RET_STOP_ALL