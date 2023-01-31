# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
# Цезаря и возвращает его.
# Шифр Цезаря заменяет каждую букву в тексте на букву, которая
# отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита.
# Если сдвиг не указан, то пусть ваша функция кодирует сдвиг алфавита на 3 позиции:

# А→Г,А→Г,
# Б→Д,Б→Д,
# В→Е,В→Е,


# Э→А,Э→А,
# Ю→Б,Ю→Б,
# Я→ВЯ→В

# Все символы, кроме русских букв должны остаться неизменными.
# Маленькие буквы должны превращаться в маленькие, большие — в большие.
# Напишите также функцию декодирования decrypt_caesar(msg, shift), также
# использующую сдвиг по умолчанию. При написании функции декодирования используйте
# вашу функцию кодирования.
# import symbol



def caesar_encrypt(msg, shift):
    if msg.isalpha():
        while shift >32:
            shift-=32
        encrypt = ord(msg) + shift % 32
        return chr(encrypt)
    return msg


def caesar_decrypt(msg, shift):
    if msg.isalpha():
        while shift >32:
            shift-=32
        decrypt = ord(caesar_encrypt(msg, shift)) - shift % 32
        return chr(decrypt)
    return caesar_encrypt(msg, shift)


shift = int(input('Введите знак: '))
msg = input('Введите текст: ')

encrypted = ''
decrypted = ''


for i in msg:
    encrypted += caesar_encrypt(i, shift)
    decrypted += caesar_decrypt(i, shift)

print(encrypted)
print(decrypted)

