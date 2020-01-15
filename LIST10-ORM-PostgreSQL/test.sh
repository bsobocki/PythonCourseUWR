python3 main.py --init
echo "

"
python3 main.py --add-person '{"id":1, "name":"John", "email":"john@my-email.com"}'
echo "

"
python3 main.py --add-person '{"id":2, "name":"Alice", "email":"alice@dot.com"}'
echo "

"
python3 main.py --add-person '{"id":3, "name":"Arthur", "email":"arth@dot.com"}'
echo "

"
python3 main.py --add-person '{"id":42, "name":"Elisabeth", "email":"eli@dot.com"}'
echo "

"
python3 main.py --add-person '{"id":24, "name":"Mark", "email":"m_kowalski@comma.com"}'
echo "

"
python3 main.py --add-person '{"id":55, "name":"Jacob", "email":"iamjacob@comma.com"}'
echo "

"
python3 main.py --add-person '{"id":77, "name":"dancer231", "email":"dancer231@dance.com"}'
echo "

"

python3 main.py --add-person '{"id":1234, "name":"sqrt12B3", "email":"sqrt12B3@mail.com"}'
echo "

"
python3 main.py --add-person '{"id":70, "name":"player12", "email":"D4V1D@prog.com"}'
echo "

"
python3 main.py --add-person '{"id":11, "name":"pow90", "email":"pow91@mail.com"}'
echo "

"
python3 main.py --add-event '{"id":42, "title":"Obi`s Birthday", "start_time":"2019-12-15 12:30", "end_time":"2019-12-15 23:30"}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":1, "event_id":42}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":2, "event_id":42}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":1234, "event_id":42}'
echo "

"
python3 main.py --add-event '{"id":48, "title":"hackaton", "start_time":"2019-12-22 11:20", "end_time":"2019-12-24 23:30"}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":77, "event_id":48}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":1234, "event_id":48}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":70, "event_id":48}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":11, "event_id":48}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":55, "event_id":48}'
echo "

"
python3 main.py --add-person-at-event '{"person_id":42, "event_id":48}'
echo "

"
python3 main.py --write '{"table":"person"}'
echo "

"
python3 main.py --delete-person '{"name":"Alice"}'
echo "

"
python3 main.py --write '{"table":"person_at_event"}'
echo "

"
python3 main.py --delete-event '{"title":"hackaton"}'
echo "

"
python3 main.py --write '{"table":"person_at_event"}'
echo "

"