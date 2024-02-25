
if __name__ == "__main__":
    class Cars:
        ''' Базовый класс. '''

        def __init__(self, brand: str, model: str):
            self._brand = brand
            self._model = model

        def __eq__(self, other):
            return __eq__(self, other)
        @property
        def brand(self) -> str:
            return self._brand

        @property
        def model(self) -> str:
            return self._model

        def __str__(self):
            return f"Cars(brand= {self.brand}, model= {self.model}"

        def __repr__(self):
            return f'(Cars{self.__class__.__name__}(brand={self.brand!r}, model=={self.model!r})'


    class PassengerCar(Cars):
        ''' Дочерний класс. '''

        def __init__(self, brand: str, model: str, engine_capacity: float):
              super().__init__(brand, model)
              self.engine_capacity = engine_capacity

        @property
        def engine_capacity(self) -> float:
            return self._engine_capacity

        @engine_capacity.setter
        def engine_capacity(self, new_engine_capacity: float):
            if not isinstance(new_engine_capacity,float):
                raise TypeError("Объём двигателя должен быть типа float")

            if new_engine_capacity <= 0:
                raise ValueError("Объём двигателя должен быть положительным ")

                self._engine_capacity = engine_capacity
            '''Перегрузка метода eq '''
        def equals(self, other):
            if type(self) is type(other):
                return self._brand == other._brand
            else:
               return False
            '''Перегрузка str'''
        def __str__(self):
            return f"Легковой автомобиль {self.brand!r}. Модель {self.model}.Объём двигателя{self.engine_capacity}"
            '''Перегрузка repr'''
        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r},model={self.model!r},engine_capacity={self.engine_capacity}"
pass




