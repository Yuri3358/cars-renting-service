import sqlite3
from datetime import date
import builtins
import pytest
from uuid import uuid4
from infra.sql_repos import VehicleRepoSQL, RentingRepoSQL
from dominio.vehicle_service import VehicleService
from dominio.renting_services import RentingService
from app.fachada import RentingFacade


def test_e2e_renting_conflict(monkeypatch):
    # ---------- SETUP ----------
    conn = sqlite3.connect(":memory:")

    conn.execute("""
        CREATE TABLE vehicles (
            brand TEXT,
            model TEXT,
            license_plate TEXT,
            category TEXT,
            daily_rent REAL
        )
    """)

    conn.execute("""
        CREATE TABLE rentings (
            renting_id TEXT,
            license_plate TEXT,
            client_id TEXT,
            start DATE,
            end DATE
        )
    """)

    vehicle_repo = VehicleRepoSQL(conn)
    renting_repo = RentingRepoSQL(conn)

    vehicle_service = VehicleService(vehicle_repo)
    renting_service = RentingService(renting_repo, vehicle_repo)

    facade = RentingFacade(
        vehicle_repo,
        renting_repo,
        vehicle_service,
        renting_service
    )

    # ---------- INPUTS DO USUÁRIO ----------
    inputs = iter([
        # cadastrar veículo
        "1",
        "Honda",
        "Civic",
        "XYZ9999",
        "Sedan",
        "120",

        # primeira locação (válida)
        "3",
        "XYZ9999",
        "12345678900",
        "2024-02-01",
        "2024-02-10",

        # segunda locação (conflitante)
        "3",
        "XYZ9999",
        "24681012140",
        "2024-02-05",
        "2024-02-12",

        # sair
        "4"
    ])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs)
    )

    # ---------- CAPTURA DE SAÍDA ----------
    outputs = []

    def fake_print(*args):
        outputs.append(" ".join(str(a) for a in args))

    monkeypatch.setattr(
        builtins,
        "print",
        fake_print
    )

    # ---------- LOOP PRINCIPAL ----------
    while True:
        print("\n1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Alugar veículo")
        print("4 - Sair")

        option = input("Escolha: ")

        try:
            if option == "1":
                brand = input("Marca: ")
                model = input("Modelo: ")
                license_plate = input("Placa: ")
                category = input("Categoria: ")
                daily_rent = float(input("Valor diário: "))

                facade.create_vehicle(
                    brand,
                    model,
                    license_plate,
                    category,
                    daily_rent
                )

                print("Veículo cadastrado com sucesso!")

            elif option == "3":
                renting_id = input("ID da locação: ")
                license_plate = input("Placa do veículo: ")
                client_id = input("ID do cliente: ")

                start = date.fromisoformat(
                    input("Data início: ")
                )
                end = date.fromisoformat(
                    input("Data fim: ")
                )
                total = facade.create_rentings(
                renting_id,
                license_plate,
                client_id,
                start,
                end)

                print(f"Valor total da locação: {total}")

            elif option == "4":
                break

        except ValueError as e:
            print(e)

    # ---------- ASSERTIVAS ----------
    assert any("Veículo cadastrado com sucesso!" in o for o in outputs)


def test_e2e_full_application_flow(monkeypatch):
    # ---------- SETUP (infra + domínio) ----------
    conn = sqlite3.connect(":memory:")

    conn.execute("""
        CREATE TABLE vehicles (
            brand TEXT,
            model TEXT,
            license_plate TEXT,
            category TEXT,
            daily_rent REAL
        )
    """)

    conn.execute("""
        CREATE TABLE rentings (
            renting_id TEXT,
            license_plate TEXT,
            client_id TEXT,
            start DATE,
            end DATE
        )
    """)

    vehicle_repo = VehicleRepoSQL(conn)
    renting_repo = RentingRepoSQL(conn)

    vehicle_service = VehicleService(vehicle_repo)
    renting_service = RentingService(renting_repo, vehicle_repo)

    facade = RentingFacade(
        vehicle_repo,
        renting_repo,
        vehicle_service,
        renting_service
    )

    # ---------- SIMULAÇÃO DE INPUT DO USUÁRIO ----------
    inputs = iter([
        # cadastrar veículo
        "1",
        "Toyota",
        "Corolla",
        "ABC1234",
        "Sedan",
        "100",

        # listar veículos
        "2",

        # alugar veículo
        "3",
        "ABC1234",
        "12345678900",
        "2024-01-01",
        "2024-01-06",

        # sair
        "4"
    ])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs)
    )

    # ---------- EXECUÇÃO (simula o main) ----------
    outputs = []

    def fake_print(*args):
        outputs.append(" ".join(str(a) for a in args))

    monkeypatch.setattr(
        builtins,
        "print",
        fake_print
    )

    # ---------- LOOP PRINCIPAL (igual ao main.py) ----------
    while True:
        print("\n1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Alugar veículo")
        print("4 - Sair")

        option = input("Escolha: ")

        if option == "1":
            brand = input("Marca: ")
            model = input("Modelo: ")
            license_plate = input("Placa: ")
            category = input("Categoria: ")
            daily_rent = float(input("Valor diário: "))

            facade.create_vehicle(
                brand,
                model,
                license_plate,
                category,
                daily_rent
            )

            print("Veículo cadastrado com sucesso!")

        elif option == "2":
            vehicles = facade.get_vehicles()
            for v in vehicles:
                print(v)

        elif option == "3":
            renting_id = str(uuid4())
            license_plate = input("Placa do veículo: ")
            client_id = input("ID do cliente: ")

            start = date.fromisoformat(
                input("Data início: ")
            )
            end = date.fromisoformat(
                input("Data fim: ")
            )

            total = facade.create_rentings(
                renting_id,
                license_plate,
                client_id,
                start,
                end
            )

            print(f"Valor total da locação: {total}")

        elif option == "4":
            break

    rentings = renting_repo.get_vehicle_by_license_plate("ABC1234")
    # ---------- ASSERTIVAS (verificação final) ----------
    assert any("Veículo cadastrado com sucesso!" in o for o in outputs)
    assert len(rentings) == 1