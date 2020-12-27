### BEGIN AUTOGENERATED SECTION - MODIFICATIONS TO THIS CODE WILL BE OVERWRITTEN

### telemParse.py
### Autogenerated by telem_file_generator.py on Thu Dec 24 19:51:28 2020

import time
import struct

class TelemParse:

	def __init__(self):
		self.csv_header = "Time (s),valve_states (),pressure[0] (counts),pressure[1] (counts),pressure[2] (counts),pressure[3] (counts),pressure[4] (counts),pressure[5] (counts),e_batt (Volts),main_cycle_time (Amps),motor_cycle_time (),ivlv[0] (Amps),ivlv[1] (Amps),ivlv[2] (Amps),ivlv[3] (Amps),ivlv[4] (Amps),ivlv[5] (Amps),ivlv[6] (Amps),ivlv[7] (Amps),evlv[0] (Volts),evlv[1] (Volts),evlv[2] (Volts),evlv[3] (Volts),evlv[4] (Volts),evlv[5] (Volts),evlv[6] (Volts),evlv[7] (Volts),e3v (Volts),e5v (Volts),i5v (amps),i3v (amps),last_command_id (),i_mtr_ab[0] (amps),i_mtr_ab[1] (amps),i_mtr_ab[2] (amps),i_mtr_ab[3] (amps),i_mtr[0] (amps),i_mtr[1] (amps),zero (Volts),zero (Volts),zero (Volts),zero (Volts),zero (us),zero (ms),zero (ms),zero (ul),\n"
		self.log_string = ""
		self.num_items = 45
		
		self.dict = {}
		
		self.items = [''] * self.num_items
		self.items[0] = 'valve_states' 
		self.items[1] = 'pressure[0]' 
		self.items[2] = 'pressure[1]' 
		self.items[3] = 'pressure[2]' 
		self.items[4] = 'pressure[3]' 
		self.items[5] = 'pressure[4]' 
		self.items[6] = 'pressure[5]' 
		self.items[7] = 'e_batt' 
		self.items[8] = 'main_cycle_time' 
		self.items[9] = 'motor_cycle_time' 
		self.items[10] = 'ivlv[0]' 
		self.items[11] = 'ivlv[1]' 
		self.items[12] = 'ivlv[2]' 
		self.items[13] = 'ivlv[3]' 
		self.items[14] = 'ivlv[4]' 
		self.items[15] = 'ivlv[5]' 
		self.items[16] = 'ivlv[6]' 
		self.items[17] = 'ivlv[7]' 
		self.items[18] = 'evlv[0]' 
		self.items[19] = 'evlv[1]' 
		self.items[20] = 'evlv[2]' 
		self.items[21] = 'evlv[3]' 
		self.items[22] = 'evlv[4]' 
		self.items[23] = 'evlv[5]' 
		self.items[24] = 'evlv[6]' 
		self.items[25] = 'evlv[7]' 
		self.items[26] = 'e3v' 
		self.items[27] = 'e5v' 
		self.items[28] = 'i5v' 
		self.items[29] = 'i3v' 
		self.items[30] = 'last_command_id' 
		self.items[31] = 'i_mtr_ab[0]' 
		self.items[32] = 'i_mtr_ab[1]' 
		self.items[33] = 'i_mtr_ab[2]' 
		self.items[34] = 'i_mtr_ab[3]' 
		self.items[35] = 'i_mtr[0]' 
		self.items[36] = 'i_mtr[1]' 
		self.items[37] = 'zero' 
		self.items[38] = 'zero' 
		self.items[39] = 'zero' 
		self.items[40] = 'zero' 
		self.items[41] = 'zero' 
		self.items[42] = 'zero' 
		self.items[43] = 'zero' 
		self.items[44] = 'zero' 

	def parse_packet(self, packet):
		self.dict[self.items[0]] = int((float(struct.unpack("<I", packet[0:4])[0]))/1)
		self.dict[self.items[1]] = float((float(struct.unpack("<h", packet[4:6])[0]))/1)
		self.dict[self.items[2]] = float((float(struct.unpack("<h", packet[6:8])[0]))/1)
		self.dict[self.items[3]] = float((float(struct.unpack("<h", packet[8:10])[0]))/1)
		self.dict[self.items[4]] = float((float(struct.unpack("<h", packet[10:12])[0]))/1)
		self.dict[self.items[5]] = float((float(struct.unpack("<h", packet[12:14])[0]))/1)
		self.dict[self.items[6]] = float((float(struct.unpack("<h", packet[14:16])[0]))/1)
		self.dict[self.items[7]] = float((float(struct.unpack("<h", packet[16:18])[0]))/1000)
		self.dict[self.items[8]] = int((float(struct.unpack("<h", packet[18:20])[0]))/100)
		self.dict[self.items[9]] = int((float(struct.unpack("<B", packet[20:21])[0]))/1)
		self.dict[self.items[10]] = float((float(struct.unpack("<B", packet[21:22])[0]))/10)
		self.dict[self.items[11]] = float((float(struct.unpack("<B", packet[22:23])[0]))/10)
		self.dict[self.items[12]] = float((float(struct.unpack("<B", packet[23:24])[0]))/10)
		self.dict[self.items[13]] = float((float(struct.unpack("<B", packet[24:25])[0]))/10)
		self.dict[self.items[14]] = float((float(struct.unpack("<B", packet[25:26])[0]))/10)
		self.dict[self.items[15]] = float((float(struct.unpack("<B", packet[26:27])[0]))/10)
		self.dict[self.items[16]] = float((float(struct.unpack("<B", packet[27:28])[0]))/10)
		self.dict[self.items[17]] = float((float(struct.unpack("<B", packet[28:29])[0]))/10)
		self.dict[self.items[18]] = float((float(struct.unpack("<B", packet[29:30])[0]))/10)
		self.dict[self.items[19]] = float((float(struct.unpack("<B", packet[30:31])[0]))/10)
		self.dict[self.items[20]] = float((float(struct.unpack("<B", packet[31:32])[0]))/10)
		self.dict[self.items[21]] = float((float(struct.unpack("<B", packet[32:33])[0]))/10)
		self.dict[self.items[22]] = float((float(struct.unpack("<B", packet[33:34])[0]))/10)
		self.dict[self.items[23]] = float((float(struct.unpack("<B", packet[34:35])[0]))/10)
		self.dict[self.items[24]] = float((float(struct.unpack("<B", packet[35:36])[0]))/10)
		self.dict[self.items[25]] = float((float(struct.unpack("<B", packet[36:37])[0]))/10)
		self.dict[self.items[26]] = float((float(struct.unpack("<i", packet[37:41])[0]))/100)
		self.dict[self.items[27]] = float((float(struct.unpack("<i", packet[41:45])[0]))/100)
		self.dict[self.items[28]] = float((float(struct.unpack("<B", packet[45:46])[0]))/100)
		self.dict[self.items[29]] = float((float(struct.unpack("<B", packet[46:47])[0]))/100)
		self.dict[self.items[30]] = float((float(struct.unpack("<H", packet[47:49])[0]))/100)
		self.dict[self.items[31]] = float((float(struct.unpack("<H", packet[49:51])[0]))/100)
		self.dict[self.items[32]] = float((float(struct.unpack("<H", packet[51:53])[0]))/100)
		self.dict[self.items[33]] = float((float(struct.unpack("<H", packet[53:55])[0]))/100)
		self.dict[self.items[34]] = float((float(struct.unpack("<H", packet[55:57])[0]))/100)
		self.dict[self.items[35]] = float((float(struct.unpack("<H", packet[57:59])[0]))/100)
		self.dict[self.items[36]] = float((float(struct.unpack("<H", packet[59:61])[0]))/100)
		self.dict[self.items[37]] = float((float(struct.unpack("<H", packet[61:63])[0]))/1000)
		self.dict[self.items[38]] = float((float(struct.unpack("<H", packet[63:65])[0]))/1000)
		self.dict[self.items[39]] = float((float(struct.unpack("<H", packet[65:67])[0]))/1000)
		self.dict[self.items[40]] = float((float(struct.unpack("<H", packet[67:69])[0]))/1000)
		self.dict[self.items[41]] = int((float(struct.unpack("<L", packet[69:77])[0]))/1)
		self.dict[self.items[42]] = int((float(struct.unpack("<I", packet[77:81])[0]))/1)
		self.dict[self.items[43]] = int((float(struct.unpack("<I", packet[81:85])[0]))/1)
		self.dict[self.items[44]] = int((float(struct.unpack("<B", packet[85:86])[0]))/1)
		self.log_string = str(time.clock()) + ',' + str(self.dict[self.items[0]]) + ',' + str(self.dict[self.items[1]]) + ',' + str(self.dict[self.items[2]]) + ',' + str(self.dict[self.items[3]]) + ',' + str(self.dict[self.items[4]]) + ',' + str(self.dict[self.items[5]]) + ',' + str(self.dict[self.items[6]]) + ',' + str(self.dict[self.items[7]]) + ',' + str(self.dict[self.items[8]]) + ',' + str(self.dict[self.items[9]]) + ',' + str(self.dict[self.items[10]]) + ',' + str(self.dict[self.items[11]]) + ',' + str(self.dict[self.items[12]]) + ',' + str(self.dict[self.items[13]]) + ',' + str(self.dict[self.items[14]]) + ',' + str(self.dict[self.items[15]]) + ',' + str(self.dict[self.items[16]]) + ',' + str(self.dict[self.items[17]]) + ',' + str(self.dict[self.items[18]]) + ',' + str(self.dict[self.items[19]]) + ',' + str(self.dict[self.items[20]]) + ',' + str(self.dict[self.items[21]]) + ',' + str(self.dict[self.items[22]]) + ',' + str(self.dict[self.items[23]]) + ',' + str(self.dict[self.items[24]]) + ',' + str(self.dict[self.items[25]]) + ',' + str(self.dict[self.items[26]]) + ',' + str(self.dict[self.items[27]]) + ',' + str(self.dict[self.items[28]]) + ',' + str(self.dict[self.items[29]]) + ',' + str(self.dict[self.items[30]]) + ',' + str(self.dict[self.items[31]]) + ',' + str(self.dict[self.items[32]]) + ',' + str(self.dict[self.items[33]]) + ',' + str(self.dict[self.items[34]]) + ',' + str(self.dict[self.items[35]]) + ',' + str(self.dict[self.items[36]]) + ',' + str(self.dict[self.items[37]]) + ',' + str(self.dict[self.items[38]]) + ',' + str(self.dict[self.items[39]]) + ',' + str(self.dict[self.items[40]]) + ',' + str(self.dict[self.items[41]]) + ',' + str(self.dict[self.items[42]]) + ',' + str(self.dict[self.items[43]]) + ',' + str(self.dict[self.items[44]]) + ','