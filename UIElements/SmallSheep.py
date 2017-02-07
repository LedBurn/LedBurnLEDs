from AbstractSheep import Sheep

class SmallSheep(Sheep):
    def __init__(self):
        self.head = range(27,78)
        self.body = [range(81,95), range(133,146), range(147,161),
                     range(200,211), range(213,225), range(227,240),
                     range(242,256), range(257,271), range(273,285),
                     range(288,300)]
        self.leg1_side1 = range(97,111)
        self.leg1_side2 = range(117,131)
        self.leg2_side1 = range(163,178)
        self.leg2_side2 = range(184,198)
        self.earl = range(0,0)
        self.earr = range(0,0)

        self.eye1 = 300
        self.eye2 = 301
        self.arr = [0,0,0] * 302

    def get_array(self):
        return self.arr
    
    def get_all_indexes(self):
        return self.get_head_indexes() + self.get_body_indexes() + self.get_legs_indexes() + [self.eye1, self.eye2]
    
    
    # -- Head -- #
    
    def get_head_indexes(self):
        return self.head

    def get_ears_indexes(self):
        return [self.eye1, self.eye2]

    def get_inner_ear_indexes(self):
        return [self.eye1]

    def get_outer_ear_indexes(self):
        return [self.eye2]

    def get_inner_ear_connection_index(self):
        return 45

    def get_outer_ear_connection_index(self):
        return 45


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


    # -- Legs -- #
    
    def get_legs_indexes(self):
        return self.get_leg12_indexes() + self.get_leg34_indexes()

    def get_leg12_indexes(self):
        return self.leg1_side1 + self.leg1_side2

    def get_leg12_side1_indexes(self):
       return self.leg1_side1

    def get_leg12_side2_indexes(self):
        return self.leg1_side2

    def get_leg12_connection_index(self):
        return 133;

    def get_leg34_indexes(self):
        return self.leg2_side1 + self.leg2_side2

    def get_leg34_side1_indexes(self):
       return self.leg2_side1

    def get_leg34_side2_indexes(self):
        return self.leg2_side2

    def get_leg34_connection_index(self):
        return 200
