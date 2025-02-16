import requests
От bs4 ymport beautifulsoup

дефект fetch_films_from_site(base_url="https://lordserialssnew14.top"):
    """
    PARSIMERMHыS SCAHTAI -ISRAHEM -SPICOCOK.
    Канхдхрим М.Предштавен kakslowarh.
    """
    пытаться:
        # Отправор
        Ответ = запросы.то, что(base_url + "/Фильмы")  # Predpolagem, чto -estth
        ответ.Raise_for_status()  # ПРОВОРМА
        суп = BeautifulSoup(ответ.Текст, "html.parser")

        # Nanaхodim -velymы na -straoniцe (эto зavipityt ortrukturы html)
        Фильмы = []
        film_blocks = суп.find_all("дивизион", сорт_="Фильм-блок")  # Primer -klAscaSABLOUCA -C PILYMOMMOM

        для block в film_blocks:
            title_element = block.Пост Прохан("А", сорт_="Фильм")  # На nawanee fiolgma
            link_element = block.Пост Прохан("А", href = Иссинн)  # СССЛКА НАПИЛММ

            если title_element и link_element:
                title = title_element.Текст.Полески()
                link = base_url + link_element["href"]  # Полная
                Фильмы.Добыча({"заголовок": заголовок, "связь": связь})

        возвращаться Фильмы

    кроме Исключение как эн:
        Пост(f "oshibka pripriprcynge: {эn}")
        возвращаться []

Эсли __IMPE__ == "__основной__":
    Фильмы = fetch_films_from_site()
    Пост(f "nanazhad {len (gilgmы)} filymow:")
    для Фильм в Фильмы:
        Пост(fohn "- {gilgm ['title']} ({ipiolmm ['link']})")
