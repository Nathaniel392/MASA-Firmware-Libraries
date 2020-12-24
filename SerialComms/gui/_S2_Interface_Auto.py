### BEGIN AUTOGENERATED SECTION - MODIFICATIONS TO THIS CODE WILL BE OVERWRITTEN

### _S2_Interface_Auto.py
### Autogenerated by cmd_file_generator.py on Thu Dec 24 18:47:43 2020

import serial

class _S2_Interface_Auto:
	def __init__(self):
		# A dictionary mapping command name to packet_type (command ID)
		self.cmd_names_dict = {
			set_vlv	:	8,
			send_telem_short	:	9,
			send_telem_all	:	10,
			set_stepper_period	:	11,
			set_stepper_direction	:	12,
			set_kp	:	13,
			set_ki	:	14,
			set_kd	:	15,
			set_control_calc_period	:	16,
			set_state	:	17,
			move_stepper_degrees	:	18
		}

		# A dictionary mapping packet_type (command ID) to a list of function argument information.
		# The nth tuple in each list corresponds to the nth argument for that command's function,
		# in the order (arg_name, arg_type, xmit_scale)
		self.cmd_args_dict = {
			8	:	[('vlv_num', 'uint32_t', 1), ('state', 'uint8_t', 1)],
			9	:	[('board_num', 'uint8_t', 1)],
			10	:	[('board_num', 'uint8_t', 1)],
			11	:	[('stepper_num', 'uint8_t', 1), ('period', 'uint16_t', 1)],
			12	:	[('stepper_num', 'uint8_t', 1), ('direction', 'int8_t', 1)],
			13	:	[('motor_num', 'uint8_t', 1), ('gain', 'double', 100)],
			14	:	[('motor_num', 'uint8_t', 1), ('gain', 'double', 100)],
			15	:	[('motor_num', 'uint8_t', 1), ('gain', 'double', 100)],
			16	:	[('period', 'uint16_t', 1)],
			17	:	[('state', 'uint8_t', 1)],
			18	:	[('motor_num', 'uint8_t', 1), ('deg', 'uint16_t', 1)]
		}

	"""
	Encodes command info and arguments with COBS and transmits them over serial
	@params
		ser (pyserial object)  - serial obejct to write to
		target_id (integer)    - ID of board the command is going to
		command_id (integer)   - packet_type of the command being sent
		argc (integer)         - number of function arguments for the command
		argv (array)           - list of function arguments as they appear in the parameter list
	"""
	def s2_command(ser, target_id, command_id, argc, argv):
		#Initialize empty packet
		packet = list()

		#Fill first 10 bytes of packet with CLB packet header information
		packet.append(command_id)	# packet_type
		packet.append(target_id)	# target_addr
		packet.append(1)	# priority
		packet.append(1)	# do_cobbs
		packet.append(0)	# checksum
		packet.append(0)	# checksum
		packet.append()	# timestamp
		packet.append()	# timestamp
		packet.append()	# timestamp
		packet.append()	# timestamp

		# Stuff packet with the function arguments according to the packet_type ID
		# set_vlv()
		if (command_id == 8):
			# vlv_num
			packet.append(((argv[0]*1) >> 24) & 0xFF)
			packet.append(((argv[0]*1) >> 16) & 0xFF)
			packet.append(((argv[0]*1) >> 8) & 0xFF)
			packet.append(((argv[0]*1) >> 0) & 0xFF)
			# state
			packet.append(((argv[1]*1) >> 0) & 0xFF)
		# send_telem_short()
		elif (command_id == 9):
			# board_num
			packet.append(((argv[0]*1) >> 0) & 0xFF)
		# send_telem_all()
		elif (command_id == 10):
			# board_num
			packet.append(((argv[0]*1) >> 0) & 0xFF)
		# set_stepper_period()
		elif (command_id == 11):
			# stepper_num
			packet.append(((argv[0]*1) >> 0) & 0xFF)
			# period
			packet.append(((argv[1]*1) >> 8) & 0xFF)
			packet.append(((argv[1]*1) >> 0) & 0xFF)
		# set_stepper_direction()
		elif (command_id == 12):
			# stepper_num
			packet.append(((argv[0]*1) >> 0) & 0xFF)
			# direction
			packet.append(((argv[1]*1) >> 0) & 0xFF)
		# set_kp()
		elif (command_id == 13):
			# motor_num
			packet.append(((argv[0]*1) >> 0) & 0xFF)
			# gain
			packet.append(((argv[1]*100) >> 56) & 0xFF)
			packet.append(((argv[1]*100) >> 48) & 0xFF)
			packet.append(((argv[1]*100) >> 40) & 0xFF)
			packet.append(((argv[1]*100) >> 32) & 0xFF)
			packet.append(((argv[1]*100) >> 24) & 0xFF)
			packet.append(((argv[1]*100) >> 16) & 0xFF)
			packet.append(((argv[1]*100) >> 8) & 0xFF)
			packet.append(((argv[1]*100) >> 0) & 0xFF)
		# set_ki()
		elif (command_id == 14):
			# motor_num
			packet.append(((argv[0]*1) >> 0) & 0xFF)
			# gain
			packet.append(((argv[1]*100) >> 56) & 0xFF)
			packet.append(((argv[1]*100) >> 48) & 0xFF)
			packet.append(((argv[1]*100) >> 40) & 0xFF)
			packet.append(((argv[1]*100) >> 32) & 0xFF)
			packet.append(((argv[1]*100) >> 24) & 0xFF)
			packet.append(((argv[1]*100) >> 16) & 0xFF)
			packet.append(((argv[1]*100) >> 8) & 0xFF)
			packet.append(((argv[1]*100) >> 0) & 0xFF)
		# set_kd()
		elif (command_id == 15):
			# motor_num
			packet.append(((argv[0]*1) >> 0) & 0xFF)
			# gain
			packet.append(((argv[1]*100) >> 56) & 0xFF)
			packet.append(((argv[1]*100) >> 48) & 0xFF)
			packet.append(((argv[1]*100) >> 40) & 0xFF)
			packet.append(((argv[1]*100) >> 32) & 0xFF)
			packet.append(((argv[1]*100) >> 24) & 0xFF)
			packet.append(((argv[1]*100) >> 16) & 0xFF)
			packet.append(((argv[1]*100) >> 8) & 0xFF)
			packet.append(((argv[1]*100) >> 0) & 0xFF)
		# set_control_calc_period()
		elif (command_id == 16):
			# period
			packet.append(((argv[0]*1) >> 8) & 0xFF)
			packet.append(((argv[0]*1) >> 0) & 0xFF)
		# set_state()
		elif (command_id == 17):
			# state
			packet.append(((argv[0]*1) >> 0) & 0xFF)
		# move_stepper_degrees()
		elif (command_id == 18):
			# motor_num
			packet.append(((argv[0]*1) >> 0) & 0xFF)
			# deg
			packet.append(((argv[1]*1) >> 8) & 0xFF)
			packet.append(((argv[1]*1) >> 0) & 0xFF)

		# Encode the packet with COBS
		stuff_array(packet, separator=0)

		# Write the bytes to serial
		ser.write(bytes(packet))

	"""
	Takes in a byte packet and return a COBS encoded version
	Note: this was copied directly from the EC3 gui code
	@params
		arr (integer array)  - Byte packet to be COBS encoded
		separator (integer)  - Packet delimiter. Should be using 0, but has the option to use any number
	"""
	def stuff_array(arr, separator=0):
		arr.append(0)
		arr.insert(0, 0)
		first_sep = 1
		for x in arr[1:]:
			if x == seperator:
				break
			first_sep += 1
		index = 1
		while(index < len(arr)-1):
			if(arr[index] == seperator):
				offset = 1
				while(arr[index+offset] != seperator):
					offset += 1
				arr[index] = offset
				index += offset
			else:
				index += 1
		arr[0] = first_sep
		return arr

