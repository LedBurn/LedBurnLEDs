from LakeAnimation import LakeAnimation

from Effects.FireEffect import FireEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

class FireLakeAnimation(LakeAnimation):
    def __init__(self, lake, props):
        LakeAnimation.__init__(self, lake, props)

        self.effects = []
        for wave in self.lake.waves_arr:
            
            if (len(wave) < 70):
                # split to 2 chunks
                size = len(wave)/2
                arr = [wave[i:i + size] for i in xrange(0, len(wave), size)]
                up = arr[0]
                down = arr[1]

                self.effects.append(FireEffect(up))
                self.effects.append(FireEffect(down[::-1]))

            else:
                # split to 4 chunks
                size = len(wave)/4
                arr = [wave[i:i + size] for i in xrange(0, len(wave), size)]
                up1 = arr[0]
                up2 = arr[2]
                down1 = arr[1]
                down2 = arr[3]

                self.effects.append(FireEffect(up1))
                self.effects.append(FireEffect(up2))
                self.effects.append(FireEffect(down1[::-1]))
                self.effects.append(FireEffect(down2[::-1]))

        # split to chunks of four
        print(len(self.lake.contour))
        arr = [self.lake.contour[i:i + 5] for i in xrange(0, len(self.lake.contour), 5)]
        for fire in arr:
            self.effects.append(FireEffect(fire))
    
    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.lake.get_array())
