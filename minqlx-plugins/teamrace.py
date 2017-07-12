import minqlx


class teamrace(minqlx.Plugin):
    def __init__(self):
        super().__init__()
        self.add_command(("teammaps"), self.cmd_teammaps, priority=minqlx.PRI_HIGH)
        self.add_command(("restart"), self.cmd_restart, priority=minqlx.PRI_HIGH)
    def cmd_teammaps(self, player, msg, channel):
        """Outputs list of teamrace maps."""
        channel.reply("Teamrace maps: aa_teamrace, aa_teamrace2, aa_teamraceshorty, aa_teamraceshorty2, aa_teamraceshorty3, aa_teamraceshorty4, aa_teamraceshorty5, 2plyr, delayed, warnedtwins")
        return minqlx.RET_STOP_ALL
    def cmd_restart(self, player, msg, channel):
        """Commands for map_restart"""

        if self.db.has_permission(player, 5):
            minqlx.console_command("map_restart")
            return minqlx.RET_STOP_ALL

			
