import requests


def get_html_info(page_url, count):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3865.75 Safari/537.36 "
    }
    for i in range(1, count + 1):
        page = requests.get(page_url, headers=headers)
        page.encoding = "utf-8"
        contents = page.text
        print("=======================================================")
        print(contents)
        print("=======================================================")
        print("第" + str(i) + "次页面抓取完成")
        print("=======================================================")
        print("\n\n")


def get_cookies_info(session_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3865.75 Safari/537.36 "
    }
    session = requests.session()
    session_page = session.get(session_url, headers=headers)
    cookies = session_page.cookies
    for index, cookie in enumerate(cookies):
        name = cookie.name
        value = cookie.value
        print("[" + name + "=" + value + "]")


if __name__ == "__main__":
    url = 'https://hotel.meituan.com/beijing/'
    get_html_info(url, 1)

