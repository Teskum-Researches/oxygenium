#    Oxygenium    #
#                 #
#        3.4      #
#                 #
#            2025 #

ver = "3.4"
name = "Oxygenium"

print(f'{name} {ver} (c) Teskum Researches, 2025')
print("")
print('Загрузка...')

# === Возможные причины для репорта ===
reasons = ["Имя пользователя", "Аватарка", "Обо мне", "Над чем я работаю"]

try:
	import datetime
	import random
	import keyboard
	import os
	import time
	from scratchplus import Session
except:
	print("У вас не установлены модули! Щас установим")
	os.system("pip install keyboard")
	os.system("pip install scratchplus")

stop_flag = False
accounts = []
passwords = []

# === Нужно для завершения по пробелу ===

# === Проверка аккаунтов ===
def check_accounts():
	print("Проверка аккаунтов на валидность, это может занять некоторое время...")
	banned = []

	for i in range(len(accounts) - 1, -1, -1):
		try:
			Session(accounts[i], passwords[i])
		except Exception as e:
			print(f"Аккаунт {accounts[i]} не прошёл проверку: {e}")
			banned.append(accounts[i])
			del accounts[i]
			del passwords[i]
	save_accounts()
	if banned:
		print(f"\nУдалено {len(banned)} аккаунтов:")
		for b in banned:
			print(f" - {b}")
	else:
		print("Все аккаунты прошли проверку!")

# === Загрузка аккаунтов из файла ===
def load_accounts():
	if os.path.exists("accounts.ini"):
		with open("accounts.ini", "r") as file:
			for line in file:
				parts = line.strip().split(":")
				if len(parts) == 2:
					accounts.append(parts[0])
					passwords.append(parts[1])
	else:
		print("А аккаунтов то у нас нету! Их нужно добавить!")
		return("no_accounts")

# === Сохранение аккаунтов в файл ===
def save_accounts():
	with open("accounts.ini", "w") as file:
		for i in range(len(accounts)):
			file.write(f"{accounts[i]}:{passwords[i]}\n")

load_accounts()



# === Меню управления аккаунтами ===
def account_managment():
	while True:
		try:
			print("Управление аккаунтами.")
			ask = int(input('0. Назад. 1. Просмотреть. 2. Добавить. 3. Изменить. 4. Удалить: '))
			match ask:
				# Просмотр
				case 1:
					for i in range(len(accounts)):
						print(f"{i + 1}. {accounts[i]} - {passwords[i]}")
					print()

				# Добавление нового аккаунта
				case 2:
					new_account = input("Введите логин: ")
					new_password = input("Введите пароль: ")
					accounts.append(new_account)
					passwords.append(new_password)
					save_accounts()
					print("Аккаунт добавлен! Файл сохранён.")

				# Изменение аккаунта
				case 3:
					for i in range(len(accounts)):
						print(f"{i + 1}. {accounts[i]} - {passwords[i]}")
					idx = int(input("Введите номер аккаунта для изменения: ")) - 1
					if 0 <= idx < len(accounts):
						new_account = input("Новый логин: ")
						new_password = input("Новый пароль: ")
						accounts[idx] = new_account
						passwords[idx] = new_password
						save_accounts()
						print("Аккаунт обновлён! Файл сохранён.")
					else:
						print("Ошибка: Неверный номер аккаунта.")

				# Удаление аккаунта
				case 4:
					for i in range(len(accounts)):
						print(f"{i + 1}. {accounts[i]} - {passwords[i]}")
					idx = int(input("Введите номер аккаунта для удаления: ")) - 1
					if 0 <= idx < len(accounts):
						del_account = accounts[idx]
						del accounts[idx]
						del passwords[idx]
						save_accounts()
						print(f"Аккаунт {del_account} удалён. Файл сохранён.")
					else:
						print("Ошибка: Неверный номер аккаунта.")

				# Выход в главное меню
				case 0:
					break
				case _:
					print("Ошибка: Неверный ввод")

		except ValueError:
			print("Ошибка: Введите число")

# === Спам-комментариями ===
def spam(tar, text):
	while True:
		try:
			cursor = random.randint(0, len(accounts) - 1)
			user = Session(accounts[cursor], passwords[cursor])
			target = user.get_user(tar)
			rand = random.randint(0, 100)  # добавляем случайное число к комменту
			target.post_comment(f'{text} ({rand})')
			print(f'{datetime.datetime.now().time()} Сообщение "{text}" отправлено к {tar} от {accounts[cursor]}')
			time.sleep(random.uniform(1.5, 3.5))
		except Exception as e:
			print(f"Ошибка: {e}")
			break

# === Репорт по всем причинам ===
def reportall(tar):
	while True:
		reason = random.randint(0, len(reasons) - 1)
		cursor = random.randint(0, len(accounts) - 1)
		try:
			ses = Session(accounts[cursor], passwords[cursor])
			target = ses.get_user(tar)
			target.report(reason)  # отправляем жалобу по случайной причине
			print(f"Репорт успешен!",
				  f"| Время: {datetime.datetime.now().time()}",
				  f"| Цель: {tar}",
				  f"| Репорт с аккаунта {accounts[cursor]}",
				  f"| Причина: {reasons[reason]}")
		except Exception as error:
			print("Ошибка:", error, f"Мы пытались отправить репорт с аккаунта {accounts[cursor]}")

# === Репорт по 1 причине ===
def reportone(tar, reason):
	while True:
		cursor = random.randint(0, len(accounts) - 1)
		try:
			reason = reason
			ses = Session(accounts[cursor], passwords[cursor])
			target = ses.get_user(tar)
			target.report(reason)
			print(f"Репорт успешен!",
				  f"| Время: {datetime.datetime.now().time()}",
				  f"| Цель: {tar}",
				  f"| Репорт с аккаунта {accounts[cursor]}")
				  #f"| Причина: {reasons[reason]}")
		except Exception as error:
			print("Ошибка:", error, f"Мы пытались отправить репорт с аккаунта {accounts[cursor]}")
								   
# === Главное меню программы ===
def main():
	while True:
		print("Выберете действие:")
		try:
			ask = int(input('0. Выход. 1. Спам 2. Репорт 3. Управление аккаунтами 4. Проверка аккаунтов: '))

			match ask:
				case 1:
					tar1 = input('Введите ник цели: ')
					text = input('Введите текст для спама: ')
					spam(tar1, text)
				case 2:
					tar1 = input("Введите ник цели: ")
					mode = int(input("Использовать 1 причину репорта или все (1 - одну, 0 - все): "))
					if mode == 1:
						print("Введите номер причины:")
						print("1 - Имя пользователя")
						print("2 - Аватарка")
						print("3 - Обо мне")
						print("4 - Над чем я работаю")
						reason = int(input("> "))
						reportone(tar1, reason)
					elif mode == 0: reportall(tar1)
				case 3:
					account_managment()
				case 4:
					check_accounts()
				case 0:
					print("Выход из программы...")
					break
				case _:
					print("Ошибка: Неверный ввод")

		except Exception as e:
			print(f"Ошибка: {e}")

# === Начало программы ===

if __name__ == '__main__':
	main()

