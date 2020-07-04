from biomed.preprocessor.cache.cache import Cache
from biomed.preprocessor.cache.cache import CacheFactory
from multiprocessing import Manager, Lock

class SharedMemoryCache( Cache ):
    def __init__( self, InitCache: dict, Lock: Lock ):
        self.__Cache = InitCache
        self.__Lock = Lock

    def has( self, Key: str ) -> bool:
        return Key in self.__Cache

    def get( self, Key: str ) -> str:
        return None if not self.has( Key ) else self.__Cache[ Key ]

    def set( self, Key: str, Value ):
        self.__Lock.acquire()

        self.__Cache[ Key ] = Value

        self.__Lock.release()

    def __str__( self ) -> str:
        return str( self.__Cache )

    def size( self ) -> int:
        return len( self.__Cache )

    def toDict( self ) -> dict:
        return dict( self.__Cache )

    class Factory( CacheFactory ):
        @staticmethod
        def getInstance( MulitprocessingManager: Manager ) -> Cache:
            return SharedMemoryCache(
                MulitprocessingManager.dict(),
                MulitprocessingManager.Lock()
            )
