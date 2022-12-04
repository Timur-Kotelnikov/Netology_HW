INSERT INTO genres (genre_id, genre_name) VALUES ('1', 'Rock'), ('2', 'Punk'), ('3', 'Rap'), ('4', 'Pop'), ('5', 'Trance');

INSERT INTO authors (author_id, author_name) VALUES ('1', 'Linkin Park'), ('2', 'Blink 182'), ('3', 'Eminem'), ('4', 'Britney Spears'), ('5', 'Paul van Dyk'), ('6', 'Nickelback'), ('7', 'Green Day'), ('8', '50 Cent');

INSERT INTO authors_genres (author_id, genre_id) VALUES ('1', '1'), ('1', '2'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '1'), ('7', '2'), ('8', '3');

INSERT INTO albums (album_id, album_name, release_year) VALUES ('1', 'Meteora', '2013'), ('2', 'Enema of the State', '2014'), ('3', 'Slim Shady', '2015'), ('4', 'Baby one more time', '2016'), ('5', '45 RPM', '2017'), ('6', 'Here and now', '2018'), ('7', 'American Idiot', '2019'), ('8', 'Get rich or die trying', '2020');

INSERT INTO albums_authors (album_id, author_id) VALUES ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'); 

INSERT INTO tracks (track_id, track_name, track_length, album_id, author_id) VALUES ('1', 'Numb', '110', '1', '1'), ('2', 'In the end', '120', '1', '1'), ('3', 'First date', '130', '2', '2'), ('4', 'Miss you', '140', '2', '2'), ('5', 'Stan', '150', '3', '3'), ('6', 'Without me', '160', '3', '3'), ('7', 'I did it again', '170', '4', '4'), ('8', 'Baby one more time', '180', '4', '4'), ('9', 'For an angel', '190', '5', '5'), ('10', 'You are in my heart', '200', '5', '5'), ('11', 'When we stand together', '210', '6', '6'), ('12', 'Animals', '220', '6', '6'), ('13', 'Boulevard of broken dreams', '230', '7', '7'), ('14', 'Basket case', '240', '7', '7'), ('15', 'In da club', '250', '8', '8'), ('16', 'Candy shop', '260', '3', '8');

INSERT INTO disks (disk_id, disk_name, release_year) VALUES ('1', 'disk1', '2015'), ('2', 'disk2', '2016'), ('3', 'disk3', '2017'), ('4', 'disk4', '2018'), ('5', 'disk5', '2019'), ('6', 'disk6', '2020'), ('7', 'disk7', '2021'), ('8', 'disk8', '2022');

INSERT INTO disks_tracks (disk_id, track_id) VALUES ('1', '1'), ('1', '9'), ('2', '2'), ('2', '10'), 
('3', '3'), ('3', '11'), ('4', '4'), ('4', '12'), ('5', '5'), ('5', '13'), ('6', '6'), ('6', '14'),
('7', '7'), ('7', '15'), ('8', '8'), ('8', '9');