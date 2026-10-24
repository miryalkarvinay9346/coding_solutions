-- your code goes here
select song_id from song s 
where not exists(
select 1 from belongs_to b where  b.song_id==s.song_id);