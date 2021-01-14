"""Constants for Daikin."""
from homeassistant.const import (
    CONF_DEVICE_CLASS,
    CONF_ICON,
    CONF_NAME,
    CONF_TYPE,
    CONF_UNIT_OF_MEASUREMENT,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    ENERGY_KILO_WATT_HOUR,
    PERCENTAGE,
    POWER_KILO_WATT,
    TEMP_CELSIUS,
)

CONTROLLERS = "controllers"

ATTR_TARGET_TEMPERATURE = "target_temperature"
ATTR_INSIDE_TEMPERATURE = "inside_temperature"
ATTR_OUTSIDE_TEMPERATURE = "outside_temperature"
SENSOR_TYPE_TEMPERATURE = "temperature"
ATTR_STATE_ON = "on"
ATTR_STATE_OFF = "off"

MIN_TEMP = 16
MAX_TEMP = 32

TIMEOUT = 60