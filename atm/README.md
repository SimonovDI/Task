Задача
Написать программу, имитирующую работу банкомата, включая ввод пин-кода, обращение к файлам для хранения информации об
аккаунтах и возможность снятия/пополнения баланса.

Требования:
1. Ввод Пин-кода:
   - Программа должна запрашивать у пользователя ввод пин-кода.
   - Пользователь должен иметь несколько попыток на ввод верного пин-кода.
   - Если пин-код введен неверно более определенного количества раз, программа должна блокировать доступ к банковскому 
   аккаунту.

2. Работа с файлами:
   - Информация об аккаунтах (например, номер счета и текущий баланс) должна быть сохранена в файлах.
   - Программа должна читать информацию о счете из файла, проводить операции и обновлять информацию о счете в файле.

3. Снятие и пополнение баланса:
   - После успешного ввода пин-кода пользователю должна быть предоставлена возможность выбора операции (снятие/пополнение).
   - При снятии или пополнении баланса программа должна обновить информацию в файле.

Дополнительные указания:
- Рекомендуется использовать функции для разделения различных этапов программы (например, проверка пин-кода, 
  чтение/запись в файл, обновление баланса и т.д.).
- Необходимо обеспечить безопасность при работе с конфиденциальной информацией (например, пин-коды, балансы).

Примерный план:
1. Создание функции для проверки пин-кода.
2. Чтение информации об аккаунте из файла.
3. Создание функций для снятия и пополнения баланса.
4. Обновление информации о счете в файле.
5. Обработка блокировки доступа к аккаунту после превышения количества попыток ввода пин-кода.
