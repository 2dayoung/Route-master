import requests
import get_taketime
import get_latlon


if __name__ == "__main__":
    naver_api_key = "a986bwktfz"
    secretcode= "uEQ7c34iw9s6XQNeIzcRungn858UJNL79g3ifFth"

    # address = "충청북도 청주시 서원구 모충로 32"  # 원하는 주소로 변경

    address_list=["충청북도 청주시 서원구 사창동 367-7",
                "충청북도 청주시 서원구 1순환로680번길 13-11",
                "충청북도 청주시 서원구 모충로3번길 26",
                "충청북도 청주시 서원구 내수동로 140",
                "충청북도 청주시 서원구 창직로31번길 12-1"]

    coordinate_list = []
    for i, address in enumerate(address_list):
        
        coordinates = get_latlon.address_to_coordinates(naver_api_key, secretcode, address)
        longitude, latitude = coordinates
        coordinate_list.append(str(longitude)+','+str(latitude))

    print(coordinate_list)
    start_location=coordinate_list[0]
    destination_location=coordinate_list[1]

    distance, seconds = get_taketime.get_travel_time(naver_api_key,secretcode, start_location, destination_location)
        # 초를 분과 초로 변환
    minutes = int(seconds // 60)  # 분
    remaining_seconds = int(seconds % 60)  # 초

    print(f"출발지에서 목적지까지 {distance}m 거리이며, 약 {minutes}분  {remaining_seconds}초 소요됩니다.")