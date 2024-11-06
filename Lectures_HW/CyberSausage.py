from fractions import Fraction


class Sausage:
    def __init__(self, *args):
        if len(args) == 0:
            self.filling = "pork!"
            self.volume = Fraction(1)
        elif len(args) == 1:
            self.filling = args[0]
            self.volume = Fraction(1)
        elif len(args) == 2:
            self.filling = args[0]
            vol = args[1]
            if isinstance(vol, str):
                self.volume = Fraction(vol)
            else:
                self.volume = Fraction(vol)
        if self.volume < 0:
            self.volume = Fraction(0)

    def __add__(self, other):
        result = Sausage(self.filling)
        result.volume = self.volume + other.volume
        return result

    def __sub__(self, other):
        result = Sausage(self.filling)
        result.volume = self.volume - other.volume
        if result.volume < 0:
            result.volume = Fraction(0)
        return result

    def __mul__(self, other):
        result = Sausage(self.filling)
        result.volume = self.volume * other
        return result

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        result = Sausage(self.filling)
        if other > 0:
            result.volume = self.volume / other
        else:
            result.volume = Fraction(0)
        return result

    def __abs__(self):
        return self.volume

    def __bool__(self):
        return self.volume != 0

    def __str__(self):
        if self.volume == 0 or (self.volume != 0 and self.volume < Fraction(1, 12)):
            top_casing = '/|'
            filling_line = '||'
            bottom_casing = '\\|'
            sausage_str = '\n'.join([top_casing, filling_line, filling_line, filling_line, bottom_casing])
            return sausage_str

        total_filling_units = int(self.volume * 12)
        num_full_loaves = total_filling_units // 12
        remaining_filling_units = total_filling_units % 12

        top_casing = ''
        bottom_casing = ''
        filling_lines = ['', '', '']

        for i in range(num_full_loaves):
            top_casing += '/------------\\'
            bottom_casing += '\\------------/'
            filling = (self.filling * ((12 + len(self.filling) - 1) // len(self.filling)))[:12]
            for j in range(3):
                filling_lines[j] += '|' + filling + '|'

        if remaining_filling_units > 0:
            top_casing += '/' + '-' * remaining_filling_units + '|'
            bottom_casing += '\\' + '-' * remaining_filling_units + '|'
            filling = (self.filling * ((remaining_filling_units + len(self.filling) - 1) // len(self.filling)))[
                      :remaining_filling_units]
            for j in range(3):
                filling_lines[j] += '|' + filling + '|'

        sausage_str = '\n'.join([top_casing] + filling_lines + [bottom_casing])
        return sausage_str
