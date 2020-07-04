from biomed.pipeline import Pipeline
from biomed.preprocessor.polymorph_preprocessor import PolymorphPreprocessor
from biomed.properties_manager import PropertiesManager
from math import ceil
from multiprocessing import Process, Manager
from time import sleep

class PipelineRunner:
    class Factory:
        @staticmethod
        def getInstance():
            return PipelineRunner()

    def __init__( self ):
        self.__Output = None
        self.__Preprocessor = None
        self.__Properties = None

    def __getChunkSize(
        self,
        SizeOfPermutations: int,
        TotalProcesses: int
    ) -> int:
        return ceil( SizeOfPermutations / TotalProcesses )

    def run( self, Permutations: list, Workers = 1 ):
        self.__Output = Manager().dict()
        self.__Properties = PropertiesManager()

        if Workers == 1:
            self.__runPipeline( Permutations )
        else:
            self.__runInParallel( Permutations, Workers )

        return dict( self.__Output )

    def __computeChunk( self, N: int, BagOfStuff: list ) -> list:
        for Index in range( 0, len( BagOfStuff ), N ):
            yield BagOfStuff[ Index:Index + N ]

    def __runInParallel( self, Permutations: list, Workers: int ):
        Jobs = list()
        DistributedPermuation = self.__computeChunk(
            self.__getChunkSize( len( Permutations ), Workers ),
            Permutations
        )

        self.__spawn( Jobs, DistributedPermuation )
        sleep( 0 )# yield
        self.__waitUntilDone( Jobs )


    def __spawn( self, Jobs: list, Chunks: list ):
        for Chunk in Chunks:
            Job = Process(
                target = PipelineRunner.__run,
                args = ( self, Chunk )
            )

            Job.start()
            Jobs.append( Job )

    def __waitUntilDone( self, Jobs ):
        for Job in Jobs:
            Job.join()

    @staticmethod
    def __run( This, Permutations: list ):
        This.__runPipeline( Permutations )

    def __runPipeline( self, Permutations: list ):
        Pipe = Pipeline.Factory.getInstance(
            self.__Properties,
            PolymorphPreprocessor.Factory.getInstance( self.__Properties )
        )

        for Configuration in Permutations:
            self.__Output[ Configuration[ "id" ] ] = Pipe.pipe( Configuration[ "data" ], Configuration )
