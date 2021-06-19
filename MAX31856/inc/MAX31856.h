/**
 * Interface for MASA's MAX31856 thermocouple firmware library
 * Datasheet: https://datasheets.maximintegrated.com/en/ds/MAX31856.pdf
 *
 *
 * REMEMBER TO FILL OUT THE README
 *
 * Created: June 19, 2021
 */

/*
 * IMPORTANT NOTE:
 *
 * All other SPI compatible chips that we have firmware libraries for each have
 * their SPI chip select line connected directly to a GPIO pin on the micro,
 * so the chip select pin could be included in a struct.
 *
 * The nosecone recovery board does CS the normal way, with CS
 * being directly connected to the micro. However, the flight engine controller
 * (and GSE controller) uses a 4bit decoder to toggle chip select, so in order to
 * select a single TC, you need to actuate 4 GPIO pins.
 *
 * This library should be able to be used for both the flight EC and the recovery
 * board, so it should be flexible and support both methods of chip selects.
 */


typedef struct {
	SPI_HandleTypeDef* SPI_bus;
	void (*chip_select)(uint8_t tc_index);  // Function pointer to select a single TC given its index
	void (*chip_release)(uint8_t tc_index);  // Function pointer to release all TCs in the array
	uint8_t num_tcs;

} MAX31856_TC_Array;

/*
 * Initialize all chips as T type thermocouples,
 *
 */
void MAX31856_init_thermocouples(MAX31856_TC_Array* tcs);

float MAX31856_read_thermocouple(MAX31856_TC_Array* tcs, uint8_t tc_index);
