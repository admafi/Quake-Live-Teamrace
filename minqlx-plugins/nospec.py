
import minqlx

class nospec(minqlx.Plugin):
    def __init__(self):
        super().__init__()
        self.add_hook("frame", self.handle_frame, priority=minqlx.PRI_LOWEST)
    def handle_frame(self):
        for p in self.players():
            if p.team == "spectator":
                p.put("free")

