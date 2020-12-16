import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date


Base = declarative_base()


class Menu(Base):
    __tablename__ = "Меню"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(64), nullable=False, unique=True)


class Klasik_menu(Base):
    __tablename__ = "Класическое Меню"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(64), unique=True, nullable=False)
    price = sa.Column(sa.Float, nullable=False)


class Alcohol(Base):
    __tablename__ = "Алкоголь"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(64), unique=True, nullable=False)
    price_botle = sa.Column(sa.Float, nullable=False)
    price_shot = sa.Column(sa.Float, nullable=False)


engine = sa.create_engine("sqlite:///db1.sqlite3")
Session = sessionmaker()
session = Session(bind=engine)
Base.metadata.create_all(engine)

menu = [
    Menu(name="Алкогольное Меню"),
    Menu(name="Класическое Меню"),
]

klas_menu = [
    Klasik_menu(name="Пельмени", price=170),
    Klasik_menu(name="Салянка", price=190),
]

alk_menu = [
    Alcohol(name="Водка", price_botle=700, price_shot=70),
    Alcohol(name="Вино", price_botle=500, price_shot=120),
]

session.add_all(menu)
session.add_all(klas_menu)
session.add_all(alk_menu)
session.commit()


while True:
    who = input("Введите пороль: ")
    if who == "admin":
        queshion = input("""Выбери действие:
1) Просмотр!
2) Изменение!
3) Удаление!
4) Выйти!
""")
        if queshion == "3":
            del_of_menu = input("""Выбериете что хотите удолить:
1)Меню
2)Класическое меню
3)Алкогольное Меню
4)В главное меню
""")
            # Удаление
            if del_of_menu == "1":
                for products in menu:
                    session.delete(products)
                session.commit()
            elif del_of_menu == "2":
                for products in klas_menu:
                    session.delete(products)
                session.commit()
            elif del_of_menu == "3":
                for products in alk_menu:
                    session.delete(products)
                session.commit()
            elif del_of_menu == "4":
                continue


        elif queshion == "2":
            Update = input("""Выбери изменение:
1)Название меню
2)В класическом меню
3)В Алкогольном меню
4)В главное меню
""")
            # Изменение
            if Update == "1":
                Update_menu = input("""Каое хотите поменять меню:
1)Алкогольное Меню
2)Класическое Меню
3)В главное меню
""")
                z = input("Введите Новое название меню: ")
                if Update_menu == "1":
                    menu[0].name = str(z)
                    session.commit()
                elif Update_menu == "2":
                    menu[1].name = str(z)
                    session.commit()
                elif Update_menu == "3":
                    continue


            # Меняю  Класическом меню
            elif Update == "2":
                Update_kls_menu = input("""Что хотете поменять в Класическом меню:
1)Цена
2)Имя
3)В главное меню
""")
                # Меняю цену в Класическом меню
                if Update_kls_menu == "1":
                    Update_product_price = input("""Цену какого продукта:
1)Пельмени
2)Салянка
3)Выйти в главное меню
""")
                    w = int(input("Новая цена: "))
                    if Update_product_price == "1":
                        klas_menu[0].price = w
                        session.commit()
                    elif Update_product_price == "2":
                        klas_menu[1].price = w
                        session.commit()
                    elif Update_product_price == "3":
                        continue


                # Меняю Имя в Класическом меню
                elif Update_kls_menu == "2":
                    Update_product_name = input("""Имя какого продукта:
1)Пельмени
2)Салянка
3)В главное меню
""")
                    w = input("Новаое имя: ")
                    if Update_product_name == "1":
                        klas_menu[0].name = str(w)
                        session.commit()
                    elif Update_product_name == "2":
                        klas_menu[1].name = str(w)
                        session.commit()
                    elif Update_product_name == "3":
                        continue
                elif Update_kls_menu == "3":
                    continue


            # Меняю алкогольного меню
            elif Update == "3":
                Update_alchol = input("""Что хотите поменять в Алкогольном меню
1)Цена за бутылку
2)Цена за шот
3)Имя
4)В главное меню
""")
                # Меняю цену за бутылку в алкогольного меню
                if Update_alchol == "1":
                    Product_alchol_botle = input("""Выберите продукт:
1)Водка
2)Вино 
3)В главное меню
""")
                    e = int(input("Укажите новую цену: "))
                    if Product_alchol_botle == "1":
                        alk_menu[0].price_botle = e
                        session.commit()
                    elif Product_alchol_botle == "2":
                        alk_menu[1].price_botle = e
                        session.commit()
                    elif Product_alchol_botle == "3":
                        continue


                # Меняю цену за шот в алкогольного меню
                elif Update_alchol == "2":
                    Product_alchol_shot = input("""Выберите продукт:
1)Водка
2)Вино
3)В главное меню
""")
                    e = int(input("Укажите новую цену: "))
                    if Product_alchol_shot == "1":
                        alk_menu[0].price_shot = e
                        session.commit()
                    elif Product_alchol_shot == "2":
                        alk_menu[1].price_shot = e
                        session.commit()
                    elif Product_alchol_shot == "3":
                        continue


                # Меняю Имя в алкогольного меню
                elif Update_alchol == "3":
                    Update_alchol_name = input("""Выберите продукт:
1)Водка
2)Вино 
3)В главное меню
""")
                    e = input("Укажите новое имя: ")
                    if Update_alchol_name == "1":
                        alk_menu[0].name = str(e)
                        session.commit()
                    elif Update_alchol_name == "2":
                        alk_menu[1].name = str(e)
                        session.commit()
                    elif Update_alchol_name == "3":
                        continue
                elif Update_alchol == "4":
                    continue
            elif Update == "4":
                continue

            # Select
        elif queshion == "1":
            Look_for = input("""Выбери что хочешь посмотреть:
1)Меню
2)Класическое меню
3)Алкогольное меню
4)В главное меню
""")
            if Look_for == "1":
                for product in menu:
                    print(product.name)
                print("---" * 10)
            elif Look_for == "2":
                for product in klas_menu:
                    print(product.name, " цена", product.price)
                print("---" * 10)
            elif Look_for == "3":
                for product in alk_menu:
                    print(product.name, " цена за бутылку", product.price_botle, " цена за шот", product.price_shot)
                print("---" * 10)
            elif Look_for == "4":
                continue
        elif queshion == "4":
            break


    elif who == "manager":
        queshion = input("""Выбери действие:
1) Просмотр!
2) Удаление!
3) Выйти!
""")
        if queshion == "1":
            Look_for = input("""Выбери что хочешь посмотреть:
1)Меню
2)Класическое меню
3)Алкогольное меню
4)В главное меню
""")
            if Look_for == "1":
                for product in menu:
                    print(product.name)
                print("---" * 10)
            elif Look_for == "2":
                for product in klas_menu:
                    print(product.name, " цена", product.price)
                print("---" * 10)
            elif Look_for == "3":
                for product in alk_menu:
                    print(product.name, " цена за бутылку", product.price_botle, " цена за шот", product.price_shot)
                print("---" * 10)
            elif Look_for == "4":
                continue


        elif queshion == "2":
            del_of_menu = input("""Выбериете что хотите удолить:
1)Меню
2)Класическое меню
3)Алкогольное Меню
4)В главное меню
""")
            # Удаление
            if del_of_menu == "1":
                for products in menu:
                    session.delete(products)
                session.commit()
            elif del_of_menu == "2":
                for products in klas_menu:
                    session.delete(products)
                session.commit()
            elif del_of_menu == "3":
                for products in alk_menu:
                    session.delete(products)
                session.commit()
            elif del_of_menu == "4":
                continue
        elif queshion == "3":
            continue
print("СМОТРИ ВСЕ ИЗМЕНЕНИЯ В БД")
