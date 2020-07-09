from keras.models import Sequential
from keras.layers import Dense, Dropout
from biomed.properties_manager import PropertiesManager
from keras.regularizers import l1_l2
from biomed.mlp.mlp import MLP
from biomed.mlp.mlp import MLPFactory

class MultiSimpleDFFN( MLP ):
    class Factory( MLPFactory ):
        @staticmethod
        def getInstance( Properties: PropertiesManager ):
            return MultiSimpleDFFN( Properties )

    def __init__( self, Properties: PropertiesManager ):
        super( MultiSimpleDFFN, self ).__init__( Properties )


    def build_mlp_model(self, input_dim, nb_classes):
        Model = Sequential()
        Model.add(Dense(64, input_dim=input_dim, activation='relu', activity_regularizer=l1_l2(0.001, 0.001)))
#        Model.add(Dropout(0.25))
        Model.add(Dense(32, activation='relu', kernel_initializer='random_uniform', bias_initializer='zero'))
#        Model.add(Dropout(0.2))
        Model.add(Dense(32, activation='relu', kernel_initializer='random_uniform', bias_initializer='zero'))
#        Model.add(Dropout(0.1))

        Model.add(Dense(nb_classes, activation='softmax'))

        Model.compile(
            loss='categorical_crossentropy',
            optimizer='nadam',
            metrics=['accuracy']
        )

        Model.summary()
        self._Model = Model
