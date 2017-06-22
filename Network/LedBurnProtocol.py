import socket
import array
import random
import time

controlers_map = {210: "10.0.0.210", 211: "10.0.0.211", 212: "10.0.0.212", 213: "10.0.0.213", 214: "10.0.0.214"}
UDP_PORT = 2000

#frame data - we store the data we are about to send here.
#these variables are static for the module
last_frame_id = random.randint(0, 100000000)
stored_msgs = {controler_ip:[] for controler_ip in controlers_map.iterkeys()} #map each ip to the messages we want to send to this ip



sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

PROTOCOL_VERSION = 0

# flower - 580 leds
FLOWER_IP = 210
FLOWER_STRIP_ID = 0

# sheep - 302 leds
SHEEP_IP = 210
SHEEP_STRIP_ID = 2

# grass1 - 600 leds
GRASS1_IP = 210
GRASS1_STRIP_ID = 2

#grass2 - how many leds?
GRASS2_IP = 213
GRASS2_STRIP_ID0 = 2
GRASS2_STRIP_ID1 = 5


# sign - 150 leds
SIGN_IP = 210
SIGN_STRIP_ID = 3

# lake
LAKE_IP = 210
LAKE_STRIP_ID = 4
LAKE_WAVE_STRIP_ID0 = 5
LAKE_WAVE_STRIP_ID1 = 6

# temp stick - 144 leds
TEMP_STICK_IP = 210
TEMP_STICK_STRIP_ID = 7


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

def send(flower_data=[0, 0, 0] * 580,
         sheep_data=[0, 0, 0] * 302):

    replaceGBRtoRGB(flower_data, range(463, 513))
    sendPacketWithIp(FLOWER_IP, FLOWER_STRIP_ID, 0, flower_data[0:900])
    sendPacketWithIp(FLOWER_IP, FLOWER_STRIP_ID, 300, flower_data[900:1800])

    replaceGBRtoRGB(sheep_data, range(300, 302))
    sendPacketWithIp(SHEEP_IP, SHEEP_STRIP_ID, 0, sheep_data)

    """"
    sendPacketWithIp(GRASS1_IP, GRASS1_STRIP_ID, 0, grass_data[0:900])
    sendPacketWithIp(GRASS1_IP, GRASS1_STRIP_ID, 300, grass_data[900:1800])
    sendPacketWithIp(GRASS2_IP, GRASS2_STRIP_ID0, 0, grass_data[1800:2700])
    sendPacketWithIp(GRASS2_IP, GRASS2_STRIP_ID0, 300, grass_data[2700:3087])
    sendPacketWithIp(GRASS2_IP, GRASS2_STRIP_ID1, 0, grass_data[3087:3987])

    sendPacketWithIp(SIGN_IP, SIGN_STRIP_ID, 0, sign_data)

    sendPacketWithIp(LAKE_IP, LAKE_STRIP_ID, 0, lake_data[0:900])
    sendPacketWithIp(LAKE_IP, LAKE_STRIP_ID, 300, lake_data[900:1800])

    sendPacketWithIp(LAKE_IP, LAKE_WAVE_STRIP_ID0, 0, lake_data[1800:2700])
    sendPacketWithIp(LAKE_IP, LAKE_WAVE_STRIP_ID0, 300, lake_data[2700:3600])
    sendPacketWithIp(LAKE_IP, LAKE_WAVE_STRIP_ID1, 0, lake_data[3600:4500])
    sendPacketWithIp(LAKE_IP, LAKE_WAVE_STRIP_ID1, 300, lake_data[4500:5400])

    sendPacketWithIp(TEMP_STICK_IP, TEMP_STICK_STRIP_ID, 0, temp_stick[0:144*3])
    """

    sendStoredFrame()

def sendPacketWithIp(controler_ip, strip_id, pixel_id, pixel_data):
    stored_msgs[controler_ip].append({"strip_id" : strip_id, "pixel_id": pixel_id, "pixel_data":pixel_data})

def sendStoredFrame():
    global stored_msgs, last_frame_id
    for ip in stored_msgs.iterkeys():
        ip_str = controlers_map[ip]
        num_of_segments = len(stored_msgs[ip])
        for i in range(0, num_of_segments):
            curr_segment = stored_msgs[ip][i]
            sendPacket(ip_str, curr_segment["strip_id"], num_of_segments, i, curr_segment["pixel_id"], curr_segment["pixel_data"])
    last_frame_id = last_frame_id + 1
    stored_msgs = {controler_ip:[] for controler_ip in controlers_map.iterkeys()} #map each ip to the messages we want to send to this ip

def sendPacket(ip, strip_id, seg_in_frame, seg_id, pixel_id, pixels_data):
    global last_frame_id
    data =  uint8_to_array(PROTOCOL_VERSION) + \
            uint32_to_array(last_frame_id) + \
            uint32_to_array(seg_in_frame) + \
            uint32_to_array(seg_id) + \
            uint16_to_array(strip_id) + \
            uint16_to_array(pixel_id)

    data = data + pixels_data
    msg = "LedBurn" + array.array('B', data).tostring()

    sock.sendto(msg, (ip, UDP_PORT))


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


