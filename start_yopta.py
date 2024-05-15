M_IN_KM = 1000



class InfoMessage:
     """Информационное сообщение о тренировке."""
     def __init__(self, training_type, duration, distance, speed, calories ):
         # Объявляем свойства класса и передаём в них необходимые значения.
         self.training_type = training_type
         self.duration = duration
         self.distance = distance
         self.speed = speed
         self.calories = calories

     def get_message(self):
         return (f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.;'
                 f' Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч;'
                 f' Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        # Объявляем свойства класса и передаём в них необходимые значения.
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = training.get_distance()
        speed = distance / self.duration
        return speed

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__, self.duration,
            self.get_distance(), self.get_mean_speed(),
            self.get_spent_calories())



class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65
    def get_spent_calories(self) -> float:
        CALORIES_MEAN_SPEED_MULTIPLIER = 18
        CALORIES_MEAN_SPEED_SHIFT = 1.79
        speed = distance / self.duration
        calories = ((CALORIES_MEAN_SPEED_MULTIPLIER * speed + CALORIES_MEAN_SPEED_SHIFT)
        * self.weight / M_IN_KM * self.duration)
        return calories
#
#
class SportsWalking(Training):
#     """Тренировка: спортивная ходьба."""
     def __init__(self,
                  action: int,
                  duration: float,
                  weight: float,
                  height: int
                  ) -> None:
         # Вызываем конструктор класса-родителя.
         super().__init__(action, duration, weight)
        # Передаём значение параметра в новое свойство.
         self.height = height

     def get_spent_calories(self) -> float:
        CALORIES_MEAN_SPEED_MULTIPLIER = 18
        CALORIES_MEAN_SPEED_SHIFT = 1.79
        speed = distance / self.duration
        calories = ((0.035 * self.weight + (speed ** 2 / self.height)
        * 0.029 * self.weight) * self.duration)
        return calories


class Swimming(Training):
     """Тренировка: плавание."""
     LEN_STEP = 1.38
     def __init__(self,
                  action: int,
                  duration: float,
                  weight: float,
                  length_pool: int,
                  count_pool: int
                  ) -> None:
         # Вызываем конструктор класса-родителя.
         super().__init__(action, duration, weight)
        # Передаём значение параметра в новое свойство.
         self.length_pool = length_pool
         self.count_pool = count_pool

     def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.length_pool * self.count_pool / M_IN_KM / self.duration
        return speed


     def get_spent_calories(self) -> float:
        CALORIES_MEAN_SPEED_MULTIPLIER = 18
        CALORIES_MEAN_SPEED_SHIFT = 1.79
        speed = distance / self.duration
        calories = (speed + 1.1) * 2 * self.weight * self.duration
        return calories


##
#def read_package(workout_type: str, data: list) -> Training:
#     """Прочитать данные полученные от датчиков."""
#      pass
#
#
def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())

#
#
# if __name__ == '__main__':
#     packages = [
#         ('SWM', [720, 1, 80, 25, 40]),
#         ('RUN', [15000, 1, 75]),
#         ('WLK', [9000, 1, 75, 180]),
#     ]
#
#     for workout_type, data in packages:
#         training = read_package(workout_type, data)
#         main(training)

if __name__ == '__main__':
    print(__name__)
    # packages = [
    #     ('SWM', [720, 1, 80, 25, 40]),
    #     ('RUN', [15000, 1, 75]),
    #     ('WLK', [9000, 1, 75, 180]),
    # ]
    #
    # for workout_type, data in packages:
    #     training = read_package(workout_type, data)
    #     main(training)
    training: Training = Training(10, 100, 82)
    distance = training.get_distance()
    print(distance)
    

    RUN = Running(20, 30,3.4)
    print(RUN.get_distance())


    WLK = SportsWalking(20, 30,3.4, 5)
    print(WLK.get_spent_calories())

    training1: Running = Running(10, 100, 82)
    distance = training1.get_spent_calories()
    print(distance)

    SWM = Swimming(20, 30,3.4, 5, 6)
    print(SWM.get_mean_speed())

    INF = InfoMessage('Ебучий бегкх',4,5,5,5)
    print(INF.get_message())

