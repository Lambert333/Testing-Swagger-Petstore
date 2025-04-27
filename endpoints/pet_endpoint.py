from utils.base_endpoint import BaseEndpoint

class PetEndpoint(BaseEndpoint):
    def add_pet(self, payload, expected_status):
        return self.post("/pet", payload=payload, expected_status=expected_status)

    def get_pet_by_id(self, pet_id, expected_status):
        return self.get(f"/pet/{pet_id}", expected_status=expected_status)

    def update_pet(self, payload, expected_status):
        return self.put("/pet", payload=payload, expected_status=expected_status)

    def delete_pet(self, pet_id, expected_status):
        return self.delete(f"/pet/{pet_id}", expected_status=expected_status)

