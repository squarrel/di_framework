from abc import ABC, abstractmethod


class Vacuum(ABC):
    @abstractmethod
    def start(self):
        '''Opening processes.'''

    @abstractmethod
    def stop(self):
        '''Closing processes.'''
