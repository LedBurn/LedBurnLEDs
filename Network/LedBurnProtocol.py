import socket
import array
import time

CONTROLER_IP1 = "10.0.0.210"
CONTROLER_IP2 = "10.0.0.211"
CONTROLER_IP3 = "10.0.0.212"
CONTROLER_IP4 = "10.0.0.213"
UDP_PORT = 2000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

PROTOCOL_VERSION = 0

# flower - ~550 leds
FLOWER_STRIP_ID = 0
FLOWER_SEG0 = 0
FLOWER_SEG0_PIXEL = 0
FLOWER_SEG1 = 1
FLOWER_SEG1_PIXEL = 300

# sheep - 302 leds
SHEEP_STRIP_ID = 1
SHEEP_SEG0 = 2
SHEEP_SEG0_PIXEL = 0

# grass - 600 leds
GRASS_STRIP_ID = 2
GRASS_SEG0 = 3
GRASS_SEG0_PIXEL = 0
GRASS_SEG1 = 4
GRASS_SEG1_PIXEL = 300

# sign - 150 leds
SIGN_STRIP_ID = 3
SIGN_SEG0 = 5
SIGN_SEG0_PIXEL = 0

# lake
LAKE_STRIP_ID = 4
LAKE_SEG0 = 6
LAKE_SEG0_PIXEL = 0
LAKE_SEG1= 7
LAKE_SEG1_PIXEL = 300

LAKE_WAVE_STRIP_ID0 = 5
LAKE_WAVE_SEG0 = 6
LAKE_WAVE_SEG0_PIXEL = 0
LAKE_WAVE_SEG1= 7
LAKE_WAVE_SEG1_PIXEL = 300
LAKE_WAVE_STRIP_ID1 = 6
LAKE_WAVE_SEG2 = 8
LAKE_WAVE_SEG2_PIXEL = 0
LAKE_WAVE_SEG3= 9
LAKE_WAVE_SEG3_PIXEL = 300

# temp stick - 144 leds
TEMP_STICK_STRIP_ID = 7
TEMP_STICK_SEG0 = 10
TEMP_STICK_PIXEL = 0

# total
SEGS_IN_FRAME = 11


def uint8_to_array(num):
    c1 = (num / (1)) % 256
    return [c1]

def uint16_to_array(num):
    c1 = (num / (256)) % 256
    c2 = (num / (1)) % 256
    return [c2, c1]

def uint32_to_array(num):
    c1 = (num / (256 * 256 * 256)) % 256
    c2 = (num / (256 * 256)) % 256
    c3 = (num / (256)) % 256
    c4 = (num / (1)) % 256
    return [c4, c3, c2, c1]

def send(frame_id,
         flower_data,
         sheep_data,
         grass_data,
         sign_data,
         lake_data,
         temp_stick):

    replaceGBRtoRGB(flower_data, range(463, 513));
    sendPacket(frame_id, FLOWER_STRIP_ID, FLOWER_SEG0, FLOWER_SEG0_PIXEL, flower_data[0:900])
    sendPacket(frame_id, FLOWER_STRIP_ID, FLOWER_SEG1, FLOWER_SEG1_PIXEL, flower_data[900:])

    replaceGBRtoRGB(sheep_data, range(300, 302));
    sendPacket(frame_id, SHEEP_STRIP_ID, SHEEP_SEG0, SHEEP_SEG0_PIXEL, sheep_data)

    sendPacket(frame_id, GRASS_STRIP_ID, GRASS_SEG0, GRASS_SEG0_PIXEL, grass_data[0:900])
    sendPacket(frame_id, GRASS_STRIP_ID, GRASS_SEG1, GRASS_SEG1_PIXEL, grass_data[900:])

    sendPacket(frame_id, SIGN_STRIP_ID, SIGN_SEG0, SIGN_SEG0_PIXEL, sign_data)
    
    sendPacket(frame_id, LAKE_STRIP_ID, LAKE_SEG0, LAKE_SEG0_PIXEL, lake_data[0:900])
    sendPacket(frame_id, LAKE_STRIP_ID, LAKE_SEG1, LAKE_SEG1_PIXEL, lake_data[900:1800])
    
    sendPacket(frame_id, LAKE_WAVE_STRIP_ID0, LAKE_WAVE_SEG0, LAKE_WAVE_SEG0_PIXEL, lake_data[1800:2700])
    sendPacket(frame_id, LAKE_WAVE_STRIP_ID0, LAKE_WAVE_SEG1, LAKE_WAVE_SEG1_PIXEL, lake_data[2700:3600])
    sendPacket(frame_id, LAKE_WAVE_STRIP_ID1, LAKE_WAVE_SEG2, LAKE_WAVE_SEG2_PIXEL, lake_data[3600:4500])
    sendPacket(frame_id, LAKE_WAVE_STRIP_ID1, LAKE_WAVE_SEG3, LAKE_WAVE_SEG3_PIXEL, lake_data[4500:5400])

    sendPacket(frame_id, TEMP_STICK_STRIP_ID, TEMP_STICK_SEG0, TEMP_STICK_PIXEL, temp_stick[0:144*3])


def sendPacket(frame_id, strip_id, seg_id, pixel_id, pixels_data):

    data =  uint8_to_array(PROTOCOL_VERSION) + \
            uint32_to_array(frame_id) + \
            uint32_to_array(SEGS_IN_FRAME) + \
            uint32_to_array(seg_id) + \
            uint16_to_array(strip_id) + \
            uint16_to_array(pixel_id)

    data = data + pixels_data
    msg = "LedBurn" + array.array('B', data).tostring()

    sock.sendto(msg, (CONTROLER_IP1, UDP_PORT))
    #sock.sendto(msg, (CONTROLER_IP2, UDP_PORT))
    #sock.sendto(msg, (CONTROLER_IP3, UDP_PORT))
    #sock.sendto(msg, (CONTROLER_IP4, UDP_PORT))


def replaceGBRtoRGB(data_array,in_range):
    for i in in_range:
        gbr = data_array[i*3:i*3+3]
        rgb = [gbr[1], gbr[0], gbr[2]]
        data_array[i*3:i*3+3] = rgb


#test:
# i = 0
# while (True):
#     i += 1
#     flower = [200, 0, 0] * 580
#     sheep = [200, 0 ,0] * 302
#     grass = [0, 200, 0] * 600
#     sign = [0, 0, 200] * 150
#     lake = [0, 200, 200] * 600 + [0, 0, 200] * 600 + [0, 0, 200] * 600
#     send(i,  flower, sheep, grass, sign, lake)
#     time.sleep(0.1)


