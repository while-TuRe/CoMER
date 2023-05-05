from pytorch_lightning.plugins.training_type.ddp import DDPPlugin
from pytorch_lightning.utilities.cli import LightningCLI

from comer.datamodule import CROHMEDatamodule
from comer.lit_comer import LitCoMER

cli = LightningCLI(
    LitCoMER,
    CROHMEDatamodule,
    save_config_overwrite=True
)
