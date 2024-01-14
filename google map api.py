import googlemaps
import requests
import pandas as pd

def funGmaps(strQuery):

    # 請替換成你的 Google Maps API 金鑰
    gmaps = googlemaps.Client(key='AIzaSyD4j_FDcUZ-JXtOxfSY5AssjViqt3ZYgfM')

    # Text Search API
    textsearch_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    textsearch_params = {
        "query": strQuery,
        "language": "zh-TW",
        "type": "cafe",
        "key":"AIzaSyD4j_FDcUZ-JXtOxfSY5AssjViqt3ZYgfM"
        }

    textsearch_response = requests.get(textsearch_url, params=textsearch_params)
    textsearch_results = textsearch_response.json()["results"]
    
    # 創建一個列表來存儲所有地點的資訊
    data_list = []
    
    # Place Details API
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    
    for result in textsearch_results:
        place_id = result.get("place_id", "N/A")
    
        details_params = {
            "place_id": place_id,
            "fields": "name,types,formatted_address,rating,user_ratings_total,geometry,formatted_phone_number,website,opening_hours",
            "language": "zh-TW",
            "key":"AIzaSyD4j_FDcUZ-JXtOxfSY5AssjViqt3ZYgfM"
        }
    
        details_response = requests.get(details_url, params=details_params)
        details_result = details_response.json().get("result", {})
    
        name = details_result.get("name", "N/A")
        types = details_result.get("types", "N/A")
        formatted_address = details_result.get("formatted_address", "N/A")
        rating = details_result.get("rating", "N/A")
        user_ratings_total = details_result.get("user_ratings_total", "N/A")
        
        geometry = details_result.get("geometry", {})
        location = geometry.get("location", {})
        lat = location.get("lat", "N/A")
        lng = location.get("lng", "N/A")
        
        formatted_phone_number = details_result.get("formatted_phone_number", "N/A")
        website = details_result.get("website", "N/A")
        
        opening_hours = details_result.get("opening_hours", {})
        weekday_text = opening_hours.get("weekday_text", "N/A")
    
        # 將地點資訊添加到列表中
        data_list.append([name, types, formatted_address, rating, user_ratings_total, lat, lng, place_id, formatted_phone_number, website, weekday_text])
    
    # 將列表轉換為 DataFrame
    columns = ["Name", "Types", "Formatted Address", "Rating", "User Ratings Total", "Latitude", "Longitude",
               "Place_id", "Formatted_phone_number", "Website", "Weekday_text"]
    df = pd.DataFrame(data_list, columns=columns)
    
    # 將 DataFrame 輸出到 Excel 文件
    excel_filename = strQuery + ".xlsx"
    df.to_excel(excel_filename, index=False)
    
    # 打印成功消息
    print(f"資料已成功輸出到 {excel_filename}")

# 請傳入區域路段
lstQuery = ["鶯歌區","鶯歌區三界公坑","鶯歌區中山路","鶯歌區中正一路建德二巷","鶯歌區中正一路阿南巷","鶯歌區中正三路曾厝巷","鶯歌區中正三路邱厝巷","鶯歌區中湖街","鶯歌區二橋新村","鶯歌區二甲路中心巷","鶯歌區仁愛路","鶯歌區光明街","鶯歌區公園街","鶯歌區南雅路","鶯歌區國中街","鶯歌區國華路","鶯歌區圳頭坑","鶯歌區大湖路金包珠巷","鶯歌區尖山埔路","鶯歌區尖山路","鶯歌區德昌二街","鶯歌區成功街","鶯歌區明圓街","鶯歌區明圓街三棟","鶯歌區明圓街五棟","鶯歌區明圓街四棟","鶯歌區晨曦街三棟","鶯歌區朝陽街五柳巷","鶯歌區東湖路","鶯歌區欣欣街一棟","鶯歌區欣欣街九棟","鶯歌區欣欣街八棟","鶯歌區欣欣街十棟","鶯歌區永利街","鶯歌區永和街","鶯歌區永明街","鶯歌區永福街","鶯歌區福安街","鶯歌區福德二街","鶯歌區福昌街","鶯歌區育德街","鶯歌區育樂街","鶯歌區莒光街","鶯歌區西湖街曾厝巷","鶯歌區重慶街酒寮巷","鶯歌區館前路","鶯歌區高職南街","鶯歌區鳳一路","鶯歌區鳳五路","鶯歌區鳳吉二街","鶯歌區鳳福路","鶯歌區鶯桃路永富巷","鶯歌區鶯華新村","鶯歌區龍七路","鶯歌區三鶯路","鶯歌區中正一路","鶯歌區中正一路建德巷","鶯歌區中正一路阿四巷","鶯歌區中正三路福德巷","鶯歌區中正三路鄭厝巷","鶯歌區中湖街東學巷","鶯歌區二橋街","鶯歌區二甲路佳美巷","鶯歌區信義街","鶯歌區光照街","鶯歌區公有市場","鶯歌區博館路","鶯歌區國光街","鶯歌區國際一路","鶯歌區大湖路","鶯歌區宏德司法新村","鶯歌區尖山埔路國小巷","鶯歌區尖山路卓厝巷","鶯歌區德昌街","鶯歌區文化路","鶯歌區明圓街一棟","鶯歌區明圓街九棟","鶯歌區明圓街八棟","鶯歌區晨曦街","鶯歌區晨曦街二棟","鶯歌區朝陽街居易巷","鶯歌區樟普坑","鶯歌區欣欣街七棟","鶯歌區欣欣街二棟","鶯歌區欣欣街六棟","鶯歌區欣欣街四棟","鶯歌區永吉街","鶯歌區永安街","鶯歌區永智街","鶯歌區湖山路","鶯歌區福德一路","鶯歌區福德五街","鶯歌區福隆一街","鶯歌區育才街","鶯歌區育英街","鶯歌區行政路","鶯歌區重慶街","鶯歌區陶瓷街","鶯歌區香賓街","鶯歌區高職東街","鶯歌區鳳七路","鶯歌區鳳吉一街","鶯歌區鳳吉五街","鶯歌區鳳鳴路","鶯歌區鶯桃路二段","鶯歌區黃厝街","鶯歌區龍三路","鶯歌區中坑","鶯歌區中正一路宛園巷","鶯歌區中正一路碧龍巷","鶯歌區中正三路","鶯歌區中正三路許厝巷","鶯歌區中正二路","鶯歌區中陽街","鶯歌區二甲路","鶯歌區二甲路光照巷","鶯歌區光復街","鶯歌區八德路","鶯歌區南昌街","鶯歌區和平街","鶯歌區國慶街","鶯歌區國際二路","鶯歌區大湖路余厝巷","鶯歌區宏德新村","鶯歌區尖山埔路二段","鶯歌區建國路","鶯歌區忠孝街","鶯歌區文昌街","鶯歌區明圓街七棟","鶯歌區明圓街二棟","鶯歌區明圓街六棟","鶯歌區晨曦街一棟","鶯歌區朝陽街","鶯歌區朝陽街東坡巷","鶯歌區欣欣街","鶯歌區欣欣街三棟","鶯歌區欣欣街五棟","鶯歌區欣欣街十一棟","鶯歌區正義新村","鶯歌區永和二街","鶯歌區永昌街","鶯歌區永樂街","鶯歌區環河路","鶯歌區福德三街","鶯歌區福德四街","鶯歌區福隆二街","鶯歌區育智路","鶯歌區育賢街","鶯歌區西湖街","鶯歌區重慶街南門商場","鶯歌區陽明街","鶯歌區香賓街得月巷","鶯歌區高職西街","鶯歌區鳳三路","鶯歌區鳳吉三街","鶯歌區鳳吉四街","鶯歌區鶯桃路","鶯歌區鶯歌路","鶯歌區龍一路","鶯歌區龍五路"]

for item in lstQuery:
    funGmaps(item)
