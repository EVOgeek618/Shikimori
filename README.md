# Shikimori
Это просто небольшой список программ, который я ради интереса писал для анализа сайта Shikimori.

## Popular_Char.py
Это программа написана была для коллекции другого пользователя. Она ищет персонажей, у которых более 200 комментариев и записывает их в файл List of popular ch.txt. Примерное время анализа - 30-32 часа

## Popular_Characters.py
Небольшой скрипт, который просит вас ввести колличество проверяемых людей, манги или аниме(необходимо выбрать в самом скрипте, убрав значок комментария в начале 7-9 строки), а после написать id через пробел. На выходе вы получите отсортированный список персонажей по избранному. Она не пишет персонажей без избранного.

## Popular_Anime.py
Пока самая важная тут программа, так как она создает 3 коллекции - популярные аниме, аниме по комментам и аниме по отзывам. Она анализирует 3000 саммых популярных аниме и записывает данные по ним в файл.

## for_collections.py
Программа берёт файлы с 2 проверок Popular_Anime.py и выбает строку, являющуюся json кодом, который просто нужно вставить в коллекцию. Только нужно убрать запятую в конце. Аниме будут отсортированны по нужному критерию, написанно их место в рейтинге, значение критерия и предыдущее место
