#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для вывода текущего времени по московскому времени (UTC+3)
"""

from datetime import datetime
import pytz
import os

def get_moscow_time():
    """Получить текущее время в московском часовом поясе"""
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    return moscow_time

def main():
    """Основная функция программы"""
    moscow_time = get_moscow_time()
    
    # Формируем вывод
    output = []
    output.append("=" * 50)
    output.append("🕐 МОСКОВСКОЕ ВРЕМЯ")
    output.append("=" * 50)
    output.append(f"Дата и время: {moscow_time.strftime('%d.%m.%Y %H:%M:%S')}")
    output.append(f"День недели: {moscow_time.strftime('%A')}")
    output.append(f"Часовой пояс: {moscow_time.tzname()}")
    output.append(f"UTC смещение: {moscow_time.strftime('%z')}")
    output.append("=" * 50)
    output.append("")  # Пустая строка для разделения записей
    
    # Выводим в консоль
    for line in output:
        print(line)
    
    # Также записываем в файл для отслеживания работы cron
    log_file = "/workspace/moscow_time.log"
    with open(log_file, "a", encoding="utf-8") as f:
        for line in output:
            f.write(line + "\n")

if __name__ == "__main__":
    main()