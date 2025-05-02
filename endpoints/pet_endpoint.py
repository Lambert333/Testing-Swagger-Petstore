from utils.base_endpoint import BaseEndpoint
import requests


class PetEndpoint(BaseEndpoint):

    # добавляем нового питомца с помощью метода POST
    def add_pet(self, payload, expected_status):
        return self.post("/pet", payload=payload, expected_status=expected_status)

    # находим питомца в базе с помощью метода GET
    def get_pet_by_id(self, pet_id, expected_status):
        return self.get(f"/pet/{pet_id}", expected_status=expected_status)

    # получаем список питомцев по их статусу с помощью метода GET
    def get_pets_by_status(self, status, expected_status=200):
        params = {'status': status}
        return self.get("/pet/findByStatus", params=params, expected_status=expected_status)

    # обновляем данные о питомце с помощью метода PUT
    def update_pet(self, payload, expected_status):
        return self.put("/pet", payload=payload, expected_status=expected_status)

    # удаляем питомца из базы с помощью метода DELETE
    def delete_pet(self, pet_id, expected_status):
        return self.delete(f"/pet/{pet_id}", expected_status=expected_status)

    # обновляем данные о питомце с помощью формы через метод POST
    def update_pet_with_form(self, pet_id, name=None, status=None, expected_status=200):
        data = {}
        if name is not None:
            data["name"] = name
        if status is not None:
            data["status"] = status
        return self.post(
            f"/pet/{pet_id}",
            data=data,
            expected_status=expected_status,
            headers={"Content-Type": "application/x-www-form-urlencoded"})

    # загружаем изображение питомца через метод POST
    def upload_pet_image(self, pet_id, file_path, additional_metadata=None, expected_status=200):
        with open(file_path, 'rb') as file:
            file_name = file_path.split('/')[-1]
            files = {'file': (file_name, file, 'image/jpeg')}
            data = {}
            if additional_metadata:
                data['additionalMetadata'] = additional_metadata

            url = f"{self.base_url}/pet/{pet_id}/uploadImage"

            # Создаем новую сессию для загрузки файлов
            session = requests.Session()
            session.headers.update({
                'accept': 'application/json',
                'api_key': self.session.headers.get('api_key')
            })

            self.response = session.post(url, files=files, data=data)
            self._handle_response(expected_status)
            return self.response

    # Проверяет ответ при загрузке изображения
    def check_upload_image_response(self, expected_code=200, expected_metadata=None):
        """
        Args:
            expected_code: ожидаемый код ответа
            expected_metadata: ожидаемые метаданные (опционально)
        """
        assert self.response_json["code"] == expected_code, (
            f"Expected code {expected_code}, got {self.response_json['code']}"
        )
        assert "message" in self.response_json, "Response should contain 'message' field"
        assert "type" in self.response_json, "Response should contain 'type' field"
        assert "File uploaded to" in self.response_json["message"], "Response message should contain 'File uploaded to'"

        if expected_metadata:
            assert expected_metadata in self.response_json["message"], (
                f"Response message should contain metadata '{expected_metadata}'")
