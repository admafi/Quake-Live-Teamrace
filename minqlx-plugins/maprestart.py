import minqlx


class maprestart(minqlx.Plugin):
    def __init__(self):
        super().__init__()
        self.add_command(("restart"), self.cmd_restart, priority=minqlx.PRI_HIGH)
    def cmd_restart(self, player, msg, channel):
        """Commands for map_restart"""

        if self.db.has_permission(player, 5):
            minqlx.console_command("map_restart")
            return minqlx.RET_STOP_ALL

			