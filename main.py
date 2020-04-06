import os
import schedule
import time
import requests
import psycopg2


def save_countries(countries):
    conn = psycopg2.connect(
            host=os.getenv("host", "127.0.0.1"),
            port=os.getenv("port", 5432),
            user=os.getenv("user", "coronaboard"),
            password=os.getenv("password", "123456"),
            database=os.getenv("database", "coronaboard"))
    cursor = conn.cursor()
    for country in countries:
        try:
            save_country(cursor, country)
        except Exception as e:
            if country.get("todayDeaths") is None:
                print(country)
            print(country.get("todayDeaths", 0))
    conn.commit()
    cursor.close()
    conn.close()


def save_country(cursor, country):

    info = country.get("countryInfo", {})
    country_id = info.get("_id")
    if country_id is None:
        return
 
    dml = """
    INSERT INTO countries
    (country_id, name, cases, today_cases, deaths, today_deaths, critical, flag)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (country_id) 
    DO UPDATE 
       SET cases = %s,
           today_cases = %s,
           deaths = %s,
           today_deaths = %s,
           critical = %s,
           flag = %s;
    """ 
    
    cursor.execute(dml, (
        country_id,
        country.get("country"),
        country.get("cases", 0) or 0,
        country.get("todayCases", 0) or 0,
        country.get("deaths", 0) or 0,
        country.get("todayDeaths", 0) or 0,
        country.get("critical", 0) or 0,
        info.get("flag", None) ,
        country.get("cases", 0) or 0,
        country.get("todayCases", 0) or 0,
        country.get("deaths", 0) or 0,
        country.get("todayDeaths", 0) or 0,
        country.get("critical", 0) or 0,
        info.get("flag", None)
        ))


def get_countries():
    countries = []
    try:
        url = 'https://corona.lmao.ninja/countries/'
        response = requests.get(url=url)
        countries = response.json()
    except Exception as e:
        print(e)
    finally:
        return countries


def download_updates():
    save_countries(get_countries())
    print("Download as successfull")


if __name__ == '__main__':
    download_updates()
    schedule.every(10).minutes.do(download_updates)
    while True:
        schedule.run_pending()
        time.sleep(1)

