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
    
    dict_address ={}
    distances = {}
    timee= {}
    coordinate_list = []
    for i, address in enumerate(address_list):
        
        coordinates = get_latlon.address_to_coordinates(naver_api_key, secretcode, address)
        longitude, latitude = coordinates
        
        dict_address[address] = str(longitude)+','+str(latitude)

    addresses = list(dict_address.keys())
    coordinate = list(dict_address.values())
    # print("addresses ",addresses )
    # print("coordinate",coordinate)

    for i in range(len(coordinate)):
        for j in range(i + 1, len(coordinate)):
            start_location = coordinate[i]
            destination_location = coordinate[j]
            distance, seconds = get_taketime.get_travel_time(naver_api_key,secretcode, start_location, destination_location)
            address_pair=f'{addresses[i]} - {addresses[j]}'
            distances[address_pair] = distance

                # 초를 분과 초로 변환
            minutes = str(int(seconds // 60) ) # 분
            remaining_seconds =str( int(seconds % 60))  # 초

            timee[address_pair] = [minutes,remaining_seconds]

    # 결과 출력
for address_pair, distance in distances.items():
    print(f'{address_pair}: {distance:.2f} km')

for address_pair, second in timee.items():
    print(f'{address_pair}:  약 {second[0]}분  {second[1]}초 소요됩니다.')

    # print(f"출발지에서 목적지까지 {distance}m 거리이며, 약 {minutes}분  {remaining_seconds}초 소요됩니다.")