class morse:
    def __init__(self, string='di dit dah .'):
        self.space_flag = True
        if len(tmp := string.split(" ")) > 1:
            self.space = ','
            self.split = ' '
            if len(tmp) == 2:
                self.dot = tmp[0][::-1]
                self.end_dot = tmp[0][::-1]
                self.tire = tmp[1][::-1]
                self.end = "."
            elif len(tmp) == 3:
                self.dot = tmp[0][::-1]
                self.end_dot = tmp[1][::-1]
                self.tire = tmp[2][::-1]
                self.end = "."
            else:
                self.dot = tmp[0][::-1]
                self.end_dot = tmp[1][::-1]
                self.tire = tmp[2][::-1]
                self.end = tmp[3][::-1]
        else:
            self.space = " "
            self.split = ''
            if len(string) == 2:
                self.dot = string[0]
                self.end_dot = string[0]
                self.tire = string[1]
                self.end = ""
            elif len(string) == 3:
                self.dot = string[0]
                self.end_dot = string[1]
                self.tire = string[2]
                self.end = ""
            else:
                self.dot = string[0]
                self.end_dot = string[1]
                self.tire = string[2]
                self.end = string[3]
        self.sequence = self.end

    def __pos__(self):
        if self.space_flag:
            self.sequence += self.end_dot
        else:
            self.sequence += self.dot
        self.sequence += self.split
        self.space_flag = False
        return self

    def __neg__(self):
        self.sequence += self.tire
        self.sequence += self.split
        self.space_flag = False
        return self

    def __invert__(self):
        self.space_flag = True
        self.sequence += self.space
        return self

    def __str__(self):
        if self.split == ' ':
            return self.sequence[len(self.sequence) - 2::-1]
        else:
            return self.sequence[::-1]
