# -*- coding: utf-8 -*-
import numpy as np
import cv2

def load_tools():

    return []




def predict_turn_number(image: np.ndarray, service: str, tools_list: list) -> int:
    """
         Функция, определяющая номер поворота к сервису, конкретного типа.
         Входные данные: изображение (bgr), строка с типом сервиса.
                         Возможны четыре варианта строк с типом сервисов:
                         "car wash", "gas station", "tire service", "auto repair shop".

         Выходные данные: номер поворота (int).
                          Возможные варианты: 1, 2, 3, 4.

         Пример вывода: 1
                        3
    """
    return  1
