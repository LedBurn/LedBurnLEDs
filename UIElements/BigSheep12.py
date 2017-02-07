from AbstractSheep import Sheep

class BigSheep12(Sheep):
    def __init__(self):
        self.head = range(470,560)
        self.body = [range(69,88), range(88,107), range(179,197),
                     range(197,222), range(222,235) + range(300, 309), range(309,329),
                     range(329,358), range(358,385), range(385,410),
                     range(410,435), range(435, 462)]
					 
        self.legll = range(272,300)
        self.leglr = range(235,265)
        self.legrl = range(147,179)
        self.legrr = range(107,140)
		
        self.earl = range(0,44)
        self.earr = range(560,600)[::-1]
		
        self.arr = [0,0,0] * 600

    def get_array(self):
        return self.arr
    
    def get_all_indexes(self):
        return self.get_head_indexes() + self.get_body_indexes() + self.get_legs_indexes() + self.get_ears_indexes()
    
    
    # -- Head -- #
    
    def get_head_indexes(self):
        return self.head


    # -- Body -- #
    
    def get_body_indexes(self):
        body_indexes = []
        for i in range(0, self.get_num_of_body_parts()):
            body_indexes += self.get_body_part_indexes(i)
        return body_indexes[::-1]
    
    def get_num_of_body_parts(self):
        return len(self.body)
    
    def get_body_part_indexes(self, body_part_number):
        return self.body[body_part_number]

    # -- Ears -- #
    def get_ears_indexes(self):
        return self.earl + self.earr

    def get_inner_ear_indexes(self):
        return self.earl

    def get_outer_ear_indexes(self):
        return self.earr

    def get_inner_ear_connection_index(self):
        return 540

    def get_outer_ear_connection_index(self):
        return 474

    # -- Legs -- #

    def get_legs_indexes(self):
        return self.legll + self.leglr + self.legrl + self.legrr

    def get_leg12_indexes(self):
        return self.legrl + self.legrr
    
    def get_leg12_connection_index(self):
        return 179;

    def get_leg12_side1_indexes(self):
       return self.legrr

    def get_leg12_side2_indexes(self):
        return self.legrl
    
    def get_leg34_indexes(self):
        return self.legll + self.leglr
    
    def get_leg34_connection_index(self):
        return 300

    def get_leg34_side1_indexes(self):
       return self.leglr

    def get_leg34_side2_indexes(self):
        return self.legll
