# Parser
Буду писать на русском, так будет проще.
Цель парсера - сохранить все изображения из раздела аниме с сайта https://wallpaperscraft.ru/catalog/anime
На сайте 2196 изображений по этой тематики, расположены по 15 на странице. Нужно спарсить 147 страниц.
Для сохранения изображения нужно открыть ссылку, открыть ссылку с нужным разрешением (1920х1080), после этого сохранять 
Сохранение будет происходить в разные директории, в зависимости от номера страницы. Имя будет иметь следующий формат 1-2 (где 1 - номер страницы, а 2 - номер изображения на странице)
Поправка, используя ссылку https://wallpaperscraft.ru/catalog/anime/1920x1080/page2 можно сразу искать нужное разрешение
Ссылка на страницу хранится в данной структуре  <a class="wallpapers__link" href="/download/animeshka_kot_tolpa_121498/1920x1080">
Ссылка для сохранения изображения находится в структуре "<img class="wallpaper__image" src="ссылка на изображение" alt="1920x1080 Обои анимешка, кот, толпа, арт">"

Осталось реализовать:
Переход со страницы на страницу
Прокрутку всех ссылок со страницы
Создание папки для каждой страницы
Создание имен для изображения
Отлов ошибок
