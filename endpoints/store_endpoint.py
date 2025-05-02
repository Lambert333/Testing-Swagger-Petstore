from utils.base_endpoint import BaseEndpoint


class StoreEndpoint(BaseEndpoint):
    # создаем новый заказ с помощью метода POST
    def add_order(self, payload, expected_status):
        return self.post("/store/order", payload=payload, expected_status=expected_status)

    # получаем данные заказа по ID с помощью метода GET
    def get_order_by_id(self, order_id, expected_status):
        return self.get(f"/store/order/{order_id}", expected_status=expected_status)

    # получаем статистику склада с помощью метода GET
    def get_inventory_statistics(self, expected_status=200):
        return self.get("/store/inventory", expected_status=expected_status)

    # проверяем структуру инвентаря
    def check_inventory_structure(self, inventory):
        assert isinstance(inventory, dict), "Ответ должен быть словарем"
        assert all(isinstance(value, int) for value in inventory.values()), "Все значения должны быть целыми числами"

        expected_statuses = ["available", "pending", "sold"]
        for status in expected_statuses:
            assert status in inventory, f"Статус {status} должен присутствовать в ответе"

    # удаляем заказ из базы с помощью метода DELETE
    def delete_order(self, order_id, expected_status):
        return self.delete(f"/store/order/{order_id}", expected_status=expected_status)
