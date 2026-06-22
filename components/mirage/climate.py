import esphome.codegen as cg
from esphome.components import climate_ir

AUTO_LOAD = ["climate_ir"]
CODEOWNERS = ["@glmnet"]

mirage_ns = cg.esphome_ns.namespace("mirage")
MirageClimate = mirage_ns.class_("MirageClimate", climate_ir.ClimateIR)

# Ported to current ESPHome climate_ir API (schema constants -> schema functions).
CONFIG_SCHEMA = climate_ir.climate_ir_with_receiver_schema(MirageClimate)


async def to_code(config):
    await climate_ir.new_climate_ir(config)
