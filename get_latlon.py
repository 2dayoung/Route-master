import requests

def address_to_coordinates(api_key, address):
    base_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

    params = {
        "query": address
    }
    qlqjs= "uEQ7c34iw9s6XQNeIzcRungn858UJNL79g3ifFth"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": api_key,
        "X-NCP-APIGW-API-KEY": qlqjs
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get('addresses'):
            first_address = data['addresses'][0]
            longitude = first_address['x']  # 경도
            latitude = first_address['y']   # 위도
            return float(longitude), float(latitude)
        else:
            print("주소 정보를 찾을 수 없습니다.")
            return None
    else:
        print("API 요청 실패:", response.status_code)
        return None

if __name__ == "__main__":
    naver_api_key = "a986bwktfz"
    address = "충청북도 청주시 서원구 모충로 32"  # 원하는 주소로 변경

    coordinates = address_to_coordinates(naver_api_key, address)

    if coordinates:
        longitude, latitude = coordinates
        print(f"주소: {address}")
        print(f"경도: {longitude}, 위도: {latitude}")
