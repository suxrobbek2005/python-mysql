from colorama import Fore, Style
import mysql.connector
import settings
from db import (

    create_books_table,
    insert_book,
    show_all_books,
    search_books_by_author_or_genre,
    update_book_price,
    update_book_availability,
    delete_book,
    sort_books_by_year,
    count_books,
    price_statistics

)

if __name__ == "__main__":
    try:
        connection2 = mysql.connector.connect(
            host=settings.host,
            user=settings.user,
            password=settings.password,
            port=settings.port
        )
        cursor = connection2.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.db_name}")
        cursor.execute(f"USE {settings.db_name}")

        create_books_table(cursor)
        connection2.commit()

        while True:

            print(f"{Fore.LIGHTCYAN_EX} == Kutubxona tabeli == {Fore.RESET}")
            print(f"\n{Fore.LIGHTCYAN_EX}1 --> Yangi kitob qo'shish {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}2 --> Barcha kitoblar ruyxatini ko'rish {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}3 --> Muallif yoki janr bo'icha izlash {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}4 --> Kitob narxini yangilash {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}5 --> Kitob mavjudligini tahrirlash {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}6 --> Kitobni o'chirish {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}7 --> Yil bo'icha saralash {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}8 --> Jami kitoblar sonini ko'rish {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}9 --> Narx bo'icha statistikani ko'rish {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}10 --> Dasturdan chiqish {Fore.RESET}")

            
            choise_menu = int(input(f"{Fore.LIGHTGREEN_EX}Xizmat turini tanlang {Fore.RESET} "))

            if choise_menu == 1:
            
                length = int(input(f"{Fore.LIGHTYELLOW_EX}Nechta kitob qo'shmoqchisiz {Fore.RESET} "))
                for i in range(length):

                    print(f"\n{Fore.LIGHTYELLOW_EX}{i + 1} - Kitob malumotini kiriting {Fore.RESET}")
                    available_input = input(f"{Fore.LIGHTRED_EX}Mavjudmi (Ha yoki Yo'q): {Fore.RESET} ").lower()
                    available = True if available_input == "ha" else False

                    insert_book(

                        cursor,
                        title=input(f"{Fore.LIGHTRED_EX}Kitob nomini kiriting {Fore.RESET} "),                          
                        author=input(f"{Fore.LIGHTRED_EX}Kitobning muallifini kiriting {Fore.RESET} "),
                        published_year=int(input(f"{Fore.LIGHTRED_EX}Kitob nashr qilingan yilini kiriting {Fore.RESET} ")),
                        genre=input(f"{Fore.LIGHTRED_EX}Kitobning janrini kiriting {Fore.RESET} "),
                        price=float(input(f"{Fore.LIGHTRED_EX}Kitobning narxini kiriting {Fore.RESET} ")),
                        available=available
                    )

                    print(f"{Fore.BLUE}Kitob muvaffaqiyatli qo'shildi!{Fore.RESET}")
                    connection2.commit()

            elif choise_menu == 2:
                    show_all_books(cursor)
                
            elif choise_menu == 3:
                search_type = input(f"{Fore.LIGHTMAGENTA_EX}Qidiruv turini kiriting (author yoki genre): {Fore.RESET} ").lower()
                search_value = input(f"{Fore.LIGHTMAGENTA_EX}Qidiriladigan qiymatni kiriting: {Fore.RESET} ")
                search_books_by_author_or_genre(cursor, search_type, search_value)

            elif choise_menu == 4:
                book_id = int(input(f"{Fore.LIGHTCYAN_EX}Kitobning ID sini kiriting {Fore.RESET} "))
                book_price = float(input(f"{Fore.LIGHTCYAN_EX}Kitobning narxini kiriting {Fore.RESET} "))
                update_book_price(cursor, book_id, book_price)

            elif choise_menu == 5:
                book_id = int(input(f"{Fore.LIGHTCYAN_EX}Kitobning ID sini kiriting {Fore.RESET} "))
                available_input = input(f"{Fore.LIGHTBLUE_EX}Kitob mavjudligi (Ha yoki Yo'q): {Fore.RESET} ").lower()
                available = True if available_input == "ha" else False
                update_book_availability(cursor, book_id, available)

            elif choise_menu == 6:
                book_id = int(input(f"{Fore.MAGENTA}Kitob ID: {Fore.RESET} "))
                delete_book(cursor, book_id)

            elif choise_menu == 7:

                sort = input(f"{Fore.LIGHTGREEN_EX}Tartiblash turini kiriting (DESC yoki ASC): {Fore.RESET} ").upper()
                if sort in {"ASC", "DESC"}:
                    sort_books_by_year(cursor, sort)

                else:
                    print(f"{Fore.RED}Noto'g'ri qiymat kiritildi!{Fore.RESET}")

            elif choise_menu == 8:
                count_books(cursor)

            elif choise_menu == 9:
                    price_statistics(cursor)

            elif choise_menu == 10:
                print(f"{Fore.BLUE}Dasturdan chiqildi {Fore.RESET}")
                break

            else:
                print(f"{Fore.RED}Noto'g'ri xizmat turi tanlandi!{Fore.RESET}")

            
    except Exception as e:
        print(f"{Fore.RED}Xato yuz berdi: {e}{Fore.RESET}")

cursor.close()
connection2.close()

   