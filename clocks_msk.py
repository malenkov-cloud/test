#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для вывода текущего времени по московскому времени (UTC+3)
"""

from datetime import datetime
import pytz

def get_moscow_time():
    """Получить текущее время в московском часовом поясе"""
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    return moscow_time

def main():
    """Основная функция программы"""
    moscow_time = get_moscow_time()
    
    print("=" * 50)
    print("🕐 МОСКОВСКОЕ ВРЕМЯ")
    print("=" * 50)
    print(f"Дата и время: {moscow_time.strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"День недели: {moscow_time.strftime('%A')}")
    print(f"Часовой пояс: {moscow_time.tzname()}")
    print(f"UTC смещение: {moscow_time.strftime('%z')}")
    print("=" * 50)

if __name__ == "__main__":
    main()