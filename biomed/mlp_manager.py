from biomed.mlp.mlp import MLP
from biomed.mlp.multiSimple import MultiSimpleFFN
from biomed.mlp.multiSimpleB import MultiSimpleBFFN
from biomed.mlp.multiSimpleBEx import MultiSimpleBExtendedFFN
from biomed.mlp.multiSimpleC import MultiSimpleCFFN
from biomed.mlp.multiSimpleD import MultiSimpleDFFN
from biomed.mlp.simple import SimpleFFN
from biomed.mlp.simpleEx import SimpleExtendedFFN
from biomed.mlp.simpleB import SimpleBFFN
from biomed.mlp.simpleBEx import SimpleBExtendedFFN
from biomed.mlp.simpleC import SimpleCFFN
from biomed.mlp.simpleCEx import SimpleCExtendedFFN
from biomed.mlp.simpleD import SimpleDFFN
from biomed.mlp.simpleDEx import SimpleDExtendedFFN
from biomed.mlp.simpleE import SimpleEFFN
from biomed.mlp.simpleBA import SimpleBAFFN
from biomed.mlp.complex import ComplexFFN
from biomed.properties_manager import PropertiesManager

class MLPManager(MLP):
    __Models = {
        "s": SimpleFFN.Factory,
        "sx": SimpleExtendedFFN.Factory,
        "sb": SimpleBFFN.Factory,
        "sxb": SimpleBExtendedFFN.Factory,
        "sc": SimpleCFFN.Factory,
        "sxc": SimpleCExtendedFFN.Factory,
        "sd": SimpleCFFN.Factory,
        "sxd": SimpleDFFN.Factory,
        "se": SimpleEFFN.Factory,
        "sba": SimpleBAFFN.Factory,
        "ms": MultiSimpleFFN.Factory,
        "msb": MultiSimpleBFFN.Factory,
        "msxb": MultiSimpleBExtendedFFN.Factory,
        "msc": MultiSimpleCFFN.Factory,
        "msd": MultiSimpleDFFN.Factory,
        "c": ComplexFFN.Factory,
    }

    def __init__( self, pm: PropertiesManager ):
        super( MLPManager, self ).__init__( pm )
        self.__Model = MLPManager.__Models[ pm.model ].getInstance( pm )

    def build_mlp_model( self, input_dim, nb_classes ):
        self.__Model.build_mlp_model( input_dim, nb_classes )

    def train_and_run_mlp_model( self, X_train, X_test, Y_train ):
        return self.__Model.train_and_run_mlp_model(X_train, X_test, Y_train )
