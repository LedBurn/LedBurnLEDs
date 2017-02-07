import math
from AbstractSheepAnimation import SheepAnimation
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.BlinkEffect import BlinkEffect
from Effects.FadeInEffect import FadeInEffect

class BlinkCircleAnimation(SheepAnimation):
    def __init__(self, sheep, color):
        SheepAnimation.__init__(self, sheep)
        self.color = color
        self.effects = []
        self.currentBlinkBodyNum = -1;
    
    def apply(self, time_precent, parent_array):
        
        blinkBodyNum = math.floor(time_precent * self.sheep.get_num_of_body_parts())
        if (self.currentBlinkBodyNum != blinkBodyNum):
            self.currentBlinkBodyNum = int(blinkBodyNum)

            headColor = [self.color[1], self.color[2],self.color[0]]
            legColor = [self.color[2], self.color[0],self.color[1]]
            bodyColor = [int(self.color[0]*0.1), int(self.color[1]*0.1), int(self.color[2]*0.1)]

            headEffect = AlwaysOnEffect(self.sheep.get_head_indexes(), headColor)
            legEffect = AlwaysOnEffect(self.sheep.get_legs_indexes(), legColor)
            bodyEffect = AlwaysOnEffect(self.sheep.get_body_indexes(), bodyColor)

            blinkEffect = BlinkEffect(self.sheep.get_body_part_indexes(self.currentBlinkBodyNum), 2, self.color)

            self.effects = [headEffect,legEffect, bodyEffect, blinkEffect]
        
        oneBodyPercent = 1.0 / self.sheep.get_num_of_body_parts()
        relativePercent = (time_precent - self.currentBlinkBodyNum * oneBodyPercent) * self.sheep.get_num_of_body_parts()
  
        for effect in self.effects:
            effect.apply(relativePercent, parent_array)
