from abc import ABCMeta, abstractmethod


class Sheep:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_array(self): pass
    
    @abstractmethod
    def get_all_indexes(self): pass
    
    # -- Head -- ##

    @abstractmethod
    def get_head_indexes(self): pass

    @abstractmethod
    def get_ears_indexes(self): pass

    @abstractmethod
    def get_inner_ear_indexes(self): pass

    @abstractmethod
    def get_inner_ear_connection_index(self): pass

    @abstractmethod
    def get_outer_ear_indexes(self): pass

    @abstractmethod
    def get_outer_ear_connection_index(self): pass

    # -- Body -- ##

    @abstractmethod
    def get_body_indexes(self): pass

    @abstractmethod
    def get_num_of_body_parts(self): pass

    @abstractmethod
    def get_body_part_indexes(self, body_part_number): pass


    # -- Legs -- ##

    @abstractmethod
    def get_leg12_indexes(self): pass

    @abstractmethod
    def get_leg12_side1_indexes(self): pass

    @abstractmethod
    def get_leg12_side2_indexes(self): pass

    @abstractmethod
    def get_leg34_indexes(self): pass

    @abstractmethod
    def get_leg34_side1_indexes(self): pass

    @abstractmethod
    def get_leg34_side2_indexes(self): pass
    
    @abstractmethod
    def get_leg12_connection_index(self): pass

    @abstractmethod
    def get_leg34_connection_index(self): pass

    @abstractmethod
    def get_legs_indexes(self): pass

