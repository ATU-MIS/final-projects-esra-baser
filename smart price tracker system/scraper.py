import requests
from bs4 import BeautifulSoup


def check_price(url, target_price):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 503:
            return {"success": False, "message": "Amazon şu an yoğun, lütfen 1 dakika sonra deneyin."}

        soup = BeautifulSoup(response.content, "html.parser")

        price_tag = (soup.find(class_="a-price-whole") or
                     soup.find(class_="a-offscreen") or
                     soup.find(id="priceblock_ourprice"))

        title_tag = soup.find(id="productTitle")

        if not price_tag or not title_tag:
            return {"success": False, "message": "Ürün bilgisi bulunamadı. Linki kontrol edin."}

        price_text = price_tag.get_text().replace(".", "").replace(",", ".").replace("TL", "").strip()
        current_price = float(''.join(c for c in price_text if c.isdigit() or c == '.'))

        title = title_tag.get_text().strip()

        if current_price <= float(target_price):
            return {"success": True, "message": f"🔥 İndirim! {title[:35]}... şu an {current_price} TL"}
        else:
            return {"success": True, "message": f"Fiyat: {current_price} TL. (Hedef: {target_price} TL)"}

    except Exception as e:
        return {"success": False, "message": f"Hata: {str(e)}"}