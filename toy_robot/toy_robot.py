import re


class ToyRobot:
    def __init__(self):
        self.faces = {
            "north": 90,
            "west": 0,
            "south": 270,
            "east": 180,
        }
        self.grid = [5, 5]
        self.face = self.faces["north"]
        self.loc = [0, 0, self.face]

    def run(self):
        cmd = ""
        while "report" not in cmd:
            cmd = str(input()).lower()
            if "place" in cmd:
                if re.match(r"^place\s\d,\d,[a-z]{4,5}", cmd):
                    cmd_list = cmd[6:].split(",")
                    x = int(cmd_list[0])
                    y = int(cmd_list[1])
                    face = cmd_list[2]

                    if face not in self.faces.keys():
                        raise ValueError(
                            f"`{face.upper()}` is not a valid input, try {list(self.faces.keys())}."
                        )
                    if x > self.grid[0] or x < 0:
                        raise ValueError(
                            f"X: {x} is not a valid coordinate value, range is from 0 to {self.grid[0]}."
                        )

                    if y > self.grid[1] or y < 0:
                        raise ValueError(
                            f"Y: {y} is not a valid coordinate value, range is from 0 to {self.grid[1]}."
                        )
                    self._place(x, y, face)
                else:
                    raise ValueError(
                        "Invalid Place Command! Should be like `PLACE 0,1,NORTH`, take note of the white space"
                    )
            elif "move" in cmd:
                self._move()
            elif cmd in ["right", "left"]:
                self._turn(cmd)
            elif "report" in cmd:
                return self._report()
            else:
                raise ValueError("Invalid Command Given!")

    def _place(self, x: int, y: int, face: str):
        self.face = self.faces[face]
        self.loc = [x, y, self.face]

    def _move(self):
        if self.loc[2] == 0:
            loc = self.loc[0] - 1
            self.loc[0] = 0 if loc < 0 else loc
        elif self.loc[2] == 90:
            loc = self.loc[1] + 1
            self.loc[1] = self.grid[0] if loc > self.grid[0] else loc
        elif self.loc[2] == 180:
            loc = self.loc[0] + 1
            self.loc[0] = self.grid[1] if loc > self.grid[1] else loc
        else:
            loc = self.loc[1] - 1
            self.loc[1] = 0 if loc < 0 else loc

    def _turn(self, d: str):
        if d == "left":
            if self.loc[2] != 270:
                self.loc[2] = self.loc[2] - 90
            else:
                self.loc[2] = self.loc[2] + 90

            if self.loc[2] == -90:
                self.loc[2] = 270

            if self.loc[2] == 360:
                self.loc[2] = 0

            self.loc[2] = abs(self.loc[2])
        elif d == "right":
            if self.loc[2] != 270:
                self.loc[2] = self.loc[2] + 90
            else:
                self.loc[2] = self.loc[2] - 90

            if self.loc[2] == 360:
                self.loc[2] = 0
        else:
            raise ValueError(f"You can only turn LEFT or RIGHT.")

    def _report(self):
        return [self.loc[0], self.loc[1], str(self._get_face_key(self.loc[2])).upper()]

    def _get_face_key(self, val):
        for key, value in self.faces.items():
            if val == value:
                return key
