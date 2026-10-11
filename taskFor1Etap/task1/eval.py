# -*- coding: utf-8 -*-
import numpy as np
import cv2


def predict_road_broken(image: np.ndarray) -> str:
    """
         Функция, определяющая, прерывается ли дорога на изображении.
         Входные данные: изображение (bgr), прочитанное cv2.imread.
         Выходные данные: строка "yes" или "no".
                          "yes" - дорога прерывается
                          "no" - дорога непрерывна

         Примеры вывода: "yes"
                         "no"
    """
    return "yes"
